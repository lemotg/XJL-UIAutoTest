# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 14:28
# @Author  : DannyDong
# @File    : base_case.py
# @describe: 基础CASE

import unittest

from PySe.operation import PySelenium
from PySe.driver import SelectBrowser

from Utils.read_ini import ReadIni
from Utils.get_log import LogInfo
from Test.Business.login_business import LoginBusiness
from Test.Business.home_business import HomeBusiness


# Case基类（登录业务）
class LoginBaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = SelectBrowser().select_browser('chrome')
        cls.dr = PySelenium(cls.driver)
        cls.dr.test_url(ReadIni('Sys_config.ini', 'Base').get_value('website_url'))
        cls.dr.maximize_window()
        # 登录业务流程-测试用例
        cls.login = LoginBusiness(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()


# Case基类（其他业务）
class BaseCase(unittest.TestCase, LogInfo):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = SelectBrowser().select_browser('chrome')
        cls.dr = PySelenium(cls.driver)
        cls.dr.test_url(ReadIni('Sys_config.ini', 'Base').get_value('website_url'))
        cls.dr.maximize_window()

        # 登录业务流程
        username = ReadIni('Sys_config.ini', 'Base').get_value('username')
        password = ReadIni('Sys_config.ini', 'Base').get_value('password')
        cls.login = LoginBusiness(cls.driver)
        cls.login.login_suc(username, password)

        # 选择校区
        cls.campus_select = HomeBusiness(cls.driver)
        cls.campus_select.select_campus(4)
        cls.log.info('Campus Selected')

        # 其他业务流程

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

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
from Test.Business.account_business import AccountBusiness
from Test.Business.course_business import CourseBusiness


# Case基类（登录业务）
class LoginBaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化开始
        LogInfo().log.info('Initialization Start')
        cls.driver = SelectBrowser().select_browser('chrome')
        cls.dr = PySelenium(cls.driver)
        cls.dr.test_url(ReadIni('Sys_config.ini', 'Base').get_value('website_url'))
        cls.dr.maximize_window()
        # 初始化开始
        LogInfo().log.info('Initialization Completed')

        # 登录业务流程-测试用例
        LogInfo().log.info('Login Cases Suite Start Running ')
        cls.login = LoginBusiness(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()


# Case基类（其他业务）
class BaseCase(unittest.TestCase, LogInfo):

    @classmethod
    def setUpClass(cls) -> None:
        # 初始化开始
        LogInfo().log.info('Initialization Start')
        cls.driver = SelectBrowser().select_browser('chrome')
        cls.dr = PySelenium(cls.driver)
        cls.dr.test_url(ReadIni('Sys_config.ini', 'Base').get_value('website_url'))
        cls.dr.maximize_window()
        # 初始化结束
        LogInfo().log.info('Initialization Completed')

        # 前置条件：登录系统
        LogInfo().log.info('Preposition: Login System')
        username = ReadIni('Sys_config.ini', 'Base').get_value('username')
        password = ReadIni('Sys_config.ini', 'Base').get_value('password')
        cls.login = LoginBusiness(cls.driver)
        cls.login.login_suc(username, password)

        # 选择校区
        cls.campus_select = HomeBusiness(cls.driver)
        cls.campus_select.select_campus(4)
        cls.log.info('Campus Selected')

        # 员工管理业务流程
        LogInfo().log.info('Account Cases Suite Start Running')
        cls.account = AccountBusiness(cls.driver)

        # 课程管理业务流程
        LogInfo().log.info('Course Cases Suite Start Running')
        cls.course = CourseBusiness(cls.driver)

        # 其他业务流程

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

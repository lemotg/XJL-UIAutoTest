# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 14:28
# @Author  : DannyDong
# @File    : base_case.py
# @describe: 基础CASE

import unittest

from PySe.operation import PySelenium
from PySe.driver import SelectBrowser

from Utils.read_ini import ReadIni
from Test.Business.login_business import LoginBusiness


# Case基类
class BaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = SelectBrowser().select_browser('chrome')
        cls.dr = PySelenium(cls.driver)
        cls.dr.test_url(ReadIni('Sys_config.ini', 'Base').get_value('website_url'))
        cls.dr.maximize_window()
        # 登录业务-测试用例
        cls.login = LoginBusiness(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

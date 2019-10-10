# -*- coding: utf-8 -*-
# @Time    : 2019/6/13 14:28
# @Author  : DannyDong
# @File    : base_case.py
# @describe: 基础CASE

import unittest

from PySe.operation import PySelenium
from PySe.driver import SelectBrowser

from Test.Business.login_business import LoginBusiness


# Case基类
class BaseCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.driver = SelectBrowser().select_browser('chrome')
        cls.dr = PySelenium(cls.driver)
        cls.dr.test_url('https://dev.xiaojing0.com/admin/login?staff=111')
        cls.dr.maximize_window()
        # 登录业务-测试用例
        cls.login = LoginBusiness(cls.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.close()

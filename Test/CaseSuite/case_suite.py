# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 12:50
# @Author  : DannyDong
# @File    : demo_suite.py
# @describe: 测试用例集合

import unittest

from Test.Case.login_case import LoginCase
from Utils.get_log import LogInfo


def case_suite():
    suite = unittest.TestSuite()
    # 登录用例集
    LogInfo().log.info('Login Cases Suite Start Running ')
    suite.addTest(LoginCase('test_000'))

    return suite

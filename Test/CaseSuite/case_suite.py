# -*- coding: utf-8 -*-
# @Time    : 2019/6/21 12:50
# @Author  : DannyDong
# @File    : demo_suite.py
# @describe: 测试用例集合

import unittest

from Test.Case.case01_Login import LoginCase
from Test.Case.case02_Account import AccountCase
from Test.Case.case03_Course import CourseCase


def case_suite():
    suite = unittest.TestSuite()
    # 登录&退出用例集
    suite.addTest(LoginCase('test_1'))
    suite.addTest(LoginCase('test_2'))

    # 员工管理用例集
    suite.addTest(AccountCase('test_1'))
    suite.addTest(AccountCase('test_2'))
    suite.addTest(AccountCase('test_3'))

    # 课程管理用例集
    suite.addTest(CourseCase('test_1'))
    suite.addTest(CourseCase('test_2'))
    suite.addTest(CourseCase('test_3'))
    suite.addTest(CourseCase('test_4'))
    suite.addTest(CourseCase('test_5'))
    suite.addTest(CourseCase('test_6'))

    return suite

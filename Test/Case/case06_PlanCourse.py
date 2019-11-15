# -*- coding: utf-8 -*-
# @Time    : 2019/11/13 16:47
# @Author  : DannyDong
# @File    : case06_PlanCourse.py
# @describe: 排课测试用例

import unittest
import time

from Utils.get_log import LogInfo
from Test.Case.base_case import BaseCase


class PlanCourseCase(BaseCase, LogInfo):
    """ 排课测试用例 """

    def test_1(self):
        """ 进入班级管理页面 """
        self.log.info('TestCase1 Start Running')
        text = self.classroom.go_class_manage()
        self.assertEqual('新建班级', text, '按钮文字不一致 --- 测试用例不通过')

    def test_2(self):
        """ 打开排课页面 """
        self.log.info('TestCase2 Start Running')
        text = self.classroom.go_plan_class_page()
        self.assertEqual('历史课表', text, '历史课表按钮文字不一致 --- 测试用例不通过')

    def test_3(self):
        """ 按时间进行排课 """
        self.log.info('TestCase3 Start Running')
        self.classroom.plan_class_by_time()
        time.sleep(5)


if __name__ == '__main__':
    unittest.main()

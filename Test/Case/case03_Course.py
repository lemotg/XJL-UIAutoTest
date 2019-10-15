# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 15:36
# @Author  : DannyDong
# @File    : case03_Course.py
# @describe: 课程管理测试用例

import unittest

from Utils.get_log import LogInfo
from Test.Case.base_case import BaseCase


class CourseCase(BaseCase, LogInfo):
    """ 课程管理测试用例 """

    def test_1(self):
        """ 进入课程管理页面 """
        self.log.info('TestCase1 Start Running')
        text = self.course.go_course_manage()
        self.assertEqual('新增课程', text, '按钮文字不一致 --- 测试用例不通过')

    def test_2(self):
        """ 打开课程添加弹框 """
        self.log.info('TestCase2 Start Running')
        text = self.course.open_add_dialog()
        self.assertEqual('新建课程', text, '弹框标题不一致 --- 测试用例不通过')


if __name__ == '__main__':
    unittest.main()

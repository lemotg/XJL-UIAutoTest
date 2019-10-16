# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 10:49
# @Author  : DannyDong
# @File    : case04_Class.py
# @describe: 班级管理测试用例

import unittest

from Utils.get_log import LogInfo
from Utils.create_data import cr_class, cr_class_num
from Test.Case.base_case import BaseCase


class ClassCase(BaseCase, LogInfo):
    """ 班级管理测试用例 """

    def test_1(self):
        """ 进入班级管理页面 """
        self.log.info('TestCase1 Start Running')
        text = self.classroom.go_class_manage()
        self.assertEqual('新建班级', text, '按钮文字不一致 --- 测试用例不通过')

    def test_2(self):
        """ 打开班级添加弹框 """
        self.log.info('TestCase2 Start Running')
        text = self.classroom.open_add_dialog()
        self.assertEqual('新建班级', text, '弹框标题不一致 --- 测试用例不通过')

    def test_3(self):
        """ 添加线下课程班级 """
        self.log.info('TestCase3 Start Running')
        # 生成数据
        name = cr_class()
        num = cr_class_num()

        class_name = self.classroom.add_offline_class(name, num, 0)
        self.assertEqual(name, class_name, '班级名称不一致 --- 测试用例不通过')


if __name__ == '__main__':
    unittest.main()

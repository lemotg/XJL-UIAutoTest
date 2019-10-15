# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 15:36
# @Author  : DannyDong
# @File    : case03_Course.py
# @describe: 课程管理测试用例

import unittest

from Utils.get_log import LogInfo
from Utils.create_data import cr_course, cr_course_num, cr_course_time, cr_course_price
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

    def test_3(self):
        """ 添加班组课（无套餐） """
        self.log.info('TestCase3 Start Running')
        # 生成数据
        course_name = cr_course()
        course_time = cr_course_time()
        course_num = cr_course_num()
        course_price = cr_course_price()

        # 1代表班组课；2代表1对1课程
        self.course.add_course(course_name, course_time, course_num, course_price, 1)

        # 1代表不加套餐；2代表带套餐
        self.course.add_course_package(course_num, course_price, 1)

        # 获取断言数据
        name = self.course.get_course_list_name()
        course_type = self.course.get_course_list_type()
        package = self.course.get_course_list_package()

        self.assertEqual(name, course_name, '课程名称不一致 --- 测试用例不通过')
        self.assertEqual('班组课', course_type, '课程类型不一致 --- 测试用例不通过')
        self.assertEqual('暂未设置', package, '是否有套餐不一致 --- 测试用例不通过')

    def test_4(self):
        """ 添加班组课（有套餐） """
        self.log.info('TestCase4 Start Running')

        # 打开添加弹框
        self.course.open_add_dialog()

        # 生成数据
        course_name = cr_course()
        course_time = cr_course_time()
        course_num = cr_course_num()
        course_price = cr_course_price()

        # 1代表班组课；2代表1对1课程
        self.course.add_course(course_name, course_time, course_num, course_price, 1)

        # 1代表不加套餐；2代表带套餐
        self.course.add_course_package(course_num, course_price, 2)

        # 获取断言数据
        name = self.course.get_course_list_name()
        course_type = self.course.get_course_list_type()
        package = self.course.get_course_list_package()

        self.assertEqual(name, course_name, '课程名称不一致 --- 测试用例不通过')
        self.assertEqual('班组课', course_type, '课程类型不一致 --- 测试用例不通过')
        self.assertNotEqual('暂未设置', package, '是否有套餐不一致 --- 测试用例不通过')

    def test_5(self):
        """ 添加1对1课（无套餐） """
        self.log.info('TestCase5 Start Running')

        # 打开添加弹框
        self.course.open_add_dialog()

        # 生成数据
        course_name = cr_course()
        course_time = cr_course_time()
        course_num = cr_course_num()
        course_price = cr_course_price()

        # 1代表班组课；2代表1对1课程
        self.course.add_course(course_name, course_time, course_num, course_price, 2)

        # 1代表不加套餐；2代表带套餐
        self.course.add_course_package(course_num, course_price, 1)

        # 获取断言数据
        name = self.course.get_course_list_name()
        course_type = self.course.get_course_list_type()
        package = self.course.get_course_list_package()

        self.assertEqual(name, course_name, '课程名称不一致 --- 测试用例不通过')
        self.assertEqual('1对1', course_type, '课程类型不一致 --- 测试用例不通过')
        self.assertEqual('暂未设置', package, '是否有套餐不一致 --- 测试用例不通过')

    def test_6(self):
        """ 添加1对1课（有套餐） """
        self.log.info('TestCase6 Start Running')

        # 打开添加弹框
        self.course.open_add_dialog()

        # 生成数据
        course_name = cr_course()
        course_time = cr_course_time()
        course_num = cr_course_num()
        course_price = cr_course_price()

        # 1代表班组课；2代表1对1课程
        self.course.add_course(course_name, course_time, course_num, course_price, 2)

        # 1代表不加套餐；2代表带套餐
        self.course.add_course_package(course_num, course_price, 2)

        # 获取断言数据
        name = self.course.get_course_list_name()
        course_type = self.course.get_course_list_type()
        package = self.course.get_course_list_package()

        self.assertEqual(name, course_name, '课程名称不一致 --- 测试用例不通过')
        self.assertEqual('1对1', course_type, '课程类型不一致 --- 测试用例不通过')
        self.assertNotEqual('暂未设置', package, '是否有套餐不一致 --- 测试用例不通过')


if __name__ == '__main__':
    unittest.main()

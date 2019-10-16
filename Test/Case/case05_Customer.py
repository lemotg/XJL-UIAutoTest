# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 20:01
# @Author  : DannyDong
# @File    : case05_Customer.py
# @describe: 客户池测试用例

import unittest

from Utils.get_log import LogInfo
from Test.Case.base_case import BaseCase
from Utils.create_data import cr_student_name, cr_age, cr_phone


class CustomerCase(BaseCase, LogInfo):
    """ 客户池测试用例 """

    def test_1(self):
        """ 进入客户池页面 """
        self.log.info('TestCase1 Start Running')
        text = self.customer.go_customer()
        self.assertEqual('快速录入', text, '按钮文字不一致 --- 测试用例不通过')

    def test_2(self):
        """ 打开客户快速录入弹框 """
        self.log.info('TestCase2 Start Running')
        text = self.customer.open_add_dialog()
        self.assertEqual('新增意向学员', text, '弹框标题不一致 --- 测试用例不通过')

    def test_3(self):
        """ 添加意向客户信息 """
        self.log.info('TestCase3 Start Running')

        # 生成数据
        name = cr_student_name()
        age = cr_age()
        phone = cr_phone()

        success_tip = self.customer.add_customer_info(name, age, phone)
        customer_name = self.customer.get_customer_name(1)
        self.assertEqual('学员档案录入成功', success_tip, '录入成功提示信息不一致 --- 测试用例不通过')
        self.assertEqual(name, customer_name, '意向客户姓名不一致 --- 测试用例不通过')


if __name__ == '__main__':
    unittest.main()

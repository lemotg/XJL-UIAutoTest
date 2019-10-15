# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 21:58
# @Author  : DannyDong
# @File    : case02_Account.py
# @describe: 员工管理测试用例

import unittest

from Utils.get_log import LogInfo
from Utils.create_data import cr_staff_name, cr_phone
from Test.Case.base_case import BaseCase


class AccountCase(BaseCase, LogInfo):
    """ 员工管理测试用例 """

    @LogInfo.get_error
    def test_1(self):
        """ 进入员工管理页面 """
        self.log.info('TestCase1 Start Running')
        text = self.account.go_account_manage()
        self.assertEqual('新增员工', text, '按钮文字不一致 --- 测试用例不通过')

    def test_2(self):
        """ 打开员工添加弹框 """
        self.log.info('TestCase2 Start Running')
        text = self.account.open_add_dialog()
        self.assertEqual('新建员工', text, '弹框标题不一致 --- 测试用例不通过')

    def test_3(self):
        """ 添加员工 """
        self.log.info('TestCase3 Start Running')
        add_name = cr_staff_name()
        add_phone = cr_phone()
        self.account.add_account(add_name, add_phone)

        # 获取列表中第一条数据，作为断言数据
        name = self.account.get_account_name()
        phone = self.account.get_account_phone()
        self.assertEqual(add_name, name, '列表员工名称与添加的不一致 --- 测试用例不通过')
        self.assertEqual(add_phone, phone, '列表员工电话与添加的不一致 --- 测试用例不通过')


if __name__ == '__main__':
    unittest.main()

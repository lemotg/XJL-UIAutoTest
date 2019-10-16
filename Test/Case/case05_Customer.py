# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 20:01
# @Author  : DannyDong
# @File    : case05_Customer.py
# @describe: 客户池测试用例

import unittest

from Utils.get_log import LogInfo
from Test.Case.base_case import BaseCase


class CustomerCase(BaseCase, LogInfo):
    """ 客户池测试用例 """

    def test_1(self):
        """ 进入客户池页面 """
        self.log.info('TestCase1 Start Running')
        text = self.customer.go_customer()
        self.assertEqual('快速录入', text, '按钮文字不一致 --- 测试用例不通过')


if __name__ == '__main__':
    unittest.main()

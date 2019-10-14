# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 21:58
# @Author  : DannyDong
# @File    : case02_Account.py
# @describe: 员工管理测试用例

import unittest

from Utils.get_log import LogInfo
from Utils.read_ini import ReadIni
from Test.Case.base_case import BaseCase


class AccountCase(BaseCase, LogInfo):
    """ 员工管理测试用例 """

    @LogInfo.get_error
    def test_1(self):
        """ 进入员工管理页面 """
        self.log.info('TestCase1 Start Running')
        text = self.account.go_account_manage()
        self.assertEqual('新增员工', text, '按钮文字不一致 --- 测试用例不通过')


if __name__ == '__main__':
    unittest.main()

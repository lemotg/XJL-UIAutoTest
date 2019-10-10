# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 17:46
# @Author  : DannyDong
# @File    : login_case.py
# @describe: 登录测试用例

import unittest

from Test.Case.base_case import BaseCase
from Utils.get_log import LogInfo


class LoginCase(BaseCase, LogInfo):
    """ 登录测试用例 """

    @LogInfo.get_error
    def test_000(self):
        """ 登录成功 """
        org_name = self.login.login_suc()
        self.log.info(org_name)
        self.assertEqual('重构测试Rock', org_name, '登录失败 --- 测试用例不通过')


if __name__ == '__main__':
    unittest.main()

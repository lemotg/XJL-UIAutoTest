# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 18:22
# @Author  : DannyDong
# @File    : account_page.py
# @describe: 员工管理页

from PySe.operation import PySelenium


# 员工管理
class AccountPage(object):
    def __init__(self, driver):
        self.element = PySelenium(driver)

    # 获取按钮名称

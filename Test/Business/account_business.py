# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 21:53
# @Author  : DannyDong
# @File    : account_business.py
# @describe: 员工管理业务

from Test.Page.account_page import AccountPage


class AccountBusiness(object):
    def __init__(self, driver):
        self.account_business = AccountPage(driver)

    # 进入员工管理页面
    def go_account_manage(self):
        self.account_business.click_menu_manage()
        self.account_business.click_account()
        return self.account_business.get_add_text()

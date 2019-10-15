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

    # 打开员工添加弹框
    def open_add_dialog(self):
        self.account_business.click_add_account_btn()
        return self.account_business.get_dialog_title()

    # 添加员工
    def add_account(self, name, phone):
        # 输入用户姓名、电话、账号
        self.account_business.input_account_name(name)
        self.account_business.input_account_nickname()
        self.account_business.input_account_phone(phone)
        # 选择角色
        self.account_business.click_role_select()
        self.account_business.select_role_and_level()
        self.account_business.click_role_select()
        # 选择等级
        self.account_business.click_level_select()
        self.account_business.select_role_and_level()
        # 创建
        self.account_business.click_create_btn()

    # 获取列表中员工姓名
    def get_account_name(self):
        return self.account_business.get_account_name()

    # 获取列表中员工电话
    def get_account_phone(self):
        return self.account_business.get_account_phone()

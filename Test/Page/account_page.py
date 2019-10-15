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

    # 点击管理菜单
    def click_menu_manage(self):
        self.element.js_click_element('Index', 'MenuManage')

    # 选择人员管理
    def click_account(self):
        self.element.get_ul_li('Index', 'ManageList', 0)

    # 获取按钮文字
    def get_add_text(self):
        return self.element.get_element_text('AccountManage', 'AddAccountBtn')

    # 点击新增人员按钮
    def click_add_account_btn(self):
        self.element.click_element('AccountManage', 'AddAccountBtn')

    # 获取对话框标题
    def get_dialog_title(self):
        return self.element.get_element_text('AccountManage', 'DialogTitle')

    # 输入员工姓名
    def input_account_name(self, content):
        self.element.element_clear('AccountManage', 'AccountName')
        self.element.click_element('AccountManage', 'AccountName')
        self.element.input_element('AccountManage', 'AccountName', content)

    # 输入用户名(由于用户名会自动生成，暂不做特殊处理)
    def input_account_nickname(self):
        self.element.click_element('AccountManage', 'AccountNickName')

    # 输入员工电话
    def input_account_phone(self, content):
        self.element.element_clear('AccountManage', 'AccountPhone')
        self.element.click_element('AccountManage', 'AccountPhone')
        self.element.input_element('AccountManage', 'AccountPhone', content)

    # 点击角色下拉菜单
    def click_role_select(self):
        self.element.js_click_element('AccountManage', 'AccountRole')

    # 点击等级下拉菜单
    def click_level_select(self):
        self.element.js_click_element('AccountManage', 'AccountLevel')

    # 选择角色
    def select_role_and_level(self):
        self.element.get_ul_li('AccountManage', 'RoleAndLevelList')

    # 点击创建员工按钮
    def click_create_btn(self):
        self.element.click_element('AccountManage', 'CreateAccountBtn')

    # 获取员工列表中的员工姓名
    def get_account_name(self):
        return self.element.get_element_text('AccountManage', 'AccountListName')

    # 获取员工列表中的员工电话
    def get_account_phone(self):
        return self.element.get_element_text('AccountManage', 'AccountListPhone')

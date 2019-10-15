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

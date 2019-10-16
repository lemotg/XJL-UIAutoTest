# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 19:39
# @Author  : DannyDong
# @File    : customer_page.py
# @describe: 客户池页面

from PySe.operation import PySelenium


# 客户池页面
class CustomerPage(object):
    def __init__(self, driver):
        self.element = PySelenium(driver)

    # 点击招生菜单
    def click_menu_solicit(self):
        self.element.js_click_element('Index', 'MenuSolicit')

    # 选择客户池
    def click_customer(self):
        self.element.get_ul_li('Index', 'SolicitList', 0)

    # 获取录入按钮文字
    def get_add_text(self):
        return self.element.get_element_text('Customer', 'AddCustomerBtn')

    # 点击快速录入按钮
    def click_add_customer_btn(self):
        self.element.click_element('Customer', 'AddCustomerBtn')

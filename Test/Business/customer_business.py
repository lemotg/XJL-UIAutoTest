# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 19:51
# @Author  : DannyDong
# @File    : customer_business.py
# @describe: 客户池业务

from Test.Page.customer_page import CustomerPage


class CustomerBusiness(object):
    def __init__(self, driver):
        self.customer_business = CustomerPage(driver)

    # 进入客户池页面
    def go_customer(self):
        self.customer_business.click_menu_solicit()
        self.customer_business.click_customer()
        return self.customer_business.get_add_text()

    # 打开客户快速录入弹框
    def open_add_dialog(self):
        self.customer_business.click_add_customer_btn()
        return self.customer_business.get_dialog_title()

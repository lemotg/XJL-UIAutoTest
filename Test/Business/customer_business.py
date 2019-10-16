# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 19:51
# @Author  : DannyDong
# @File    : customer_business.py
# @describe: 客户池业务

import random

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

    # 添加意向客户信息
    def add_customer_info(self, name, age, phone):
        self.customer_business.input_student_name(name)
        random_num = random.randint(1, 3)
        # 随机选择性别（1：男；2：女；3：未知）
        if random_num == 1:
            self.customer_business.select_student_sex_man()
        elif random_num == 2:
            self.customer_business.select_student_sex_woman()
        else:
            self.customer_business.select_student_sex_none()
        self.customer_business.input_student_age(age)
        self.customer_business.select_contact()
        self.customer_business.input_phone(phone)
        self.customer_business.select_source()
        self.customer_business.select_want_course()
        self.customer_business.select_want_level()
        self.customer_business.submit_customer_info()
        return self.customer_business.get_add_success_tip()

    # 获取意向客户列表中客户姓名
    def get_customer_name(self, td_num):
        self.customer_business.close_add_success_dialog()
        return self.customer_business.get_list_customer_name(td_num)

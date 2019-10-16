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

    # 获取对话框文字
    def get_dialog_title(self):
        return self.element.get_element_text('Customer', 'DialogTitle')

    # 输入学员姓名
    def input_student_name(self, content):
        self.element.click_element('Customer', 'StudentName')
        self.element.input_element('Customer', 'StudentName', content)

    # 选择性别（男）
    def select_student_sex_man(self):
        self.element.js_click_element('Customer', 'StudentSexMen')

    # 选择性别（女）
    def select_student_sex_woman(self):
        self.element.js_click_element('Customer', 'StudentSexWomen')

    # 选择性别（无）
    def select_student_sex_none(self):
        self.element.js_click_element('Customer', 'StudentSexNone')

    # 输入年龄
    def input_student_age(self, content):
        self.element.click_element('Customer', 'StudentAge')
        self.element.input_element('Customer', 'StudentAge', content)

    # 选择联系人（目前只选择本人）
    def select_contact(self):
        self.element.js_click_element('Customer', 'Contact')
        self.element.get_ul_li('Customer', 'SelectList', 0)

    # 输入手机号
    def input_phone(self, content):
        self.element.click_element('Customer', 'Phone')
        self.element.input_element('Customer', 'Phone', content)

    # 选择来源渠道
    def select_source(self):
        self.element.js_click_element('Customer', 'Source')
        self.element.get_ul_li('Customer', 'SelectList')

    # 选择意向课程
    def select_want_course(self):
        self.element.js_click_element('Customer', 'WantCourse')
        self.element.get_ul_li('Customer', 'SelectList')

    # 选择意向程度
    def select_want_level(self):
        self.element.js_click_element('Customer', 'WantLevel')
        self.element.get_ul_li('Customer', 'SelectList')

    # 点击保存意向客户信息
    def submit_customer_info(self):
        self.element.js_click_element('Customer', 'SaveCustomerInfo')

    # 获取意向客户添加成功提示
    def get_add_success_tip(self):
        return self.element.get_element_text('Customer', 'AddSuccessTip')

    # 关闭添加成功提示弹框
    def close_add_success_dialog(self):
        self.element.js_click_element('Customer', 'CloseBtn')

    # 获取意向客户列表中的客户姓名
    def get_list_customer_name(self, num):
        return self.element.get_tr_td_desc('Customer', 'CustomerListFirstRow', num)

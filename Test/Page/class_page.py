# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 10:38
# @Author  : DannyDong
# @File    : class_page.py
# @describe: 班级管理页

from PySe.operation import PySelenium


# 班级管理页
class ClassPage(object):
    def __init__(self, driver):
        self.element = PySelenium(driver)

    # 点击教务菜单
    def click_menu_education(self):
        self.element.js_click_element('Index', 'MenuEducation')

    # 选择班级管理
    def click_class(self):
        self.element.get_ul_li('Index', 'EducationList', 3)

    # 获取按钮文字
    def get_add_text(self):
        return self.element.get_element_text('ClassManage', 'AddClassBtn')

    # 点击新增班级按钮
    def click_add_class_btn(self):
        self.element.click_element('ClassManage', 'AddClassBtn')

    # 获取对话框标题
    def get_dialog_title(self):
        return self.element.get_element_text('ClassManage', 'DialogTitle')

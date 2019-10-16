# -*- coding: utf-8 -*-
# @Time    : 2019/10/16 10:44
# @Author  : DannyDong
# @File    : class_business.py
# @describe: 班级管理业务流程

from Test.Page.class_page import ClassPage


class ClassBusiness(object):
    def __init__(self, driver):
        self.class_business = ClassPage(driver)

    # 进入班级管理页面
    def go_class_manage(self):
        self.class_business.click_menu_education()
        self.class_business.click_class()
        return self.class_business.get_add_text()

    # 打开课程添加弹框
    def open_add_dialog(self):
        self.class_business.click_add_class_btn()
        return self.class_business.get_dialog_title()

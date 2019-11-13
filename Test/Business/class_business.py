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

    # 打开班级添加弹框
    def open_add_dialog(self):
        self.class_business.click_add_class_btn()
        return self.class_business.get_dialog_title()

    # 添加线下课程班级信息
    def add_offline_class(self, name, num, td_num):
        self.class_business.select_course()
        self.class_business.input_class_name(name)
        self.class_business.select_class_time()
        self.class_business.select_teacher()
        self.class_business.input_student_num(num)
        self.class_business.select_sup_teacher()
        self.class_business.submit_class_info()
        return self.class_business.get_list_class_name(td_num)

    # 打开线上课程班级添加弹框
    def open_add_online_dialog(self):
        self.class_business.click_online_class_tab()
        self.class_business.click_add_class_btn()
        return self.class_business.get_dialog_title()

    # 添加线上课程班级信息
    def add_online_class(self, name, td_num):
        self.class_business.select_online_course()
        self.class_business.input_class_name(name)
        self.class_business.submit_online_class_info()
        return self.class_business.get_list_online_class_name(td_num)

    # 进入排课页面
    def go_plan_class_page(self):
        self.class_business.click_plan_class_btn()
        return self.class_business.get_history_schedule()


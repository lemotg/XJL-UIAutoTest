# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 15:31
# @Author  : DannyDong
# @File    : course_business.py
# @describe: 课程管理业务

from Test.Page.course_page import CoursePage


class CourseBusiness(object):
    def __init__(self, driver):
        self.course_business = CoursePage(driver)

    # 进入课程管理页面
    def go_course_manage(self):
        self.course_business.click_menu_education()
        self.course_business.click_course()
        return self.course_business.get_add_text()

    # 打开课程添加弹框
    def open_add_dialog(self):
        self.course_business.click_add_course_btn()
        return self.course_business.get_dialog_title()

    # 添加课程（Base）
    def add_course(self, name, time, num, price, flag):
        self.course_business.click_offline_course()
        # 1代表班组课；2代表1对1课程
        if flag == 1:
            self.course_business.click_group_course()
        else:
            self.course_business.click_one_for_one()
        self.course_business.input_course_name(name)
        self.course_business.input_course_time(time)
        self.course_business.input_course_num(num)
        self.course_business.input_course_price(price)

    # 是否添加套餐
    def add_course_package(self, package_num, package_price, flag):
        # 1代表不加套餐；2代表带套餐
        if flag == 1:
            pass
        else:
            self.course_business.click_add_course_package()
            self.course_business.input_course_package_num(package_num)
            self.course_business.input_course_package_price(package_price)
        self.course_business.submit_course_info()

    # 获取列表中课程名称
    def get_course_list_name(self):
        return self.course_business.get_list_course_name()

    # 获取课程类型
    def get_course_list_type(self):
        return self.course_business.get_list_course_type()

    # 获取是否有套餐
    def get_course_list_package(self):
        return self.course_business.get_list_course_package()

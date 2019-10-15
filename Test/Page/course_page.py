# -*- coding: utf-8 -*-
# @Time    : 2019/10/15 15:24
# @Author  : DannyDong
# @File    : course_page.py
# @describe: 课程管理页

from PySe.operation import PySelenium


# 课程管理
class CoursePage(object):
    def __init__(self, driver):
        self.element = PySelenium(driver)

    # 点击教务菜单
    def click_menu_education(self):
        self.element.js_click_element('Index', 'MenuEducation')

    # 选择人员管理
    def click_course(self):
        self.element.get_ul_li('Index', 'EducationList', 4)

    # 获取按钮文字
    def get_add_text(self):
        return self.element.get_element_text('CourseManage', 'AddCourseBtn')

    # 点击新增课程按钮
    def click_add_course_btn(self):
        self.element.click_element('CourseManage', 'AddCourseBtn')

    # 获取对话框标题
    def get_dialog_title(self):
        return self.element.get_element_text('CourseManage', 'DialogTitle')

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

    # 选择课程信息
    def select_course(self):
        self.element.js_click_element('ClassManage', 'SelectCourse')
        self.element.get_ul_li('ClassManage', 'SelectList')

    # 输入班级名称
    def input_class_name(self, content):
        self.element.click_element('ClassManage', 'ClassName')
        self.element.element_force_clear('ClassManage', 'ClassName')
        self.element.input_element('ClassManage', 'ClassName', content)

    # 选择开课时间
    def select_class_time(self):
        self.element.click_element('ClassManage', 'ClassTime')
        self.element.js_click_element('ClassManage', 'Today')

    # 选择上课教师
    def select_teacher(self):
        self.element.js_click_element('ClassManage', 'ClassTeacher')
        self.element.get_ul_li('ClassManage', 'SelectList')

    # 输入预招人数
    def input_student_num(self, content):
        self.element.element_force_clear('ClassManage', 'ClassNum')
        self.element.input_element('ClassManage', 'ClassNum', content)

    # 选择助教
    def select_sup_teacher(self):
        self.element.js_click_element('ClassManage', 'ClassSup')
        self.element.get_ul_li('ClassManage', 'SelectList')

    # 保存新班级信息
    def submit_class_info(self):
        self.element.js_click_element('ClassManage', 'SaveClassInfo')

    # 获取线下课程列表中第一条数据的班级名称
    def get_list_class_name(self, num):
        return self.element.get_tr_td_desc('ClassManage', 'OfflineListFirstRow', num)

    # 选择线上视频班级
    def click_online_class_tab(self):
        self.element.js_click_element('ClassManage', 'OnlineTab')

    # 选择课程信息
    def select_online_course(self):
        self.element.js_click_element('ClassManage', 'SelectCourse')
        self.element.get_ul_li('ClassManage', 'SelectOnlineList')

    # 保存新班级信息
    def submit_online_class_info(self):
        self.element.js_click_element('ClassManage', 'SaveOnlineClassInfo')

    # 获取线上课程列表中第一条数据的班级名称
    def get_list_online_class_name(self, num):
        return self.element.get_tr_td_asc('ClassManage', 'OnlineListFirstRow', num)

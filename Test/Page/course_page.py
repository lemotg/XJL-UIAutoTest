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

    # 课程设置选择线下班组课
    def click_offline_course(self):
        self.element.js_click_element('CourseManage', 'OfflineCourseRadio')

    # 课程设置选择线上视频课
    def click_online_course(self):
        self.element.js_click_element('CourseManage', 'OnlineCourseRadio')

    # 课程类型选择班组课
    def click_group_course(self):
        self.element.js_click_element('CourseManage', 'GroupCourseRadio')

    # 课程类型选择1对1
    def click_one_for_one(self):
        self.element.js_click_element('CourseManage', 'OneForOneCourseRadio')

    # 输入课程名称
    def input_course_name(self, content):
        self.element.click_element('CourseManage', 'CourseName')
        self.element.input_element('CourseManage', 'CourseName', content)

    # 输入上课时间
    def input_course_time(self, content):
        self.element.click_element('CourseManage', 'CourseTime')
        self.element.input_element('CourseManage', 'CourseTime', content)

    # 输入单次扣课时数
    def input_course_num(self, content):
        self.element.click_element('CourseManage', 'CourseNum')
        self.element.input_element('CourseManage', 'CourseNum', content)

    # 输入课时单价
    def input_course_price(self, content):
        self.element.click_element('CourseManage', 'CoursePrice')
        self.element.input_element('CourseManage', 'CoursePrice', content)

    # 点击添加套餐按钮
    def click_add_course_package(self):
        self.element.click_element('CourseManage', 'AddCoursePackage')

    # 输入套餐课时数
    def input_course_package_num(self, content):
        self.element.click_element('CourseManage', 'CoursePackageNum')
        self.element.input_element('CourseManage', 'CoursePackageNum', content)

    # 输入套餐价格
    def input_course_package_price(self, content):
        self.element.click_element('CourseManage', 'CoursePackagePrice')
        self.element.input_element('CourseManage', 'CoursePackagePrice', content)

    # 保存课程信息
    def submit_course_info(self):
        self.element.js_click_element('CourseManage', 'SaveCourseInfo')

    # 获取列表中课程名称
    def get_list_course_name(self):
        return self.element.get_element_text('CourseManage', 'CourseListName')

    # 获取列表中课程类型
    def get_list_course_type(self):
        return self.element.get_element_text('CourseManage', 'CourseListType')

    # 获取列表中是否有套餐
    def get_list_course_package(self):
        return self.element.get_element_text('CourseManage', 'CourseListPackage')

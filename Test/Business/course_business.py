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

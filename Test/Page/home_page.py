# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 16:14
# @Author  : DannyDong
# @File    : home_page.py
# @describe: 首页

from PySe.operation import PySelenium


# 首页
class HomePage(object):
    def __init__(self, driver):
        self.element = PySelenium(driver)

    # 点击选择校区按钮
    def click_campus(self):
        self.element.js_click_element('Index', 'Campus')

    # 从下拉框中选择校区
    def select_campus(self, campus_index):
        self.element.get_ul_li('Index', 'CampusList', campus_index)

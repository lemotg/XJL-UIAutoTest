# -*- coding: utf-8 -*-
# @Time    : 2019/10/14 16:27
# @Author  : DannyDong
# @File    : home_business.py
# @describe: 首页业务（校区选择业务）

from Test.Page.home_page import HomePage


class HomeBusiness(object):
    def __init__(self, driver):
        self.home_business = HomePage(driver)

    # 选择校区
    def select_campus(self, campus_index):
        self.home_business.click_campus()
        self.home_business.select_campus(campus_index)

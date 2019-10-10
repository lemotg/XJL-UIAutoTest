# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 17:37
# @Author  : DannyDong
# @File    : login_business.py
# @describe: 登录业务逻辑

from Test.Page.login_page import LoginPage


class LoginBusiness(object):
    def __init__(self, driver):
        self.login_Business = LoginPage(driver)

    # 登录成功
    def login_suc(self, username, password):
        self.login_Business.clear_input()
        self.login_Business.send_username(username)
        self.login_Business.send_password(password)
        self.login_Business.click_submit()
        return self.login_Business.get_org_name()

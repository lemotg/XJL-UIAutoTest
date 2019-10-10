# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 17:21
# @Author  : DannyDong
# @File    : login_page.py
# @describe: 登录页面

from PySe.operation import PySelenium


# 登录页面
class LoginPage(object):
    def __init__(self, driver):
        self.element = PySelenium(driver)

    # 清空输入框
    def clear_input(self):
        self.element.element_clear('Login', 'UserName')
        self.element.element_clear('Login', 'PassWord')

    # 输入用户名
    def send_username(self, keywords):
        self.element.input_element('Login', 'UserName', keywords)

    # 输入密码
    def send_password(self, keywords):
        self.element.input_element('Login', 'PassWord', keywords)

    # 点击登录
    def click_submit(self):
        self.element.click_element('Login', 'Submit')

    # 获取首页机构名称
    def get_org_name(self):
        return self.element.get_element_text('Index', 'OrgName')

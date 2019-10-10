# -*- coding: utf-8 -*-
# @Time    : 2019/10/10 17:37
# @Author  : DannyDong
# @File    : login_business.py
# @describe: 登录业务逻辑

from Utils.read_ini import ReadIni
from Test.Page.login_page import LoginPage


class LoginBusiness(object):
    def __init__(self, driver):
        self.login_Business = LoginPage(driver)
        self.username = ReadIni('Sys_config.ini', 'Base').get_value('username')
        self.password = ReadIni('Sys_config.ini', 'Base').get_value('password')

    # 登录成功
    def login_suc(self):
        self.login_Business.send_username(self.username)
        self.login_Business.send_password(self.password)
        self.login_Business.click_submit()
        return self.login_Business.get_org_name()

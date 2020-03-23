# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/7
#File: login_page.py

from PageLocators.login_page_locators import LoinPageLocators as loc
from common.base_page import BasePage

class LoginPage(BasePage):

    def login(self,username,password):
        doc="登录页面-登录功能"
        self.wait_eleVisible(loc.username_loc,doc=doc)
        self.input_text(loc.username_loc, username, doc=doc)
        self.input_text(loc.pwd_loc, password, doc=doc)
        self.click_element(loc.button_loc,doc=doc)

    # 获取错误提示信息--登录区域
    def get_errorMsg_from_loginArea(self):
        doc="登录页面-获取登录区域错误提示信息"
        self.wait_eleVisible(loc.form_error_loc,doc=doc)
        return self.get_text(loc.form_error_loc,doc=doc)

    # 获取错误信息--页面正中间
    def get_errorMsg_from_pageCenter(self):
        doc="登录页面-获取页面正中间错误信息"
        self.wait_eleVisible(loc.center_error_loc,doc=doc)
        return self.get_text(loc.center_error_loc,doc=doc)
if __name__ == '__main__':
    pass
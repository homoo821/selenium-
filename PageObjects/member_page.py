# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/8
#File: member_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageLocators.member_page_locators import MemberPageLocators as loc
from common.base_page import BasePage

class MemberPage(BasePage):

    def isExist_avialable_balance_loc(self):
        doc="个人中心-余额可见"
        self.wait_eleVisible(loc.available_balance_loc,doc)

    def get_user_available_balance(self):
        doc="个人中心-余额"
        return self.get_text(loc.available_balance_loc,doc)

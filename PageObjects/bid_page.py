# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/7
#File: bid_page.py

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from PageObjects.member_page import MemberPage
from PageLocators.bid_page_locators import BidPageLocators as loc
from common.base_page import BasePage

class BidPage(BasePage):

    def isExist_button(self):
        doc = "标页面-投标按钮是否可见"
        return self.wait_eleVisible(loc.button_loc,doc=doc)

    def invest(self,money):
        doc = "标页面-输入投标金额"
        self.input_text(loc.invest_input_loc,money,doc=doc)
        doc = "标页面-点击投标"
        self.click_element(loc.button_loc,doc=doc)

    def get_pagecenter_error_text(self):
        doc = "获取页面中间错误信息"
        return self.get_text(loc.pagecenter_error_loc,doc=doc)

    def get_user_money(self):
        doc = "标页面-获取用户余额"
        return self.get_ele_attribute(loc.invest_input_loc,"data-amount",doc=doc)

    def isExist_logout_activeButton_ele(self):
        doc = "标页面-投标成功弹出查看并激活"
        self.wait_eleVisible(loc.success_button_loc,doc=doc)

    # 投资成功的提示框
    def click_activeButton_on_success_popup(self):
        doc = "标页面-点击查看并激活"
        self.isExist_logout_activeButton_ele()
        self.click_element(loc.success_button_loc,doc=doc)

    # def check_money(self):
    #     befor_money = self.get_user_befor_money()
    #     MemberPage(self.driver).isExist_avialable_balance_loc()
    #     last_money = MemberPage(self.driver).get_user_available_balance()
    #     befor = int(filter(str.isdigit, befor_money))
    #     last = int(filter(str.isdigit, last_money))
    #     print(befor)
    #     print(last)
    #     return 200 == (befor - last)



    # # 错误提示框 --非100的倍数，空
    # def get_arrorMsg_from_pageCenter(self):
    #     # 获取文本信息
    #     # 关闭提示框
    #     pass
    #
    # # 获取提示信息
    # def get_errorMsg_investButton(self):
    #     pass
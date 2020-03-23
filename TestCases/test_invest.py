# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/7
#File: test_invest.py


# 前提
# 1用户已登录
# 2有可用的标
# 3余额可用
# 步骤
# 1选标  默认选第一个
# 标页面--获取投资前的金额
# 2标页面--输入金额，点击投资
# 3标页面--点击投资超过的弹出框--查看并激活
# 断言
# 钱 投资后的金额是不是少了投资的量
# 个人页面 获取投资后的金额
# 投资前的金额-投资后的金额=投资金额
# 投资记录对不对
from selenium import webdriver
import unittest,time
from TestDatas import login_datas
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from PageObjects.bid_page import BidPage
from TestDatas import common_datas
from common.user_log import UserLogs
from PageObjects.member_page import MemberPage
from TestDatas.invest_datas import *
import ddt
import pytest


@pytest.mark.usefixtures("login_click_first_bid")
@pytest.mark.usefixtures("refresh_page")
# @ddt.ddt
class TestInvest():

    # @classmethod
    # def setUpClass(cls):
    #     UserLogs().info("=====初始化浏览器会话，登陆系统，选第一个标=====")
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get(common_datas.web_loginurl)
    #     cls.driver.maximize_window()
    #     LoginPage(cls.driver).login(login_datas.success_data["user"], login_datas.success_data["pwd"])
    #     time.sleep(1)
    #     # 选择第一个标点击投标
    #     IndexPage(cls.driver).click_first_bid()

    # @classmethod
    # def tearDownClass(cls):
    #     # 后置
    #     print("=====关闭浏览器会话=====")
    #     cls.driver.quit()
    #
    # def tearDown(self):
    #     # 每个用例执行后执行
    #     self.driver.refresh()

    # @ddt.data(*no100_data)
    # def test_invest_01_failed_money_is_no_100(self,data):
    #     UserLogs().info("*****投资用例：异常场景：投资金额不为100的整倍数、错误的格式等")
    #     # 标页面-获取用户的余额
    #     befor_money = BidPage(self.driver).get_user_money()
    #     # 标页面-输入投标金额，点击投标
    #     BidPage(self.driver).invest(data["money"])
    #     # 获取提示信息
    #     time.sleep(1)
    #     errorMsg = BidPage(self.driver).get_pagecenter_error_text()
    #     # 刷新页面
    #     self.driver.refresh()
    #     # 获取用户余额
    #     last_money = BidPage(self.driver).get_user_money()
    #     # 断言
    #     assert errorMsg == data["msg_check"]
        # assert befor_money == last_money


    @pytest.mark.smoke
    def test_invest_03_success(self,login_click_first_bid):
        UserLogs().info("*****投资用例：正常场景：投资成功")
        # 标页面-获取投资前的余额
        befor_money =  BidPage(login_click_first_bid[0]).get_user_money()
        # print(type(befor_money))
        print(befor_money)
        # 标页面-输入投标金额，点击投标
        BidPage(login_click_first_bid[0]).invest(success_invest_data["money"])
        time.sleep(1)
        # 点击查看并激活
        BidPage(login_click_first_bid[0]).click_activeButton_on_success_popup()
        # 个人页面-获取投资后的余额
        last_money = MemberPage(login_click_first_bid[0]).get_user_available_balance()
        # last_money = last_money.strip("元")
        # print(type(last_money))
        print(last_money)
        # 断言  投标是否成功
        # assert success_invest_data["money"] == int(float(befor_money)-float(last_money))

# if __name__ == '__main__':
#     unittest.main()
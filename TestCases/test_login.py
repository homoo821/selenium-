# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/7
#File: test_login.py
import unittest
from selenium import webdriver
from PageObjects.login_page import LoginPage
from PageObjects.index_page import IndexPage
from TestDatas import common_datas
from TestDatas import login_datas
from ddt import ddt,data
from common.user_log import UserLogs
import pytest


# @ddt
@pytest.mark.usefixtures("refresh_page")
@pytest.mark.usefixtures("access_web")

class TestLogin():

    # @classmethod
    # def setUpClass(cls):
    #     UserLogs().info("=====测试类执行之前执行=====")
    #     cls.driver = webdriver.Chrome()
    #     cls.driver.get(common_datas.web_loginurl)
    #     cls.driver.maximize_window()
    #     cls.lg = LoginPage(cls.driver)
    #
    # @classmethod
    # def tearDownClass(cls):
    #     # 后置
    #     UserLogs().info("==========测试类执行之后执行==========")
    #     cls.driver.quit()

    # def tearDown(self):
    #     # 每个用例执行后执行
    #     UserLogs().info("==========执行完成==========")
    #     self.driver.refresh()

    # 手机号格式不正确  ddt(phone 大于11位，小于11位，空，特殊符号，不存在号段)

    @pytest.mark.parametrize("data", login_datas.form_data)
    # @data(*login_datas.form_data)
    def test_login_01_form_wrong(self,data,access_web):
        UserLogs().info("*****登录用例：异常场景：没有用户名/没有密码/用户名格式不正确")
        # 步骤    输入用户名，密码，点击登录
        access_web[1].login(data["user"],data['pwd'])
        # 断言    请输入正确的手机号码
        # 登录页面获取文本内容 期望值是否相等
        assert access_web[1].get_errorMsg_from_loginArea() == data['msg_check']


    @pytest.mark.parametrize("data",login_datas.pagecenter_data)
    # @data(*login_datas.pagecenter_data)
    def test_login_02_pagecenter_wrong(self, data,access_web):
        UserLogs().info("*****登录用例：异常场景：帐号或密码错误/未经过授权账号")
        # 步骤    输入用户名，密码，点击登录
        access_web[1].login(data["user"], data['pwd'])
        # 断言    请输入正确的手机号码
        # 登录页面获取文本内容 期望值是否相等
        assert access_web[1].get_errorMsg_from_pageCenter() == data['msg_check']

    # 正常登录  fixture的函数名称用来接收他的返回值
    @pytest.mark.smoke
    def test_login_03_success(self,access_web):
        # 步骤    输入用户名，密码，点击登录
        access_web[1].login(login_datas.success_data["user"],login_datas.success_data["pwd"])
        # 断言    首页当中能否找到退出元素
        assert IndexPage(access_web[0]).is_exist_logout_ele()


@pytest.mark.demo
def test_demo():
    assert 1 == 3
    print("++++++failure+++++")

def demo():
    print("1111111")
    print("2222222")
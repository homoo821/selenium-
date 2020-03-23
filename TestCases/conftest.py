# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/13
#File: conftest.py
import pytest,time
from selenium import webdriver
from PageObjects.login_page import LoginPage
from TestDatas import common_datas
from common.user_log import UserLogs
from PageObjects.index_page import IndexPage

driver = None

@pytest.fixture(scope="class")
def access_web():
    # 前置操作
    global driver
    UserLogs().info("=====测试类执行之前执行=====")
    driver = webdriver.Chrome()
    driver.get(common_datas.web_loginurl)
    driver.maximize_window()
    lg = LoginPage(driver)
    yield (driver,lg)   # 分割线：返回值
    # 后置操作
    UserLogs().info("==========测试类执行之后执行==========")
    driver.quit()


@pytest.fixture()
def refresh_page():
    global driver
    yield
    UserLogs().info("==========执行完成==========")
    driver.refresh()


@pytest.fixture(scope="class")
def login_click_first_bid():
    global driver
    UserLogs().info("=====初始化浏览器会话，登陆系统，选第一个标=====")
    driver = webdriver.Chrome()
    driver.get(common_datas.web_loginurl)
    driver.maximize_window()
    LoginPage(driver).login("18684720553", "python")
    time.sleep(1)
    # 选择第一个标点击投标
    IndexPage(driver).click_first_bid()
    yield (driver,)
    # 后置操作
    UserLogs().info("==========测试类执行之后执行==========")
    driver.quit()

# @pytest.fixture(scope="session")
# def refresh_page():
#     UserLogs().info("==========会话开始==========")
#     yield
#     UserLogs().info("==========会话结束==========")
# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/7
#File: login_page_locators.py
from selenium.webdriver.common.by import By

class LoinPageLocators():

    username_loc = (By.XPATH,'//*[@name="phone"]')
    pwd_loc = (By.XPATH,'//*[@name="password"]')
    rememberme_loc = (By.XPATH,'//*[@name="remember_me"]')
    button_loc = (By.XPATH,'//button[contains(text(),"登录")]')
    form_error_loc = (By.XPATH,'//*[@class="form-error-info"]')
    center_error_loc = (By.XPATH,'//div[@class="layui-layer-content"]')
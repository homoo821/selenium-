# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/7
#File: index_page_locators.py

from selenium.webdriver.common.by import By

class IndexPageLocators():

    logout_loc = (By.XPATH,'//a[contains(text(),"退出")]')
    bid_locs = (By.XPATH,'//*[text()="抢投标"]')
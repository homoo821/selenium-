# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/7
#File: bid_page_locators.py

from selenium.webdriver.common.by import By

class BidPageLocators():

    invest_input_loc = (By.XPATH,'//div[@class="in"]/div/input')
    button_loc = (By.XPATH,'//button[text()="投标"]')
    success_button_loc = (By.XPATH, '//*[text()="投标成功！"]/following-sibling::div//button')
    form_error_loc = (By.XPATH,'//*[@class="layui-layer-content"]/div')
    pagecenter_error_loc = (By.XPATH, '//*[@class="layui-layer-content"]/div')

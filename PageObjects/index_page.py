# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/7
#File: index_page.py

from PageLocators.index_page_locators import IndexPageLocators as loc
from common.base_page import BasePage

class IndexPage(BasePage):

    def is_exist_logout_ele(self):
        doc="首页-是否有退出按钮"
        return self.wait_eleVisible(loc.logout_loc,doc=doc)


    # 选第一个标
    def click_first_bid(self):
        doc="首页-点击投标按钮"
        self.click_element(loc.bid_locs,doc=doc)

    # 随机选一个
    # def click_bid_by_random(self,):
    #     eles = self.driver.find_elements()
    #     index = random.randint(0,len(eles)-1)
    #     eles[index].click()
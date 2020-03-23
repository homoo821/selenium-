# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/8
#File: base_page.py
from selenium import webdriver
from common.user_log import UserLogs
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from common.file_path import *
import win32gui
import win32con
import time

# 封装基本函数  --执行日志、异常处理、失败截图
# 所有页面公共的

class BasePage():
    def __init__(self,driver):
        self.driver = driver

    def wait_eleVisible(self, locator, timeout=30, poll_frequency=0.2, doc=""):
        """
        :param locator: 元素定位，元祖形式
        :param timeout:
        :param poll_frequency:
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        UserLogs().info('等待元素{0}可见'.format(locator))
        try:
            # 开始等待的时间
            start_time=datetime.datetime.now()
            WebDriverWait(self.driver, timeout, poll_frequency).until(EC.visibility_of_element_located(locator))
            # 结束等待的时间
            end_time = datetime.datetime.now()
            # 等待时间
            wait_time=(end_time-start_time).seconds
            UserLogs().info("{0}:元素{1}可见，等待时长为：{2}s".format(doc, locator, wait_time))
            return True
        except Exception as e:
            # 捕获异常到日志
            UserLogs().exception("{0}:元素{1}等待异常，开始截图！！！".format(doc, locator))
            # 截图
            self.get_screenshots(doc)
            # 抛出异常
            raise e

    # 等待元素存在
    # def wait_elePresence(self):
    #     pass

    # 查找一个元素
    def get_element(self,locator,doc=""):
        """
        :param locator: 元素定位，元祖形式
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        UserLogs().info("{0}:查找元素：{1}".format(doc, locator))
        try:
            return self.driver.find_element(*locator)
        except:
            UserLogs().exception("查找元素失败，开始截图！！！")
            # 截图
            self.get_screenshots(doc)
            # 抛出异常
            raise

    # 查找一组元素
    def get_elements(self, locator, doc=""):
        """
        :param locator: 元素定位，元祖形式
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        UserLogs().info("{0}:查找符合表达式的所有元素：{1}".format(doc, locator))
        try:
            return self.driver.find_elements(*locator)
        except:
            UserLogs().exception("查找元素失败，开始截图！！！")
            # 截图
            self.get_screenshots(doc)
            # 抛出异常
            raise

    # 点击操作
    def click_element(self,locator,doc=""):
        """
        :param locator: 元素定位，元祖形式
        :param doc: 模块名_页面名称_操作名称
        :return:
        """
        # 找元素
        ele = self.get_element(locator,doc)
        UserLogs().info("{0}:点击元素：{1}".format(doc, locator))
        try:
            ele.click()
        except:
            UserLogs().exception("元素点击失败，开始截图！！！")
            self.get_screenshots(doc)
            raise

    # 输入操作
    def input_text(self,locator, text, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        UserLogs().info("{0}：向元素{1}输入内容：{2}".format(doc, locator, text))
        try:
            ele.send_keys(text)
        except:
            UserLogs().exception("输入失败，开始截图！！！")
            self.get_screenshots(doc)
            raise

    # 获取元素文本内容
    def get_text(self,locator,doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        UserLogs().info("{0}:获取元素：{1}的文本内容".format(doc, locator))
        try:
            text = ele.text
            UserLogs().info("元素：{0}的文本内容为：{1}".format(locator, text))
            return text
        except:
            UserLogs().exception("获取元素文本内容失败，开始截图！！！")
            self.get_screenshots(doc)
            raise

    # 获取元素属性
    def get_ele_attribute(self, locator, attr, doc=""):
        # 找元素
        ele = self.get_element(locator, doc)
        UserLogs().info("{0}：获取元素：{1}的属性：{2}".format(doc, locator, attr))
        try:
            ele_attr = ele.get_attribute(attr)
            UserLogs().info("元素：{0}的属性{1}值为：{2}".format(doc, locator, ele_attr))
            return ele_attr
        except:
            UserLogs().exception("获取元素属性失败，开始截图！！！")
            self.get_screenshots(doc)
            raise

    # 元素存在则为True，否则为False
    def is_eleExist(self,locator,timeout=10,):
        UserLogs().info("在页面{0}中是否存在元素：{1}".format(doc, locator))
        try:
            WebDriverWait(self.driver,timeout=timeout).until(EC.presence_of_element_located(locator))
            UserLogs().info("{0}秒内页面{1}中存在元素：{2}".format(timeout, doc, locator))
            return True
        except:
            UserLogs().exception("{0}秒内页面{1}中不存在元素：{2}，开始截图！！！".format(timeout, doc, locator))
            self.get_screenshots(doc)
            return False

    def alert_action(self,action="accept"):
        pass
    def switch_iframe(self):
        pass
    def upload_file(self):
        pass
    # 滚动条
    # 窗口

    def get_screenshots(self,doc=""):
        # 图片名称：模块名_页面名称_年-月-日-时-分-秒.png
        file_path=screenshot_path + \
            "/{0}_{1}.png".format(doc,time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime()))
        UserLogs().info("截图文件为：{0}".format(file_path))
        try:
            self.driver.get_screenshot_as_file(file_path)
            UserLogs().info("截图成功。图片路径为：{0}".format(file_path))
        except:
            UserLogs().exception("截图失败，开始截图！！！")
            raise

    # 上传操作
    def upload_file(self,windows_title,filepath):
        # 获取一级窗口
        dialog=win32gui.FindWindow("#32770",windows_title)
        # 获取二级窗口
        comboxex32=win32gui.FindWindowEx(dialog,0,'ComboBoxEx32',None)
        # 获取三级窗口
        combox = win32gui.FindWindowEx(comboxex32, 0, 'ComboBox', None)
        # 文本输入窗口--四级
        edit = win32gui.FindWindowEx(combox, 0, 'Edit', None)
        # 打开按钮--二级
        button = win32gui.FindWindowEx(combox, 0, 'Button', None)
        # 输入文件地址
        win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,filepath)
        # 点击打开按钮--提交文件
        win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    doc="1234"
    BasePage(driver).get_screenshots(doc)
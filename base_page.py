# -*- coding: utf-8 -*- 
# @File : base_page.py
# @Author : 尐玹 
# @Time : 2019/7/20 20:08
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from web_auto_test.public_layer.my_logger import MyLogging
from web_auto_test.public_layer import my_path
import time, datetime


class BasePage:
    def __init__(self,driver:WebDriver):
        self.driver = driver
        self.logger = MyLogging("page_logger")

    def wait_element_visible(self, loc, timeout=30, frequency=0.5, annotation=""):
        """
        :func: 等待元素可见
        :param loc: 元素表达式
        :param timeout: 等待最大时长，默认30秒
        :param frequency: 等待元素存在时，轮询周期0.5
        :param annotation: 代码注释
        :return:
        """
        start = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout, frequency, annotation).until(EC.visibility_of_element_located(loc))
        except:
            self.logger.exception("等待{0}元素可见，超时!!!".format(loc))
            self.failure_screenshots(annotation)
            raise
        else:
            # 记录时长
            end = datetime.datetime.now()
            self.logger.info("开始等待时间点：{0}，结束等待时间点：{1}，等待的时长为：{1}".format(start, end, end-start))

    def wait_element_exists(self, loc, timeout=30, frequency=0.5, annotation=""):
        """
        :func: 等待元素存在
        :param loc: 元素表达式
        :param timeout: 等待最大时长，默认30秒
        :param frequency: 等待元素存在时，轮询周期0.5
        :param annotation: 代码注释
        :return:
        """
        self.logger.info("等待元素{0}存在".format(loc))
        start = datetime.datetime.now()
        try:
            WebDriverWait(self.driver, timeout, frequency, annotation).until(EC.presence_of_all_elements_located(loc))
        except:
            self.logger.exception("{0}元素存在，超时!!!".format(loc))
            self.failure_screenshots(annotation)
            raise
        else:
            # 结束等待时间
            end = datetime.datetime.now()
            self.logger.info("开始等待时间点：{0}，结束等待时间点：{1}，等待的时长为：{1}".format(start, end, end-start))

    def find_the_element(self, loc, timeout=30, frequency=0.5, annotation="", waitType="visible"):
        """
        :func: 查找某个元素
        :param loc: 元素表达式
        :param annotation: 代码注释
        :param waitType: 等待类型，默认等待其可见
        :return: 返回找到的元素
        """
        if waitType =="visible":
            self.wait_element_visible(loc, timeout, frequency, annotation)
        else:
            self.wait_element_exists(loc, timeout, frequency, annotation)
        try:
            element = self.driver.find_element(*loc)
        except:
            self.logger.exception("查找{0}元素失败!!!".format(loc))
            self.failure_screenshots(annotation)
            raise
        else:
            self.logger.info("查找{0}元素{1}成功!!!".format(annotation, loc))
            return element

    def input_text(self, loc, *args, timeout=30, frequency=0.5, annotation="", waitType="visible", isScroll=False):
        """
        :func:对元素输入框输入文本
        :param loc: 元素表达式
        :param args: 输入多个文本值
        :param timeout: 等待最大时长，默认30秒
        :param frequency: 等待元素存在时，轮询周期0.5
        :param annotation: 代码注释
        :param waitType: 等待类型，默认等待其可见
        :param isScroll: 是否需要滚动，默认不需要
        :return:
        """
        # 输入文本值，前提是元素可见并找到
        element = self.find_the_element(loc, timeout, frequency, annotation, waitType)

        if isScroll == True:
            self.scroll_IntoView(element)
        try:
            element.clear()
            element.send_keys(*args)
            # time.sleep(1)
        except:
            self.logger.exception("搜索框{0}输入：{1}失败!!!".format(loc, args))
            self.failure_screenshots(annotation)
            raise
        else:
            self.logger.info("搜索框{0}输入：{1}成功!!!".format(loc, args))

    def scroll_IntoView(self, element):
        '''
        :func: 将元素滚动至可见区域
        :param ele: 需要滚动的元素
        '''
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.logger.info("将元素{}滚动至可见区域".format(element))

    def do_js(self,js):
        self.driver.execute_script(js)

    def js_scroll_top(self):
        '''滚动到顶部'''
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)

    def js_scroll_end(self, x=0):
        '''滚动到底部'''
        js = "window.scrollTo(%s,document.body.scrollHeight)" % x
        self.driver.execute_script(js)

    def get_element_text(self, loc,timeout=30, frequency=0.5, annotation="", waitType="visible", isScroll=False):
        """
        :func:等待某个元素存在，获取文本内容
        :param loc: 元素表达式
        :param timeout: 等待最大时长，默认30秒
        :param frequency: 等待元素存在时，轮询周期0.5
        :param annotation: 代码注释
        :param waitType: 等待类型，默认等待其可见
        :param isScroll: 是否需要滚动，默认不需要
        :return: 返回text
        """
        # 查找某个元素
        element = self.find_the_element(loc, timeout, frequency, annotation, waitType)
        # 获取属性
        if isScroll == True:
            self.scroll_IntoView(element)
        try:
            text = element.text
        except:
            self.logger.exception("获取元素文本值失败!!!")
            self.failure_screenshots(annotation)
            raise
        else:
            self.logger.info("获取元素 {0} 的文件值为:{1}".format(loc, text))
            return text

    def click_operation(self, loc, timeout=30, frequency=0.5, annotation="", waitType="visible", isScroll=False):
        """
        :func: 点击元素操作
        :param loc: 元素表达式
        :param timeout: 等待最大时长，默认30秒
        :param frequency: 等待元素存在时，轮询周期0.5
        :param annotation: 代码注释
        :param waitType: 等待类型，默认等待其可见
        :param isScroll: 是否需要滚动，默认不需要
        :return:
        """
        element = self.find_the_element(loc, timeout, frequency, annotation, waitType)

        if isScroll == True:
            self.scroll_IntoView(element)
            time.sleep(1)
        try:
            element.click()
        except:
            self.logger.exception("点击元素{0}失败!!!".format(loc))
            self.failure_screenshots(annotation)
            raise
        else:
            self.logger.info("点击元素{0}成功!!!".format(loc))

    def get_element_attribute(self, loc, attr_name, timeout=30, frequency=0.5, annotation="", waitType="visible"):
        """
        :func: 获取元素的某个属性值
        :param loc: 元素表达式
        :param attr_name: 元素的属性名称
        :param timeout: 等待最大时长，默认30秒
        :param frequency: 等待元素存在时，轮询周期0.5
        :param annotation: 代码注释
        :param waitType: 等待类型，默认等待其可见
        :return: 返回元素的属性值
        """
        # 查找元素
        element = self.find_the_element(loc, timeout, frequency, annotation, waitType)
        # 获取属性
        try:
            attr_value = element.get_attribute(attr_name)
        except:
            # 日志
            self.logger.exception("获取元素属性失败!!!")
            # 截图
            self.failure_screenshots(annotation)
            raise
        else:
            self.logger.info("获取元素 {0} 的属性 {1} 值为:{2}".format(loc, attr_name, attr_value))
            return attr_value

    def wait_switch_iframe(self, loc, timeout=30, frequency=0.5, annotation=""):
        """
        :func: 切换iframe
        :param loc: 元素表达式
        :param timeout: 等待最大时长，默认30秒
        :param frequency: 等待元素存在时，轮询周期0.5
        :param annotation: 代码注释
        :return:
        """
        try:
            WebDriverWait(self.driver, timeout, frequency).until(EC.frame_to_be_available_and_switch_to_it(loc))
            # 退出到default - content主页面
            # self.driver.switch_to.default_content()
        except:
            self.logger.exception("iframe界面：{0}元素不存在，查找失败!!!".format(loc))
            self.failure_screenshots(annotation)
            raise
        else:
            self.logger.info("iframe界面：{0}元素存在，查找成功!!!".format(loc))

    # 鼠标操作封装
    def mouse_hover(self, loc, timeout=30, frequency=0.5, annotation="", waitType="visible", isScroll=False):
        '''
        :func:鼠标悬浮点击操作
        :param loc: 元素表达式
        :param timeout: 等待最大时长，默认30秒
        :param frequency: 等待元素存在时，轮询周期0.5
        :param annotation: 代码注释
        :param waitType: 等待类型，默认等待其可见
        :param isScroll: 是否需要滚动，默认不需要
        :return:
        '''
        element = self.find_the_element(loc, timeout, frequency, annotation, waitType)
        ac = ActionChains(self.driver)

        if isScroll == True:
            self.scroll_IntoView(element)
        try:
            ac.move_to_element(element).perform()
            ac.click(element).perform()
        except:
            self.logger.exception("{0}:元素不存在，鼠标悬浮点击失败!!!".format(loc))
            self.failure_screenshots(annotation)
            raise
        else:
            self.logger.info("{0}:元素存在，鼠标悬浮点击成功!!!".format(loc))

    def context_click(self, loc, timeout=30, frequency=0.5, annotation="", waitType="visible", isScroll=False):
        '''
        :func:鼠标右击操作
        :param loc: 元素表达式
        :param timeout: 等待最大时长，默认30秒
        :param frequency: 等待元素存在时，轮询周期0.5
        :param annotation: 代码注释
        :param waitType: 等待类型，默认等待其可见
        :param isScroll: 是否需要滚动，默认不需要
        :return:
        '''
        element = self.find_the_element(loc, timeout, frequency, annotation, waitType)
        ac = ActionChains(self.driver)

        if isScroll == True:
            self.scroll_IntoView(element)
        try:
            ac.context_click(element).perform()
        except:
            self.logger.exception("{0}:元素不存在，鼠标右击操作失败!!!".format(loc))
            self.failure_screenshots(annotation)
            raise
        else:
            self.logger.info("{0}:元素存在，鼠标右击操作成功!!!".format(loc))

    def double_click(self, loc, timeout=30, frequency=0.5, annotation="", waitType="visible", isScroll=False):
        '''
        :func:鼠标双击操作
        :param loc: 元素表达式
        :param timeout: 等待最大时长，默认30秒
        :param frequency: 等待元素存在时，轮询周期0.5
        :param annotation: 代码注释
        :param waitType: 等待类型，默认等待其可见
        :param isScroll: 是否需要滚动，默认不需要
        :return:
        '''
        element = self.find_the_element(loc, timeout, frequency, annotation, waitType)
        ac = ActionChains(self.driver)

        if isScroll == True:
            self.scroll_IntoView(element)
        try:
            ac.double_click(element).perform()
        except:
            self.logger.exception("{0}:元素不存在，鼠标双击操作失败!!!".format(loc))
            self.failure_screenshots(annotation)
            raise
        else:
            self.logger.info("{0}:元素存在，鼠标双击操作成功!!!".format(loc))

    def mouse_release(self, loc, timeout=30, frequency=0.5, annotation="", waitType="visible", isScroll=False):
        '''
        :func:鼠标释放操作
        :param loc: 元组形式的元素表达式
        :param timeout: 等待最大时长，默认30秒
        :param frequency: 等待元素存在时，轮询周期0.5
        :param annotation: 代码注释
        :param waitType: 等待类型，默认等待其可见
        :param isScroll: 是否需要滚动，默认不需要
        :return:
        '''
        element = self.find_the_element(loc, timeout, frequency, annotation, waitType)
        ac = ActionChains(self.driver)

        if isScroll == True:
            self.scroll_IntoView(element)
        try:
            ac.release(element).perform()
        except:
            self.logger.exception("{0}:元素不存在，鼠标释放操作失败!!!".format(loc))
            self.failure_screenshots(annotation)
            raise
        else:
            self.logger.info("{0}:元素存在，鼠标释放操作成功!!!".format(loc))

    def switch_window(self, index, annotation=""):
        """
        :func: 窗口切换
        :param index: 切换窗口的下标
        :param annotation: 代码注释
        :return:
        """
        try:
            # 获取当前窗口的handles
            windows = self.driver.window_handles
            # 切换窗口
            self.driver.switch_to.window(windows[index])
        except:
            self.logger.exception("切换窗口失败!!!")
            self.failure_screenshots(annotation)
            raise
        # 回到主窗口页面
        # self.driver.switch_to.window(windows[0])

    def failure_screenshots(self, annotation=""):
        """
        :func: 页面截图
        :param annotation: 代码注释
        :return:
        """
        # file = 某页面_某操作_时间.png
        # 当前时间
        current_time = time.strftime("%Y%m%d_%H%M%S")
        filename = my_path.screen_file + "{0}_{1}.png".format(annotation, current_time)
        try:
            self.driver.save_screenshot(filename)
        except:
            self.logger.exception("网页截图操作失败!!!")
        else:
            self.logger.info("网页截图成功，截图存储路径为：{0}".format(filename))



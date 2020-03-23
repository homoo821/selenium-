# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/8
#File: user_log.py

import logging
from common.file_path import *

class UserLogs():
    def __init__(self):
        # 实例化日志收集器
        self.logger = logging.getLogger("homoo")
        # 设置输出格式
        formatter = logging.Formatter("%(asctime)s-%(levelname)s-%(filename)s-%(name)s-日志信息:%(message)s")
        # 输出渠道
        log_name = logs_path+"/user_logs.txt"
        self.f_handler = logging.FileHandler(log_name,encoding='utf-8')
        self.s_handler = logging.StreamHandler()

        self.f_handler.setFormatter(formatter)
        self.s_handler.setFormatter(formatter)
        # 指定输出渠道
        self.logger.addHandler(self.f_handler)
        self.logger.addHandler(self.s_handler)

    def user_log(self, msg, level='INFO'):
        # 设置级别
        self.logger.setLevel(level)
        # 收集日志
        if level == 'DEBUG':
            self.logger.debug(msg)
        elif level == 'INFO':
            self.logger.info(msg)
        elif level == 'WARNING':
            self.logger.warning(msg)
        elif level == 'ERROR':
            self.logger.error(msg)
        elif level == 'CRITICAL':
            self.logger.critical(msg)
        else:
            print('请核对你输入的日志级别！')
        # 关闭输出渠道
        self.logger.removeHandler(self.f_handler)
        self.logger.removeHandler(self.s_handler)

    # debug信息收集
    def debug(self,msg):
        self.user_log(msg,"DEBUG")

    # info信息收集
    def info(self,msg):
        self.user_log(msg,"INFO")

    # warning信息收集
    def warning(self, msg):
        self.user_log(msg, "WARNING")

    # error信息收集
    def error(self, msg):
        self.user_log(msg, "ERROR")

    # critical信息收集
    def critical(self, msg):
        self.user_log(msg, "CRITICAL")

    # excption信息收集
    def exception(self,msg):
        self.logger.exception(msg)
        # 关闭输出渠道
        self.logger.removeHandler(self.f_handler)
        self.logger.removeHandler(self.s_handler)

if __name__ == '__main__':
    UserLogs().debug("debug")
    UserLogs().info("info")
    UserLogs().warning("warning")
    UserLogs().error("error")
    UserLogs().critical("critical")
    try:
        6/0
    except:
        UserLogs().exception("sfaesfogwe")



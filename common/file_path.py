# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/8
#File: file_path.py


import os


pro_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

testdatas_path = os.path.join(pro_path,"TestDatas")

testcases_path = os.path.join(pro_path,"TestCases")

htmlreport_path = os.path.join(pro_path, 'Result/reports')

logs_path = os.path.join(pro_path, 'Result/logs')

screenshot_path = os.path.join(pro_path, 'Result/imgs')

# print(testdatas_path)
# print(testcases_path)
# print(htmlreport_path)
# print(logs_path)
# print(screenshot_path)


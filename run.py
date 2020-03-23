# -*- coding:utf-8 -*-
#Author: homoo
#Data: 2020/3/10
#File: run.py

import unittest
from common.HTMLTestReportEN import HTMLTestRunner
from common.file_path import *
from TestCase import test_login
from TestCase import test_invest

suite = unittest.TestSuite()
loader = unittest.TestLoader()
suite.addTest(loader.loadTestsFromModule(test_invest))
with open(test_report_path,'wb') as f:
    runner = HTMLTestRunner(stream=f,
                            verbosity=2,
                            title="test login",
                            description="this is the first test login",
                            tester="homoo")
    runner.run(suite)
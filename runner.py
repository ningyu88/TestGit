'''
@File:runner.py
@DateTime:2022/1/22 0022 18:27
@Author:xiaoning
@Desc:
'''

import unittest
from BeautifulReport import BeautifulReport

# suite = unittest.TestSuite()
# suite.addTests(unittest.defaultTestLoader.discover(start_dir=r'D:\KeJian\PyCharm_GZKJ\Ning\first\python_study\web_selenium_script\TestCases_script', pattern='test*.py'))
# test_runner = unittest.TextTestRunner
# test_runner.run(suite)


# 加载已经准备好的测试用例
cases = unittest.defaultTestLoader.discover(start_dir=r'/python_study/web_selenium_script/testcases', pattern='test*.py')
# 执行测试用例
result = BeautifulReport(cases)
# 生成测试报告
result.report(description='系统用户的测试报告', filename='ST测试报告', report_dir=r'/python_study/web_selenium_script/report')


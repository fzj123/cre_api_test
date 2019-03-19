import unittest

from BeautifulReport import BeautifulReport
import os
from tomorrow import threads
# 获取路径
curpath = os.path.dirname(os.path.realpath(__file__))
casepath = os.path.join(curpath, 'case')
reportpath = os.path.join(curpath, "report")


if not os.path.exists(reportpath):
    os.mkdir(reportpath)

def add_case(case_path=casepath, rule="*case.py"):
    '''加载所有的测试用例'''
    discover = unittest.defaultTestLoader.discover(case_path,
    pattern=rule,
    top_level_dir=None)
    return discover

def run(test_suit):

    result = BeautifulReport(test_suit)
    result.report(filename='TestReport.html', description='测试报告', log_path='report')

if __name__ == "__main__":
    # 用例集合
    cases = add_case()
    print(cases)
    for i in cases:
        print(i)
        run(i)


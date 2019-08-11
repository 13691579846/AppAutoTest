"""
------------------------------------
@Time : 2019/8/11 18:22
@Auth : linux超
@File : run.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import unittest
import os

from config.globalconf import CASE_DIR, REPORT_DIR, ENVIRONMENT
from common.dirAndTime import DirTime as Dt
from lib.HTMLTestRunner import HTMLTestRunner


def tc_suite():
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(
        start_dir=CASE_DIR,
        pattern="test_*.py"
    )
    suite.addTest(discover)
    return suite


def report_name():
    report_dir = REPORT_DIR
    if not os.path.exists(report_dir):
        report_dir = Dt.create_path(report_dir)
    html = Dt.file_name('html', 'report')
    return os.path.join(report_dir, html)


def main(report_path):
    suite = tc_suite()
    with open(report_path, 'wb') as f:
        runner = HTMLTestRunner(
            stream=f,
            description=ENVIRONMENT,
            title="app自动化测试",
            tester="linux超",
            verbosity=2
        )
        runner.run(suite)


if __name__ == '__main__':
    report = report_name()
    main(report)

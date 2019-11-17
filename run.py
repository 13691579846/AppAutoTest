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

from config.globalconf import (CASE_DIR, REPORT_DIR, LOG_DIR, ENVIRONMENT)
from common.dirAndTime import DirTime as Dt
from common.log import logger
from lib.HTMLTestRunner import HTMLTestRunner
# from BeautifulReport import BeautifulReport


report_dir = REPORT_DIR
log_dir = LOG_DIR


def tc_suite():
    logger.info("加载测试用例")
    suite = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(
        start_dir=CASE_DIR,
        pattern="test_invest.py"
    )
    suite.addTest(discover)
    return suite


def report_name():
    Dt.create_path(report_dir)
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
            verbosity=2,
            retry=0
        )
        runner.run(suite)
    logger.info("生成测试报告{}".format(report_path))


if __name__ == '__main__':
    Dt.create_path(log_dir)
    report = report_name()
    main(report)

"""
------------------------------------
@Time : 2019/8/8 22:33
@Auth : linux超
@File : test_invest.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import unittest
from ddt import ddt, data
import inspect

from common.log import logger
from datas.invest_data import InvestData
from cases.unitcase.rootcase import UnitTest


@ddt
class TestInvest(UnitTest):
    """投资"""
    invest_fail = InvestData.invest_fail
    invest_success = InvestData.invest_success

    def setUp(self):
        logger.info("开始执行测试用例")
        self.home_page.into_home_page()
        self.login_page.click_login_register_btn()
        self.login_page.login(self.phone, self.password)
        self.user_page.click_cancel()

    @data(*invest_fail)
    def test_invest_fail(self, amount):
        self.home_page.select_loan()
        self.invest_page.invest(amount["amount"])
        actual = self.invest_page.get_invest_toast("投资金额")
        try:
            self.assertEqual(amount["expected"], actual)
        except AssertionError as e:
            logger.debug("测试用例:{}->失败:{}".format(inspect.stack()[0][3], e))
            raise e
        else:
            logger.info("测试用例:{}->通过".format(inspect.stack()[0][3]))

    @data(*invest_success)
    def test_invest_success(self, amount):
        self.home_page.select_loan()
        self.invest_page.invest(amount["amount"])
        actual = self.invest_page.get_invest_success_massage
        try:
            self.assertEqual(amount["expected"], actual)
        except AssertionError as e:
            logger.debug("测试用例:{}->失败:{}".format(inspect.stack()[0][3], e))
            raise e
        else:
            logger.info("测试用例:{}->通过".format(inspect.stack()[0][3]))

    def tearDown(self):
        self.driver.reset()
        self.driver.start_activity(self.start_activity["package"], self.start_activity["activity"])
        logger.info("执行测试用例结束")


if __name__ == '__main__':
    unittest.main()

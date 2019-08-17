"""
------------------------------------
@Time : 2019/8/8 22:35
@Auth : linux超
@File : test_loan.py
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
from datas.loan_data import LoanData
from cases.unitcase.rootcase import UnitTest


@ddt
class TestLoan(UnitTest):
    """借款"""
    loan_amount_fail_data = LoanData.loan_amount_none
    loan_amount_success_data = LoanData.loan_amount_success
    loan_fail_data = LoanData.loan_lack_required_items
    loan_success_data = LoanData.loan_success

    def setUp(self):
        logger.info("开始执行测试用例")
        self.home_page.into_home_page()
        self.login_page.click_login_register_btn()
        self.login_page.login(self.phone, self.password)
        self.user_page.click_cancel()
        self.home_page.click_loan_btn()

    @data(*loan_amount_fail_data)
    def test_loan_amount_fail(self, amount):
        self.loan_page.loan_amount(amount["amount"])
        actual = self.loan_page.get_fail_massage
        try:
            self.assertEqual(amount["expected"], actual)
        except AssertionError as e:
            logger.debug("测试用例:{}->失败:{}".format(inspect.stack()[0][3], e))
            self.loan_page.screen_shot("amount_error")
            raise e
        else:
            logger.info("测试用例:{}->通过".format(inspect.stack()[0][3]))

    @data(*loan_amount_success_data)
    def test_loan_amount_success(self, amount):
        self.loan_page.loan_amount(amount["amount"])
        actual = self.loan_page.get_submit_text
        try:
            self.assertEqual(amount["expected"], actual)
        except AssertionError as e:
            logger.debug("测试用例:{}->失败:{}".format(inspect.stack()[0][3], e))
            self.loan_page.screen_shot("amount_success")
            raise e
        else:
            logger.info("测试用例:{}->通过".format(inspect.stack()[0][3]))

    @data(*loan_fail_data)
    def test_loan_lack_required_items(self, loan):
        self.loan_page.loan_amount(loan["amount"])
        self.loan_page.loan_business(loan["rate"],
                                     loan["bidding"],
                                     loan["uses"],
                                     loan["limit"],
                                     loan["day_mouth"],
                                     loan["payment"],
                                     loan["address"]
                                     )
        actual = self.loan_page.get_fail_massage
        try:
            self.assertEqual(loan["expected"], actual)
        except AssertionError as e:
            logger.debug("测试用例:{}->失败:{}".format(inspect.stack()[0][3], e))
            self.loan_page.screen_shot("lack_required")
            raise e
        else:
            logger.info("测试用例:{}->通过".format(inspect.stack()[0][3]))

    @data(*loan_success_data)
    def test_loan_success(self, loan):
        self.loan_page.loan_amount(loan["amount"])
        self.loan_page.loan_business(loan["rate"],
                                     loan["bidding"],
                                     loan["uses"],
                                     loan["limit"],
                                     loan["day_mouth"],
                                     loan["payment"],
                                     loan["address"]
                                     )
        actual = self.loan_page.get_loan_success_info
        try:
            self.assertEqual(loan["expected"], actual)
        except AssertionError as e:
            logger.debug("测试用例:{}->失败:{}".format(inspect.stack()[0][3], e))
            self.loan_page.screen_shot("loan_success")
            raise e
        else:
            logger.info("测试用例:{}->通过".format(inspect.stack()[0][3]))

    def tearDown(self):
        self.driver.reset()
        logger.info("执行测试用例结束")


if __name__ == '__main__':
    unittest.main()

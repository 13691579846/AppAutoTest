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
from appium import webdriver

from config.globalconf import YML_PATH, APK_PATH
from common.parseYaml import ParseYml
from pages.loan_page import LoanPage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.user_page import UserPage
from datas.loan_data import LoanData

phone = "13691579846"
password = "****"


@ddt
class TestLoan(unittest.TestCase):
    """借款"""
    yml = ParseYml(YML_PATH)
    loan_amount_fail_data = LoanData.loan_amount_none
    loan_amount_success_data = LoanData.loan_amount_success
    loan_fail_data = LoanData.loan_fail
    loan_success_data = LoanData.loan_success

    @classmethod
    def setUpClass(cls):
        desired = cls.yml.read_alone
        desired["app"] = APK_PATH
        cls.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                                      desired_capabilities=desired)
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.user_page = UserPage(cls.driver)
        cls.loan_page = LoanPage(cls.driver)
        cls.user_page = UserPage(cls.driver)

    def setUp(self):
        self.home_page.into_home_page()
        self.login_page.click_login_register_btn()
        self.login_page.login(phone, password)
        self.user_page.click_cancel()
        self.home_page.click_loan_btn()

    @data(*loan_amount_fail_data)
    def test_loan_amount_fail(self, amount):
        self.loan_page.loan_amount(amount["amount"])
        actual = self.loan_page.get_fail_massage
        self.assertEqual(amount["expected"], actual)

    @data(*loan_amount_success_data)
    def test_loan_amount_success(self, amount):
        self.loan_page.loan_amount(amount["amount"])
        actual = self.loan_page.get_submit_text
        self.assertEqual(amount["expected"], actual)

    @data(*loan_fail_data)
    def test_loan_fail(self, loan):
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
        self.assertEqual(loan["expected"], actual)

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
        self.assertEqual(loan["expected"], actual)

    def tearDown(self):
        self.driver.reset()
        self.driver.start_activity('com.xxzb.fenwoo', ".activity.addition.SplashActivity")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

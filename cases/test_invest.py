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
from appium import webdriver

from common.parseYaml import ParseYml
from config.globalconf import APK_PATH, YML_PATH
from pages.home_page import HomePage
from pages.invest_page import InvestPage
from pages.login_page import LoginPage
from pages.user_page import UserPage
from datas.invest_data import InvestData

phone = "13691579846"
password = "****"


@ddt
class TestInvest(unittest.TestCase):
    """投资"""
    conf = ParseYml(YML_PATH)
    invest_fail = InvestData.invest_fail
    invest_success = InvestData.invest_success

    @classmethod
    def setUpClass(cls):
        desired = cls.conf.read_alone
        desired["app"] = APK_PATH
        cls.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                                      desired_capabilities=desired)
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.user_page = UserPage(cls.driver)
        cls.invest_page = InvestPage(cls.driver)

    def setUp(self):
        self.home_page.into_home_page()
        self.login_page.click_login_register_btn()
        self.login_page.login("13691579846", 'xiaochao11520')
        self.user_page.click_cancel()

    @data(*invest_fail)
    def test_invest_fail(self, amount):
        self.home_page.select_loan()
        self.invest_page.invest(amount["amount"])
        actual = self.invest_page.get_invest_toast(amount["expected"])
        self.assertEqual(amount["expected"], actual)

    @data(*invest_success)
    def test_invest_success(self, amount):
        self.home_page.select_loan()
        self.invest_page.invest(amount["amount"])
        actual = self.invest_page.get_invest_success_massage
        self.assertEqual(amount["expected"], actual)

    def tearDown(self):
        self.driver.reset()
        self.driver.start_activity('com.xxzb.fenwoo', ".activity.addition.SplashActivity")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

"""
------------------------------------
@Time : 2019/8/14 14:14
@Auth : linux超
@File : rootcase.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import unittest
from appium import webdriver

from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.loan_page import LoanPage
from pages.user_page import UserPage
from pages.invest_page import InvestPage
from pages.register_page import RegisterPage
from common.parseYaml import ParseYml
from config.globalconf import YML_PATH, APK_PATH


class UnitTest(unittest.TestCase):
    driver = None
    conf = ParseYml(YML_PATH)
    start_activity = {"package": "com.xxzb.fenwoo", "activity": ".activity.addition.SplashActivity"}
    phone = "13691579846"
    password = "xiaochao11520"

    @classmethod
    def setUpClass(cls):
        desired = cls.conf.read_alone
        desired["app"] = APK_PATH
        cls.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                                      desired_capabilities=desired)
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)
        cls.loan_page = LoanPage(cls.driver)
        cls.user_page = UserPage(cls.driver)
        cls.invest_page = InvestPage(cls.driver)
        cls.register_page = RegisterPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    pass

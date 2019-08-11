"""
------------------------------------
@Time : 2019/8/1 14:44
@Auth : linux超
@File : test_login.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import unittest
import ddt
from appium import webdriver

from common.parseYaml import ParseYml
from config.globalconf import APK_PATH, YML_PATH
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from pages.user_page import UserPage
from datas.login_data import LoginData


@ddt.ddt
class TestLogin(unittest.TestCase):
    """登录"""
    conf = ParseYml(YML_PATH)
    phone_incorrect_data = LoginData.login_phone_incorrect
    phone_format_incorrect = LoginData.login_phone_format_incorrect
    phone_registered = LoginData.login_phone_registered
    phone_unregister = LoginData.login_phone_unregister
    password_error = LoginData.login_password_error
    login_success = LoginData.login_success

    @classmethod
    def setUpClass(cls):
        desired = cls.conf.read_alone
        desired["app"] = APK_PATH
        cls.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                                      desired_capabilities=desired)

    def setUp(self):
        self.home_page = HomePage(self.driver)
        self.login_page = LoginPage(self.driver)
        self.home_page.into_home_page()

    # 点击[登录/注册]登录流程
    @ddt.data(*phone_incorrect_data)
    def test_login_phone_incorrect(self, login_dict):
        self.login_page.click_login_register_btn()
        self.login_page.login_phone(login_dict["phone"])
        actual = self.login_page.get_phone_error_info
        self.assertEqual(login_dict["expected"], actual)

    @unittest.expectedFailure
    @ddt.data(*phone_format_incorrect)
    def test_login_phone_format_incorrect(self, login_dict):
        self.login_page.click_login_register_btn()
        self.login_page.login_phone(login_dict["phone"])
        actual = self.login_page.get_phone_format_incorrect
        self.assertEqual(login_dict["expected"], actual)

    @ddt.data(*phone_registered)
    def test_login_phone_registered(self, login_dict):
        self.login_page.click_login_register_btn()
        self.login_page.login_phone(login_dict["phone"])
        actual = self.login_page.get_password_label_info
        self.assertEqual(login_dict["expected"], actual)

    @ddt.data(*phone_unregister)
    def test_login_phone_unregister(self, login_dict):
        register_page = RegisterPage(self.driver)
        self.login_page.click_login_register_btn()
        self.login_page.login_phone(login_dict["phone"])
        actual = register_page.get_register_text
        self.assertEqual(login_dict["expected"], actual)

    @ddt.data(*password_error)
    def test_login_password_error(self, login_dict):
        self.login_page.click_login_register_btn()
        self.login_page.login(login_dict["phone"], login_dict["password"])
        actual = self.login_page.get_password_error_info
        self.assertEqual(login_dict["expected"], actual)

    @ddt.data(*login_success)
    def test_a_login_success(self, login_dict):
        user_page = UserPage(self.driver)
        self.login_page.click_login_register_btn()
        self.login_page.login(login_dict["phone"], login_dict["password"])
        user_page.click_cancel()
        self.home_page.click_myself()
        actual = user_page.get_name
        self.assertIn(login_dict["expected"], actual)

    def tearDown(self):
        self.driver.reset()
        self.driver.start_activity('com.xxzb.fenwoo', ".activity.addition.SplashActivity")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

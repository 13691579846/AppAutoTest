"""
------------------------------------
@Time : 2019/8/10 16:04
@Auth : linux超
@File : test_register.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import unittest
import ddt
from appium import webdriver

from config.globalconf import APK_PATH, YML_PATH
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from datas.register_data import RegisterData
from common.parseYaml import ParseYml


@ddt.ddt
class TestRegister(unittest.TestCase):
    """注册"""
    conf = ParseYml(YML_PATH)
    code_agree_pwd_error = RegisterData.code_agree_pwd_error
    code_pwd_incorrect = RegisterData.code_pwd_incorrect

    @classmethod
    def setUpClass(cls):
        desired = cls.conf.read_alone
        desired["app"] = APK_PATH
        cls.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                                      desired_capabilities=desired)
        cls.register_page = RegisterPage(cls.driver)
        cls.home_page = HomePage(cls.driver)
        cls.login_page = LoginPage(cls.driver)

    def setUp(self):
        self.home_page.into_home_page()
        self.login_page.click_login_register_btn()
        self.login_page.login_phone('13274517393')

    @ddt.data(*code_pwd_incorrect)
    def test_register_fail_1(self, register_dict):
        self.register_page.register(register_dict["code"],
                                    register_dict["login_pwd"],
                                    register_dict["verify_pwd"],
                                    register_dict["agree"],
                                    )
        actual = self.register_page.get_register_fail_massage
        self.assertEqual(register_dict["expected"], actual)

    @unittest.expectedFailure
    @ddt.data(*code_agree_pwd_error)
    def test_register_fail_2(self, register_dict):
        self.register_page.register(register_dict["code"],
                                    register_dict["login_pwd"],
                                    register_dict["verify_pwd"],
                                    register_dict["agree"],
                                    )
        actual = self.register_page.get_register_toast_massage
        self.assertIn(register_dict["expected"], actual)

    def tearDown(self):
        self.driver.reset()
        self.driver.start_activity('com.xxzb.fenwoo', ".activity.addition.SplashActivity")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == '__main__':
    unittest.main()

"""
------------------------------------
@Time : 2019/8/1 9:47
@Auth : linux超
@File : test_lemon.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import time
from appium import webdriver
import unittest
from appium.webdriver.common.mobileby import MobileBy


from config.globalconf import APK_PATH
from pages.base.base import Base


class TestLemon(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        desired = {
            "platformName": "Android",
            "platformVersion": '5.1.1',
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.xxzb.fenwoo",
            "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
            "app": APK_PATH,
            "unicodeKeyboard": True,  # 屏蔽键盘
            "resetKeyboard": True
        }
        cls.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                                       desired_capabilities=desired)
    def setUp(self):
        time.sleep(3)
        self.base = Base(self.driver)
        x = 4
        for _ in range(x):
            self.base.swipe_left()
        start_element = self.base.find_element((MobileBy.ID, "com.xxzb.fenwoo:id/btn_start"))
        start_element.click()

    def test_lemon(self):
        self.assertLessEqual(1, 1)

    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()

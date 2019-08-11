"""
------------------------------------
@Time : 2019/8/6 20:47
@Auth : linux超
@File : test.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import time
import unittest
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy

from base import Base


class TestGesture(unittest.TestCase):

    def setUp(self):
        desired = {
            "automationName": "uiautomator1",
            "platformName": "Android",
            "platformVersion": '5.1.1',
            "deviceName": "127.0.0.1:62001",
            "appPackage": "com.xxzb.fenwoo",
            "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
            "app": r"D:\AppAutoTest\appPackage\Future-release-2018.apk",
            "unicodeKeyboard": True,  # 屏蔽键盘
            "resetKeyboard": True
        }
        self.driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                                       desired_capabilities=desired)
        self.base = Base(self.driver)

    def test_gesture_password(self):
        self.base.skip_welcome_page('left', 3)  # 滑动屏幕
        time.sleep(3)  # 为了看滑屏的效果
        self.driver.start_activity(app_package="com.xxzb.fenwoo",
                                   app_activity=".activity.user.CreateGesturePwdActivity")
        commit_btn = (MobileBy.ID, 'com.xxzb.fenwoo:id/right_btn')
        password_gesture = (MobileBy.ID, 'com.xxzb.fenwoo:id/gesturepwd_create_lockview')
        element_commit = self.base.find_element(commit_btn)
        element_commit.click()
        password_element = self.base.find_element(password_gesture)
        self.base.gesture_password(password_element, 1, 2, 3, 6, 5, 4, 7, 8, 9)
        time.sleep(5)  # 看效果

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()

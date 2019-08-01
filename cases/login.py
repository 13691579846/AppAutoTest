"""
------------------------------------
@Time : 2019/8/1 14:44
@Auth : linux超
@File : login.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from appium import webdriver
import unittest

from config.globalconf import APK_PATH


desired = {
    "platformName": "Android",
    "platformVersion": '5.1.1',
    "deviceName": "127.0.0.1:62001",
    "appPackage": "com.xxzb.fenwoo",
    "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
    "app": APK_PATH
}
driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub",
                               desired_capabilities=desired)

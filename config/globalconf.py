"""
------------------------------------
@Time : 2019/8/1 9:48
@Auth : linux超
@File : globalconf.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import os


ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(ROOT_DIR)
APP_DIR = os.path.join(ROOT_DIR, "appPackage")
print(APP_DIR)
APK_PATH = os.path.join(APP_DIR, "Future-release-2018.apk")
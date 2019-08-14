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
import platform

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
APP_DIR = os.path.join(ROOT_DIR, "appPackage")
IMG_DIR = os.path.join(ROOT_DIR, "img")
CASE_DIR = os.path.join(ROOT_DIR, 'cases')
CONF_DIR = os.path.join(ROOT_DIR, 'config')
DATA_DIR = os.path.join(ROOT_DIR, 'datas')
REPORT_DIR = os.path.join(ROOT_DIR, "report")
LOG_DIR = os.path.join(ROOT_DIR, 'log')
APK_PATH = os.path.join(APP_DIR, "Future-release-2018.apk")
YML_PATH = os.path.join(CONF_DIR, "config.yml")
ENVIRONMENT = \
    "Windows Version:" + \
    platform.system() + \
    platform.version() + \
    platform.release() + \
    "Python Version" + \
    platform.python_build()[0]

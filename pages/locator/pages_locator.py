"""
------------------------------------
@Time : 2019/8/1 17:13
@Auth : linux超
@File : pages_locator.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from appium.webdriver.common.mobileby import MobileBy


class HomePageLocator(object):

    welcome_btn = \
        (MobileBy.ID, 'com.xxzb.fenwoo:id/btn_start')
    home_btn = \
        (MobileBy.XPATH, r'//android.widget.TabWidget[@resource-id=\"android:id/tabs\"]/android.widget.LinearLayout[1]')
    project_btn = \
        (MobileBy.XPATH, r'//android.widget.TabWidget[@resource-id=\"android:id/tabs\"]/android.widget.LinearLayout[2]')
    found_btn = \
        (MobileBy.XPATH, r'//android.widget.TabWidget[@resource-id=\"android:id/tabs\"]/android.widget.LinearLayout[3]')
    myself_btn = \
        (MobileBy.XPATH, r'//android.widget.TabWidget[@resource-id=\"android:id/tabs\"]/android.widget.LinearLayout[4]')


if __name__ == '__main__':
    pass
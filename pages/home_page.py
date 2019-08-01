"""
------------------------------------
@Time : 2019/8/1 17:11
@Auth : linux超
@File : home_page.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from pages.base.base import Base
from pages.locator.pages_locator import HomePageLocator


class HomePage(Base):
    locator = HomePageLocator

    def click_myself(self):
        self.click(self.locator.myself_btn)

    def click_welcome(self):
        self.click(self.locator.welcome_btn)

    def skip_welcome_page(self):
        for _ in range(4):
            self.swipe_left()

if __name__ == '__main__':
    pass
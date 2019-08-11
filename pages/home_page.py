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
from .base.base import Base
from .locator.pages_locator import HomePageLocator as Locator


class HomePage(Base):

    def into_home_page(self):
        self.skip_start_page()
        return self.click_welcome()

    def skip_start_page(self):
        return self.skip_welcome_page("left")

    def click_myself(self):
        return self.click(Locator.myself_btn)

    def click_welcome(self):
        return self.click(Locator.welcome_btn)

    def select_loan(self):
        return self.click(Locator.invest_btn)

    def click_more(self):
        return self.click(Locator.more_loan)

    def click_loan_btn(self):
        return self.click(Locator.loan_btn)


if __name__ == '__main__':
    pass

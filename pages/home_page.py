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
from common.log import logger


class HomePage(Base):

    def into_home_page(self):
        self.skip_start_page()
        return self.click_welcome()

    def skip_start_page(self):
        logger.info("跳过欢迎页")
        return self.skip_welcome_page("left")

    def click_myself(self):
        logger.info("点击[我的]菜单")
        return self.click(Locator.myself_btn)

    def click_welcome(self):
        logger.info("点击[立即体验]按钮")
        return self.click(Locator.welcome_btn)

    def select_loan(self):
        logger.info("点击[投标]按钮")
        return self.click(Locator.invest_btn)

    def click_more(self):
        logger.info("点击[...]加载更多标")
        return self.click(Locator.more_loan)

    def click_loan_btn(self):
        logger.info("点击[我要借款]按钮")
        return self.click(Locator.loan_btn)


if __name__ == '__main__':
    pass

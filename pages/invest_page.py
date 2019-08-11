"""
------------------------------------
@Time : 2019/8/10 21:16
@Auth : linux超
@File : invest_page.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from .base.base import Base
from .locator.pages_locator import InvestPageLocator as Locator


class InvestPage(Base):

    def invest(self, amount):
        if amount:
            self.input_invest_amount(amount)
        return self.click_invest_btn()

    def input_invest_amount(self, amount):
        return self.input_value(Locator.amount_view, amount)

    def click_invest_btn(self):
        return self.click(Locator.invest_now_btn)

    def get_invest_toast(self, message):
        return self.get_toast(message)

    @property
    def get_invest_success_massage(self):
        return self.get_element_text(Locator.invest_success_massage)


if __name__ == '__main__':
    pass

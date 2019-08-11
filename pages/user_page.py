"""
------------------------------------
@Time : 2019/8/10 16:11
@Auth : linux超
@File : user_page.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from .base.base import Base
from .locator.pages_locator import UserPageLocator as Locator


class UserPage(Base):

    @property
    def get_name(self):
        return self.get_element_text(Locator.my_name)

    def click_cancel(self):
        return self.click(Locator.cancel_btn)

    def click_confirm(self):
        return self.click(Locator.confirm_btn)

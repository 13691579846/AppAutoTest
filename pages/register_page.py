"""
------------------------------------
@Time : 2019/8/10 12:12
@Auth : linux超
@File : register_page.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from .base.base import Base
from .locator.pages_locator import RegisterLocator as Locator


class RegisterPage(Base):

    def register(self, code, login_pwd, verify_pwd, agree):
        if code:
            self.input_verify_code(code)
        if login_pwd:
            self.input_login_password(login_pwd)
        if verify_pwd:
            self.input_verify_password(verify_pwd)
        if agree:
            self.click_agree()
        return self.click_register_btn()

    @property
    def get_register_text(self):
        return self.get_element_text(Locator.register_btn)

    def input_verify_code(self, code):
        return self.input_value(Locator.verify_code, code)

    def input_login_password(self, password):
        return self.input_value(Locator.login_password, password)

    def input_verify_password(self, password):
        return self.input_value(Locator.confirm_password, password)

    def click_agree(self):
        return self.click(Locator.agree_btn)

    def click_register_btn(self):
        return self.click(Locator.register_btn)

    @property
    def get_register_fail_massage(self):
        return self.get_element_text(Locator.register_message)

    @property
    def get_register_toast_massage(self):
        return self.get_toast("验证码错误或已过期")

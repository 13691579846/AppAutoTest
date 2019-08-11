"""
------------------------------------
@Time : 2019/8/1 9:48
@Auth : linux超
@File : login_page.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
from .base.base import Base
from .locator.pages_locator import LoginLocator as Locator


class LoginPage(Base):

    def login(self, username, password):
        self.input_username(username)
        self.click_next_setup()
        self.input_password(password)
        return self.click_commit_btn()

    def login_phone(self, phone):
        self.input_username(phone)
        return self.click_next_setup()

    def click_login_register_btn(self):
        return self.click(Locator.login_register_btn)

    def input_username(self, phone):
        return self.input_value(Locator.phone_input, phone)

    @property
    def get_phone_error_info(self):
        return self.get_element_text(Locator.invalid_phone)

    def click_next_setup(self):
        return self.click(Locator.next_step)

    def input_password(self, password):
        return self.input_value(Locator.password_view, password)

    @property
    def get_password_label_info(self):
        return self.get_element_text(Locator.password_label)

    def click_commit_btn(self):
        return self.click(Locator.commit_btn)

    @property
    def get_password_error_info(self):
        return self.get_element_text(Locator.password_warn)

    @property
    def get_phone_format_incorrect(self):
        return self.get_toast("手机号码格式不正确")


if __name__ == '__main__':
    pass

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
from common.log import logger


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
        logger.info("获取[注册]按钮文本信息")
        return self.get_element_text(Locator.register_btn)

    def input_verify_code(self, code):
        logger.info("输入[验证码]{}".format(code))
        return self.input_value(Locator.verify_code, code)

    def input_login_password(self, password):
        logger.info("输入[登录密码]{}".format(password))
        return self.input_value(Locator.login_password, password)

    def input_verify_password(self, password):
        logger.info("输入[确认密码]{}".format(password))
        return self.input_value(Locator.confirm_password, password)

    def click_agree(self):
        logger.info("点击[我已阅读并同意]按钮")
        return self.click(Locator.agree_btn)

    def click_register_btn(self):
        logger.info("点击[注册]按钮")
        return self.click(Locator.register_btn)

    @property
    def get_register_fail_massage(self):
        logger.info("获取注册失败的提示信息")
        return self.get_element_text(Locator.register_message)

    @property
    def get_code_incorrect(self):
        logger.info("获取验证码错误时toast信息")
        return self.get_toast("验证码错误或已过期")

    @property
    def get_non_agree(self):
        logger.info("获取不勾选协议时toast信息")
        return self.get_toast("请阅读并同意")

    @property
    def get_password_format_incorrect(self):
        logger.info("获取密码格式错误时toast信息")
        return self.get_toast("密码格式错误")

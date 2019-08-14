"""
------------------------------------
@Time : 2019/8/10 16:04
@Auth : linux超
@File : test_register.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import unittest
import ddt

from datas.register_data import RegisterData
from common.log import logger
from cases.unitcase.rootcase import UnitTest


@ddt.ddt
class TestRegister(UnitTest):
    """注册"""
    unregister_phone = RegisterData.phone
    code_agree_pwd_error = RegisterData.code_agree_pwd_error
    code_pwd_incorrect = RegisterData.code_pwd_incorrect

    def setUp(self):
        self.home_page.into_home_page()
        self.login_page.click_login_register_btn()
        self.login_page.login_phone(self.unregister_phone)

    @ddt.data(*code_pwd_incorrect)
    def test_register_fail_1(self, register_dict):
        self.register_page.register(register_dict["code"],
                                    register_dict["login_pwd"],
                                    register_dict["verify_pwd"],
                                    register_dict["agree"],
                                    )
        actual = self.register_page.get_register_fail_massage
        try:
            self.assertEqual(register_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("fail")
            raise e
        else:
            logger.info("pass")

    @unittest.expectedFailure
    @ddt.data(*code_agree_pwd_error)
    def test_register_fail_2(self, register_dict):
        self.register_page.register(register_dict["code"],
                                    register_dict["login_pwd"],
                                    register_dict["verify_pwd"],
                                    register_dict["agree"],
                                    )
        actual = self.register_page.get_register_toast_massage
        try:
            self.assertIn(register_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("fail")
            raise e
        else:
            logger.info("pass")

    def tearDown(self):
        self.driver.reset()
        self.driver.start_activity(self.start_activity["package"], self.start_activity["activity"])


if __name__ == '__main__':
    unittest.main()

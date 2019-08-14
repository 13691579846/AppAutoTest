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
import inspect

from datas.register_data import RegisterData
from common.log import logger
from cases.unitcase.rootcase import UnitTest


@ddt.ddt
class TestRegister(UnitTest):
    """注册"""
    unregister_phone = RegisterData.phone
    code_incorrect = RegisterData.code_incorrect
    lack_required_items = RegisterData.lack_required_items
    non_agree = RegisterData.non_agree
    password_format_error = RegisterData.password_format_error

    def setUp(self):
        logger.info("开始执行测试用例")
        self.home_page.into_home_page()
        self.login_page.click_login_register_btn()
        self.login_page.login_phone(self.unregister_phone)

    @ddt.data(*lack_required_items)
    def test_lack_required_items(self, register_dict):
        self.register_page.register(register_dict["code"],
                                    register_dict["login_pwd"],
                                    register_dict["verify_pwd"],
                                    register_dict["agree"],
                                    )
        actual = self.register_page.get_register_fail_massage
        try:
            self.assertEqual(register_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("测试用例:{}->失败:{}".format(inspect.stack()[0][3], e))
            raise e
        else:
            logger.info("测试用例:{}->通过".format(inspect.stack()[0][3]))

    @ddt.data(*code_incorrect)
    def test_code_incorrect(self, register_dict):
        self.register_page.register(register_dict["code"],
                                    register_dict["login_pwd"],
                                    register_dict["verify_pwd"],
                                    register_dict["agree"],
                                    )
        actual = self.register_page.get_code_incorrect
        try:
            self.assertIn(register_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("测试用例:{}->失败:{}".format(inspect.stack()[0][3], e))
            raise e
        else:
            logger.info("测试用例:{}->通过".format(inspect.stack()[0][3]))

    @ddt.data(*non_agree)
    def test_non_agree(self, register_dict):
        self.register_page.register(register_dict["code"],
                                    register_dict["login_pwd"],
                                    register_dict["verify_pwd"],
                                    register_dict["agree"],
                                    )
        actual = self.register_page.get_non_agree
        try:
            self.assertIn(register_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("测试用例:{}->失败:{}".format(inspect.stack()[0][3], e))
            raise e
        else:
            logger.info("测试用例:{}->通过".format(inspect.stack()[0][3]))

    @ddt.data(*password_format_error)
    def test_pwd_format_error(self, register_dict):
        self.register_page.register(register_dict["code"],
                                    register_dict["login_pwd"],
                                    register_dict["verify_pwd"],
                                    register_dict["agree"],
                                    )
        actual = self.register_page.get_password_format_incorrect
        try:
            self.assertIn(register_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("测试用例:{}->失败:{}".format(inspect.stack()[0][3], e))
            raise e
        else:
            logger.info("测试用例:{}->通过".format(inspect.stack()[0][3]))

    def tearDown(self):
        self.driver.reset()
        self.driver.start_activity(self.start_activity["package"], self.start_activity["activity"])
        logger.info("测试用例执行结束")


if __name__ == '__main__':
    unittest.main()

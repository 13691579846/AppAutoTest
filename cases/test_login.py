"""
------------------------------------
@Time : 2019/8/1 14:44
@Auth : linux超
@File : test_login.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import unittest
import ddt

from common.log import logger
from datas.login_data import LoginData
from cases.unitcase.rootcase import UnitTest


@ddt.ddt
class TestLogin(UnitTest):
    """登录"""
    phone_incorrect_data = LoginData.login_phone_incorrect
    phone_format_incorrect = LoginData.login_phone_format_incorrect
    phone_registered = LoginData.login_phone_registered
    phone_unregister = LoginData.login_phone_unregister
    password_error = LoginData.login_password_error
    password_null = LoginData.login_password_null
    login_success = LoginData.login_success

    def setUp(self):
        self.home_page.into_home_page()

    # 点击[登录/注册]登录流程
    @ddt.data(*phone_incorrect_data)
    def test_login_phone_incorrect(self, login_dict):
        self.login_page.click_login_register_btn()
        self.login_page.login_phone(login_dict["phone"])
        actual = self.login_page.get_phone_error_info
        try:
            self.assertEqual(login_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("fail")
            raise e
        else:
            logger.info("pass")

    @unittest.expectedFailure
    @ddt.data(*phone_format_incorrect)
    def test_login_phone_format_incorrect(self, login_dict):
        self.login_page.click_login_register_btn()
        self.login_page.login_phone(login_dict["phone"])
        actual = self.login_page.get_phone_format_incorrect
        try:
            self.assertEqual(login_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("fail")
            raise e
        else:
            logger.info("pass")

    @ddt.data(*phone_registered)
    def test_login_phone_registered(self, login_dict):
        self.login_page.click_login_register_btn()
        self.login_page.login_phone(login_dict["phone"])
        actual = self.login_page.get_password_label_info
        try:
            self.assertEqual(login_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("fail")
            raise e
        else:
            logger.info("pass")

    @ddt.data(*phone_unregister)
    def test_login_phone_unregister(self, login_dict):
        self.login_page.click_login_register_btn()
        self.login_page.login_phone(login_dict["phone"])
        actual = self.register_page.get_register_text
        try:
            self.assertEqual(login_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("fail")
            raise e
        else:
            logger.info("pass")

    @ddt.data(*password_error)
    def test_login_password_error(self, login_dict):
        self.login_page.click_login_register_btn()
        self.login_page.login(login_dict["phone"], login_dict["password"])
        actual = self.login_page.get_password_error_info
        try:
            self.assertEqual(login_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("fail")
            raise e
        else:
            logger.info("pass")

    @ddt.data(*password_null)
    def test_login_password_null(self, login_dict):
        self.login_page.click_login_register_btn()
        self.login_page.login(login_dict["phone"], login_dict["password"])
        actual = self.login_page.assert_commit_is_exist
        try:
            self.assertTrue(login_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("fail")
            raise e
        else:
            logger.info("pass")

    @ddt.data(*login_success)
    def test_a_login_success(self, login_dict):
        self.login_page.click_login_register_btn()
        self.login_page.login(login_dict["phone"], login_dict["password"])
        self.user_page.click_cancel()
        self.home_page.click_myself()
        actual = self.user_page.get_name
        try:
            self.assertIn(login_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("fail")
            raise e
        else:
            logger.info("pass")

    # 点击[我的]登录流程
    @ddt.data(*phone_incorrect_data)
    def test_myself_phone_incorrect(self, login_dict):
        self.home_page.click_myself()
        self.login_page.login_phone(login_dict["phone"])
        actual = self.login_page.get_phone_error_info
        try:
            self.assertEqual(login_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("fail")
            raise e
        else:
            logger.info("pass")

    @unittest.expectedFailure
    @ddt.data(*phone_format_incorrect)
    def test_myself_phone_format_incorrect(self, login_dict):
        self.home_page.click_myself()
        self.login_page.login_phone(login_dict["phone"])
        actual = self.login_page.get_phone_format_incorrect
        try:
            self.assertEqual(login_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("fail")
            raise e
        else:
            logger.info("pass")

    @ddt.data(*phone_registered)
    def test_myself_phone_registered(self, login_dict):
        self.home_page.click_myself()
        self.login_page.login_phone(login_dict["phone"])
        actual = self.login_page.get_password_label_info
        try:
            self.assertEqual(login_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("fail")
            raise e
        else:
            logger.info("pass")

    @ddt.data(*phone_unregister)
    def test_myself_phone_unregister(self, login_dict):
        self.home_page.click_myself()
        self.login_page.login_phone(login_dict["phone"])
        actual = self.register_page.get_register_text
        try:
            self.assertEqual(login_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("fail")
            raise e
        else:
            logger.info("pass")

    @ddt.data(*password_error)
    def test_myself_password_error(self, login_dict):
        self.home_page.click_myself()
        self.login_page.login(login_dict["phone"], login_dict["password"])
        actual = self.login_page.get_password_error_info
        try:
            self.assertEqual(login_dict["expected"], actual)
        except AssertionError as e:
            logger.debug("fail")
            raise e
        else:
            logger.info("pass")

    @ddt.data(*login_success)
    def test_myself_login_success(self, login_dict):
        self.home_page.click_myself()
        self.login_page.login(login_dict["phone"], login_dict["password"])
        self.user_page.click_cancel()
        actual = self.user_page.get_name
        try:
            self.assertIn(login_dict["expected"], actual)
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

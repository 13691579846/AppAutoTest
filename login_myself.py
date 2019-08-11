"""
------------------------------------
@Time : 2019/8/10 18:31
@Auth : linux超
@File : login_myself.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
# # 点击[我的]登录流程
# @ddt.data(*phone_incorrect_data)
# def test_myself_phone_incorrect(self, login_dict):
#     # self.home_page.skip_welcome_page('left')
#     # self.home_page.click_welcome()
#     self.home_page.click_myself()
#     self.login_page.login_phone(login_dict["phone"])
#     actual = self.login_page.get_phone_error_info
#     self.assertEqual(login_dict["expected"], actual)

# @unittest.expectedFailure
# @ddt.data(*phone_format_incorrect)
# def test_myself_phone_format_incorrect(self, login_dict):
#     # self.home_page.skip_welcome_page('left')
#     # self.home_page.click_welcome()
#     self.home_page.click_myself()
#     self.login_page.login_phone(login_dict["phone"])
#     actual = self.login_page.get_phone_format_incorrect
#     self.assertEqual(login_dict["expected"], actual)
#
# @ddt.data(*phone_registered)
# def test_myself_phone_registered(self, login_dict):
#     # self.home_page.skip_welcome_page('left')
#     # self.home_page.click_welcome()
#     self.home_page.click_myself()
#     self.login_page.login_phone(login_dict["phone"])
#     actual = self.login_page.get_password_label_info
#     self.assertEqual(login_dict["expected"], actual)
#
# @ddt.data(*phone_unregister)
# def test_myself_phone_unregister(self, login_dict):
#     register_page = RegisterPage(self.driver)
#     # self.home_page.skip_welcome_page('left')
#     # self.home_page.click_welcome()
#     self.home_page.click_myself()
#     self.login_page.login_phone(login_dict["phone"])
#     actual = register_page.get_register_text
#     self.assertEqual(login_dict["expected"], actual)
#
# @ddt.data(*password_error)
# def test_myself_password_error(self, login_dict):
#     # self.home_page.skip_welcome_page('left')
#     # self.home_page.click_welcome()
#     self.home_page.click_myself()
#     self.login_page.login(login_dict["phone"], login_dict["password"])
#     actual = self.login_page.get_password_error_info
#     self.assertEqual(login_dict["expected"], actual)
#
# @ddt.data(*login_success)
# def test_myself_login_success(self, login_dict):
#     user_page = UserPage(self.driver)
#     # self.home_page.skip_welcome_page('left')
#     # self.home_page.click_welcome()
#     self.home_page.click_myself()
#     self.login_page.login(login_dict["phone"], login_dict["password"])
#     user_page.click_cancel()
#     actual = user_page.get_name
#     self.assertIn(login_dict["expected"], actual)

# def tearDown(self):
#     self.driver.start_activity('com.xxzb.fenwoo', ".activity.addition.SplashActivity")

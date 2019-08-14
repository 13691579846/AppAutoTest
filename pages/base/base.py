# coding=utf-8
"""
------------------------------------
@Time : 2019/8/1 9:45
@Auth : linux超
@File : base.py
@IDE  : PyCharm
@Motto: Real warriors,dare to face the bleak warning,dare to face the incisive error!
@QQ   : 28174043@qq.com
@GROUP: 878565760
------------------------------------
"""
import time

from appium.webdriver import WebElement
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.common.touch_action import TouchAction
from appium.webdriver.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec

from common.dirAndTime import DirTime as Dt
from common.log import logger
from config.globalconf import IMG_DIR as IMG


class Base(object):

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @property
    def get_phone_size(self):
        """获取屏幕的大小"""
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        return width, height

    def swipe_left(self, duration=300):
        """左滑"""
        width, height = self.get_phone_size
        start = width * 0.9, height * 0.5
        end = width * 0.1, height * 0.5
        return self.driver.swipe(*start, *end, duration)

    def swipe_right(self, duration=300):
        """右滑"""
        width, height = self.get_phone_size
        start = width * 0.1, height * 0.5
        end = width * 0.9, height * 0.5
        return self.driver.swipe(*start, *end, duration)

    def swipe_up(self, duration=300):
        """上滑"""
        width, height = self.get_phone_size
        start = width * 0.5, height * 0.9
        end = width * 0.5, height * 0.1
        return self.driver.swipe(*start, *end, duration)

    def swipe_down(self, duration=300):
        """下滑"""
        width, height = self.get_phone_size
        start = width * 0.5, height * 0.1
        end = width * 0.5, height * 0.9
        return self.driver.swipe(*start, *end, duration)

    def skip_welcome_page(self, direction, num=3, duration=300):
        """滑动页面跳过引导动画"""
        direction_dic = {
            "left": "swipe_left",
            "right": "swipe_right",
            "up": "swipe_up",
            "down": "swipe_down"
        }
        time.sleep(3)
        if hasattr(self, direction_dic[direction]):
            for _ in range(num):
                getattr(self, direction_dic[direction])(duration)  # 使用反射执行不同的滑动方法
        else:
            logger.error("参数{}不存在, direction可以为{}中任意一个字符串".
                         format(direction, direction_dic.keys()))
            raise ValueError("参数{}不存在, direction可以为{}任意一个字符串".
                             format(direction, direction_dic.keys()))

    @staticmethod
    def get_element_size_location(element):
        if not isinstance(element, WebElement):
            logger.error("{} should be WebElement object".format(element))
            raise TypeError("{} should be WebElement object".format(element))
        width = element.rect["width"]
        height = element.rect["height"]
        start_x = element.rect["x"]
        start_y = element.rect["y"]
        return width, height, start_x, start_y

    def get_password_location(self, element: WebElement) -> dict:
        if not isinstance(element, WebElement):
            logger.error("{} should be WebElement object".format(element))
            raise TypeError("{} should be WebElement object".format(element))
        width, height, start_x, start_y = self.get_element_size_location(element)
        point_1 = {"x": int(start_x + width * (1 / 6) * 1), "y": int(start_y + height * (1 / 6) * 1)}
        point_2 = {"x": int(start_x + width * (1 / 6) * 3), "y": int(start_y + height * (1 / 6) * 1)}
        point_3 = {"x": int(start_x + width * (1 / 6) * 5), "y": int(start_y + height * (1 / 6) * 1)}
        point_4 = {"x": int(start_x + width * (1 / 6) * 1), "y": int(start_y + height * (1 / 6) * 3)}
        point_5 = {"x": int(start_x + width * (1 / 6) * 3), "y": int(start_y + height * (1 / 6) * 3)}
        point_6 = {"x": int(start_x + width * (1 / 6) * 5), "y": int(start_y + height * (1 / 6) * 3)}
        point_7 = {"x": int(start_x + width * (1 / 6) * 1), "y": int(start_y + height * (1 / 6) * 5)}
        point_8 = {"x": int(start_x + width * (1 / 6) * 3), "y": int(start_y + height * (1 / 6) * 5)}
        point_9 = {"x": int(start_x + width * (1 / 6) * 5), "y": int(start_y + height * (1 / 6) * 5)}
        keys = {
            1: point_1,
            2: point_2,
            3: point_3,
            4: point_4,
            5: point_5,
            6: point_6,
            7: point_7,
            8: point_8,
            9: point_9
        }
        return keys

    def gesture_password(self, element: WebElement, *pwd, duration=200):
        """手势密码: 直接输入需要链接的点对应的数字，最多9位
        pwd: 传递你想要连线的点对应的数字密码
        """
        if not isinstance(element, WebElement):
            logger.error("{} should be WebElement object".format(element))
            raise TypeError("{} should be WebElement object".format(element))
        if len(pwd) > 9:
            logger.error("需要设置的密码不能超过9位!")
            raise ValueError("需要设置的密码不能超过9位!")
        keys_dict = self.get_password_location(element)
        action = TouchAction(self.driver)
        action.press(x=keys_dict[pwd[0]]["x"], y=keys_dict[pwd[0]]["y"]).wait(duration)
        for index in range(len(pwd) - 1):  # 0,1,2,3
            action.move_to(x=keys_dict[pwd[index + 1]]["x"] - keys_dict[pwd[index]]["x"],
                           y=keys_dict[pwd[index + 1]]["y"] - keys_dict[pwd[index]]["y"]).wait(duration)
        return action.release().perform()

    def find_element(self, locator: tuple, timeout=30) -> WebElement:
        wait = WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(lambda driver: driver.find_element(*locator))
            return element
        except TimeoutException as e:
            logger.error('no found element {} by {}'.format(locator[1], locator[0]))
            raise e

    def find_elements(self, locator, timeout=30) -> list:
        wait = WebDriverWait(self.driver, timeout)
        try:
            elements = wait.until(lambda driver: driver.find_elements(*locator))
            return elements
        except TimeoutException as e:
            logger.error('no found elements {} by {}'.format(locator[1], locator[0]))
            raise e

    def input_value(self, locator: tuple, value):
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(value)
        else:
            logger.error("the element not found, so doesn't input value")
            raise NoSuchElementException("the element not found, so doesn't input value")

    def wait_element_presence(self, locator, timeout=30) -> WebElement:
        """等待元素出现在DOM中，但是不一定是可见的"""
        wait = WebDriverWait(self.driver, timeout, 0.01)
        try:
            element = wait.until(ec.presence_of_element_located(locator))
            return element
        except TimeoutException as e:
            logger.error("the element {} not presence".format(locator[1]))
            raise e

    def wait_element_visibility(self, locator, timeout=30):
        """等待元素出现在DOM树中，且可见"""
        wait = WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(ec.visibility_of_element_located(locator))
            return element
        except TimeoutException as e:
            logger.error("the element {} invisibility".format(locator[1]))
            raise e

    def wait_element_clickable(self, locator: tuple, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(ec.element_to_be_clickable(locator))
            return element
        except TimeoutException as e:
            logger.error("the element  {} not clickable".format(locator[1]))
            raise e

    def get_element_text(self, locator, timeout=30):
        element = self.find_element(locator, timeout)
        try:
            try:
                context = element.text
            except AttributeError:
                context = element.get_attribute('value')
            return context
        except AttributeError as e:
            logger.error("get context of element {} fail".format(locator[1]))
            raise e

    def get_element_attribute(self, locator, attribute, timeout=30):
        element = self.find_element(locator, timeout)
        try:
            ele_attribute = element.get_attribute(attribute)
            return ele_attribute
        except AttributeError as e:
            logger.error("get attribute of element fail with attribute {}".format(attribute))
            raise e

    def is_existed(self, locator, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        try:
            wait.until(ec.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def click(self, locator: tuple):
        element = self.wait_element_clickable(locator)
        if element:
            return element.click()
        else:
            logger.error("the element not found, so un-clickable")
            raise NoSuchElementException("the element not found, so un-clickable")

    def select_list_option(self, locator: tuple, option: int):
        """选择列表选项"""
        elements = self.find_elements(locator)
        return elements[option].click()

    def switch_to_context(self, context=None):
        """[NAVTIVE_APP, WEB_VIEW]
        如果context为空，默认切换到原生app
        """
        all_contexts = self.driver.contexts
        if not context:
            # 默认切换到原生
            return self.driver.switch_to.context(None)
        for con in all_contexts:
            if context == con:
                return self.driver.switch_to.context(context)
        else:
            logger.error("{} no exist".format(context))
            raise ValueError("{} no exist".format(context))

    def key_board(self, key_code):
        """key_code: 手机的键盘码"""
        return self.driver.press_keycode(key_code)

    def get_toast(self, context):
        """text: toast的文本值
        只支持appium server 版本在1.6.3以上，且"automationName"为"uiautomator2"
        """
        locator = (MobileBy.XPATH, "//*[contains(@text, '{}')]".format(context))
        toast = self.wait_element_presence(locator)
        try:
            try:
                cont = toast.text
            except AttributeError:
                cont = toast.get_attribute("text")
            return cont
        except AttributeError as e:
            logger.error("get context of toast fail")
            raise e

    def screen_shot(self, explain=None):
        if Dt.create_path(IMG):
            img_name = IMG + '\\' + Dt.file_name('png', explain)
            return self.driver.get_screenshot_as_file(img_name)


if __name__ == '__main__':
    pass

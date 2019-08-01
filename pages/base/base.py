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
from appium.webdriver import webelement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support import expected_conditions as ec


class Base(object):

    def __init__(self, driver: webelement):
        self.driver = driver

    @property
    def get_phone_size(self):
        width = self.driver.get_window_size()['width']
        height = self.driver.get_window_size()['height']
        return width, height

    def swipe_left(self, duration=500):
        width, height = self.get_phone_size
        width1 = width * 0.75
        height1 = height * 0.5
        width2 = width * 0.25
        self.driver.swipe(width1, height1, width2, height1, duration)

    def find_element(self, locator: tuple, timeout=30) -> webelement:
        wait = WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(lambda driver: driver.find_element(*locator))
            return element
        except (NoSuchElementException, TimeoutException):
            print('no found element {} by {}',format(locator[1], locator[0]))

    def input_value(self, locator: tuple, value):
        element = self.find_element(locator)
        if element:
            element.clear()
            element.send_keys(value)
        else:
            raise NoSuchElementException("the element not found, so doesn't input value")

    def wait_element_clickable(self, locator: tuple, timeout=30):
        wait = WebDriverWait(self.driver, timeout)
        try:
            element = wait.until(ec.element_to_be_clickable(locator))
            return element
        except (NoSuchElementException, TimeoutException):
            print("no found element {} by {}".format(locator[1], locator[1]))

    def click(self, locator: tuple):
        element = self.wait_element_clickable(locator)
        if element:
            element.click()
        else:
            raise NoSuchElementException("the element not found, so un-clickable")


if __name__ == '__main__':
    pass

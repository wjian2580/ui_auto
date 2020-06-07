import os
import time
import allure
import pytest
from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction


class BasePage:

    # _instance = None

    # def __new__(cls):
    #     if not cls._instance:
    #         desired_caps = {
    #             "platformName": "Android",
    #             "platformVersion": "9",
    #             "deviceName": "vivo x27",
    #             "appPackage": "cn.xdf.woxue.student",
    #             "appActivity": ".activity.SplashActivity",
    #             "newCommandTimeout": 3000
    #         }
    #     pass

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def find_element(self, *loc):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(loc))
        element = self.driver.find_element(*loc)
        return element

    def get_text(self, *loc):
        element = self.find_element(*loc)
        text = element.get_attribute('text')
        return text

    def click_by_partial_text(self, text):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(f"//*[contains(@text, '{text}')]"))
        element = self.driver.find_element_by_xpath(f"//*[contains(@text, '{text}')]")
        element.click()

    def click_by_text(self, text):
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_xpath(f'//*[@text="{text}"]'))
        element = self.driver.find_element_by_xpath(f'//*[@text="{text}"]')
        element.click()

    def click_by_id(self, id):
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_id(id))
        element = self.driver.find_element_by_id(id)
        element.click()

    def click_by_accessibility_id(self, accessibility_id):
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element_by_accessibility_id(accessibility_id))
        element = self.driver.find_element_by_accessibility_id(accessibility_id)
        element.click()

    def find_by_text(self, text):
        WebDriverWait(self.driver, 10).until(lambda x: x.find_element_by_xpath(f"//*[contains(@text, '{text}')]"))
        element = self.driver.find_element_by_xpath(f"//*[contains(@text, '{text}')]")
        return element

    def click(self, *loc):
        element = self.find_element(*loc)
        element.click()

    def send_keys(self, text, *loc):
        element = self.find_element(*loc)
        element.clear()
        element.send_keys(text)

    def long_press(self, *loc):
        element = self.find_element(*loc)
        TouchAction(self.driver).long_press(element).perform()
        self.sleep()

    def sleep(self, sec=2):
        time.sleep(sec)

    def clear_app(self):
        os.system('adb shell pm clear cn.xdf.woxue.student')

    def back(self, times=1):
        for i in range(times):
            time.sleep(0.5)
            self.driver.back()

    def swipe_down(self, n=1):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        # pytest.set_trace()
        for i in range(n):
            self.driver.swipe(width / 2, height / 4, width / 2, height * 3 / 4, 500)

    def swipe_up(self, n=1):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        for i in range(n):
            self.driver.swipe(width / 2, height * 3 / 4, width / 2, height / 4, 500)

    def swipe_left(self, n=1):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        for i in range(n):
            self.driver.swipe(width / 4, height / 2, width * 3 / 4, height / 2, 500)

    def swipe_rigth(self, n=1):
        window_size = self.driver.get_window_size()
        width = window_size.get("width")
        height = window_size.get("height")
        for i in range(n):
            self.driver.swipe(width * 4 / 5, height / 2, width / 5, height / 2, 500)

    def attach_screenshot(self, name):
        self.sleep()
        allure.attach(self.driver.get_screenshot_as_png(), f'{name}.png', allure.attachment_type.PNG)

    def element_existed(self, *loc):
        try:
            self.find_element(*loc)
        except TimeoutException:
            return False
        return True

    def text_existed(self, text):
        try:
            self.find_by_text(text)
        except TimeoutException:
            return False
        return True

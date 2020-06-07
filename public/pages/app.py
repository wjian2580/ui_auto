import datetime

from appium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait

from public.pages.login import LoginPage
from public.pages.study_page import StudyPage


class App:
    driver: WebDriver = None

    @classmethod
    def start(cls):
        desired_caps = {
            "platformName": "Android",
            "platformVersion": "6.0.1",
            "deviceName": "MuMu",
            "appPackage": "cn.xdf.woxue.student",
            "appActivity": ".activity.SplashActivity",
            "newCommandTimeout": 3000,
            "autoGrantPermissions": True,
            'unicodeKeyboard': True,
            "chromedriverExecutable": "/Users/jian/chromedriver/2.20/chromedriver",
            'noReset': True,
            "showChromedriverLog": True
        }

        cls.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
        cls.driver.implicitly_wait(10)

        return LoginPage(cls.driver)

    @classmethod
    def quit(cls):
        cls.driver.quit()

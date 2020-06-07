from selenium.webdriver.common.by import By

from public.pages.base import BasePage
from public.pages.home import HomePage
from public.pages.my_tab import MyHomePage


class StudyPage(BasePage):
    _home_tab_loc = (By.XPATH, '//*[@text="首页"]')
    _my_tab_loc = (By.XPATH, '//*[@text="我的"]')
    _message_tab = (By.XPATH, '//*[@text="消息"]')
    _free_course_tab = (By.XPATH, '//*[@text="免费课"]')

    def to_my_home(self):
        self.click(*self._my_tab_loc)
        return MyHomePage(self.driver)

    def to_home_page(self):
        self.click(*self._home_tab_loc)
        return HomePage(self.driver)

    def to_free_course_page(self):
        self.click(*self._free_course_tab)

    def to_message_page(self):
        self.click(*self._message_tab)


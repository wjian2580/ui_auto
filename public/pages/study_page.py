from selenium.webdriver.common.by import By

from public.pages.base import Action
from public.pages.home import HomePage
from public.pages.my_tab import MyHomePage


class StudyPage(Action):
    _home_tab_loc = (By.XPATH, '//*[@text="首页"]')
    _my_tab_loc = (By.XPATH, '//*[@text="我的"]')

    def to_my_home(self):
        self.click(*self._my_tab_loc)
        return MyHomePage(self.driver)

    def to_home_page(self):
        self.click(*self._home_tab_loc)
        return HomePage(self.driver)

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from public.pages.base import Action
from public.pages.my_student import StudentManagePage
from public.pages.setting_page import SettingPage


class MyHomePage(Action):

    def __init__(self, driver: WebDriver):
        super(MyHomePage, self).__init__(driver)
        self.click_by_partial_text('知道了')
        self.click_by_partial_text('知道了')

    _setting_btn = (By.ID, 'cn.xdf.woxue.student:id/iv_setup')
    _student_manage_btn = (By.ID, 'cn.xdf.woxue.student:id/tv_manager')

    def to_student_management_page(self):
        self.click(*self._student_manage_btn)
        return StudentManagePage(self.driver)

    def to_setting_page(self):
        self.click(*self._setting_btn)
        return SettingPage(self.driver)

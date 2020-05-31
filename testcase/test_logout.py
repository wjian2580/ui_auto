import allure

from public.pages.app import App
from public.pages.login import LoginPage


@allure.feature('退出登录')
class TestLogout:

    def setup(self):

        self.setting_page = App.start().login().to_my_home().to_setting_page()

    def test_logout(self):
        self.setting_page.logout()


import allure

from public.pages.app import App
from public.pages.login import LoginPage


@allure.feature('退出登录')
class TestSettings:

    def test_logout(self, init_setting):
        init_setting.logout()


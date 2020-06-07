from selenium.webdriver.common.by import By

from public.pages.base import BasePage


class SettingPage(BasePage):
    _logout_btn = (By.ID, 'cn.xdf.woxue.student:id/tv_logout')
    _logout_confirm = (By.ID, 'cn.xdf.woxue.student:id/btn_OnClick')

    def logout(self):

        self.click(*self._logout_btn)
        self.click(*self._logout_confirm)
        self.attach_screenshot('成功退出登录')
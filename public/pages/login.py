from selenium.webdriver.common.by import By

from public.pages.base import Action
from public.pages.study_page import StudyPage


class LoginPage(Action):
    
    _login_by_passwd_tab_loc = (By.ID, "cn.xdf.woxue.student:id/pwdTv")
    _phone_number_loc = (By.ID, "cn.xdf.woxue.student:id/phoneNum")
    _password_loc = (By.ID, "cn.xdf.woxue.student:id/pwd")
    _login_btn_loc = (By.ID, "cn.xdf.woxue.student:id/loginBtnBg")
    _privacy_sure = (By.ID, "cn.xdf.woxue.student:id/tv_sure")

    def login(self):
        self.click(*self._privacy_sure)
        self.click(*self._login_by_passwd_tab_loc)
        self.send_keys('13520637568', *self._phone_number_loc)
        self.send_keys('123123', *self._password_loc)
        self.click(*self._login_btn_loc)
        return StudyPage(self.driver)



    #XNDF3172
    #测测


from selenium.webdriver.common.by import By

from public.pages.base import BasePage


class Register(BasePage):

    entrance = (By.ID, 'cn.xdf.woxue.student:id/signupBtn')
    phone_num_box = (By.ID, 'cn.xdf.woxue.student:id/phoneNum')
    veri_code_box = (By.ID, 'cn.xdf.woxue.student:id/vertificationCode')
    register_btn = (By.ID, 'cn.xdf.woxue.student:id/loginBtnBg')

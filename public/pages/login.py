from selenium.webdriver.common.by import By


class Login():
    
    login_by_passwd_tab_loc = (By.ID, "cn.xdf.woxue.student:id/pwdTv")
    phone_number_loc = (By.ID, "cn.xdf.woxue.student:id/phoneNum")
    password_loc = (By.ID, "cn.xdf.woxue.student:id/pwd")
    login_btn_loc = (By.ID, "cn.xdf.woxue.student:id/loginBtnBg")
    privacy_sure = (By.ID, "cn.xdf.woxue.student:id/tv_sure")


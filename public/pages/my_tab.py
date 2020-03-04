from selenium.webdriver.common.by import By


class MyTab():

    my_tab = (By.XPATH, '//*[@text="我的"]')
    setting_btn = (By.ID, 'cn.xdf.woxue.student:id/iv_setup')
    logout_btn = (By.ID, 'cn.xdf.woxue.student:id/tv_logout')
    logout_confirm = (By.ID, 'cn.xdf.woxue.student:id/btn_OnClick')
    
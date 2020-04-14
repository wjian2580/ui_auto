from selenium.webdriver.common.by import By

# from public.base import Action


class MyTab:

    _my_tab = (By.XPATH, '//*[@text="我的"]')
    _setting_btn = (By.ID, 'cn.xdf.woxue.student:id/iv_setup')
    _logout_btn = (By.ID, 'cn.xdf.woxue.student:id/tv_logout')
    _logout_confirm = (By.ID, 'cn.xdf.woxue.student:id/btn_OnClick')

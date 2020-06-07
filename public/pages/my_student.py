from selenium.webdriver.common.by import By
from public.pages.base import BasePage


class StudentManagePage(BasePage):

    add_btn = (By.XPATH, '//android.view.View[@content-desc="添加"]')
    bind_confirm_btn = (By.ID, 'cn.xdf.woxue.student:id/loginBtnBg')
    bind_toast_btn = (By.ID, 'cn.xdf.woxue.student:id/okBtn')

    student_loc = (By.XPATH, '//android.view.View[@content-desc="XNDF3172"]')
    unbind_btn = (By.XPATH, '//android.view.View[@content-desc="解除绑定"]')
    unbind_confirm_btn = (By.XPATH, '//android.view.View[@content-desc="确定"]')

    # def unbind_
    # def to

from selenium.webdriver.common.by import By

from public.pages.base import Action


class HomePage(Action):

    _course_system = (By.XPATH, '//*[@text="课程体系"]')
    _all_school_areas = (By.XPATH, '//*[@text="全部校区"]')
    banner = (By.ID, "cn.xdf.woxue.student:id/banner_img")
    my_tab = (By.XPATH, '//*[@text="我的"]')
    service_tab = (By.XPATH, '//*[@text="服务"]')
    home_tab = (By.XPATH, '//*[@text="首页"]')
    message_tab = (By.XPATH, '//*[@text="消息"]')




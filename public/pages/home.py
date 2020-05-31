from selenium.webdriver.common.by import By

from public.pages.base import Action


class HomePage(Action):

    _course_system = (By.XPATH, '//*[@text="课程体系"]')
    _all_school_areas = (By.XPATH, '//*[@text="全部校区"]')
    _shopping_cart = (By.ID, 'cn.xdf.woxue.student:id/iv_shopping')
    _search_btn = (By.ID, 'cn.xdf.woxue.student:id/iv_search')
    _grade_select = (By.ID, 'cn.xdf.woxue.student:id/tv_class')
    _course_select = (By.XPATH, '//*[@text="选课"]')
    _banner = (By.ID, "cn.xdf.woxue.student:id/banner_img")
    _school_detail_nearby = (By.XPATH, '//*[@text="查看校区课程"]')
    my_tab = (By.XPATH, '//*[@text="我的"]')
    service_tab = (By.XPATH, '//*[@text="服务"]')
    home_tab = (By.XPATH, '//*[@text="首页"]')
    message_tab = (By.XPATH, '//*[@text="消息"]')




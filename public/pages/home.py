from selenium.webdriver.common.by import By

from public.pages.base import BasePage


class HomePage(BasePage):

    _sure_btn = (By.ID, 'cn.xdf.woxue.student:id/tv_sure')
    _allow_btn = (By.ID, 'com.android.packageinstaller:id/permission_allow_button')
    _course_system = (By.XPATH, '//*[@text="课程体系"]')
    _all_school_areas = (By.XPATH, '//*[@text="全部校区"]')
    _shopping_cart = (By.ID, 'cn.xdf.woxue.student:id/iv_shopping')
    _web_title = (By.ID, 'cn.xdf.woxue.student:id/web_view_title')
    _search_btn = (By.ID, 'cn.xdf.woxue.student:id/iv_search')
    _search_input = (By.ID, "sh-input-content")
    _grade_btn = (By.ID, 'cn.xdf.woxue.student:id/tv_class')
    _city_btn = (By.ID, 'cn.xdf.woxue.student:id/tv_city')
    _city_select = (By.ID, 'cn.xdf.woxue.student:id/grade_tv_city')
    _course_select = (By.XPATH, '//*[@text="选课"]')
    _banner = (By.ID, "cn.xdf.woxue.student:id/banner_img")
    _school_detail_nearby = (By.XPATH, '//*[@text="查看校区课程"]')
    _city_back_btn = (By.ID, "cn.xdf.woxue.student:id/commom_left_btn")
    _web_back = (By.ID, "cn.xdf.woxue.student:id/web_view_back")

    def change_grade(self, grade_phase, grade):
        grade_btn = self.find_element(*self._grade_btn)
        grade_btn.click()
        self.click_by_text(grade_phase)
        if grade_phase != '在职':
            self.click_by_text(grade)

    def change_city(self, city):
        self.click(*self._city_btn)
        self.click(*self._city_select)
        self.click_by_text(city)
        self.click(*self._city_back_btn)

    def banner(self):
        self.click(*self._banner)
        self.click(*self._web_back)

    def school_areas(self):
        self.click(*self._all_school_areas)

    def course_search(self, key_word):
        self.click(*self._search_btn)
        self.send_keys(key_word, *self._search_input)
        self.driver.press_keycode(66)

    def school_detail_nearby(self):
        self.click(*self._school_detail_nearby)

    def enter_shopping_cart(self):
        self.click(*self._shopping_cart)
        self.sleep(5)

    def enter_course_system(self):
        self.click(*self._course_system)
        self.sleep(5)

    def permission_grant(self):
        self.click(*self._sure_btn)
        self.click(*self._allow_btn)
        self.click(*self._allow_btn)










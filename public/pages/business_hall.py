import time
from selenium.webdriver.common.by import By

from public.pages.base import BasePage


class BusinessHallPage(BasePage):

    _pp_loc = (By.ID, '泡泡小学')
    _youcan_loc = (By.ID, '优能中学')
    _grade_search_loc = (By.XPATH, "//*[contains(@text, '选择年级')]")
    _subject_search_loc = (By.XPATH, "//*[contains(@text, '选择学科')]")
    _school_loc = (By.XPATH, "//*[contains(@text, '选择校区')]")
    _quarter_loc = (By.XPATH, "//*[contains(@text, '选择季度')]")

    _search_button_loc = (By.XPATH, "//*[contains(@text, '搜索班级')]")
    _confirm_button_loc = (By.XPATH, "//*[@text='确认']")

    def to_pp(self):
        self.click(*self._pp_loc)


#     def classified_search(select_items):
#         classifictions = ['请选择年级', '请选择学科', '请选择校区', '请选择季度']
#         swipe_location = [1800, 1700, 2200, 1900]
#         for i in range(4):
#             action.click_by_accessibility_id(classifictions[i])
#             time.sleep(0.5)
#             action.driver.swipe(500, 2200, 500, swipe_location[i])
#             action.click_by_text(select_items[i])
# #           action.click(*self.confirm_button_loc)

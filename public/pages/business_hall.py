import pytest
import time
from selenium.webdriver.common.by import By

class BusinessHall():
    entrance_loc = (By.XPATH, '//*[@text="营业厅"]')
    # pp_loc = (By.ID, '泡泡小学')
    # youcan_loc = (By.ID '优能中学')
    pp_loc = (By.XPATH, '//android.view.View[@content-desc="泡泡小学"]')
    youcan_loc = (By.XPATH, '//android.view.View[@content-desc="优能中学"]')
    grade_search_loc = (By.XPATH, "//*[contains(@text, '选择年级')]")
    
    subject_search_loc = (By.XPATH, "//*[contains(@text, '选择学科')]")
    school_loc = (By.XPATH, "//*[contains(@text, '选择校区')]")
    quarter_loc = (By.XPATH, "//*[contains(@text, '选择季度')]")


    search_button_loc = (By.XPATH, "//*[contains(@text, '搜索班级')]")
    confirm_button_loc = (By.XPATH, "//*[@text='确认']")


    def classified_search(self, action, select_items):
        classifictions = ['请选择年级', '请选择学科', '请选择校区', '请选择季度']
        swipe_location = [1800, 1700, 2200, 1900]
        for i in range(4):
            action.click_by_accessibility_id(classifictions[i])
            time.sleep(0.5)
            action.driver.swipe(500, 2200, 500, swipe_location[i])
            action.click_by_text(select_items[i])
 #           action.click(*self.confirm_button_loc)
    

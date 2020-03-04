import pytest
import allure
from public.pages import core_module, home
from selenium.webdriver.common.by import By


@allure.feature('练习')
class TestPractice():

    entrance = core_module.CoreModuleEntrance()
    tabs = home.Tabs()
    practice_locs = core_module.Practice()

    @allure.story('做教师端手动发的练习')
    def test_manual_practice(self, action):
        with allure.step('进入练习列表'):
            action.click(*self.entrance.practice)
            action.attach_screenshot('练习列表')
            action.click(*self.practice_locs.all_practices_tab)
        with allure.step('进入详情'):
            action.click(*self.practice_locs.practice_name)
            action.attach_screenshot('练习详情')
        with allure.step('上传作业图片'):
            action.click_by_text('传照片')
            action.click(*self.practice_locs.img_select_btn)
            action.click(*self.practice_locs.select_finish_btn)
            action.attach_screenshot('图片上传完成')
        with allure.step('删除作业图片'):
            action.swipe_Up(3)
            action.click(*self.practice_locs.pic_delete_btn)
            action.attach_screenshot('图片删除确认')
            action.click(*self.practice_locs.pic_delete_confirm_btn)
        with allure.step('上传音频作业'):
            action.click_by_text('传语音')
            action.click(*self.practice_locs.record_btn)
            action.sleep()
            action.attach_screenshot('录音中')
            action.click(*self.practice_locs.record_btn)
            action.click(*self.practice_locs.record_finish_btn)

            # action.driver.find_element_by_class_name('android.view.View').click()
#            action.click('cn.xdf.woxue.student:id/zuoYeRecordTimeView')
        # with allure.step('删除音频作业'):
        #     action.long_press(By.ID, 'cn.xdf.woxue.student:id/controlBtn')
        #     action.click('cn.xdf.woxue.student:id/deleteBtn')
        #     action.click('cn.xdf.woxue.student:id/confirm_btn')

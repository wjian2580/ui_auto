import pytest
import allure
from public.pages import my_student
from selenium.webdriver.common.by import By


@allure.feature('学员绑定与解绑')
class TestBindAndUnbind():

    student_locs = my_student.MyStudent()

    @allure.story('绑定学员')
    def test_bind_student(self, action):
        with allure.step('进入学员管理'):
            action.click_by_text('我的')
            action.click_by_partial_text('知道了')
            action.click(*self.student_locs.entrance)
            action.attach_screenshot('学员列表')
        with allure.step('进入绑定'):
            action.click(*self.student_locs.add_btn)
            action.attach_screenshot('可绑定学员列表')
        with allure.step('绑定成功'):
            action.click(*self.student_locs.bind_confirm_btn)
            action.click(*self.student_locs.bind_toast_btn)
            action.attach_screenshot('绑定成功进入首页')

    @allure.story('解绑学员')
    def test_unbind_student(self, action):
        with allure.step('进入学员管理'):
            action.click_by_text('我的')
            action.click_by_partial_text('知道了')
            action.click(*self.student_locs.entrance)
            action.attach_screenshot('学员列表')
        with allure.step('解绑'):
            action.click(*self.student_locs.student_loc)
            action.attach_screenshot('学员信息')
            action.click(*self.student_locs.unbind_btn)
            action.click(*self.student_locs.unbind_confirm_btn)
            action.attach_screenshot('解绑成功')

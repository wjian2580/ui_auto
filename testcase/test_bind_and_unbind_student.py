import pytest
import allure
from public.pages import my_student
from selenium.webdriver.common.by import By


@allure.feature('学员绑定与解绑')
class TestBindAndUnbind:

    student_locs = my_student.MyStudent()

    # def setup(self, self):
    #     self.self = self

    @allure.story('绑定学员')
    def test_bind_student(self):
        with allure.step('进入学员管理'):
            self.click_by_text('我的')
            self.click_by_partial_text('知道了')
            self.click(*self.student_locs.entrance)
            # self.attach_screenshot('学员列表')
        with allure.step('进入绑定'):
            self.click(*self.student_locs.add_btn)
            # self.attach_screenshot('可绑定学员列表')
        with allure.step('绑定成功'):
            self.click(*self.student_locs.bind_confirm_btn)
            self.click(*self.student_locs.bind_toast_btn)
            # self.attach_screenshot('绑定成功进入首页')

    @allure.story('解绑学员')
    def test_unbind_student(self):
        with allure.step('进入学员管理'):
            self.click_by_text('我的')
            self.click_by_partial_text('知道了')
            self.click(*self.student_locs.entrance)
            self.attach_screenshot('学员列表')
        with allure.step('解绑'):
            self.click(*self.student_locs.student_loc)
            self.attach_screenshot('学员信息')
            self.click(*self.student_locs.unbind_btn)
            self.click(*self.student_locs.unbind_confirm_btn)
            self.attach_screenshot('解绑成功')

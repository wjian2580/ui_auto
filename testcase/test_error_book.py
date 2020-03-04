import pytest
import allure
from public.pages import core_module, home
from selenium.webdriver.common.by import By


@allure.feature('错题本')
class TestErrorBook():

    entrance = core_module.CoreModuleEntrance()
    error_book_locs = core_module.ErrorBook()

    @allure.story('查看错题本')
    def test_error_book(self, action):
        with allure.step('进入错题列表'):
            action.click(*self.entrance.error_book)
            action.attach_screenshot('错题列表')
            action.click(*self.error_book_locs.book_name)
            action.attach_screenshot('错题详情')
            assert action.element_existed(*self.error_book_locs.audio_item)

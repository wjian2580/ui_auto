import pytest
import allure
from public.pages import core_module, home
from selenium.webdriver.common.by import By


@allure.feature('报告')
class TestReport():

    entrance = core_module.CoreModuleEntrance()
    report_locs = core_module.Report()

    @allure.story('查看学习报告')
    def test_manual_practice(self, action):
        with allure.step('进入报告列表'):
            action.click(*self.entrance.report)
            action.attach_screenshot('报告列表')
            action.click(*self.report_locs.report_name)
            action.attach_screenshot('报告详情')
            assert action.element_existed(*self.report_locs.report_detail)

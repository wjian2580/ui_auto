import pytest
import allure
from public.pages import core_module, home
from selenium.webdriver.common.by import By


@allure.feature('资料')
class TestMaterial():

    entrance = core_module.CoreModuleEntrance()
    material_locs = core_module.Material()

    @allure.story('查看资料')
    def test_material(self, action):
        with allure.step('进入资料列表'):
            action.click(*self.entrance.material)
            action.attach_screenshot('资料列表')
            action.click(*self.material_locs.material_name)
            action.attach_screenshot('资料详情')
            assert action.element_existed(*self.material_locs.check_item)

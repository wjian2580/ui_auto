import pytest
import allure
from public.pages import business_hall, home
from public.base import Action


# @pytest.fixture(scope='class', autouse=True)
# def set_request(driver):
#     print('hello')
#     yield 'hello'
#     driver.quit()


# def teardown_class(driver):
#     driver.quit()

@allure.feature('营业厅')
class TestBusinessHall(Action):
    business_hall_page = business_hall.BusinessHall()

    def setup(self, action):
        business_hall_page = business_hall.BusinessHall()
        tabs = home.Tabs()
        with allure.step('进入我的tab'):
            action.click_by_text('我的')
            action.attach_screenshot('我的tab')
        with allure.step('新手引导-点击知道了'):
            action.attach_screenshot('新手引导')
            action.click_by_partial_text('知道了')
            action.click_by_partial_text('知道了')
        with allure.step('点击营业厅icon进入营业厅'):
            # action.click(business_hall_page.entrance_loc)
            action.click_by_text('营业厅')
            action.attach_screenshot('营业厅')

    @allure.story('泡泡小学-搜课-加入购物车')
    def test_pp(self, action):
        with allure.step('分类搜索'):
            pytest.set_trace()
            action.click(*self.business_hall_page.pp_loc)
            select_items = ['四年级', '英语', '东城东四三友大厦校区', '寒假']

    #           self.business_hall_page.classified_search(action, select_items)
    #           action.attach_screenshot('分类搜索')
    #          action.click(*self.business_hall_page.search_button_loc)
    #          action.attach_screenshot('搜索结果')
    #      with allure.step('加入购物车'):
    #         action.click_by_text('加入购物车')
    #         assert action.text_existed('加入成功')
    #          action.attach_screenshot('加入购物车')
    @allure.story('优能中学')
    # @pytest.mark.flaky(reruns=5, reruns_delay=2)
    def test_youcan(self, action):
        action.click(*self.business_hall_page.youcan_loc)

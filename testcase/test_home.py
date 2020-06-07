import pytest

from public.pages.app import App
from public.pages.study_page import StudyPage


class TestHome:

    def test_course_system(self, init_home):
        init_home.permission_grant()
        init_home.enter_course_system()

    def test_enter_shopping_cart(self, init_home):
        init_home.enter_shopping_cart()
        # assert init_home(*init_home._shopping_cart_title) == '购物车'

    def test_change_grade(self, init_home):
        init_home.change_grade('小学', '三年级')
        assert init_home.get_text(init_home._grade_btn) == '三年级'
        # print(init_home.driver.find_element_by_id(init_home._grade_btn))

    def test_change_city(self, init_home):
        init_home.change_city('上海')

    def test_banner(self, init_home):
        init_home.banner()

    def test_school_area(self, init_home):
        init_home.school_areas()
        assert init_home.get_text(init_home._web_title) == '全部校区'

    def test_course_search(self, init_home):
        init_home.course_search('英语')

    def test_school_detail_nearby(self, init_home):
        init_home.school_detail_nearby()

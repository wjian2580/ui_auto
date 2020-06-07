from public.pages.app import App
from public.pages.study_page import StudyPage


class TestHome:
    def setup(self, init: StudyPage):
        self.home_page = init.to_home_page()

    def test_course_system(self):
        self.home_page.enter_course_system()

    def test_change_grade(self):
        self.home_page.change_grade('小学', '三年级')
        assert self.home_page.get_text(self.home_page._grade_btn) == '三年级'

    def enter_shopping_cart(self):
        self.home_page.enter_shopping_cart()

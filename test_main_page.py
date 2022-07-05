import pytest
from pages.main_page import MainPage
from pages.links import MainPageLinks


@pytest.mark.yandex
class TestSearchFromMainPage:
    def test_users_can_go_to_the_tensor_main_page_from_the_yandex_one(self, browser):
        link = MainPageLinks.YANDEX_MANE_PAGE
        page = MainPage(browser, link)
        page.open()
        page.there_should_be_a_search_box()
        page.enter_the_search_request()
        page.there_should_be_a_suggestion_table_after_search_request()
        page.go_to_the_search_result_page()
        page.there_should_be_a_search_results_table()
        page.go_to_first_link_in_search_results()
        page.first_link_should_lead_to_the_tensor_main_page()

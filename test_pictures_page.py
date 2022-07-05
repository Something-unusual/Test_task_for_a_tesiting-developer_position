import pytest
from pages.pictures_page import PicturesPage
from pages.links import MainPageLinks


@pytest.mark.yandex
class TestSearchFroPicturesPage:
    def test_users_can_swipe_pictures_on_yandex_pictures_page(self, browser):
        link = MainPageLinks.YANDEX_MANE_PAGE
        page = PicturesPage(browser, link)
        page.open()
        page.there_should_be_a_pictures_link()
        page.go_to_the_pictures_page()
        page.pictures_link_should_lead_to_the_pictures_page()
        page.go_to_the_first_category_page()
        page.there_should_be_first_category_name_in_search_box()
        page.open_first_picture()
        page.first_picture_should_be_opened()
        page.get_first_picture_source()
        page.press_the_next_button()
        page.second_picture_should_be_opened()
        page.get_second_picture_source()
        page.second_picture_should_be_different()
        page.press_the_prev_button()
        page.get_previous_picture_source()
        page.there_is_still_previous_picture_after_getting_back()

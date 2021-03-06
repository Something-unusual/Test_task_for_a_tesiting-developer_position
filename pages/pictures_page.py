from .base_page import BasePage
from .locators import PicturesPageLocators
from .links import PicturesPageLinks


class PicturesPage(BasePage):
    PICTURES_LINKS = []

    def there_should_be_a_pictures_link(self):
        assert self.is_element_present(*PicturesPageLocators.PICTURES_LINK), "Pictures link is not presented"

    def go_to_the_pictures_page(self):
        link = self.browser.find_element(*PicturesPageLocators.PICTURES_LINK)
        link.click()
        pictures_page_window = self.browser.window_handles[1]
        self.browser.switch_to.window(pictures_page_window)

    def pictures_link_should_lead_to_the_pictures_page(self):
        assert PicturesPageLinks.YANDEX_PICTURES_URL in self.browser.current_url, \
            f"Expected \'{PicturesPageLinks.YANDEX_PICTURES_URL}\' in url-link"

    def there_should_be_an_active_first_category_widget_on_pictures_page(self):
        assert self.is_element_present(*PicturesPageLocators.PICTURES_FIRST_CATEGORY_WIDGET), \
            "First category widget is inactive"

    def go_to_the_first_category_page(self):
        self.there_should_be_an_active_first_category_widget_on_pictures_page()
        link = self.browser.find_element(*PicturesPageLocators.PICTURES_FIRST_CATEGORY_WIDGET)
        link.click()

    def there_should_be_first_category_name_in_search_box(self):
        assert self.is_element_present(*PicturesPageLocators.PICTURES_FIRST_CATEGORY_NAME), \
            "Category name is not presented in search box"

    def open_first_picture(self):
        first_picture = self.browser.find_element(*PicturesPageLocators.FIRST_PICTURE)
        first_picture.click()

    def first_picture_should_be_opened(self):
        assert self.is_element_present(*PicturesPageLocators.PICTURE_SELECTED), "First picture is not opened"

    def get_first_picture_source(self):
        self.first_picture_should_be_opened()
        first_picture = self.browser.find_element(*PicturesPageLocators.PICTURE_SELECTED)
        first_picture_source = first_picture.get_attribute("src")
        PicturesPage.PICTURES_LINKS.append(first_picture_source)

    def there_should_be_next_button(self):
        assert self.is_element_present(*PicturesPageLocators.NEXT_BUTTON), "Next button is not presented"

    def press_the_next_button(self):
        self.there_should_be_next_button()
        next_button = self.browser.find_element(*PicturesPageLocators.NEXT_BUTTON)
        next_button.click()

    def second_picture_should_be_opened(self):
        assert self.is_element_present(*PicturesPageLocators.PICTURE_SELECTED), "Second picture is not opened"

    def get_second_picture_source(self):
        self.second_picture_should_be_opened()
        second_picture = self.browser.find_element(*PicturesPageLocators.PICTURE_SELECTED)
        second_picture_source = second_picture.get_attribute("src")
        PicturesPage.PICTURES_LINKS.append(second_picture_source)

    @staticmethod
    def second_picture_should_be_different():
        assert PicturesPage.PICTURES_LINKS[0] != PicturesPage.PICTURES_LINKS[1], \
            "Expected another picture, got the same one"

    def there_should_be_prev_button(self):
        assert self.is_element_present(*PicturesPageLocators.PREV_BUTTON), "Prev button is not presented"

    def press_the_prev_button(self):
        self.there_should_be_prev_button()
        prev_button = self.browser.find_element(*PicturesPageLocators.PREV_BUTTON)
        prev_button.click()

    def there_should_be_opened_previous_picture(self):
        assert self.is_element_present(*PicturesPageLocators.PICTURE_SELECTED), "Previous picture is not opened"

    def get_previous_picture_source(self):
        self.there_should_be_opened_previous_picture()
        previous_picture = self.browser.find_element(*PicturesPageLocators.PICTURE_SELECTED)
        previous_picture_source = previous_picture.get_attribute("src")
        PicturesPage.PICTURES_LINKS.append(previous_picture_source)

    @staticmethod
    def there_is_still_previous_picture_after_getting_back():
        assert PicturesPage.PICTURES_LINKS[0] == PicturesPage.PICTURES_LINKS[2], "First picture has changed"

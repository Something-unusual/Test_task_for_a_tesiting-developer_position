from .base_page import BasePage
from .locators import MainPageLocators
from .requests import MainPageRequests
from .links import MainPageLinks
from selenium.webdriver.common.keys import Keys


class MainPage(BasePage):
    def there_should_be_a_search_box(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_BOX), "Search box is not presented"

    def enter_the_search_request(self):
        self.there_should_be_a_search_box()
        search_box = self.browser.find_element(*MainPageLocators.SEARCH_BOX)
        search_box.self.browser.send_keys(MainPageRequests.TENSOR_SEARCH_REQUEST)

    def there_should_be_a_suggestion_table_after_search_request(self):
        assert self.is_element_present(*MainPageLocators.SUGGESTION_TABLE), "Suggestion table is not presented"

    def go_to_the_search_result_page(self):
        self.browser.send_keys(Keys.RETURN)

    def there_should_be_a_search_results_table(self):
        assert self.is_element_present(*MainPageLocators.SEARCH_RESULTS), "Search results table is not presented"

    def there_is_active_first_link_in_the_results_table(self):
        assert self.is_element_present(*MainPageLocators.FIRST_LINK_IN_RESULTS), \
            "First link is inactive"

    def go_to_first_link_in_search_results(self):
        self.there_is_active_first_link_in_the_results_table()
        link = self.browser.find_element(*MainPageLocators.FIRST_LINK_IN_RESULTS)
        link.click()

    def first_link_should_lead_to_the_tensor_main_page(self):
        assert MainPageLinks.TENSOR_MANE_PAGE == self.browser.current_url, \
            f"Expected \'{MainPageLinks.TENSOR_MANE_PAGE}\' in url-link"

from selenium.webdriver.common.by import By


class MainPageLocators:
    SEARCH_BOX = (By.CSS_SELECTOR, "#text")
    SUGGESTION_TABLE = (By.CSS_SELECTOR, "div.mini-suggest__popup_visible")
    SEARCH_RESULTS = (By.CSS_SELECTOR, "div #search-result")
    FIRST_LINK_IN_RESULTS = (By.CSS_SELECTOR, "li:nth-child(3) .organic__url span")


class PicturesPageLocators:
    PICTURES_LINK = (By.LINK_TEXT, "Картинки")
    PICTURES_FIRST_CATEGORY_WIDGET = (By.CSS_SELECTOR, ".PopularRequestList-Item.PopularRequestList-Item_pos_0 > a")
    PICTURES_FIRST_CATEGORY_NAME = (By.CSS_SELECTOR, ".mini-suggest__input-clear.input__clear_visibility_visible")
    FIRST_PICTURE = (By.CSS_SELECTOR, ".serp-item_pos_0 a")
    PICTURE_SELECTED = (By.CSS_SELECTOR, ".MMImage-Preview")
    NEXT_BUTTON = (By.CSS_SELECTOR, ".CircleButton.CircleButton_type_next")
    PREV_BUTTON = (By.CSS_SELECTOR, ".CircleButton.CircleButton_type_prev")

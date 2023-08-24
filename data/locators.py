from selenium.webdriver.common.by import By


class ItemPageLocators:
    ADD_TO_FAVORITES_BUTTON = (By.CSS_SELECTOR, '.style-header-add-favorite-M7nA2 button')
    ADD_TO_FAVORITES_BUTTON_TEXT = (By.CSS_SELECTOR, '.style-header-add-favorite-M7nA2 button span')


class FavouritesPageLocators:
    FIRST_ITEM_TITLE = (By.XPATH, '//*[text()="Domain-Driven Design Distilled Vaughn Vernon"]')


from pages.base_page import BasePage
from data.locators import ItemPageLocators


class ItemPage(BasePage):
    def should_be_add_to_favorites_button(self):
        assert self.is_element_present(*ItemPageLocators.ADD_TO_FAVORITES_BUTTON),\
            'Кнопка "Добавить в избранное" не отображена на странице'

    def click_on_add_to_favorites_button(self):
        self.should_be_add_to_favorites_button()
        self.browser.find_element(*ItemPageLocators.ADD_TO_FAVORITES_BUTTON).click()

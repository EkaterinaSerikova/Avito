from pages.base_page import BasePage
from data.locators import FavouritesPageLocators


class FavoritesPage(BasePage):
    def item_is_visible(self):
        assert self.is_element_present(*FavouritesPageLocators.FIRST_ITEM_TITLE), 'Объявление не отображено в Избранном'

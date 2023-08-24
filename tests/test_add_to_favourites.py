from data.url import Url
from pages.item_page import ItemPage
from pages.favourites_page import FavoritesPage


def test_add_to_favourites(browser):
    item_page = ItemPage(browser, Url.ITEM_PAGE)
    favourites_page = FavoritesPage(browser, Url.FAVORITES_PAGE)

    # Открыть страницу объявления
    item_page.open()

    # Нажать на кнопку "Добавить в избранное"
    item_page.click_on_add_to_favorites_button()

    # Открыть страницу Избранное
    favourites_page.open()

    # Проверить, что объявление добавлено в Избранное
    favourites_page.item_is_visible()

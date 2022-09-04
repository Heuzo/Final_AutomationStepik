from .base_page import BasePage
from .locators import MainPageLocators, ProductPageLocators


class ProductPage(BasePage):

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def get_item_name(self):
        name = self.browser.find_element(*ProductPageLocators.ITEM_NAME).text
        return name

    def add_to_basket(self):
        button = self.browser.find_element(*MainPageLocators.BASKET_BUTTON)
        button.click()

    def item_added_successed(self, book):
        message = self.browser.find_element(*ProductPageLocators.ITEM_ADDED_SUCCESS_MSG).text
        print(f'Книга : {book}')
        print(f'Сообщение: {message}')
        assert message.count(book) == 1, 'Название добавленной книги не совпадает'

    def get_item_price(self):
        price = self.browser.find_element(*ProductPageLocators.ITEM_PRICE).text
        print(f'Цена книги: {price}')
        return price

    def get_basket_price(self):
        price = self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text
        print(f'Стоимость корзины: {price}')
        return price

    def is_prices_correct(self, price_book, price_basket):
        assert price_book == price_basket, 'Цена книги и цена корзины не совпадают'

    def get_book_info(self):
        price = self.get_item_price()
        book =  self.get_item_name()
        return price, book
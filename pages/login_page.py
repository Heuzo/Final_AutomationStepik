from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # Проверка на корректный url адрес
        assert (self.browser.current_url), 'URL неверный'

    def should_be_login_form(self):
        # Проверка, что есть форма логина
        assert (self.browser.find_element(*LoginPageLocators.LOGIN_FORM)), 'Не отобразилась форма логина'

    def should_be_register_form(self):
        # Проверка, что есть форма регистрации на странице
        assert (self.browser.find_element(*LoginPageLocators.REGISTER_FORM)), 'Не отобразилась форма регистрации'

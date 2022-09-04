from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_BUTTON = (By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')


class LoginPageLocators:
    LOGIN_FORM = (By.XPATH, '//form[@id="login_form"]')
    REGISTER_FORM = (By.XPATH, '//form[@id="register_form"]')


class ProductPageLocators:
    ITEM_ADDED_SUCCESS_MSG = (By.XPATH, '//div[@class="alertinner " and ./strong]')
    ITEM_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    ITEM_PRICE = (By.XPATH, '//div[@class="col-sm-6 product_main"]/p[@class="price_color"]')
    BASKET_PRICE = (By.XPATH, '//div[@class="alertinner "]/p/strong')

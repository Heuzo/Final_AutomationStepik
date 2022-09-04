from .pages.product_page import ProductPage

def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    price, book = page.get_book_info()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.item_added_successed(book)
    basket = page.get_basket_price()
    page.is_prices_correct(price, basket)





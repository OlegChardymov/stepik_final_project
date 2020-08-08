from .pages.product_page import ProductPage
from .pages.product_page import ProductPageLocators


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_product_page()
    browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
    page.solve_quiz_and_get_code()
    page.should_match_product_and_basket()

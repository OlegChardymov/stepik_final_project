from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_not_be_category_url()  #feeling cute, might delete later
        self.should_be_product_url()
        self.should_be_add_to_basket_btn()

    def should_match_product_and_basket(self):
        self.should_be_success_basket_msg()
        self.should_match_product_and_basket_names()
        self.should_match_product_and_basket_price()

    def should_not_be_category_url(self):  #checking if we are not in category
        assert "category" not in self.browser.current_url, "'category' in current url"

    def should_be_product_url(self):
        assert "catalogue" in self.browser.current_url, "'catalogue' not in current url"

    def should_be_add_to_basket_btn(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET), "Basket btn is not present"

    def should_be_success_basket_msg(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_SUCCESS), "Basket success msg is not present"

    def should_match_product_and_basket_names(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_NAME).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, "Basket product name is different"

    def should_match_product_and_basket_price(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_PRICE).text == \
               self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text, "Basket product price is different"

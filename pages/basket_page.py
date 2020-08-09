from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "'basket' not in current url"

    def should_be_empty_basket(self):
        assert self.is_element_not_present(*BasketPageLocators.BASKET_SUMMARY), \
            "basket is not empty"

    def should_be_empty_basket_text(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "no empty basket text"

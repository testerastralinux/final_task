from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_FORM), "Product in basket, but should not be"

    def should_be_right_text_in_empty_basket(self):
        assert not \
            "Your basket is empty." == self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_MESSAGE).text, \
            "Wrong text for empty basket"

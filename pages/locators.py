from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators:
    LOGIN_FORM = (By.ID, "#login_form")
    REG_FORM = (By.ID, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > p.price_color")
    PRODUCT_NAME_IN_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(1) strong")
    PRODUCT_PRICE_IN_MESSAGE = (By.CSS_SELECTOR, ".alert:nth-child(3) strong")

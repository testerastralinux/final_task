from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        reg_id = self.browser.find_element(*LoginPageLocators.REG_ID)
        reg_pass1 = self.browser.find_element(*LoginPageLocators.REG_PASS1)
        reg_pass2 = self.browser.find_element(*LoginPageLocators.REG_PASS2)
        reg_button = self.browser.find_element(*LoginPageLocators.REG_BUTTON)
        reg_id.send_keys(email)
        reg_pass1.send_keys(password)
        reg_pass2.send_keys(password)
        reg_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Substring 'login' not in login url"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_FORM), "Registration form is not presented"

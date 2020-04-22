import time
from pages.base_page import BasePage
from pages.locators import (
    _email_field, _password_field, _login_button, _login_link, _my_profile, _login_error
)


class LoginPage(BasePage):

    def click_login_link(self):
        self.element_click(_login_link)
        time.sleep(3)

    def login(self, email, password):
        self.enter_data(email, _email_field, locatorType="name")
        self.enter_data(password, _password_field, locatorType="name")
        self.element_click(_login_button)
        time.sleep(5)

    def verify_login_successful(self):
        return self.is_element_present(_my_profile)

    def verify_login_failed(self):
        return self.is_element_present(_login_error)

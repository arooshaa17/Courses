from pages.base_page import BasePage
import time
import logging
import utilities.custom_logger as cl
from locators import*


class LoginPage(BasePage):

    log = cl.custom_logger(logging.DEBUG)

    # Locators #
    _login_link = "//a[@class='btn' and contains(text(), 'Sign In')]"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//button[@type='submit']"
    _my_profile = "//section[@id='my-courses']"

    def click_login_link(self):
        self.element_click(self._login_link)

    def enter_email(self, email):
        self.enter_data(email, self._email_field, "name")

    def enter_password(self, password):
        self.enter_data(password, self._password_field, "name")

    def click_login_button(self):
        self.element_click(self._login_button)

    def login(self, email, password):
        self.click_login_link()
        time.sleep(3)
        self.enter_email(email)
        self.enter_password(password)
        self.click_login_button()
        time.sleep(5)

    def verify_login_successful(self):
        result = self.is_element_present("//section[@id='my-courses']", locatorType="xpath")
        return result

import time
from pages.base_page import BasePage
from pages.locators import (
    email_field, password_field, login_button, login_link, my_profile, login_error,
    user_menu, log_out)


class LoginPage(BasePage):

    def click_login_link(self):
        self.element_click(login_link)
        self.wait_for_element(login_button)

    def login(self, email, password):
        self.enter_data(email, email_field, locator_type="name")
        self.enter_data(password, password_field, locator_type="name")
        self.element_click(login_button)

    def logout(self):
        self.wait_for_element(user_menu)
        self.element_click(user_menu)
        time.sleep(2)
        self.click_by_action_chains(log_out)
        time.sleep(3)

    def verify_login_successful(self):
        return self.is_element_present(my_profile)

    def verify_login_failed(self):
        return self.is_element_present(login_error)

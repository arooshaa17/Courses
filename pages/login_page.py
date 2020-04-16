from pages.base_page import BasePage
import time
import logging
import utilities.custom_logger as cl


class LoginPage(BasePage):
    log = cl.customLogger(logging.DEBUG)

    # Locators

    _login_link = "//a[@class='btn' and contains(text(), 'Sign In')]"
    _email_field = "email"
    _password_field = "password"
    _login_button = "//button[@type='submit']"
    _my_profile = "//section[@id='my-courses']"

    def clickLoginLink(self):
        self.elementClick(self._login_link)

    def enterEmail(self, email):
        self.enterData(email, self._email_field, "name")

    def enterPassword(self, password):
        self.enterData(password, self._password_field, "name")

    def clickLoginButton(self):
        self.elementClick(self._login_button)

    def login(self, email, password):
        self.clickLoginLink()
        time.sleep(3)
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        time.sleep(5)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//section[@id='my-courses']", locatorType="xpath")
        return result


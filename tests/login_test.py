import time
import unittest

from selenium import webdriver
from pages.login_page import LoginPage


class LoginTest(unittest.TestCase):

    def setUp(self):
        baseURL = "https://www.edx.org/"
        self.driver = webdriver.Firefox()
        # self.driver = webdriver.Chrome("C:/Users/Aroosha Arif/workspace_python/drivers/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(3)
        self.driver.get(baseURL)
        self.login_page = LoginPage(self.driver)

    def test_valid_login(self):
        self.login_page.login('newtest5718@gmail.com', 'testselenium123')
        time.sleep(2)
        result = self.login_page.verifyLoginSuccessful()
        assert result == True

    def tearDown(self):
        """
        Tear down
        """
        # self.driver.close()

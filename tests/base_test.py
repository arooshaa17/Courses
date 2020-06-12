import unittest
from selenium import webdriver
from pages.courses_page import CoursePage
from pages.home_page import HomePage
from pages.login_page import LoginPage
from data_set import BASE_URL, EMAIL, PASSWORD
from pages.user_settings_page import UserSettingsPage


class BaseTest(unittest.TestCase):

    def setUp(self):
        """
        Setup runs before every test
        """
        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        self.login_page = LoginPage(self.driver)
        self.course_page = CoursePage(self.driver)
        self.home_page = HomePage(self.driver)
        self.user_page = UserSettingsPage(self.driver)

        self.login_page.click_login_link()
        self.login_page.login(EMAIL, PASSWORD)

    def tearDown(self):
        """
        Tear down runs after every test
        """
        # self.driver.close()

import unittest
from selenium import webdriver
from pages.courses_page import CoursePage
from pages.login_page import LoginPage
from data_set import BASE_URL
import os


class BaseTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(BASE_URL)
        self.login_page = LoginPage(self.driver)
        self.course = CoursePage(self.driver)


    def tearDown(self):
        """
        Tear down
        """
        self.driver.close()

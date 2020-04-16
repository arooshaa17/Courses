# import unittest
#
# from selenium import webdriver
# from pages.login_page import LoginPage
#
#
# class BaseTest(unittest.TestCase):
#
#     def setUp(self):
#         baseURL = "https://www.udemy.com/"
#         driver = webdriver.Firefox()
#         driver.maximize_window()
#         driver.implicitly_wait(3)
#         driver.get(baseURL)
#         self.lp = self.LoginPage(driver)
#         self.lp.login('aroosha_17@hotmail.com', 'testselenium123')
#
#     def tearDown(self):
#         """
#         Tear down
#         """
#         self.driver.close()

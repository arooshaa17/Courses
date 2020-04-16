import time
import unittest

from selenium import webdriver

from pages.courses_page import CoursePage
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
        self.course = CoursePage(self.driver)

    def test_course_enrollment(self):
        course_name = "Introduction to Python: Absolute Beginner"
        self.login_page.login('newtest5718@gmail.com', 'testselenium123')
        time.sleep(3)
        self.course.exploreCourses()
        time.sleep(3)
        self.course.searchCourse("Python")
        time.sleep(3)
        self.course.selectCourse(course_name)
        result = self.course.verifyEnrollSuccessful(course_name)
        assert result == True

    def tearDown(self):
        """
        Tear down
        """


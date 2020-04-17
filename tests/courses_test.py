import time
from selenium import webdriver
from pages.login_page import LoginPage
from tests.base_test import BaseTest
from data_set import*


class CourseTest(BaseTest):

    def test_course_enrollment(self):
        """
        Verify that user is able to enroll in a course

        """
        self.login_page.login(EMAIL, PASSWORD)
        time.sleep(3)
        self.course.explore_courses()
        time.sleep(3)
        self.course.search_course(SEARCH_KEY)
        time.sleep(3)
        self.course.select_course(COURSE_NAME)
        result = self.course.verify_enroll_successful(COURSE_NAME)
        self.assertTrue(result, "Enrollment failed")



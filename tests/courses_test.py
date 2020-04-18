import time
from data_set import *
from tests.base_test import BaseTest


class CourseTest(BaseTest):

    def test_course_enrollment(self):
        """
        Verify that user is able to enroll in a course
        """
        self.login_page.click_login_link()
        self.login_page.login(EMAIL, PASSWORD)
        self.course_page.explore_courses()
        self.course_page.search_course(SEARCH_KEY)
        self.course_page.select_course(COURSE_NAME)
        result = self.course_page.verify_enroll_successful(COURSE_NAME)
        self.assertTrue(result, "Enrollment failed")



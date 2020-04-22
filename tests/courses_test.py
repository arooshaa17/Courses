from data_set import *
from pages.locators import page_selectors_list
from tests.base_test import BaseTest


class CourseTest(BaseTest):

    def test_home_page_nav_bar(self):
        """
        Verify that nav bar items on Home page are redirected to correct page
        """
        actual_home_page_title_list = self.home_page.verify_homepage_nav_bar(page_selectors_list)
        self.assertEqual(actual_home_page_title_list, EXPECTED_HOME_PAGE_TITLE_LIST)

    def test_course_enrollment(self):
        """
        Verify that user can search and enroll in a course, and after enrollment it is added to My courses
        """
        self.course_page.explore_courses()
        self.course_page.search_course(SEARCH_KEY)
        self.course_page.select_course(COURSE_NAME)
        result = self.course_page.verify_enroll_successful(COURSE_NAME)
        self.assertTrue(result, "Enrollment failed")

    def test_upgrading_course_enrollment(self):
        """
        Verify that user can upgrade his/her course enrollment following the payment flow
        """
        result = self.course_page.verify_upgrade_enrollment(COURSE_NAME)
        self.assertTrue(result, "Upgrade failed")


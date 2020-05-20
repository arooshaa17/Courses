from data_set import *
from pages.locators import page_selectors_list, footer_elements_list
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

    def test_course_pages_response_code(self):
        """
        Verify that internal course pages are showing OK response
        """
        result = self.course_page.verify_course_pages_response(COURSE_NAME)
        self.assertTrue(result, "Response code is not OK")

    def test_resume_course(self):
        """
        Verify that user can resume a previous course successfully
        """
        self.course_page.open_any_course()
        actual_title = self.course_page.get_course_title()
        self.login_page.logout()
        self.driver.get(BASE_URL)
        self.login_page.click_login_link()
        self.login_page.login(EMAIL, PASSWORD)
        expected_title = self.course_page.verify_resume_course_title()
        self.assertEqual(expected_title, actual_title, "User could not resume previous course")

    def test_page_footer(self):
        """
        Verify that footer links are present on dashboard, programs and courses pages
        """
        result = self.home_page.verify_footer_for_all_pages(page_selectors_list, footer_elements_list)
        self.assertTrue(result, "Footer elements are missing")

    def test_course_price(self):
        """
        Verify that course price at checkout is same as is on the Course page
        """
        result = self.course_page.verify_course_price_in_cart(COURSE_NAME2)
        self.assertTrue(result, "Prices are not same")

    def test_courses_filters(self):
        """
        Verify that applying filters on courses shows the correct result
        """
        self.course_page.explore_courses()
        self.assertTrue(self.course_page.verify_search_filters(SEARCH_KEY))
        self.assertTrue(self.course_page.verify_course_filters(VERIFIED_LINK))
        self.assertTrue(self.course_page.verify_course_partner_filters(PARTNER_VALUE))
        self.assertTrue(self.course_page.verify_all_filters_applied(EXPECTED_FILTERS))


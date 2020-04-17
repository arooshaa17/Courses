import time
import logging
from pages.base_page import BasePage
import utilities.custom_logger as cl


class CoursePage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    # Locators #
    _search_box = "//input[@name='search_query']"
    _explore_course = "//a[@class='btn-neutral']"
    _search_button = "//*[@class='icon fa fa-search']"
    # _course = "//h3[contains(text(),'Introduction to Python: Fundamentals')]"
    _course = "//h3[contains(text(),'{0}')]"
    _enroll_button = "//button[@class='btn enroll-btn legacy w-100']"
    _free_trial = "//button[@id='free_trial_start_button_button']"
    _amount = "//div[@class='total-subscriptions-container price-line horizontal-box']"
    _my_course = "//a[contains(text(),'{0}')]"

    # Element Interactions #

    def explore_courses(self):
        self.element_click(self._explore_course)

    def search_course(self, name):
        self.enter_data(name, self._search_box)
        time.sleep(1)
        self.element_click(self._search_button)

    def select_course(self, fullCourseName):
        self.element_click(locator=self._course.format(fullCourseName), locatorType="xpath")

    def click_enroll_course_link(self):
        self.element_click(self._enroll_button)

    def enroll_course(self, name, fullCourseName):
        self.search_course(name)
        self.select_course(fullCourseName)
        self.click_enroll_course_link()

    def verify_enroll_successful(self, fullCourseName):
        self.navigate_to_page("https://courses.edx.org/dashboard")
        result = self.is_element_present(locator=self._my_course.format(fullCourseName))
        return result

import time
import logging

from data_set import DASHBOARD
from pages.base_page import BasePage
import utilities.custom_logger as cl
from locators import (
    _search_box, _search_button, _enroll_button, _course, _my_course, _explore_course
)


class CoursePage(BasePage):
    log = cl.custom_logger(logging.DEBUG)

    def explore_courses(self):
        self.element_click(_explore_course)
        time.sleep(3)

    def search_course(self, name):
        self.enter_data(name, _search_box)
        time.sleep(3)
        self.element_click(_search_button)
        time.sleep(3)

    def select_course(self, full_course_name):
        self.element_click(_course.format(full_course_name))
        time.sleep(3)

    def click_enroll_course_link(self):
        self.element_click(_enroll_button)
        time.sleep(1)

    def enroll_course(self, name, full_course_name):
        self.search_course(name)
        self.select_course(full_course_name)
        self.click_enroll_course_link()

    def verify_enroll_successful(self, full_course_name):
        self.navigate_to_page(DASHBOARD)
        return self.is_element_present(_my_course.format(full_course_name))

import time

from data_set import DASHBOARD
from pages.base_page import BasePage
from pages.locators import *
from pages.locators import (
    _search_box, _search_button, _enroll_button, _course, _my_course, _explore_course
)


class CoursePage(BasePage):

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

    def verify_upgrade_enrollment(self, full_course_name):
        self.element_click(_my_course.format(full_course_name))
        self.wait_for_element(upgrade_link)
        self.element_click(upgrade_link)
        self.wait_for_element(first_name)
        self.enter_random_data(first_name, 7)
        self.enter_random_data(last_name, 7)
        self.enter_random_data(address, 7)
        self.enter_random_data(unit, 7)
        self.enter_random_data(city, 7)
        self.select_value_from_dropdown(country, 'US')
        self.select_value_from_dropdown(state, 'MA')
        self.enter_random_data(postal_code, 5, type='digits')
        self.enter_random_data(card_number, 20, type='digits')
        self.enter_random_data(security_code, 3, type='digits')
        self.select_value_from_dropdown(card_expiration_month, '12')
        self.select_value_from_dropdown(card_expiration_year, '2020')
        self.element_click(place_order_button)
        time.sleep(3)
        return self.is_element_present(card_error)

import time

from data_set import DASHBOARD
from pages.base_page import BasePage
from pages.locators import *


class CoursePage(BasePage):

    def explore_courses(self):
        self.wait_for_element(explore_course)
        self.element_click(explore_course)

    def search_course(self, search_key):
        search_key.lower()
        self.wait_for_element(search_button)
        self.enter_data(search_key, search_box)
        self.element_click(search_button)

    def select_course(self, full_course_name):
        self.element_click(course.format(full_course_name))
        time.sleep(3)

    def click_enroll_course_link(self):
        self.element_click(enroll_button)
        time.sleep(1)

    def open_any_course(self):
        self.wait_for_element(enter_course)
        self.click_random_element_from_list(enter_course)
        self.wait_for_element(course_title)

    def enroll_course(self, name, full_course_name):
        self.search_course(name)
        self.select_course(full_course_name)
        self.click_enroll_course_link()

    def go_to_home_page(self):
        self.element_click(logo)

    def verify_enroll_successful(self, full_course_name):
        self.navigate_to_page(DASHBOARD)
        return self.is_element_present(my_course.format(full_course_name))

    def verify_upgrade_enrollment(self, full_course_name):
        self.element_click(my_course.format(full_course_name))
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
        self.enter_random_data(postal_code, 5, data_type='digits')
        self.enter_random_data(card_number, 20, data_type='digits')
        self.enter_random_data(security_code, 3, data_type='digits')
        self.select_value_from_dropdown(card_expiration_month, '12')
        self.select_value_from_dropdown(card_expiration_year, '2020')
        self.element_click(place_order_button)
        time.sleep(3)
        return self.is_element_present(card_error)

    def verify_course_pages_response(self, full_course_name):
        """
        Explore a course and verify that all 4 tabs are present and are loaded with response code OK"
        """
        courses_tabs = [course_tab, progress_tab, wiki_tab, discussion_tab]
        self.element_click(my_course.format(full_course_name))
        self.wait_for_element(start_course_link)
        self.element_click(start_course_link)
        time.sleep(2)
        try:
            for tab in courses_tabs:
                self.element_click(tab)
                self.verify_response_code(self.driver.current_url)
                time.sleep(1)
        except:
            return False
        return True

    def get_course_title(self):
        actual_title = self.get_element_text(course_title)
        return actual_title

    def verify_resume_course_title(self):
        """
        Resume a course from user menu and return its Title
        """
        self.wait_for_element(user_menu)
        self.element_click(user_menu)
        time.sleep(2)
        self.click_by_action_chains(resume_course_link)
        self.wait_for_element(course_title)
        resume_course_title = self.get_element_text(course_title)
        return resume_course_title

    def verify_course_price_in_cart(self, full_course_name):
        """
        Go to cart and check price of course is the same as shown on upgrade link page
        """
        self.explore_courses()
        self.select_course(full_course_name)
        self.wait_for_element(enroll_button)
        self.element_click(enroll_button)
        self.wait_for_element(upgrade_link)
        self.get_element(upgrade_link)
        upgrade_course_price = self.get_element_text(upgrade_price)
        self.element_click(upgrade_link)
        self.wait_for_element(cart_price)
        cart_course_price = self.get_element_text(cart_price)
        return upgrade_course_price in cart_course_price

    def verify_search_filters(self, search_key):
        self.search_course(search_key)
        self.wait_for_element(filter_buttons_list)
        return self.is_element_present(filter_element.format(search_key))

    def verify_course_filters(self, filter_value):
        self.element_click(any_filter.format(filter_value))
        self.wait_for_element(filter_buttons_list)
        return self.is_element_present(filter_element.format(filter_value))

    def verify_course_partner_filters(self, filter_value):
        self.select_value_from_dropdown(partner_dropdown, filter_value, select_by='text')
        self.element_click(partner_submit_button)
        self.wait_for_element(filter_buttons_list)
        return self.is_element_present(filter_element.format(filter_value))

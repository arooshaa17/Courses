import time
from pages.base_page import BasePage


class HomePage(BasePage):

    def verify_homepage_nav_bar(self, selectors_list):
        """
        Verify page titles of all links on home page
        :param selectors_list: list of locators for all main nav links pages
        :return: List of actual page titles of all re-directions of nav links
        """
        page_title_list = []
        for selector in selectors_list:
            self.element_click(selector)
            page_title_list.append(self.driver.title)
            time.sleep(3)
        return page_title_list

    def verify_footer_for_all_pages(self, selectors_list, footer_elements_list):
        """
         Verify that footer links are present on dashboard, programs and courses pages
               :param footer_elements_list: expected list of all footer links on pages
               :param selectors_list: list of locators for all main nav links pages
               :return: True or False
        """
        # for each page, verify every footer link
        is_present = None
        for selector in selectors_list:
            self.element_click(selector)
            print(self.driver.title)
            self.scrollPage(1000)
            time.sleep(3)
            for footer_element in footer_elements_list:
                is_present = self.is_element_present(footer_element)
        return is_present

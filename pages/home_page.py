import time
from pages.base_page import BasePage


class HomePage(BasePage):

    def verify_homepage_nav_bar(self, selectors_list):
        """
        Verify page titles of all links on home page
        :param selectors_list: list of locators for all main nav links
        :return: List of actual page titles of all re-directions of nav links
        """
        page_title_list = []
        for selector in selectors_list:
            self.element_click(selector)
            page_title_list.append(self.driver.title)
            time.sleep(3)
        return page_title_list

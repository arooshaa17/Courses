import time
from pages.base_page import BasePage
import requests


class HomePage(BasePage):

    def verify_homepage_nav_bar(self, selectors_list):
        """
        Verify page titles of all links on home page
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
        """
        # for each page, verify every footer link
        for selector in selectors_list:
            try:
                self.element_click(selector)
                print(self.driver.title)
                time.sleep(3)
                for footer_element in footer_elements_list:
                    self.is_element_present(footer_element)
            except:
                return False
        return True

    def verify_response_code(self, url):
        r = requests.get(url)
        print(r.status_code)

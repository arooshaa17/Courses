import logging
import random
import string
import time
import requests
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
import utilities.custom_logger as cl


class BasePage(object):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locator_type):
        locator_type = locator_type.lower()
        if locator_type == "id":
            return By.ID
        elif locator_type == "name":
            return By.NAME
        elif locator_type == "xpath":
            return By.XPATH
        elif locator_type == "css":
            return By.CSS_SELECTOR
        elif locator_type == "class":
            return By.CLASS_NAME
        elif locator_type == "tag":
            return By.TAG_NAME
        elif locator_type == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locator_type +
                          " not correct/supported")
        return False

    def get_element(self, locator, locator_type="xpath"):
        byType = self.get_by_type(locator_type)
        element = self.driver.find_element(byType, locator)
        return element

    def get_element_list(self, locator, locator_type="xpath"):
        byType = self.get_by_type(locator_type)
        elements = self.driver.find_elements(byType, locator)
        if len(elements) > 0:
            print("Element list FOUND")
            print(len(elements))
        else:
            print("Element list NOT FOUND")
        return elements

    def get_element_text(self, locator, locator_type="xpath"):
        element = self.get_element(locator, locator_type)
        return element.text

    def get_attribute_value(self, attribute, locator, locator_type="xpath"):
        element = self.get_element(locator, locator_type)
        return element.get_attribute(attribute)

    def element_displayed(self, locator, locator_type="xpath"):
        element = self.get_element(locator, locator_type)
        return element.is_displayed()

    def element_click(self, locator, locator_type="xpath"):
        element = self.get_element(locator, locator_type)
        element.click()

    def click_random_element_from_list(self, locator, locator_type="xpath"):
        element_list = self.get_element_list(locator, locator_type)
        print(element_list)
        random_element = random.choice(element_list)
        print(random_element)
        random_element.click()

    def enter_data(self, data, locator, locator_type="xpath"):
        element = self.get_element(locator, locator_type)
        element.send_keys(data)

    def enter_random_data(self, locator, length, locator_type="xpath", data_type='letters'):
        element = self.get_element(locator, locator_type)
        element.send_keys(self.get_alpha_numeric_data(length, data_type))

    def is_element_displayed(self, locator, locator_type="xpath"):
        element = self.get_element(locator, locator_type)
        displayed = element.is_displayed()
        return displayed

    def navigate_to_page(self, url):
        self.driver.get(url)

    def get_page_title(self):
        return self.driver.title

    def is_element_present(self, locator, locator_type="xpath"):
        element = self.get_element(locator, locator_type)
        if element is not None:
            return True
        else:
            self.log.info("Element not present with locator: " + locator +
                          " locator_type: " + locator_type)
            return False

    def select_value_from_dropdown(self, locator, data, locator_type="xpath", select_by='value'):

        element = self.get_element(locator, locator_type)
        time.sleep(3)
        selection = Select(element)
        if select_by == 'index':
            selection.select_by_index(data)
        elif select_by == 'text':
            selection.select_by_visible_text(data)
        else:
            selection.select_by_value(data)

    def click_by_action_chains(self, locator, locator_type="xpath"):
        submenu = self.get_element(locator, locator_type)
        actions = ActionChains(self.driver)
        actions.move_to_element(submenu).click(submenu).perform()

    def wait_for_element(self, locator, locator_type="xpath"):
        """
        Wait for element visibility
        """
        byType = self.get_by_type(locator_type)
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((byType, locator))
        )

    def get_alpha_numeric_data(self, length, data_type='letters'):
        """
        Get random string of characters

        Parameters:
            length: Length of string, number of characters string should have
            data_type: Type of characters string should have. Default is letters
            Provide lower/upper/digits for different types
        """
        alpha_num = ''
        if data_type == 'lower':
            case = string.ascii_lowercase
        elif data_type == 'upper':
            case = string.ascii_uppercase
        elif data_type == 'digits':
            case = string.digits
        elif data_type == 'mix':
            case = string.ascii_letters + string.digits
        else:
            case = string.ascii_letters
        return alpha_num.join(random.choice(case) for i in range(length))

    def verify_page_titles_list(self, locators_list, expected_list):

        actual_page_titles_list = []
        for locator in locators_list:
            self.element_click(locator)
            actual_page_titles_list.append(self.get_page_title)
            time.sleep(3)
        return actual_page_titles_list == expected_list

    def scrollPage(self, offset):
        self.driver.execute_script("window.scrollBy(0, arguments[0])", offset)
        time.sleep(3)

    def verify_response_code(self, url):
        r = requests.get(url)
        print(r.status_code)

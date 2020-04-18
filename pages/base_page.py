import logging
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import utilities.custom_logger as cl


class BasePage(object):
    log = cl.custom_logger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def get_by_type(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        else:
            self.log.info("Locator type " + locatorType +
                          " not correct/supported")
        return False

    def get_element(self, locator, locatorType="xpath"):
        byType = self.get_by_type(locatorType)
        element = self.driver.find_element(byType, locator)
        return element

    def element_click(self, locator, locatorType="xpath"):
        element = self.get_element(locator, locatorType)
        element.click()

    def enter_data(self, data, locator, locatorType="xpath"):
        element = self.get_element(locator, locatorType)
        element.send_keys(data)

    def is_element_displayed(self, locator, locatorType="xpath"):
        element = self.get_element(locator, locatorType)
        displayed = element.is_displayed()
        return displayed

    def navigate_to_page(self, url):
        self.driver.get(url)

    def is_element_present(self, locator, locatorType="xpath"):
        element = self.get_element(locator, locatorType)
        if element is not None:
            return True
        else:
            self.log.info("Element not present with locator: " + locator +
                          " locatorType: " + locatorType)
            return False

    def wait_for_element(self, locator):
        """
        Wait for element
        """
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, locator))
        )

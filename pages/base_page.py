import logging
import time
from traceback import print_stack
from selenium.common.exceptions import *
from selenium.webdriver.common.by import By
import logging
import utilities.custom_logger as cl
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class BasePage(object):
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        self.driver = driver

    def getByType(self, locatorType):
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

    def getElement(self, locator, locatorType="xpath"):
        byType = self.getByType(locatorType)
        element = self.driver.find_element(byType, locator)
        return element

    def elementClick(self, locator, locatorType="xpath"):
        element = self.getElement(locator, locatorType)
        element.click()

    def enterData(self, data, locator, locatorType="xpath"):
        element = self.getElement(locator, locatorType)
        element.send_keys(data)

    def isElementDisplayed(self, locator, locatorType="xpath"):
        element = self.getElement(locator, locatorType)
        isDisplayed = element.is_displayed()
        return isDisplayed

    def navigateTo(self, url):
        self.driver.get(url)

    def isElementPresent(self, locator, locatorType="xpath"):
        element = self.getElement(locator, locatorType)
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

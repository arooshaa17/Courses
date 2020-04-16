import time
import logging
from pages.base_page import BasePage
import utilities.custom_logger as cl


class CoursePage(BasePage):
    log = cl.customLogger(logging.DEBUG)

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

    def exploreCourses(self):
        self.elementClick(self._explore_course)

    def searchCourse(self, name):
        self.enterData(name, self._search_box)
        self.elementClick(self._search_button)

    def selectCourse(self, fullCourseName):
        self.elementClick(locator=self._course.format(fullCourseName), locatorType="xpath")

    def clickEnrollButton(self):
        self.elementClick(self._enroll_button)

    def enrollCourse(self, name, fullCourseName):
        self.searchCourse(name)
        self.selectCourse(fullCourseName)
        self.clickEnrollButton()

    def verifyEnrollSuccessful(self, fullCourseName):
        self.navigateTo("https://courses.edx.org/dashboard")
        result = self.isElementPresent(locator=self._my_course.format(fullCourseName))
        return result

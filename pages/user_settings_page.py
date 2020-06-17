import time

import pyautogui
from selenium.webdriver import ActionChains

from data_set import IMAGE_PATH
from pages.base_page import BasePage
from pages.locators import *


class UserSettingsPage(BasePage):

    def upload_profile_picture(self):
        time.sleep(10)
        self.wait_for_element(user_menu)
        self.element_click(user_menu)
        self.wait_for_element(profile_link)
        self.click_by_action_chains(profile_link)
        self.wait_for_element(upload_photo_link)
        self.element_click(upload_photo_link)
        pyautogui.write(IMAGE_PATH)
        time.sleep(10)
        pyautogui.press('enter')
        time.sleep(10)
        self.element_click(change_dropdown)
        actions = ActionChains(self.driver)
        remove_image_link = self.get_element(remove_option)
        actions.move_to_element(remove_image_link).perform()
        return self.is_element_present(remove_option)

    def remove_profile_picture(self):
        self.click_by_action_chains(remove_option)
        time.sleep(10)
        return self.is_element_present(upload_photo_link)

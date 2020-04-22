import time
import os
from tests.base_test import BaseTest
from data_set import *


class LoginTest(BaseTest):
    username = os.environ.get('EDX_USERNAME')
    password = os.environ.get('EDX_PASSWORD')

    def test_valid_login(self):
        """
        Verify that user is able to Login successfully
        """
        self.login_page.click_login_link()
        self.login_page.login(EMAIL, PASSWORD)
        result = self.login_page.verify_login_successful()
        self.assertTrue(result, "Login failed!")

    def test_invalid_login(self):
        """
        Verify that user is able to Login successfully
        """
        self.login_page.click_login_link()
        self.login_page.login(EMAIL, INVALID_PASSWORD)
        result = self.login_page.verify_login_failed()
        self.assertTrue(result, "Login failed!")

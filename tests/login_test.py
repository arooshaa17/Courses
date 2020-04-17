import time
from tests.base_test import BaseTest
from data_set import *
import os


class LoginTest(BaseTest):
    username = os.environ.get('EDX_USERNAME')
    access_key = os.environ.get('EDX_PASSWORD')

    def test_valid_login(self):
        """
        Verify that user is able to Login successfully
        """
        self.login_page.login(EMAIL, PASSWORD)
        time.sleep(2)
        self.assertTrue(self.login_page.verify_login_successful(), "Login failed!")

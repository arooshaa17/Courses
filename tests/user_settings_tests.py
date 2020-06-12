from tests.base_test import BaseTest


class UserTest(BaseTest):

    def test_updating_user_profile(self):
        """
        Verify that user is able to update its profile successfully
        """
        self.assertTrue(self.user_page.update_user_profile(), "Unable to upload image")

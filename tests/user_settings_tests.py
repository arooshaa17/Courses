from tests.base_test import BaseTest


class UserTest(BaseTest):

    def test_updating_user_profile(self):
        """
        Verify that user is able to update its profile successfully
        """
        try:
            result1 = self.user_page.upload_profile_picture()
            self.assertTrue(result1, "Unable to upload user's profile picture")
        except:
            self.user_page.screen_shot()

        result2 = self.user_page.remove_profile_picture()
        self.assertTrue(result2, "Unable to remove user's profile picture")
        if result2 is not True:
            self.user_page.screen_shot()

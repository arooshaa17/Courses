import unittest
from tests.login_test import LoginTest
from tests.courses_test import CourseTest
from tests.user_settings_tests import UserTest

# Get all tests from the test classes
tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(CourseTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(UserTest)

# Create a test suite combining all test classes
smokeTest = unittest.TestSuite([tc1, tc2, tc3])

unittest.TextTestRunner(verbosity=3).run(smokeTest)

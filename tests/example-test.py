import unittest

from tests.base_test import BaseTest
from utils.constants.logger_messages import LoggerMessages


class ExampleTest(BaseTest):

    def test_google_connection(self):
        title = self.driver.title
        self.assertEqual(title, "Google", "Failed to connect to Google")
        self.file_logger.log_info(LoggerMessages.ON_PASSED)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()

import P
from utils.config import Config
from utils.driver_factory import DriverFactory
from pages.example_page import ExamplePage
from utils.logger_manager import FileLogger


class BaseTest(unittest.TestCase):
    example_page = None
    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = DriverFactory.get_driver(Config.BROWSER)
        cls.file_logger = FileLogger(Config.LOGER_FILE_PATH)
        cls.example_page = ExamplePage(cls.driver)
        cls.example_page.open_url(Config.BASE_URL + cls.example_page.path)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

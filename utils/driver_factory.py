from selenium import webdriver


class DriverFactory:
    @staticmethod
    def get_driver(browser_name):
        if browser_name.lower() == 'chrome':
            return webdriver.Chrome()
        elif browser_name.lower() == 'firefox':
            return webdriver.Firefox()
        elif browser_name.lower() == 'safari':
            return webdriver.Safari()
        else:
            raise ValueError(f"Unsupported browser: {browser_name}")

class BasePage:
    path = None

    def __init__(self, driver):
        self.timeout = 10
        self.driver = driver
        if self.path is None:
            raise NotImplementedError("Subclasses must override base_url")

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.driver.find_element(*locator)

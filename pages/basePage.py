from selenium.webdriver.common.by import By

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open_url(self, url):
        self.driver.get(url)

    def take_screenshot(self, name):
        # Save the screenshot to a file
        return self.driver.get_screenshot_as_png()

    def find_element(self, locator_type, locator):
        return self.driver.find_element(locator_type, locator)

    def click(self, locator_type, locator):
        self.find_element(locator_type, locator).click()

    def send_keys(self, locator_type, locator, text):
        self.find_element(locator_type, locator).send_keys(text)
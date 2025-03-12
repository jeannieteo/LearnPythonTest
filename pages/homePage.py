from selenium.webdriver.common.by import By
from pages.basePage import BasePage

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.search_box = (By.ID, "search-bar")
        self.search_button = (By.ID, "search-button")

    def perform_search(self, search_term):
        self.send_keys(*self.search_box, search_term)
        self.click(*self.search_button)
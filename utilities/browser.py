from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_browser():
    # Automatically set up a Chrome browser instance
    driver = webdriver.Chrome(service=Service())
    driver.maximize_window()
    return driver
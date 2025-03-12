import allure
import pages.basePage as bp
import utilities.browser as browse

import allure
from pages.basePage import BasePage

@allure.feature("Web Test Example")
@allure.story("Open Google and validate title")
def test_open_google(browser):
    page = BasePage(browser)
    
    with allure.step("Open Google homepage"):
        page.open_url("https://www.google.com")

    with allure.step("Validate page title and capture screenshot"):
        allure.attach(
            browser.get_screenshot_as_png(),
            name="Google Homepage",
            attachment_type=allure.attachment_type.PNG
        )
        assert "Google" in browser.title
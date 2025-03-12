import pytest
from utilities.browser import get_browser
import allure

@pytest.fixture
def browser():
    # Setup: Initialize the browser
    driver = get_browser()
    yield driver
    # Teardown: Take a screenshot on failure and close the browser
    if pytest.last_failed:
        allure.attach(
            driver.get_screenshot_as_png(),
            name="Failure Screenshot",
            attachment_type=allure.attachment_type.PNG
        )
    driver.quit()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Check if the test has failed
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        pytest.last_failed = True  # Mark test as failed
    else:
        pytest.last_failed = False
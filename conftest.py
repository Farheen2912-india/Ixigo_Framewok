import pytest
from selenium import webdriver
import os
from datetime import datetime


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.ixigo.com/")
    driver.implicitly_wait(10)
    yield driver

    driver.quit()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    # Take screenshot only when test fails
    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")

        if driver:
            folder = "Screenshots"
            os.makedirs(folder, exist_ok=True)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            screenshot_path = os.path.join(folder,f"{item.name}_{timestamp}.png")
            driver.save_screenshot(screenshot_path)
            print(f"Failed screenshot saved: {screenshot_path}")
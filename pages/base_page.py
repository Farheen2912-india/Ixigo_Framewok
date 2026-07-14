from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException
from datetime import datetime
import os


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def click(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))

        try:
            element.click()
        except ElementClickInterceptedException:
            # If normal click fails, use JavaScript click
            self.driver.execute_script("arguments[0].click();", element)

    def enter_text(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def is_displayed(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()

    def send_keys(self, locator, text):
        self.wait.until(EC.element_to_be_clickable(locator)).send_keys(text)

    def take_screenshot(self, name=None):
        folder = "screenshots"
        os.makedirs(folder, exist_ok=True)
        if name is None:
            name = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.driver.save_screenshot(os.path.join(folder, f"{name}.png"))
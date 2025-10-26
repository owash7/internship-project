from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
from datetime import datetime

class Page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_url(self, url):
        self.driver.get(url)

    def find_element(self, *locator):
        return self.driver.find_element(*locator)

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def click(self, *locator):
        self.driver.find_element(*locator).click()

    def input_text(self, text, *locator):
        self.driver.find_element(*locator).send_keys(text)


    # Waits

    def wait_for_element_clickable_click(self, *locator, message=None):
         self.wait.until(EC.element_to_be_clickable(locator), message= f'Element by {locator} not clickable').click()

    def wait_for_element_visible(self, *locator, message=None):
        return self.wait.until(EC.visibility_of_element_located(locator), f'Element by {locator} did not appear')

    # Verification Commands

    def verify_url(self, expected_url):
        actual_url = self.driver.current_url
        assert expected_url in actual_url, f'Expected {expected_url}, but got {actual_url}'

    def verify_text(self, expected_text, *locator):
        actual_text = self.find_element(*locator).text
        assert expected_text in actual_text, f'Expected {expected_text}, but got {actual_text}'


    def debug_snapshot(self, name="debug"):
        """Save screenshot and page source with timestamp for debugging."""
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        folder = "debug_artifacts"
        os.makedirs(folder, exist_ok=True)

        screenshot_path = os.path.join(folder, f"{name}_{timestamp}.png")
        html_path = os.path.join(folder, f"{name}_{timestamp}.html")

        self.driver.save_screenshot(screenshot_path)
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(self.driver.page_source)

        print(f"\n🪲 Debug files saved:\n  Screenshot → {screenshot_path}\n  HTML → {html_path}\n")

        return screenshot_path, html_path
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click_element(self, locator):
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def enter_text(self, locator, text):
        el = self.wait.until(EC.visibility_of_element_located(locator))
        el.clear()
        if text:  # checks for None or empty string
            el.send_keys(text)

    def wait_until_element_visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from utils import wait_for_file
from web_driver import WebDriver
from wolt.wolt_shopping_actions import WoltShoppingActions


class WoltAutomation:
    def __init__(self, web_driver: WebDriver, shopping_actions: WoltShoppingActions):
        self.web_driver = web_driver
        self.driver = web_driver.driver
        self.shopping_actions = shopping_actions
        self.run_automation()

    def accept_cookies(self):
        cookies_accept_button_xpath = "//button[@data-localization-key='gdpr-consents.banner.accept-button']"
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, cookies_accept_button_xpath))).click()

    def click_profile_pic_or_login(self):
        login_button_test_id = "UserStatus.Login"
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, f'button[data-test-id="{login_button_test_id}"]'))
        ).click()

    def is_logged_in(self):
        """check if the user-specific element (search input) is present, indicating a logged-in state."""
        try:
            search_input_css = "input[placeholder='חיפוש באתר']"
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, search_input_css)))
            return True
        except TimeoutException:
            return False

    def navigate_to_site(self, url="https://wolt.com"):
        self.driver.get(url)

    def run_automation(self):
        amount = wait_for_file('saved_texts_files/amount.txt')

        self.navigate_to_site()
        if not self.is_logged_in():
            self.accept_cookies()
            self.click_profile_pic_or_login()

        self.shopping_actions.complete_shopping_flow("Gift Card", amount)

        time.sleep(50)
        self.driver.quit()

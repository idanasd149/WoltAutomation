from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from utils import wait_for_file
from web_driver import WebDriver


class WoltAutomation:
    def __init__(self, web_driver: WebDriver):
        self.web_driver = web_driver
        self.driver = web_driver.driver
        self.run_automation()

    def accept_cookies(self):
        try:
            cookies_accept_button_xpath = "//button[@data-localization-key='gdpr-consents.banner.accept-button']"
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, cookies_accept_button_xpath))).click()
        except TimeoutException:
            pass

    def click_profile_pic_or_login(self):
        try:
            login_button_test_id = "UserStatus.Login"
            WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, f'button[data-test-id="{login_button_test_id}"]'))
            ).click()
        except TimeoutException:
            pass

    def search_for_gift_card(self, search_term="Gift Card"):
        search_input_css = "input[placeholder='חיפוש באתר']"
        search_input = WebDriverWait(self.driver, 50).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, search_input_css)))
        search_input.send_keys(search_term)
        search_input.send_keys(Keys.ENTER)

    def select_gift_card(self, amount):
        gift_card_link_xpath = "//a[@data-test-id='venueCard.woltilgiftcards']"
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, gift_card_link_xpath))).click()

        button_xpath = f"//h3[@data-test-id='horizontal-item-card-header' and contains(text(), '{amount}')]/ancestor::button"
        WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, button_xpath))).click()

    def add_to_order(self):
        # XPath to find the span element by its data-localization-key and text content
        add_to_order_xpath = "//span[@data-localization-key='product-modal.submit.add' and contains(text(), 'להוסיף להזמנה')]"

        # Wait for the element to be clickable
        add_to_order_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, add_to_order_xpath)))

        # Scroll the element into view and click it
        self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_order_button)
        add_to_order_button.click()

    def view_order(self):
        view_order_css = ".sc-c1361b55-7.fQHDMh"
        view_order_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, view_order_css)))
        view_order_button.click()

    def proceed_to_payment(self):
        proceed_to_payment_css = ".sc-bd015adf-2.iCiubM"
        proceed_to_payment_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, proceed_to_payment_css)))
        proceed_to_payment_button.click()

    def run_automation(self):
        amount = wait_for_file('amount.txt')
        self.navigate_to_site()
        self.accept_cookies()
        self.click_profile_pic_or_login()
        self.search_for_gift_card("Gift Card")
        self.select_gift_card(amount)  # change it to get input through the UI somehow
        self.add_to_order()
        self.view_order()  # New step to view the order
        self.proceed_to_payment()  # New step to proceed to payment
        time.sleep(500)
        self.driver.quit()

    def navigate_to_site(self, url="https://wolt.com"):
        self.driver.get(url)

    def is_logged_in_to_google(self):
        # Navigate to a Google service where login is required, such as Gmail, to check for cookies
        self.driver.get("https://mail.google.com/")
        required_cookies = ['SSID', 'SID', 'HSID']  # Example list of cookies used by Google for sessions
        for cookie_name in required_cookies:
            try:
                # Attempt to get each required cookie
                cookie = self.driver.get_cookie(cookie_name)
                if not cookie:
                    return False  # If any of the cookies is missing, assume the user is not logged in
            except Exception as e:
                print(f"Error checking for cookie: {e}")
                return False
        return True  # All required cookies were found, assume user is logged in

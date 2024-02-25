from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from web_driver import WebDriver


class WoltShoppingActions:
    def __init__(self, web_driver: WebDriver):
        self.driver = web_driver.driver

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
        add_to_order_button = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, add_to_order_xpath)))
        #self.driver.execute_script("arguments[0].scrollIntoView(true);", add_to_order_button)
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

    def complete_shopping_flow(self, search_term, amount):
        self.search_for_gift_card(search_term)
        self.select_gift_card(amount)
        self.add_to_order()
        self.view_order()
        self.proceed_to_payment()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShopPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, password):
        self.driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def add_to_cart(self, item_id):
        self.driver.find_element(By.CSS_SELECTOR, f'#add-to-cart-{item_id}').click()

    def go_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

    def proceed_to_checkout(self):
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    def enter_checkout_info(self, first_name, last_name, postal_code):
        self.driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def get_total(self):
        return self.driver.find_element(By.CSS_SELECTOR, '[data-test="total-label"]').text
        
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver

    def set_delay(self, delay):
        input_field = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        input_field.clear()
        input_field.send_keys(delay)

    def click_button(self, button_text):
        button = self.driver.find_element(By.XPATH, f"//div[@class='keys']//span[text()='{button_text}']")
        button.click()

    def wait_for_spinner_to_disappear(self, timeout=45):
        WebDriverWait(self.driver, timeout).until_not(
            EC.visibility_of(self.driver.find_element(By.CSS_SELECTOR, '#spinner'))
        )

    def get_result(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text
        
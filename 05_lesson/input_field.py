from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver_service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=driver_service)

driver.get("http://the-internet.herokuapp.com/inputs")

sleep(2)

input_field = driver.find_element(By.CSS_SELECTOR, "input[type='number']")

input_field.send_keys("1000")

sleep(2)

input_field.clear()

input_field.send_keys("999")

sleep(2)

driver.quit()

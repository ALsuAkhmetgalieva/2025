from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver_service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=driver_service)

driver.get("http://the-internet.herokuapp.com/login")

sleep(2)

username_field = driver.find_element(By.ID, "username")
username_field.send_keys("tomsmith")

password_field = driver.find_element(By.ID, "password")
password_field.send_keys("SuperSecretPassword!")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

sleep(2)

driver.quit()

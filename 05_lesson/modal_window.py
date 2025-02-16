from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep

driver_service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=driver_service)

driver.get("http://the-internet.herokuapp.com/entry_ad")

sleep(5)

driver.find_element(By.CSS_SELECTOR, "div.modal-footer > p").click()

sleep(2)

driver.quit()

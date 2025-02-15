from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

driver = webdriver.Chrome()

driver.get("http://uitestingplayground.com/classattr")

driver.find_element(By.CSS_SELECTOR, "button.btn.class1.btn-primary.btn-test").click()

sleep(10)

driver.quit()

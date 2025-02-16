from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
for _ in range(5):
    driver.find_element(By.XPATH, "//button[text()='Add Element']").click()
sleep(2)

delete_buttons = driver.find_elements(By.XPATH, "//button[text()='Delete']")
print(len(delete_buttons))

driver.quit()

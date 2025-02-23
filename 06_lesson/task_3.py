from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager

driver_service = FirefoxService(GeckoDriverManager().install())
driver = webdriver.Firefox(service=driver_service)

driver.get(
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

element = WebDriverWait(driver, 40)
element.until(
 EC.text_to_be_present_in_element
 ((By.CSS_SELECTOR, "div:nth-child(4)"), "Done!")
    )

src = driver.find_element(
                          By.CSS_SELECTOR, "#image-container img:nth-child(3)"
                         ).get_attribute("src")

print(src)

driver.quit()

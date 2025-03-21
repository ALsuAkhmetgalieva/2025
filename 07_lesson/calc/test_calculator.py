import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


@pytest.mark.test_2
def test_calc():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
    driver.maximize_window()

    calculator_page = CalculatorPage(driver)

    calculator_page.set_delay('45')
    calculator_page.click_button('7')
    calculator_page.click_button('+')
    calculator_page.click_button('8')
    calculator_page.click_button('=')

    calculator_page.wait_for_spinner_to_disappear()

    assert '15' in calculator_page.get_result()

    driver.quit()

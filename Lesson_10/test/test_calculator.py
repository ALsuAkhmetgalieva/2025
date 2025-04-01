import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage

@pytest.mark.test_2
@allure.title("Ккалькулятор")
@allure.description("Ожидание времени загрузки и ввод значений")
@allure.feature("DELAY")
@allure.severity("blocker")
def test_calc():
    with allure.step("Открытие страницы"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html')
        driver.maximize_window()

        calculator_page = CalculatorPage(driver)

    with allure.step("Ввод времени задержки"):
        calculator_page.set_delay('45')
    with allure.step("Нажатие выбраныых кнопок"):
        calculator_page.click_button('7')
        calculator_page.click_button('+')
        calculator_page.click_button('8')
        calculator_page.click_button('=')

    with allure.step("Ожидание окончания лоадера"):
        calculator_page.wait_for_spinner_to_disappear()

    with allure.step("Проверка совпадения выведенного итогового значения"):
        assert '15' in calculator_page.get_result()

    driver.quit()
    
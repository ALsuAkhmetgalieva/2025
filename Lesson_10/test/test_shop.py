import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.shop_page import ShopPage

@pytest.mark.test_3
@allure.title("Итоговая сумма заказа")
@allure.description("Корректность подсчета стоимости добавленных товаров в корзине")
@allure.feature("SUM")
@allure.severity("critical")
def test_shop():
    with allure.step("Открытие страницы"):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get('https://www.saucedemo.com/')
        driver.maximize_window()

        shop_page = ShopPage(driver)

    with allure.step("Ввод логина и пароля"):
        shop_page.login('standard_user', 'secret_sauce')

    with allure.step("Добавление товаров в корзину"):
        shop_page.add_to_cart('sauce-labs-backpack')
        shop_page.add_to_cart('sauce-labs-bolt-t-shirt')
        shop_page.add_to_cart('sauce-labs-onesie')

    with allure.step("Переход в корзину"):
        shop_page.go_to_cart()
    with allure.step("Заполнение данных"):    
        shop_page.proceed_to_checkout()
        shop_page.enter_checkout_info('Имя', 'Фамилия', '123456')

    with allure.step("Получение итоговой суммы"):
        total = shop_page.get_total()

    driver.quit()
    assert '$58.29' in total

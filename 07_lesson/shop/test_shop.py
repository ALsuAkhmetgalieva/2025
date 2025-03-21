import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.shop_page import ShopPage


@pytest.mark.test_3
def test_shop():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://www.saucedemo.com/')
    driver.maximize_window()

    shop_page = ShopPage(driver)

    shop_page.login('standard_user', 'secret_sauce')

    shop_page.add_to_cart('sauce-labs-backpack')
    shop_page.add_to_cart('sauce-labs-bolt-t-shirt')
    shop_page.add_to_cart('sauce-labs-onesie')

    shop_page.go_to_cart()
    shop_page.proceed_to_checkout()
    shop_page.enter_checkout_info('Имя', 'Фамилия', '123456')

    total = shop_page.get_total()

    driver.quit()
    assert '$58.29' in total
    
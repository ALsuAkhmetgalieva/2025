import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.main_page import AviaPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('')
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.test
@allure.title("Ввод латиницы")
@allure.description("Поиск авиабилетов по предустановленным фильтрам в одну сторону.")
@allure.severity("critical")
def test_avia_1(driver): 
    with allure.step("Открытие страницы"): 
     main_page = AviaPage(driver)
    with allure.step("Заполнение формы"):
     main_page.enter_form_destination('Moskow')
    with allure.step("Выбор даты"):
     main_page.date_avia()
    with allure.step("Клик на кнопку поиска"):
     main_page.get_result_avia()
    with allure.step("Проверка совпадения выведенного текста"):
     assert 'Москва' in main_page.result_avia()


@allure.title("Ввод кириллицы")
@allure.description("Поиск авиабилетов по предустановленным фильтрам в одну сторону.")
@allure.severity("critical")
def test_avia_2(driver):  # Кириллица
    with allure.step("Открытие страницы"): 
     main_page = AviaPage(driver)
    with allure.step("Заполнение формы"):
     main_page.enter_form_destination('Казань')
    with allure.step("Выбор даты"):
     main_page.date_avia()
    with allure.step("Клик на кнопку поиска"):
     main_page.get_result_avia()
    with allure.step("Проверка совпадения выведенного текста"):
     assert 'Казань' in main_page.result_avia()


@allure.title("Ввод текста с пробелом")
@allure.description("Поиск авиабилетов по предустановленным фильтрам в одну сторону.")
@allure.severity("critical")
def test_avia_3(driver):  # Текст с пробелом
    with allure.step("Открытие страницы"): 
     main_page = AviaPage(driver)
    with allure.step("Заполнение формы"):
     main_page.enter_form_destination('Нижний Новгород')
    with allure.step("Выбор даты"):
     main_page.date_avia()
    with allure.step("Клик на кнопку поиска"):
     main_page.get_result_avia()
    with allure.step("Проверка совпадения выведенного текста"):
     assert 'Нижний Новгород' in main_page.result_avia()

@allure.title("Ввод кириллицы")
@allure.description("Поиск отеля по предустановленным фильтрам.")
@allure.severity("critical")
def test_hotel_1(driver):
    with allure.step("Открытие страницы"): 
     main_page = AviaPage(driver)
    with allure.step("Клик на кнопку отели"):
     main_page.hotel()
    with allure.step("Ввод названия города в поле поиска"):
     main_page.search_hotel("Москва")
    with allure.step("Выбор даты заезда"):
     main_page.start_date()
    with allure.step("Выбор даты выезда"):
     main_page.end_date()
    with allure.step("Клик на поле поиска"):
     main_page.get_result_otel()
    with allure.step("Проверка совпадения выведенного текста"):
     assert 'Нашли' in main_page.result_otel()


@allure.title("Ввод текста с тире")
@allure.description("Поиск отеля по предустановленным фильтрам.")
@allure.severity("critical")
def test_hotel_2(driver):
    with allure.step("Открытие страницы"): 
     main_page = AviaPage(driver)
    with allure.step("Клик на кнопку отели"):
     main_page.hotel()
    with allure.step("Ввод названия города в поле поиска"):
     main_page.search_hotel("Нижний Новгород")
    with allure.step("Выбор даты заезда"):
     main_page.start_date()
    with allure.step("Выбор даты выезда"):
     main_page.end_date()
    with allure.step("Клик на поле поиска"):
     main_page.get_result_otel()
    with allure.step("Проверка совпадения выведенного текста"):
      assert 'Нашли' in main_page.result_otel()

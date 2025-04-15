import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from new_page import AviaPage
from new_page import HotelPage


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get('https://www.aviasales.ru/?params=CSY1')
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.test
@allure.title("Ввод латиницы")
@allure.description("Поиск авиабилетов по предустановленным фильтрам в одну сторону.")
@allure.severity("critical")
def test_avia_1(driver): 
    with allure.step("Открытие страницы"): 
     avia_page = AviaPage(driver)
    with allure.step("Заполнение формы"):
     avia_page.enter_form_destination("Moskow")
    with allure.step("Клик на поле Дата"):
     avia_page.select_date_field()
    with allure.step("Выбор даты вылета"):
     avia_page.select_date("28.04.2025")  # Передайте нужную дату в формате "дд.мм.гггг"
    with allure.step("Клик на кнопку поиска"):
     avia_page.get_result_avia()
    with allure.step("Проверка совпадения выведенного текста"):
     result_text = avia_page.result_avia()
     print(result_text)


@allure.title("Ввод кириллицы")
@allure.description("Поиск авиабилетов по предустановленным фильтрам в одну сторону.")
@allure.severity("critical")
def test_avia_2(driver):  # Кириллица 
    with allure.step("Открытие страницы"): 
     avia_page = AviaPage(driver)
    with allure.step("Заполнение формы"):
     avia_page.enter_form_destination("Казань")
    with allure.step("Клик на поле Дата"):
     avia_page.select_date_field()
    with allure.step("Выбор даты вылета"):
     avia_page.select_date("28.04.2025")  # Передайте нужную дату в формате "дд.мм.гггг"
    with allure.step("Клик на кнопку поиска"):
     avia_page.get_result_avia()
    with allure.step("Проверка совпадения выведенного текста"):
     result_text = avia_page.result_avia()
     print(result_text)


@allure.title("Ввод текста с пробелом")
@allure.description("Поиск авиабилетов по предустановленным фильтрам в одну сторону.")
@allure.severity("critical")
def test_avia_3(driver): #Текст с пробелом
    with allure.step("Открытие страницы"): 
     avia_page = AviaPage(driver)
    with allure.step("Заполнение формы"):
     avia_page.enter_form_destination("Нижний Новгород")
    with allure.step("Клик на поле Дата"):
     avia_page.select_date_field()
    with allure.step("Выбор даты вылета"):
     avia_page.select_date("28.04.2025")  # Передайте нужную дату в формате "дд.мм.гггг"
    with allure.step("Клик на кнопку поиска"):
     avia_page.get_result_avia()
    with allure.step("Проверка совпадения выведенного текста"):
     result_text = avia_page.result_avia()
     print(result_text)


@allure.title("Ввод латиницы")
@allure.description("Поиск отеля по предустановленным фильтрам.")
@allure.severity("critical")
def test_hotel_1(driver):
    with allure.step("Открытие страницы"): 
     hotel_page = HotelPage(driver)
    with allure.step("Клик на кнопку отели"):
     hotel_page.hotel()
    with allure.step("Ввод названия города в поле поиска"):
     hotel_page.search_hotel("Hilton")
    with allure.step("Клик на поле дата"): 
     hotel_page.date_otel() 
    with allure.step("Выбор даты заезда"):
     hotel_page.start_date()
    with allure.step("Выбор даты выезда"):
     hotel_page.end_date()
    with allure.step("Клик на поле поиска"):
     hotel_page.get_result_otel()
    with allure.step("Проверка совпадения выведенного текста"):
     result_text = hotel_page.result_otel()
     print(result_text)

@allure.title("Ввод текста с тире")
@allure.description("Поиск отеля по предустановленным фильтрам.")
@allure.severity("critical")
def test_hotel_2(driver):
    with allure.step("Открытие страницы"): 
     hotel_page = HotelPage(driver)
    with allure.step("Клик на кнопку отели"):
     hotel_page.hotel()
    with allure.step("Ввод названия города в поле поиска"):
     hotel_page.search_hotel("Санкт-Петербург")
    with allure.step("Клик на поле дата"): 
     hotel_page.date_otel() 
    with allure.step("Выбор даты заезда"):
     hotel_page.start_date()
    with allure.step("Выбор даты выезда"):
     hotel_page.end_date()
    with allure.step("Клик на поле поиска"):
     hotel_page.get_result_otel()
    with allure.step("Проверка совпадения выведенного текста"):
     result_text = hotel_page.result_otel()
     print(result_text)

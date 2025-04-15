from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AviaPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_form_destination(self, form_destination):
        """Вводит пункт назначения в форму поиска авиабилетов."""
        destination_input = self.wait.until(
            EC.visibility_of_element_located((By.ID, "avia_form_destination-input"))
        )
        destination_input.send_keys(form_destination)

    def select_date_field(self):
        """Выбирает поле дата для авиаперелета."""
        date_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test-id='start-date-field']"))
        )
        date_button.click()

    def select_date(self, date_value):
        """Выбирает дату для авиаперелета."""
        date_selector = f'div[data-test-id="date-{date_value}"]'
        date_element = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, date_selector)))
        date_element.click()

    def get_result_avia(self):
        """Получает результат поиска авиабилетов."""
        submit_button = self.wait.until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test-id='form-submit']"))
        )
        submit_button.click()

    def result_avia(self):
        """Возвращает текст результата поиска билетов."""
        try:
            # Явное ожидание элемента
            result_element = self.wait.until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, ".s__YzBVrv0Ig2EqTTmSTi0k"))
            )
            return result_element.text
        except Exception as e:
            print(f"Ошибка при получении текста результата поиска билетов: {e}")
            return None
    
class HotelPage:
    def __init__(self, driver):
        self.driver = driver

    def hotel(self):
        """Переходит на страницу поиска отелей."""
        hotel_link = self.driver.find_element(By.XPATH, "//a[@class='s__copbTnCU01Z8RvQlTAy3' and .//div[@data-test-id='text' and text()='Отели']]")
        hotel_link.click()

    def search_hotel(self, enter_form_otel):
        """Вводит название отеля в форму поиска."""
        hotel_input = self.driver.find_element(By.ID, "hotel_autocomplete-input")
        hotel_input.send_keys(enter_form_otel)

    def date_otel(self):
        """Открывает выбор даты заезда."""
        date_field = self.driver.find_element(By.XPATH, "//div[@data-test-id='start-date-value' and text()='Дата заезда']")
        date_field.click()

    def start_date(self):
        """Выбирает начальную дату бронирования отеля."""
        wait = WebDriverWait(self.driver, 15)
        start_date_element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Wed Apr 23 2025"]')))
        start_date_element.click()

    def end_date(self):
        """Выбирает конечную дату бронирования отеля."""
        end_date_element = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Mon Apr 28 2025"]')
        end_date_element.click()

    def get_result_otel(self):
        """Клик на кнопку поиска отелей."""
        search_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test-id='form-submit']"))
        )
        search_button.click()

    def result_otel(self):
        """Возвращает текст результата поиска отелей."""
        try:
            # Явное ожидание элемента
            result_element = WebDriverWait(self.driver, 60).until(
                EC.visibility_of_element_located(
                    (By.CSS_SELECTOR, ".s__sKkvfJDIxRicM2rUUvFJ.s__z5Bj55bhHL3Q8aoLNCjw")
                )
            )
            return result_element.text
        except Exception as e:
            print(f"Ошибка при получении текста результата поиска отелей: {e}")
            return None    
            
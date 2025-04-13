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
        self.driver.find_element(By.ID, "avia_form_destination-input").send_keys(form_destination)

    def date_avia(self):
        """Выбирает поле дата для авиаперелета."""
        self.driver.find_element(By.CSS_SELECTOR, ".s__Ri8DaLigC3WqN5MS5LyK").click()
        """Выбирает дату для авиаперелета."""
    def date_avia_1(self): 
        wait = WebDriverWait(self.driver, 15)   
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Wed Apr 23 2025"]')))
        element.click()
    def date_avia_2(self):     
        self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Mon Apr 28 2025"]').click()

    def get_result_avia(self):
        """Получает результат поиска авиабилетов."""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test-id='form-submit']"))
        )
        element.click()  

    def result_avia(self):
        """Возвращает текст результата поиска билетов."""
        try:
        # Явное ожидание элемента
         result_element = WebDriverWait(self.driver, 60).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR, ".s__YzBVrv0Ig2EqTTmSTi0k")
            )
        )
         return result_element.text
        except Exception as e:
         print(f"Ошибка при получении текста результата поиска билетов: {e}")
         return None

    def hotel(self):
        """Переходит на страницу поиска отелей."""
        self.driver.find_element(By.XPATH, "//a[@class='s__copbTnCU01Z8RvQlTAy3' and .//div[@data-test-id='text' and text()='Отели']]").click()

    def search_hotel(self, enter_form_otel):
        """Вводит название отеля в форму поиска."""
        self.driver.find_element(By.ID, "hotel_autocomplete-input").send_keys(enter_form_otel)
    def date_otel(self):
        self.driver.find_element(By.XPATH, "//div[@data-test-id='start-date-value' and text()='Дата заезда']").click()
        
    def start_date(self):
        """Выбирает начальную дату бронирования отеля."""
        wait = WebDriverWait(self.driver, 15)   
        element = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[aria-label="Wed Apr 23 2025"]')))
        element.click()

    def end_date(self):
        """Выбирает конечную дату бронирования отеля."""
        self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Mon Apr 28 2025"]').click()

    def get_result_otel(self):
        """Клик на кнопку поиска поиска отелей."""
        element = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//button[@data-test-id='form-submit']"))
        )
        element.click()
        
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
         
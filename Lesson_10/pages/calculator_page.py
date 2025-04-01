from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CalculatorPage:
    def __init__(self, driver):
        """
        Инициализация страницы калькулятора.

        :param driver: Экземпляр веб-драйвера (тип: webdriver).
        """
        self.driver = driver

    def set_delay(self, delay: int):
        """
        Ввести задержку в поле ввода.

        :param delay: Задержка, которую нужно установить.
        :return: None
        """
        input_field = self.driver.find_element(By.CSS_SELECTOR, '#delay')
        input_field.clear()
        input_field.send_keys(delay)

    def click_button(self, button_text: str):
        """
        Нажимает на кнопку калькулятора по тексту кнопки.

        :param button_text: Текст кнопки, на которую нужно нажать .
        :return: None
        """
        button = self.driver.find_element(By.XPATH, f"//div[@class='keys']//span[text()='{button_text}']")
        button.click()

    def wait_for_spinner_to_disappear(self, timeout=45):
        """
        Ожидает исчезновения спиннера загрузки.

        :param timeout: Максимальное время ожидания в секундах .
        :return: None
        """
        WebDriverWait(self.driver, timeout).until_not(
            EC.visibility_of(self.driver.find_element(By.CSS_SELECTOR, '#spinner'))
        )

    def get_result(self):
        """
        Получает результат вычисления из экрана калькулятора.

        :return: Результат как строка (тип: int).
        """
        return self.driver.find_element(By.CSS_SELECTOR, '.screen').text
    
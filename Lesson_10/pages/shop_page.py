from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ShopPage:
    def __init__(self, driver):
        """
        Инициализация страницы.

        :param driver: Экземпляр веб-драйвера.
        """
        self.driver = driver

    def login(self, username: str, password: str):
        """
        Выполняет вход на страницу с использованием имени пользователя и пароля.

        :param username: Имя пользователя для входа.
        :param password: Пароль для входа.
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, '#user-name').send_keys(username)
        self.driver.find_element(By.CSS_SELECTOR, '#password').send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, '#login-button').click()

    def add_to_cart(self, item_id: str):
        """
        Добавляет товар в корзину по его идентификатору.

        :param item_id: Идентификатор товара для добавления в корзину.
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, f'#add-to-cart-{item_id}').click()

    def go_to_cart(self):
        """
        Переходит на страницу корзины.

        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, '.shopping_cart_link').click()

    def proceed_to_checkout(self):
        """
        Переходит к оформлению заказа.

        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, '#checkout').click()

    def enter_checkout_info(self, first_name: str, last_name: str, postal_code: int):
        """
        Ввод информации для оформления заказа.

        :param first_name: Имя покупателя.
        :param last_name: Фамилия покупателя.
        :param postal_code: Почтовый код покупателя.
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, '#first-name').send_keys(first_name)
        self.driver.find_element(By.CSS_SELECTOR, '#last-name').send_keys(last_name)
        self.driver.find_element(By.CSS_SELECTOR, '#postal-code').send_keys(postal_code)
        self.driver.find_element(By.CSS_SELECTOR, '#continue').click()

    def get_total(self) -> str:
        """
       Получает итоговую сумму из корзины.

       :return: Итоговая сумма как строка.
       """
        return self.driver.find_element(By.CSS_SELECTOR, '[data-test="total-label"]').text
    
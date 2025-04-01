from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        """
        Инициализация страницы формы.

        :param driver: Экземпляр веб-драйвера (тип: webdriver).
        """
        self.driver = driver

    def enter_first_name(self, first_name: str):
        """
        Вводит имя в поле "Имя".

        :param first_name: Имя для ввода .
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(first_name)

    def enter_last_name(self, last_name: str):
        """
        Вводит фамилию в поле "Фамилия".

        :param last_name: Фамилия для ввода .
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)

    def enter_address(self, address: str):
        """
        Вводит адрес в поле "Адрес".

        :param address: Адрес для ввода .
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(address)

    def enter_email(self, email: str):
        """
        Вводит электронную почту в поле "Электронная почта".

        :param email: Электронная почта для ввода .
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(email)

    def enter_phone(self, phone: str):
        """
        Вводит номер телефона в поле "Телефон".

        :param phone: Номер телефона для ввода .
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)

    def enter_city(self, city: str):
        """
        Вводит город в поле "Город".

        :param city: Город для ввода .
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)

    def enter_country(self, country: str):
        """
        Вводит страну в поле "Страна".

        :param country: Страна для ввода .
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)

    def enter_job_position(self, job_position: str):
        """
        Вводит должность в поле "Должность".

        :param job_position: Должность для ввода .
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job_position)

    def enter_company(self, company: str):
        """
        Вводит название компании в поле "Компания".

        :param company: Название компании для ввода .
        :return: None
        """
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)

    def submit_form(self):
        """
         Нажатие кнопки

         :return: None
         """
        self.driver.find_element(By.CSS_SELECTOR, '.btn-outline-primary').click()

    def get_field_class(self, field_id: str):
        """
         Получает класс указанного поля по его ID.

         :param field_id: ID поля для получения класса.
         :return: Класс поля как строка .
         """
        return self.driver.find_element(By.CSS_SELECTOR, f'#{field_id}').get_attribute('class')

    def get_zip_code_class(self):
        """
        Получает класс поля "Почтовый индекс".

        :return: Класс поля почтового индекса как строка (тип: str).
        """
        return self.get_field_class('zip-code')
    
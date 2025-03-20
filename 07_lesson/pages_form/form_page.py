from selenium.webdriver.common.by import By

class FormPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_first_name(self, first_name):
        self.driver.find_element(By.CSS_SELECTOR, '[name="first-name"]').send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.CSS_SELECTOR, '[name="last-name"]').send_keys(last_name)

    def enter_address(self, address):
        self.driver.find_element(By.CSS_SELECTOR, '[name="address"]').send_keys(address)

    def enter_email(self, email):
        self.driver.find_element(By.CSS_SELECTOR, '[name="e-mail"]').send_keys(email)

    def enter_phone(self, phone):
        self.driver.find_element(By.CSS_SELECTOR, '[name="phone"]').send_keys(phone)

    def enter_city(self, city):
        self.driver.find_element(By.CSS_SELECTOR, '[name="city"]').send_keys(city)

    def enter_country(self, country):
        self.driver.find_element(By.CSS_SELECTOR, '[name="country"]').send_keys(country)

    def enter_job_position(self, job_position):
        self.driver.find_element(By.CSS_SELECTOR, '[name="job-position"]').send_keys(job_position)

    def enter_company(self, company):
        self.driver.find_element(By.CSS_SELECTOR, '[name="company"]').send_keys(company)

    def submit_form(self):
        self.driver.find_element(By.CSS_SELECTOR, '.btn-outline-primary').click()

    def get_field_class(self, field_id):
        return self.driver.find_element(By.CSS_SELECTOR, f'#{field_id}').get_attribute('class')

    def get_zip_code_class(self):
        return self.get_field_class('zip-code')
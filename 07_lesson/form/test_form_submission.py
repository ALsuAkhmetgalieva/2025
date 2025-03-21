import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from pages.form_page import FormPage


@pytest.mark.test_1
def test_form():
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(4)

    driver.get('https://bonigarcia.dev/selenium-webdriver-java/data-types.html')

    form_page = FormPage(driver)

    form_page.enter_first_name('Иван')
    form_page.enter_last_name('Петров')
    form_page.enter_address('Ленина, 55-3')
    form_page.enter_email('test@skypro.com')
    form_page.enter_phone('+7985899998787')
    form_page.enter_city('Москва')
    form_page.enter_country('Россия')
    form_page.enter_job_position('QA')
    form_page.enter_company('SkyPro')

    form_page.submit_form()

    # Проверка классов полей
    fields = ['first-name', 'last-name', 'address', 'city', 'country', 'e-mail', 'phone', 'job-position', 'company']
    for field in fields:
        assert form_page.get_field_class(field) == 'alert py-2 alert-success'

    assert form_page.get_zip_code_class() == 'alert py-2 alert-danger'

    driver.quit()
    
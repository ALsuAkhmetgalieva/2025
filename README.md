# Дипломный проект "Авиасейлс. Автоматизирование тестирования"
## Цель проекта
Автоматизация рутинных тестов и проведение минимального смоук тестирования для основных функций сайта.
## Тестовые данные 
URL "https://www.aviasales.ru/?params=CSY1"\
BASE URL : https://auth.avs.io/\
Token для выполнения автоматизированных Api тестов \eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJzdWIiOiJiMzViN2MwMi1jYjBmLTQ1YTEtYTAxNy01MjM4MDllMjJkNWUiLCJhY3RpdmVfZW1haWwiOiJha2htZXRnYWxpZXZhX2Fsc3VAbWFpbC5ydSJ9.lRE_8cg8FCJTcQcltgCCSiS_wQruxdoomdvYloW_v7ta1lVTkD9dmKXLrQ6jUouwoviUKBkL2XiQX4m3lXOSobCZVATV4XozvQneu24nJghLec6klnpBCSWygOexjesC9GwYMF2HpTZYc1WNhrO9jInmr2fBmS2VInGjra4t6IPJFDG00d0xGP7_9WFbDChlFzD80Fmg0RcEVmAkKaEEWexn2YzoA5_cWwu61ApS_WfuNPGTPJJCmmR-TCOGmVcS7KCSNELuDil8AxWxFu1VJ2lyoibizQXa89U97CNlX0rs0oFuHOsQrLTPBxkV3ZnQC9M8C3VYgfVugLV6rPdevw
## Проведение тестирования
Импорт библиотек: Импортируем необходимые модули из Selenium.
Настройка драйвера: Создаем экземпляр веб-драйвера.
Открытие сайта: Переходим на сайт Aviasales.
Поиск билетов\ отделей: Находим поле ввода для города и вводим данные. 
Выбор дат: Указываем даты
Нажатие кнопки поиска: Находим кнопку поиска и нажимаем ее.
Проверка результатов: Проверяем наличие результатов поиска.
Закрытие браузера: Закрываем браузер после завершения теста. 
Файл test_ui автоматизированных ручных тестов из функционального чек-листа
Файл test_api для автоматизированныз api- тестов
# Отчетность в Allure  
## Запуск тестов для формирования отчета  
Для запуска тестов необходимо:   
1. Перейти в необходимую директорию  
2. Подключите Allure:
**pip install allure-pytest**
3. Запустите тесты и укажите путь к каталогу результатов тестирования:
**pytest --alluredir allure-result**
4.  Конвертируйте результаты теста в отчет:
**allure serve allure-result**  
## Просмотр результатов тестирования  
1. Overview — раздел с общей информацией: сколько всего тестов запустили, процент успешных тестов, доля успешных и неуспешных тестов.
2. В разделе Suits — список тестов и конкретная информация о каждом из них.
3. На вкладке Behaviors результаты тестирования распределены по фичам. Указаны статусы и время прохождения тестирования
4. На вкладке Graph результаты тестирования описаны в форме графиков и диаграмм. Отображена информация по распределению тестов по критичности.   

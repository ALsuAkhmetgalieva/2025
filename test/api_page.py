import requests
import pytest

class ProjectAPI:
    def __init__(self, base_url, token):
        """
        Инициализация класса ProjectAPI.
        
        :param base_url: Базовый URL сайта.
        :param token: Токен для авторизации.
        """
        self.BASE_URL = base_url
        self.TOKEN = token  

    def get_headers(self):
        """
        Возвращает заголовки для авторизационного запроса.
        
        :return: Словарь с заголовками.
        """
        return {
            "Authorization": f"Bearer {self.TOKEN}",
            "Content-Type": "application/json"
        }

    def post_avia(self, data):
        """
        Отправляет POST-запрос для поиска авиабилетов.
        
        :param data: Данные для запроса в формате JSON.
        :return: Ответ от сервера.
        """
        try:
            response = requests.post(
                f"{self.BASE_URL}api/v2/user/searches/",
                json=data,
                headers=self.get_headers()
            )
            response.raise_for_status()  # Проверка на ошибки HTTP
            return response.json()  # Возвращаем JSON-ответ
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")  # Логирование ошибки
            return None
        except Exception as err:
            print(f"An error occurred: {err}")  # Логирование других ошибок
            return None
            
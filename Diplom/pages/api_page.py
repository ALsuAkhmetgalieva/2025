import pytest
import requests
"""
        Создание класса для авторизации и открытия страницы
        :param BASE URL: сайт).
        :param TOKEN: токен для авторизации
        """
class ProjectAPI:
    BASE_URL = ""
    TOKEN = ""  

    def get_headers(self):
        
        """
        Ввод авторизационных данных для запроса
        Параметр возвращаемого ответа
        
        """
        return {
            "Authorization": f"Bearer {self.TOKEN}",
            "Content-Type": "application/json"
        }
    def post_avia(self, data):
        
        """
        Ввод данных для запроса
        """
        response = requests.post(
            f"{self.BASE_URL}api/v2/user/searches/",
            json=data,
            headers=self.get_headers()
        )
        return response
        
import pytest
import requests


BASE_URL = "https://ru.yougile.com"
TOKEN = ""  

def put_project(data):
    headers = {
        "Authorization": f"Bearer {TOKEN}",  
        "Content-Type": "application/json"  
    }
    response = requests.put(f"{BASE_URL}/api-v2/projects/f2da38aa-77e0-4ae8-bf65-81e8697f547b",
                             json=data, headers=headers)
    return response

def test_put_project_positive():
    # Позитивный тест: Изменение названия проекта
    data = {
         "deleted": False,
         "title": "Тестовый изменен2",
         "users": {
        "1e2ba932-5bd5-46b7-9e9f-c2f72e2a015d": "admin"
        }
}
    response = put_project(data)
    assert response.status_code == 200  

def test_put_project_negative():
    # Негативный тест: Изменение названия в проекте с несуществующим пользователем
    data = {
        "deleted": False,
         "title": "Тестовый изменен2",
         "users": {
        "1e2ba932-5bd5-46b7-9e9f-c2f72e2a01": "admin"
        }
    }
    response = put_project(data)
    assert response.status_code == 400 

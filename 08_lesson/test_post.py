import pytest
import requests


BASE_URL = "https://ru.yougile.com"
TOKEN = ""  

def create_project(data):
    headers = {
        "Authorization": f"Bearer {TOKEN}",  
        "Content-Type": "application/json"  
    }
    response = requests.post(f"{BASE_URL}/api-v2/projects",
                              json=data, headers=headers)
    return response

def test_create_project_positive():
    # Позитивный тест: создание проекта с корректными данными
    data = {
          "title": "Тестовый2",
          "users": {
                  "1e2ba932-5bd5-46b7-9e9f-c2f72e2a015d": "admin"
                   }
           }
    response = create_project(data)
    assert response.status_code == 201  

def test_create_project_negative():
    # Негативный тест: создание проекта с некорректными данными
    data = {
        "title": "",
  "users": {
    "1e2ba932-5bd5-46b7-9e9f-c2f72e2a015d": "admin"
        }
    }
    response = create_project(data)
    assert response.status_code == 400  

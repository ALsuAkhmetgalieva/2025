import pytest
import requests


BASE_URL = "https://ru.yougile.com"
TOKEN = ""  
ID = ""
ID_F = "76859484748490404"

def get_project():
    headers = {
        "Authorization": f"Bearer {TOKEN}",  
        "Content-Type": "application/json"  
    }
    response = requests.get(f"{BASE_URL}/api-v2/projects/{ID}",
                              headers=headers)
    return response

def get_project_F():
    headers = {
        "Authorization": f"Bearer {TOKEN}",  
        "Content-Type": "application/json"  
    }
    response = requests.get(f"{BASE_URL}/api-v2/projects/{ID_F}",
                              headers=headers)
    return response

def test_get_project_positive():
    # Позитивный тест: Получение информации с корректным id
    
    response = get_project()
    assert response.status_code == 200  

def test_get_project_negative():
    # Негативный тест: с некорректным id
    
    response = get_project_F()
    assert response.status_code == 404 

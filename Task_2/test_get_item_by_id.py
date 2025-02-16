import pytest
import requests

BASE_URL = "https://qa-internship.avito.com/api/1/item"
HEADERS = {"Accept": "application/json"}

# Позитивный тест: Успешное получение данных объявления
def test_get_item_by_id_success():
    item_id = "0cd4183f-a699-4486-83f8-b513dfde477a"
    response = requests.get(f"{BASE_URL}/{item_id}", headers=HEADERS)
    
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    data = response.json()
    assert isinstance(data, list)
    assert "id" in data[0]
    assert "sellerId" in data[0]
    assert "name" in data[0]
    assert "price" in data[0]
    assert "statistics" in data[0]
    assert "createdAt" in data[0]

# Негативный тест: Объявление не найдено
def test_get_item_by_id_not_found():
    item_id = "12345678-1234-1234-1234-123456789012"
    response = requests.get(f"{BASE_URL}/{item_id}", headers=HEADERS)
    
    assert response.status_code == 404
    assert response.headers["Content-Type"] == "application/json"
    data = response.json()
    assert "result" in data
    assert "message" in data["result"]

'''
# Негативный тест: Ошибка сервера
# тест будет возращать ошибку т.к. сервер работает
def test_get_item_by_id_server_error():
    item_id = "0cd4183f-a699-4486-83f8-b513dfde477a"
    response = requests.get(f"{BASE_URL}/{item_id}", headers=HEADERS)
    print (response)
    assert response.status_code == 500
    assert response.headers["Content-Type"] == "application/json"
    data = response.json()
    assert "result" in data
    assert "message" in data["result"]
'''

# Негативный тест: Некорректный тип идентификатора (не UUID)
def test_get_item_by_id_invalid_type():
    item_id = "123"  # Некорректный тип (не UUID)
    response = requests.get(f"{BASE_URL}/{item_id}", headers=HEADERS)
    
    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    data = response.json()
    assert "result" in data
    assert "message" in data["result"]
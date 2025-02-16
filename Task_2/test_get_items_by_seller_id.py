import pytest
import requests

BASE_URL = "https://qa-internship.avito.com/api/1"
HEADERS = {"Accept": "application/json"}

# Позитивный тест: Успешное получение списка объявлений продавца
def test_get_items_by_seller_id_success():
    seller_id = "1234345231"
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers=HEADERS)
    
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

# Негативный тест: Некорректный тип идентификатора продавца (строка вместо числа)
def test_get_items_by_seller_id_invalid_type():
    seller_id = "invalid_seller_id"  # Некорректный тип (строка вместо числа)
    response = requests.get(f"{BASE_URL}/{seller_id}/item", headers=HEADERS)
    
    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    data = response.json()
    assert "result" in data
    assert "message" in data["result"]
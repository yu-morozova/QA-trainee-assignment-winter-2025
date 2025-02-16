import pytest
import requests

BASE_URL = "https://qa-internship.avito.com/api/1/item"
HEADERS = {"Content-Type": "application/json", "Accept": "application/json"}

# Позитивный тест: Успешное создание объявления
def test_create_item_success():
    payload = {
        "sellerID": 1234345231,
        "name": "dsds",
        "price": 1,
        "statistics": {
            "contacts": 3,
            "likes": 123,
            "viewCount": 12
        }
    }
    response = requests.post(
        BASE_URL,
        json=payload,
        headers=HEADERS
    )
    
    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json"
    data = response.json()
    assert "status" in data

# Негативный тест: Некорректные данные в запросе
def test_create_item_bad_request():
    payload = {
        "sellerID": "invalid_id",
        "name": "",
        "price": -1
    }
    response = requests.post(
        BASE_URL,
        json=payload,
        headers=HEADERS
    )
    
    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    data = response.json()
    assert "result" in data
    assert "messages" in data["result"]
    assert "message" in data["result"]

# Негативный тест: Некорректный тип для sellerID (строка вместо числа)
def test_create_item_invalid_seller_id_type():
    payload = {
        "sellerID": "invalid_id",  # Некорректный тип (строка вместо числа)
        "name": "Test Item",
        "price": 100
    }
    response = requests.post(
        BASE_URL,
        json=payload,
        headers=HEADERS
    )
    
    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    data = response.json()
    assert "result" in data
    assert "message" in data["result"]

# Негативный тест: Некорректный тип для price (строка вместо числа)
def test_create_item_invalid_price_type():
    payload = {
        "sellerID": 1234345231,
        "name": "Test Item",
        "price": "invalid_price"  # Некорректный тип (строка вместо числа)
    }
    response = requests.post(
        BASE_URL,
        json=payload,
        headers=HEADERS
    )
    
    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    data = response.json()
    assert "result" in data
    assert "message" in data["result"]

# Негативный тест: Некорректный тип для price (Отрицательное число)
def test_create_item_negative_price_type():
    payload = {
        "sellerID": 1234345231,
        "name": "Test Item",
        "price": -256  # Некорректный тип (Отрицательное число)
    }
    response = requests.post(
        BASE_URL,
        json=payload,
        headers=HEADERS
    )
    
    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    data = response.json()
    assert "result" in data
    assert "message" in data["result"]


# Негативный тест: Пустое обязательное поле (name)
def test_create_item_empty_name():
    payload = {
        "sellerID": 1234345231,
        "name": "",  # Пустое обязательное поле
        "price": 100
    }
    response = requests.post(
        BASE_URL,
        json=payload,
        headers=HEADERS
    )
    
    assert response.status_code == 400
    assert response.headers["Content-Type"] == "application/json"
    data = response.json()
    assert "result" in data
    assert "message" in data["result"]
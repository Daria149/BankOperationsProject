import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions, transactions


@pytest.fixture
def test_filter_by_currency():
    """Функция для тестирования функцию списка операций по валюте"""
    assert next(filter_by_currency(transactions)) == {
          "id": 939719570,
          "state": "EXECUTED",
          "date": "2018-06-30T02:08:58.425572",
          "operationAmount": {
              "amount": "9824.07",
              "currency": {
                  "name": "USD",
                  "code": "USD"
              }
          },
          "description": "Перевод организации",
          "from": "Счет 75106830613657916952",
          "to": "Счет 11776614605963066702"
      }
    assert next(filter_by_currency(transactions)) == {
              "id": 142264268,
              "state": "EXECUTED",
              "date": "2019-04-04T23:20:05.206878",
              "operationAmount": {
                  "amount": "79114.93",
                  "currency": {
                      "name": "USD",
                      "code": "USD"
                  }
              },
              "description": "Перевод со счета на счет",
              "from": "Счет 19708645243227258542",
              "to": "Счет 75651667383060284188"
       }
    assert next(filter_by_currency(transactions)) == {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    }


@pytest.fixture
def test_2_filter_by_currency():
    """Функция для тестирования выдачу списка данных по валюте с отствующимим данными"""
    assert next(filter_by_currency([])) == "Нет данных"


@pytest.fixture
def test_3_filter_by_currency():
    """Функция для тестирования выдачу списка данных по валюте с отствующимим данными"""
    new_data = [{
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    }]
    assert next(filter_by_currency([new_data])) == []


@pytest.fixture
def test_transaction_descriptions():
    """Функция для тестирования функции, формирующей список описания операций"""
    assert next(transaction_descriptions(transactions)) == "Перевод организации"
    assert next(transaction_descriptions(transactions)) == "Перевод со счета на счет"
    assert next(transaction_descriptions(transactions)) == "Перевод со счета на счет"
    assert next(transaction_descriptions(transactions)) == "Перевод с карты на карту"
    assert next(transaction_descriptions(transactions)) == "Перевод организации"


@pytest.fixture
def test_2_transaction_descriptions():
    """Функция для тестирования функции, формирующей список описания операций, с отствующимим данными"""
    assert next(transaction_descriptions([])) == "Нет данных"


def test_card_number_generator():
    """Функция для тестирования генератора, формирующего номера банковских карт в определенном формате"""
    card_number = card_number_generator(1, 9999)
    assert next(card_number) == "0000 0000 0000 0001"
    assert next(card_number) == "0000 0000 0000 0002"
    assert next(card_number) == "0000 0000 0000 0003"
    assert next(card_number) == "0000 0000 0000 0004"
    assert next(card_number) == "0000 0000 0000 0005"
    assert next(card_number) == "0000 0000 0000 0006"
    assert next(card_number) == "0000 0000 0000 0007"
    assert next(card_number) == "0000 0000 0000 0008"
    assert next(card_number) == "0000 0000 0000 0009"
    assert next(card_number) == "0000 0000 0000 0010"
    assert next(card_number) == "0000 0000 0000 0011"
    assert next(card_number) == "0000 0000 0000 0012"
    assert next(card_number) == "0000 0000 0000 0013"
    assert next(card_number) == "0000 0000 0000 0014"
    assert next(card_number) == "0000 0000 0000 0015"
    assert next(card_number) == "0000 0000 0000 0016"
    assert next(card_number) == "0000 0000 0000 0017"
    assert next(card_number) == "0000 0000 0000 0018"
    assert next(card_number) == "0000 0000 0000 0019"
    assert next(card_number) == "0000 0000 0000 0020"
    assert next(card_number) == "0000 0000 0000 0021"
    assert next(card_number) == "0000 0000 0000 0022"
    assert next(card_number) == "0000 0000 0000 0023"
    assert next(card_number) == "0000 0000 0000 0024"
    assert next(card_number) == "0000 0000 0000 0025"

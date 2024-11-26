from unittest.mock import patch

from src.utils import get_operations_transactions, transactions_sum


def test_get_operations_transactions():
    """Функция, тестирующая функцию преобразования данных из Json-файла с положительным результатом"""
    path = get_operations_transactions(
        "C:/Users/Darya/Desktop/ProjectsHometasks/BankOperationsProject/data/operations.json"
    )
    assert path[0] == {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2019-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }


def test_2_get_operations_transactions():
    """Функция, тестирующая функцию преобразования данных из Json-файла без указания пути файла"""
    path = get_operations_transactions("")
    assert path == []


def test_3_get_operations_transactions():
    """Функция, тестирующая функцию преобразования данных из Json-файла с ошибочным указанием файла."""
    path = get_operations_transactions("BankOperationsProject/data/operations")
    assert path == []


def test_transactions_sum():
    """Функция, тестирующая функцию, которая возвращает сумму транзакции."""
    assert (
        transactions_sum(
            get_operations_transactions(
                "C:/Users/Darya/Desktop/ProjectsHometasks/BankOperationsProject/data/operations_for_tests.json"
            )
        )
        == 40178.95
    )


def test_2_transactions_sum():
    """Функция, тестирующая функцию, которая возвращает сумму транзакции с ошибочным указанием файла."""
    assert (
        transactions_sum(
            get_operations_transactions(
                "C:/Users/Darya/Desktop/ProjectsHometasks/BankOperationsProject/data/operatis.json"
            )
        )
        == 0.0
    )


@patch("src.external_api.get_currency")
def test_3_transactions_sum(mock_get_currency):
    """Функция, тестирующая функцию, которая возвращает сумму транзакции с ошибочным указанием файла"""
    mock_get_currency.return_value == 10.00
    assert (
        transactions_sum(
            get_operations_transactions(
                "C:/Users/Darya/Desktop/ProjectsHometasks/BankOperationsProject/data/operations_for_tests_3.json"
            )
        )
        == 5.00
    )


def test_4_transactions_sum():
    """Функция, тестирующая функцию, которая возвращает сумму транзакции без указания валюты"""
    path = transactions_sum(
        get_operations_transactions(
            "C:/Users/Darya/Desktop/ProjectsHometasks/BankOperationsProject/data/operations_for_tests_2.json"
        )
    )
    assert path == 0.0

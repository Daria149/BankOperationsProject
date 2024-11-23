from unittest.mock import patch

from src.with_re import count_operations, search_description

test_data = [
    {
        "id": 441945886,
        "state": "EXECUTED",
        "date": "2020-08-26T10:50:58.294041",
        "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Maestro 1596837868705199",
        "to": "Счет 64686473678894779589",
    }
]


@patch("re.findall")
def test_search_description(mock_findall):
    mock_findall.return_value == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2020-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]
    assert search_description(list(test_data), "Организации") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2020-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


def test_2_search_description():
    assert search_description(test_data, "Перевод организации") == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2020-08-26T10:50:58.294041",
            "operationAmount": {"amount": "31957.58", "currency": {"name": "руб.", "code": "RUB"}},
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589",
        }
    ]


def test_count_operations():
    assert count_operations(test_data) == {"Перевод организации": 1}

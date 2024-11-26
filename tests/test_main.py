from unittest import mock
from unittest.mock import MagicMock, Mock, mock_open, patch

from main import get_transactions_from_file

for_tests = [
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


@patch("main.input")
@patch("main.input")
@patch("main.input")
@patch("main.input")
@patch("main.input")
@patch("main.input")
def test_main(
    mock_input_point, mock_input_status, mock_data_sort, mock_order_sort, mock_currency_sort, mock_word_filter
):
    mock_input_point.return_value = "1"
    mock_input_status.return_value = "CANCELED"
    mock_data_sort.return_value = "нет"
    mock_currency_sort.return_value = "ДА"
    mock_word_filter.return_value = "нет"
    assert get_transactions_from_file() == []


@patch("main.input")
@patch("main.get_operations_transactions")
@patch("main.input")
@patch("main.input")
@patch("main.input")
@patch("main.input")
@patch("main.input")
def test_2_main(
    mock_input_point,
    mock_transactions,
    mock_input_status,
    mock_data_sort,
    mock_order_sort,
    mock_currency_sort,
    mock_word_filter,
):
    mock_input_point.return_value = "1"
    mock_transactions.return_value = for_tests
    mock_input_status.return_value = "pending"
    mock_data_sort.return_value = "да"
    mock_order_sort.return_value = "по убыванию"
    mock_currency_sort.return_value = "дА"
    mock_word_filter.return_value = "организации"
    assert get_transactions_from_file() == []


@patch("main.input")
@patch("main.get_operations_transactions")
@patch("main.input")
@patch("main.input")
@patch("main.input")
@patch("main.input")
@patch("main.input")
def test_3_main(
    mock_input_point,
    mock_transactions,
    mock_input_status,
    mock_data_sort,
    mock_order_sort,
    mock_currency_sort,
    mock_word_filter,
):
    mock_input_point.return_value = "3"
    mock_transactions.return_value = for_tests
    mock_input_status.return_value = "executed"
    mock_data_sort.return_value = "да"
    mock_order_sort.return_value = "по возdрастанию"
    mock_currency_sort.return_value = "нет"
    mock_word_filter.return_value = "нет"
    assert get_transactions_from_file() == [
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


@patch("main.input")
@patch("main.get_operations_transactions")
@patch("main.input")
@patch("main.input")
@patch("main.input")
@patch("main.input")
def test_4_main(
    mock_input_point, mock_transactions, mock_input_status, mock_data_sort, mock_currency_sort, mock_word_filter
):
    mock_input_point.return_value = "3"
    mock_transactions.return_value = for_tests
    mock_input_status.return_value = "executed"
    mock_data_sort.return_value = "нет"
    mock_currency_sort.return_value = "нет"
    mock_word_filter.return_value = "нет"
    assert get_transactions_from_file() == [
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


@patch("main.input")
def test_5_main(mock_input, test_operations=for_tests):
    with patch("get_operations_transactions", test_operations):
        mock_input.side_effect = ["executed", "Да", "по возрастанию", "Да", "Перевод организации"]
    assert get_transactions_from_file() == for_tests


@patch("main.input")
def test_6_main(mock_input_point):
    with patch(
        "get_operations_transactions",
        mock_open(
            read_data="C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\BankOperationsProject\\data\\operations_for_tests.json"
        ),
    ):
        mock_input_point.return_value = "1"
        mock_input = MagicMock()
        mock_input.side_effect = ["executed", "нет", "да", "нет"]
    assert get_transactions_from_file() == [
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

import pytest
from src.widget import get_date, mask_account_card


@pytest.mark.parametrize(
    "information, expected_result",
    [
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),
        ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
        ("Счет 35383033474447895560", "Счет **5560"),
        ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
    ],
)
def test_mask_account_card(information: str, expected_result: str) -> None:
    """Функция, тестирующая функцию, которая маскирует номер карты/счета"""
    assert mask_account_card(information) == expected_result


with pytest.raises(ValueError):
    mask_account_card("")
with pytest.raises(ValueError):
    mask_account_card("MasterCard 71583007347")


@pytest.fixture
def test_get_date() -> None:
    """Функция, тестирующая функцию, которая выводит корректную дату."""
    assert get_date("2024-03-11T02:26:18.671407") == "03.11.2024"


@pytest.fixture
def test_2_get_date() -> None:
    """Функция, тестирующая функцию, которая выводит корректную дату."""
    assert get_date("") == "No date"

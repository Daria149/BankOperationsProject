from typing import Union
import pytest
from src.masks import get_mask_account, get_mask_card_number


def test_get_mask_card_number() -> None:
    assert get_mask_card_number("7000792289606361") == "7000 79** **** 6361"


@pytest.mark.parametrize(
    "card_number, expected_result",
    [(7000792289606361, "7000 79** **** 6361"), ("5555900038761111", "5555 90** **** 1111")],
)
def test_2_get_mask_card_number(card_number: Union[int, str], expected_result: str) -> None:
    assert get_mask_card_number(card_number) == expected_result


@pytest.mark.parametrize(
    "account_number, expected_results", [(73654108430135874305, "**4305"), ("73556788430135872211", "**2211")]
)
def test_get_mask_account(account_number: Union[int, str], expected_results: str) -> None:
    assert get_mask_account(account_number) == expected_results

import pytest
from src.masks import get_mask_account, get_mask_card_number

@pytest.mark.parametrize("card_numbers, expected_result", [("7000792289606361", "7000 79** **** 6361"),
                                                           (2345896599990000, "2345 89** **** 0000")]
                         )
def test_get_mask_card_number(card_numbers, expected_result):
    assert get_mask_card_number(card_numbers) == expected_result

@pytest.fixture
def test_account_numbers():
    assert get_mask_account(23458965999900003333) == "**3333"


@pytest.mark.parametrize("acc_numbers, expected_result", [("73654108430135874305", "**4305"),
                                                          (73654108430135874305, "**4305")]
                         )
def test_get_mask_account(acc_numbers, expected_result):
    assert get_mask_account(acc_numbers) == expected_result

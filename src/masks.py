from typing import Union


def get_mask_account(number: Union[int, str]) -> str:
    """Функция, которая принимает на вход номер счёта и возвращает его маску"""

    account_number = str(number)
    return f"**{account_number[-4:]}"


def get_mask_card_number(numbers: Union[int, str]) -> str:
    """Функция, принимающая на вход номер карты и возвращает её маску"""

    card_number = str(numbers)
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"

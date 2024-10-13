from typing import Union


def get_mask_account(number: Union[int, str]) -> str:
    """Функция, принимает на вход номер счета и возвращает его маску"""

    account_number = str(number)
    return f"**{account_number[-4:]}"


def get_mask_card_number(numbers: Union[int, str]) -> str:
    """Функция, которая принимает на вход номер карты и возвращает ее маску"""

    card_number = str(numbers)
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_information: str) -> str:
    """Функция, которая маскирует номер карты/счета."""
    card_account_number = ""
    space_symbol_index = account_information.rfind(" ")

    for symbol in account_information:
        if symbol.isdigit():
            card_account_number += symbol
        else:
            card_account_type = account_information[0:space_symbol_index]
    if len(card_account_number) == 20:
        return f"{card_account_type} {get_mask_account(card_account_number)}"
    elif len(card_account_number) == 16 or len(card_account_number) == 18 or len(card_account_number) == 19:
        return f"{card_account_type} {get_mask_card_number(card_account_number)}"
    else:
        raise ValueError("Ошибка ввода")


def get_date(information: str) -> str:
    """Функция, которая выводит корректную дату."""
    if information == "":
        return "No date"
    else:
        return f"{information[5:7]}.{information[8:10]}.{information[0:4]}"

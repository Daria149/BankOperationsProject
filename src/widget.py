from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_information: str) -> str:
    """Функция, маскирует номер карты/счета"""
    card_account_type = ""
    card_account_number = ""

    for symbol in account_information:
        if symbol.isalpha():
            card_account_type += symbol
        elif symbol.isdigit():
            card_account_number += symbol
    if len(card_account_number) > 16:
        return f"{card_account_type} {get_mask_account(card_account_number)}"
    elif len(card_account_number) == 16:
        return f"{card_account_type} {get_mask_card_number(card_account_number)}"
    else:
        return f"Ошибка ввода"


print(mask_account_card("Maestro 1596837868705199"))


def get_date(information: str) -> str:
    """Функция выводит корректную дату"""
    return f"{information[5:7]}.{information[8:10]}.{information[0:4]}"


print(get_date("2024-03-11T02:26:18.671407"))

from src.masks import get_mask_account, get_mask_card_number

def mask_account_card(account_information: str) -> str:
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

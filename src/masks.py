import logging
from typing import Union

logger = logging.getLogger("masks")
file_handler = logging.FileHandler(
    "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\BankOperationsProject\\logs\\masks.log", mode="w", encoding="utf-8"
)
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)


def get_mask_account(number: Union[int, str]) -> str:
    """Функция, которая принимает на вход номер счёта и возвращает его маску."""

    account_number = str(number)
    logger.info("Данные для вывода маски счёта получены")
    return f"**{account_number[-4:]}"


def get_mask_card_number(numbers: Union[int, str]) -> str:
    """Функция, которая принимает на вход номер карты и возвращает её маску"""

    card_number = str(numbers)
    logger.info("Данные для вывода маски карты получены")
    return f"{card_number[0:4]} {card_number[4:6]}** **** {card_number[-4:]}"

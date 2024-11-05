import json
import logging
from typing import Any

from src.external_api import get_currency

logger = logging.getLogger('utils')
file_handler = logging.FileHandler('logs\\utils.log', mode='w', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)
logger.setLevel(logging.ERROR)


def get_operations_transactions(file_path: Any) -> Any:
    """Обработка Json-файла и преобразование данных в список словарей"""
    datas = []
    try:
        with open(file_path, "r", encoding="utf-8") as transactions_file:
            try:
                transaction_info = json.load(transactions_file)
                if type(transaction_info) is not list or len(transaction_info) == 0:
                    return datas
                else:
                    logging.info(f"Обработка данных Json-файла прошла успешно")
                    return transaction_info
            except json.JSONDecodeError:
                logging.error(f"Ошибка декодирования")
                return datas
    except FileNotFoundError:
        logging.error("Ошибка поиска файла")
        return datas


def transactions_sum(func: Any) -> float:
    """Функция возвращает сумму транзакции в рублях"""
    datas = func
    data_str = []
    amount = []
    for trans in datas:
        if trans["operationAmount"]["currency"]["code"] == "":
            logging.info("В данных есть транзакции без указания валюты")
            continue
        elif trans["operationAmount"]["currency"]["code"] == "RUB":
            data_str.append(trans["operationAmount"]["amount"])
        elif trans["operationAmount"]["currency"]["code"] != "RUB":
            get_currency("RUB", trans["operationAmount"]["currency"]["code"], trans["operationAmount"]["amount"])
            data_str.append(trans["operationAmount"]["amount"])
    for d in data_str:
        amount.append(float(d))
    result_amount = round(float(sum(amount)), 2)
    logging.info("Сумма транзакций получена")
    return result_amount

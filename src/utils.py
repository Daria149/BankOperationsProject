import json
from typing import Any

from src.external_api import get_currency


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
                    return transaction_info
            except json.JSONDecodeError:
                print("Ошибка декодирования")
                return datas
    except FileNotFoundError:
        print("Ошибка поиска файла")
        return datas


def transactions_sum(func: Any) -> float:
    """Функция возвращает сумму транзакции в рублях"""
    datas = func
    data_str = []
    amount = []
    for trans in datas:
        if trans["operationAmount"]["currency"]["code"] == "":
            continue
        elif trans["operationAmount"]["currency"]["code"] == "RUB":
            data_str.append(trans["operationAmount"]["amount"])
        elif trans["operationAmount"]["currency"]["code"] != "RUB":
            get_currency("RUB", trans["operationAmount"]["currency"]["code"], trans["operationAmount"]["amount"])
            data_str.append(trans["operationAmount"]["amount"])
    for d in data_str:
        amount.append(float(d))
    result_amount = round(float(sum(amount)), 2)
    return result_amount


if __name__ == "__main__":
    print(
        transactions_sum(
            get_operations_transactions(
                "C:/Users/Darya/Desktop/ProjectsHometasks/BankOperationsProject/data/operations.json"
            )
        )
    )


# if __name__ == "__main__":
#    print(get_operations_transactions(
#        "C:/Users/Darya/Desktop/ProjectsHometasks/BankOperationsProject/data/operations_for_tests.json"
#    ))

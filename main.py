from typing import Any

from src.csv_pandas import read_from_csv, read_from_excel
from src.generators import filter_by_currency, transaction_descriptions
from src.processing import filter_by_state, sort_by_date
from src.utils import get_operations_transactions
from src.widget import get_date, mask_account_card
from src.with_re import count_operations, search_description

json_path = "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\BankOperationsProject\\data\\operations.json"
excel_path = "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\transactions_excel.xlsx"
csv_path = "C:\\Users\\Darya\\Desktop\\ProjectsHometasks\\FilesForTasks\\transactions.csv"


def get_transactions_from_file() -> list[dict]:
    """Функция, запрашивающая файл для чтения и читающая указанный файл ."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    while True:
        print("Выберите необходимый пункт меню: 1, 2 или 3")
        print(
            "1. Получить информацию о транзакциях из JSON -файла.\n"
            "2. Получить информацию о транзакциях из CSV -файла.\n"
            "3. Получить информацию о транзакциях из XLSX -файла."
        )
        input_point = int(input())
        if input_point == 1:
            print("Для обработки выбран JSON -файл")
            operations_file = get_operations_transactions(json_path)
            break
        elif input_point == 2:
            print("Для обработки выбран CSV -файл")
            operations_file = read_from_csv(csv_path)
            break
        elif input_point == 3:
            print("Для обработки выбран XLSX -файл")
            operations_file = read_from_excel(excel_path)
            break
        else:
            print("Неверный ввод")
            continue

    while True:
        print(
            "Введите статус, по которому необходимо выполнить фильтрацию."
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
        )
        input_status = input().upper()
        if input_status == "EXECUTED" or input_status == "CANCELED" or input_status == "PENDING":
            print(f"Операции отфильтрованы по статусу {input_status}")
            break
        else:
            print(f"Статус операции {input_status} недоступен")
            continue
    filter_operations = filter_by_state(operations_file, input_status)
    data_sort = input("Программа: Отсортировать операции по дате? Да/Нет   ").lower()
    if data_sort == "да":
        order_sort = input("Программа: Отсортировать 'по возрастанию' или 'по убыванию'?   ").lower()
        if order_sort == "по возрастанию":
            data_sort_flag = False
            filter_order_transactions = sort_by_date(filter_operations, data_sort_flag)
        elif order_sort == "по убыванию":
            data_sort_flag = True
            filter_order_transactions = sort_by_date(filter_operations, data_sort_flag)
        else:
            print("Ответ не понятен. Операции будут отсортированы по возрастанию.")
            data_sort_flag = False
            filter_order_transactions = sort_by_date(filter_operations, data_sort_flag)
    elif data_sort == "нет":
        filter_order_transactions = filter_operations
    else:
        print("Введён некорректный ответ. Операции будут выведены без сортировки")
        filter_order_transactions = filter_operations

    currency_sort = input("Выводить только рублевые тразакции? Да / Нет   ").lower()
    if currency_sort == "да":
        filter_currency_transactions = []
        for trans in filter_order_transactions:
            if input_point == 2 or input_point == 3:
                filter_result = filter_by_currency(filter_order_transactions, "RUB")
                filter_currency_transactions = filter_result
            elif input_point == 1:
                if trans.get("currency_code") == "RUB":
                    filter_currency_transactions.append(trans)
    elif currency_sort == "нет":
        filter_currency_transactions = filter_order_transactions
    else:
        print("Введён некорректный ответ. Будут выведены все операции")
        filter_currency_transactions = filter_order_transactions

    print(
        "Отфильтровать список транзакций по определенному слову в описании?\n"
        "Для фильтрации введите, по какому слову выполнить фильтр.\n"
        "Если фильтровать по слову не нужно, введите 'Нет'"
    )
    word_filter = input().lower()
    if word_filter == "нет":
        filter_word_transactions = filter_currency_transactions
    elif word_filter != "нет":
        try:
            filter_word_transactions = search_description(filter_currency_transactions, word_filter)
        except AttributeError:
            print("Транзакции не найдены")
            filter_word_transactions = []

    print("Распечатываю итоговый список транзакций...")
    if len(filter_word_transactions) == 0:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
    else:
        print(f"Всего банковских операций в выборке: {count_operations(filter_word_transactions)}")
        for element in filter_word_transactions:
            if input_point == 1:
                currency = element["operationAmount"]["currency"]["name"]
                element_data = get_date(element["date"])
                if element["description"] == "Открытие вклада":
                    card_accound = mask_account_card(element["to"])
                else:
                    card_accound = mask_account_card(element["from"]) + " -> " + mask_account_card(element["to"])
                amount = element["operationAmount"]["amount"]

            elif input_point == 2 or input_point == 3:
                currency = get_date(element["currency_code"])
                element_data = get_date(element["date"])
                if element["description"] == "Открытие вклада":
                    card_accound = mask_account_card(element["to"])
                else:
                    card_accound = mask_account_card(element["from"]) + " -> " + mask_account_card(element["to"])
                amount = element["amount"]
            print(f"{element_data} {element["description"]}\n{card_accound}\n Сумма:{round(float(amount))} {currency}")


if __name__ == "__main__":
    get_transactions_from_file()

from mypy.server.objgraph import Iterable


def filter_by_state(dictionary_list: dict) -> list:
    """Функция, фильтрующая список словарей по статусу (state)"""
    new_dictionary_list = []
    if dictionary_list == []:
        raise ValueError("Нет данных. Ошибка ввода.")
    else:
        for element in dictionary_list:
            if element["state"] == "EXECUTED":
                new_dictionary_list.append(element)
            else:
                continue
    return new_dictionary_list


def sort_by_date(dictionary_list: Iterable[dict], parameter: bool = True) -> list:
    """Функция, сортирующая список словарей по дате (date)"""
    sorted_dictionary_list = sorted(
        dictionary_list, key=lambda x: x["date"], reverse=parameter
    )
    return sorted_dictionary_list

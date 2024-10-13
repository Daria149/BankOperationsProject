from typing import List


def filter_by_state(dictionary_list: list) -> list:
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
    sorted_dictionary_list = sorted(dictionary_list, key=lambda x: x["date"], reverse=parameter)
    return sorted_dictionary_list

dictionary_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def filter_by_state(dictionary_list: List[dict], state: str = "EXECUTED") -> List[dict]:
    '''Функция фильтрует список словарей по статусу (state)'''
    new_dictionary_list = []
    for element in dictionary_list:
        if element["state"] == state:
            new_dictionary_list.append(element)
        else:
            continue
    return new_dictionary_list


def sort_by_date(dictionary_list: List[dict], parameter: bool = True) -> List[dict]:
    '''Функция сортирует список словарей по дате (date)'''
    return sorted(dictionary_list, key=lambda x: x["date"], reverse=parameter)

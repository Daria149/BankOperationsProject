from typing import List, Any


def filter_by_state(dictionary_list: List, state: str = "EXECUTED") -> List[dict]:
    """Функция, которая фильтрует список словарей по статусу(state)"""
    new_dictionary_list = []
    for element in dictionary_list:
        if element.get("state") == state:
            new_dictionary_list.append(element)
        else:
            continue
    return new_dictionary_list


def sort_by_date(dictionary_list: Any, parameter: bool = True) -> List[dict]:
    """Функция, которая сортирует список словарей по дате(date)"""
    return sorted(dictionary_list, key=lambda x: x["date"], reverse=parameter)

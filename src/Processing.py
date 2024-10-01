def filter_by_state(dictionary_list: dict) -> list:
    new_dictionary_list = []
    for element in dictionary_list:
        if element['state'] == 'EXECUTED':
            new_dictionary_list.append(element)
        else:
            continue
    return new_dictionary_list



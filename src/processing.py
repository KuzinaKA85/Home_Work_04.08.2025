from typing import Any, Dict, List


def filter_by_state(list_of_dicts: List[Dict], state: str) -> List:
    """Функция, которая сортирует список словарей по значению ключа 'state'"""
    if not list_of_dicts:
        raise ValueError("Пустой список")
    new_list = []
    for element in list_of_dicts:
        for key, value in element.items():
            if element[key] == state:
                new_list.append(element)
    return new_list


user_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]


def sort_by_date(list_of_dicts: List[Dict], reverse: bool) -> Any:
    """Функция, которая сортирует список словарей по дате в порядке убывания"""
    if not list_of_dicts:
        raise ValueError("Пустой список")
    key_to_check = "date"
    for dictionary in list_of_dicts:
        if dictionary.get(key_to_check) is None:
            return "Дата не найдена"
        else:
            sorted_list_of_dicts = sorted(list_of_dicts, key=lambda element: element["date"], reverse=True)
            return sorted_list_of_dicts


# Функция проверки работы кода
if __name__ == "__main__":
    print(filter_by_state(my_list, "EXECUTED"))
    print(filter_by_state(my_list, "CANCELED"))
    print(sort_by_date(my_list, reverse=True))
    print(sort_by_date([{"id": 41428829, "state": "EXECUTED"}], reverse=True))
    print(filter_by_state([], "EXECUTED"))

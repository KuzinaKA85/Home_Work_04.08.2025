from datetime import datetime
from typing import Dict, List


def filter_by_state(list_of_dicts: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Функция, которая сортирует данные по статусу 'state'"""
    filtered_list = []
    for element in list_of_dicts:
        if "state" in element and element["state"] == state:
            filtered_list.append(element)
    return filtered_list


user_list = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

print(filter_by_state(user_list))


def sort_by_date(list_of_dicts: List[Dict], date_key: str = "date", descending: bool = True) -> List:
    """Функция, которая сортирует список словарей по дате в порядке убывания"""
    return sorted(
        list_of_dicts, key=lambda x: datetime.strptime(x[date_key], "%Y-%m-%dT%H:%M:%S.%f"), reverse=descending
    )


print(sort_by_date(user_list))

from typing import Dict, Iterable, List

transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {"amount": "79114.93", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188",
    },
    {
        "id": 873106923,
        "state": "EXECUTED",
        "date": "2019-03-23T01:09:46.296404",
        "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод со счета на счет",
        "from": "Счет 44812258784861134719",
        "to": "Счет 74489636417521191160",
    },
    {
        "id": 895315941,
        "state": "EXECUTED",
        "date": "2018-08-19T04:27:37.904916",
        "operationAmount": {"amount": "56883.54", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод с карты на карту",
        "from": "Visa Classic 6831982476737658",
        "to": "Visa Platinum 8990922113665229",
    },
    {
        "id": 594226727,
        "state": "CANCELED",
        "date": "2018-09-12T21:27:25.241689",
        "operationAmount": {"amount": "67314.70", "currency": {"name": "руб.", "code": "RUB"}},
        "description": "Перевод организации",
        "from": "Visa Platinum 1246377376343588",
        "to": "Счет 14211924144426031657",
    },
]


def filter_by_currency(transactions_: List[Dict], name: str) -> Iterable:
    """Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции
    соответствует заданной"""
    for dictionary in transactions_:
        if dictionary["operationAmount"]["currency"]["name"] == "USD":
            yield dictionary


usd_transactions = filter_by_currency(transactions, "USD")
for item in usd_transactions:
    print(item)


def transaction_descriptions(my_list: List[Dict]) -> Iterable:
    """Функция принимает список словарей с транзакциями на вход, возвращает описание
    каждой операции по очереди"""
    for element in my_list:
        yield element["description"]


descriptions = transaction_descriptions(transactions)


for item in descriptions:
    print(item)


def generator_numbers_card(start: int = 1, stop: int = 9999999999999999) -> Iterable[str]:
    """Генератор номеров банковских карт в формате XXXX XXXX XXXX XXXX"""
    if start < 1:
        raise ValueError("Начальный номер должен быть не менее 1")
    if stop > 9999999999999999:
        raise ValueError("Конечный номер должен быть 16 символов")
    if start > stop:
        raise ValueError("Начальный номер должен быть меньше или равен конечному")
    current = start
    while current <= stop:
        number = str(current).zfill(16)
        number_modified = f"{number[:4]} {number[4:8]} {number[8:12]} {number[12:]}"
        yield number_modified
        current += 1


card_number_generator = generator_numbers_card(1, 5)


for card_number in card_number_generator:
    print(card_number)

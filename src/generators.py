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
        "id": 939710000,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "EURO", "code": "EURO"}},
        "description": "Перевод со счета на счет",
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
        "id": 939711111,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "EURO", "code": "EURO"}},
        "description": "Перевод с карты на карту",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
    },
    {
        "id": 939717555,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702",
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

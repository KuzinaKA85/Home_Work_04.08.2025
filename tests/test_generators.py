from typing import Dict, Iterator, List

import pytest

from src.generators import filter_by_currency, transaction_descriptions, generator_numbers_card


@pytest.fixture
def sample_transactions() -> List[Dict]:
    """Фикстура с тестовыми транзакциями."""
    return [
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
    }
]

def test_filter_usd_transactions(sample_transactions):
    """Тест корректной фильтрации USD транзакций."""

    usd_transactions = list(filter_by_currency(sample_transactions, "USD"))

    assert len(usd_transactions) == 3
    assert all(t["operationAmount"]["currency"]["name"] == "USD" for t in usd_transactions)
    assert usd_transactions[0]["id"] == 939719570
    assert usd_transactions[1]["id"] == 142264268
    assert usd_transactions[2]["id"] == 895315941


def test_empty_list(sample_transactions):
    """Тест обработки пустого списка транзакций."""

    result = list(filter_by_currency([], "USD"))

    assert result == []


def test_iterator_behavior(sample_transactions):
    """Тест поведения итератора (поочередная выдача)."""

    usd_iterator = filter_by_currency(sample_transactions, "USD")

    assert isinstance(usd_iterator, Iterator)

    # Получаем транзакции по одной
    first = next(usd_iterator)
    second = next(usd_iterator)
    third = next(usd_iterator)

    assert first["id"] == 939719570
    assert second["id"] == 142264268
    assert third["id"] == 895315941

    # Проверяем, что больше нет элементов
    with pytest.raises(StopIteration):
        next(usd_iterator)


def test_card_number_generator():
    """Тест генерации номеров."""
    # Act
    generate = generator_numbers_card(1, 5)
    result = list(generate)

    # Expected
    expected = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert result == expected


def test_transaction_descriptions(sample_transactions):
    """Проверяет, что функция возвращает корректные описания."""

    result = list(transaction_descriptions(sample_transactions))

    assert result == [
        "Перевод организации",
        "Перевод со счета на счет",
        "Перевод со счета на счет",
        "Перевод с карты на карту",
        "Перевод организации"
    ]


def test_empty_list_descriptions(sample_transactions):
    """Тест обработки пустого списка транзакций."""

    result = list(filter_by_currency([], "USD"))

    assert result == []


def test_extreme_values_card_number_generator():
    """Тест генерации крайних значений"""

    generate = generator_numbers_card(9999999999999995, 9999999999999999)
    result = list(generate)

    expected = [
        "9999 9999 9999 9995",
        "9999 9999 9999 9996",
        "9999 9999 9999 9997",
        "9999 9999 9999 9998",
        "9999 9999 9999 9999",
    ]
    assert result == expected


def test_wrong_card_number_generator():
    """Тест генерации номеров c некоректными значениями."""
    with pytest.raises(ValueError):
        list(generator_numbers_card(15, 7))


def test_invalid_start_card_number_generator():
    """Тест некорректного начального значения."""
    with pytest.raises(ValueError):
        list(generator_numbers_card(0, 7))


def test_invalid_end_card_number_generator():
    """Тест некорректного конечного значения."""
    with pytest.raises(ValueError):
        list(generator_numbers_card(1, 10000000000000000))


def test_default_card_number_generator():
    """Тест работы с параметрами по умолчанию."""
    # Получаем первые 3 номера из полного диапазона
    gen = generator_numbers_card()
    first_three = [next(gen) for _ in range(3)]

    expected = ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]
    assert first_three == expected
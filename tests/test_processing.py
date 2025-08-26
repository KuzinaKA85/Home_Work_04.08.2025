import pytest

from src.processing import filter_by_state, sort_by_date

@pytest.fixture()
def data():
    return [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

@pytest.mark.parametrize("state, expected", [
    ("EXECUTED", [
        {"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 2, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]),
])
def test_filter_by_state(data, state, expected):
    """Тест фильтрации по состоянию EXECUTED"""
    assert filter_by_state(data, state) == expected


@pytest.mark.parametrize("state, expected", [
    ("CANCELED", [
        {"id": 3, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 4, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]),
])
def test_filter_by_state_custom_canceled(data, state, expected):
    """Тест фильтрации по состоянию CANCELED"""
    assert filter_by_state(data, state) == expected

def test_filter_by_state_no_data():
    with pytest.raises(ValueError):
        filter_by_state([], state="")


def test_sort_by_date_in_descending():
    """Тестирование сортировки списка словарей по датам в порядке убывания"""

    data = [
        {"id": 1, "date": "2023-10-26T10:00:00.000000"},
        {"id": 2, "date": "2023-10-25T12:00:00.000000"},
        {"id": 3, "date": "2023-10-27T08:00:00.000000"},
    ]
    sorted_desc = sort_by_date(data, reverse=True)
    assert sorted_desc[0]["date"] == "2023-10-27T08:00:00.000000"
    assert sorted_desc[1]["date"] == "2023-10-26T10:00:00.000000"
    assert sorted_desc[2]["date"] == "2023-10-25T12:00:00.000000"


def test_sort_by_date_with_invalid_date_formats():
    """Тестирование с отсутствующим ключом 'date'"""
    missing_key_data = [
        {"id": 1, "date": "2023-10-26T10:00:00.000000"},
        {"id": 2, "timestamp": "2023-10-25T12:00:00.000000"}, # Отсутствует 'date'
        {"id": 3, "date": "2023-10-27T08:00:00.000000"},
    ]
    with pytest.raises(KeyError, match="date"): # Или другой код ошибки, если `x[data_key]` вызовет ее
        sort_by_date(missing_key_data, reverse=True)

def test_sort_by_date_no_data():
    with pytest.raises(ValueError):
        filter_by_state([], state="")
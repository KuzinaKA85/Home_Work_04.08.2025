import pytest

from src.widget import mask_account_card, get_date


@pytest.fixture
def number_card_for_widget():
    return "Visa Platinum 7000792289606361"


@pytest.fixture
def number_account_for_widget():
    return "Счёт 73654108430135874305"


@pytest.fixture
def date():
    return "2024-03-11T02:26:18.671407"


@pytest.mark.parametrize("expected", ["Visa Platinum 7000 79** **** 6361"])
def test_mask_account_card(number_card_for_widget, expected):
    assert mask_account_card(number_card_for_widget) == expected


@pytest.mark.parametrize("expected", ["Счёт **4305"])
def test_mask_account_card(number_account_for_widget, expected):
    assert mask_account_card(number_account_for_widget) == expected


@pytest.mark.parametrize("expected", ["11.03.2024"])
def test_get_date(date, expected):
    assert get_date(date) == expected
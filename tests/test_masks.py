import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.fixture
def number_card():
    return "7000792289606361"


@pytest.mark.parametrize("expected", ["7000 79** **** 6361"])
def test_get_mask_card_number(number_card, expected):
    assert get_mask_card_number(number_card) == expected


def test_get_mask_card_number_wrong_length():
    with pytest.raises(ValueError):
        get_mask_card_number("70007922896063611264564")


@pytest.fixture
def number_account():
    return "73654108430135874305"


@pytest.mark.parametrize("expected", ["**4305"])
def test_get_mask_account(number_account, expected):
    assert get_mask_account(number_account) == expected


def test_get_mask_account_wrong_length():
    with pytest.raises(ValueError):
        get_mask_account("73654108430135874305123")

import unittest
from unittest.mock import patch, mock_open
import os
import json
from src.utils import transaction_data
from typing import List, Dict
import pytest

@pytest.fixture
def sample_transactions() -> List[Dict]:
    """Фикстура с тестовыми транзакциями."""
    return [
  {
    "id": 441945886,
    "state": "EXECUTED",
    "date": "2019-08-26T10:50:58.294041",
    "operationAmount": {
      "amount": "31957.58",
      "currency": {
        "name": "руб.",
        "code": "RUB"
      }
    },
    "description": "Перевод организации",
    "from": "Maestro 1596837868705199",
    "to": "Счет 64686473678894779589"
  },
  {
    "id": 41428829,
    "state": "EXECUTED",
    "date": "2019-07-03T18:35:29.512364",
    "operationAmount": {
      "amount": "8221.37",
      "currency": {
        "name": "USD",
        "code": "USD"
      }
    },
    "description": "Перевод организации",
    "from": "MasterCard 7158300734726758",
    "to": "Счет 35383033474447895560"
  }
]

@pytest.mark.parametrize("expected", [31957.58])
def test_transaction_data(sample_transactions, expected):
  assert transaction_data(sample_transactions) == expected


@pytest.mark.parametrize("expected", ["7000 79** **** 6361"])
def test_get_mask_card_number(number_card, expected):
    assert get_mask_card_number(number_card) == expected

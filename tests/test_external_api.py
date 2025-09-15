from typing import Dict
from unittest.mock import MagicMock, patch

import pytest

from src.external_api import convert


@pytest.fixture
def transaction() -> Dict:
    """Фикстура с тестовыми транзакциями."""
    return {
        "date": "2019-08-16T04:23:41.621065",
        "description": "Перевод с карты на счет",
        "from": "MasterCard 8826230888662405",
        "id": 86608620,
        "operationAmount": {"amount": 6004.0, "currency": {"code": "USD", "name": "руб."}},
        "state": "EXECUTED",
        "to": "Счет 96119739109420349721",
    }


def test_convert(transaction):
    """Проверка корректного результат"""
    mock_response = MagicMock()
    mock_response.json.return_value = {"result": 502844.78652}
    with patch("requests.get", return_value=mock_response):
        assert convert(transaction) == 502844.78652

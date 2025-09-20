from unittest.mock import MagicMock, mock_open, patch

from src.transactions_read import read_transactions_csv, read_transactions_xlsx


def test_read_transactions_csv():
    # Создаем список, который будет возвращать наш мок вместо csv.DictReader
    mock_data = [
        {
            "amount": "16210",
            "currency_code": "PEN",
            "currency_name": "Sol",
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "id": "650703",
            "state": "EXECUTED",
            "to": "Счет 39745660563456619397",
        },
        {
            "amount": "29740",
            "currency_code": "COP",
            "currency_name": "Peso",
            "date": "2020-12-06T23:00:58Z",
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "id": "3598919",
            "state": "EXECUTED",
            "to": "Discover 0720428384694643",
        },
    ]

    # Используем patch для замены поведения csv.DictReader и open
    with patch("builtins.open", mock_open(read_data="")) as mock_file:
        with patch("csv.DictReader", return_value=mock_data) as mock_reader:
            result = read_transactions_csv(mock_file)

            # Проверяем, что функция была вызвана один раз
            mock_reader.assert_called_once()

    # Проверяем, что результат функции соответствует ожиданиям
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["amount"] == "16210"
    assert result[1]["description"] == "Перевод с карты на карту"


def test_read_transactions_xlsx():
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [
        {
            "amount": 16210.0,
            "currency_code": "PEN",
            "currency_name": "Sol",
            "date": "2023-09-05T11:30:32Z",
            "description": "Перевод организации",
            "from": "Счет 58803664561298323391",
            "id": 650703.0,
            "state": "EXECUTED",
            "to": "Счет 39745660563456619397",
        },
        {
            "amount": 29740.0,
            "currency_code": "COP",
            "currency_name": "Peso",
            "date": "2020-12-06T23:00:58Z",
            "description": "Перевод с карты на карту",
            "from": "Discover 3172601889670065",
            "id": 3598919.0,
            "state": "EXECUTED",
            "to": "Discover 0720428384694643",
        },
    ]

    # Используем patch для замены поведения pandas.read_excel
    with patch("pandas.read_excel", return_value=mock_df) as mock_read_excel:
        result = read_transactions_xlsx("fake_path.xlsx")

        # Проверяем, что функция была вызвана один раз
        mock_read_excel.assert_called_once()

        # Проверяем, что функция была вызвана с аргументом orient="records"
        mock_df.to_dict.assert_called_once_with(orient="records")

    # Проверяем, что результат функции соответствует ожиданиям
    assert isinstance(result, list)
    assert len(result) == 2
    assert result[0]["amount"] == 16210.0
    assert result[1]["description"] == "Перевод с карты на карту"

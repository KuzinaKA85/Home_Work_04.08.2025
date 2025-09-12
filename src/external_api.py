import json
import os
from typing import Dict, List

import requests
from dotenv import load_dotenv

from src.utils import filepath, transaction_data

load_dotenv()

API_KEY = os.getenv("API_KEY")

if API_KEY is None:
    print("API_KEY не найден")


def converted_transactions(transactions: List[Dict]) -> None | float | str:
    """Фуекция принимает на вход транзакции и возвращает сумму в рублях. Если транзакция была в USD,
    происходит обращение к внешнему API для получения текущего курса валют и конвертации"""
    try:
        for dictionary in transactions:
            if dictionary:
                if dictionary["operationAmount"]["currency"]["code"] == "RUB":
                    amount = float(dictionary["operationAmount"]["amount"])
                    return amount
                    currency_to = "RUB"
                    currency_from = "USD"
                    URL = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"
                    payload = {}
                    headers = {"apikey": API_KEY}
                    if currency_from:
                        response = requests.request("GET", URL, headers=headers, data=payload)
                        status_code = response.status_code
                        result = response.text
                        print(result)
                        if status_code == 200:
                            python_response = json.loads(result)
                            print(python_response)
                        else:
                            print(f"Ошибка API: {response.status_code}")
    except json.JSONDecodeError as e:
        print(f"Ошибка декодирования JSON: {e}")
    except KeyError:
        return "Ключ не найден."


print(converted_transactions(transaction_data(filepath)))

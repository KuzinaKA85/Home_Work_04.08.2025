import os
import json
from dotenv import load_dotenv
import requests
from typing import List, Dict
from src.utils import transaction_data, filepath

load_dotenv('.env')

API_KEY = os.getenv('API_KEY')


# URL = "https://api.apilayer.com/exchangerates_data/convert?to={to}&from={from}&amount={amount}"
# payload = {}
# headers= {
#   "apikey": "vqvUMSCNWz8jesGxEdsLEYjzhhsLBQF2"
# }
# transactions = transaction_data(filepath)

def filtered_transactions(transactions1: List[Dict]) -> None:
    try:
        for dictionary in transactions1:
            if dictionary:
                if dictionary["operationAmount"]["currency"]["code"] == "RUB":
                    amount = dictionary["operationAmount"]["amount"]
                    print(amount)

                    currency_to = "RUB"
                    currency_from = ["USD", "EUR"]
                    URL = f"https://api.apilayer.com/exchangerates_data/convert?to={currency_to}&from={currency_from}&amount={amount}"
                    payload = {}
                    headers = {"apikey": API_KEY}
                    if currency_from:
                        response = requests.request("GET", URL, headers=headers, data = payload)
                        status_code = response.status_code
                        result = response.text
                        print(result)
                        if status_code == 200:
                            python_response = json.loads(result)
                            print(python_response)
                        else:
                            print(f"Ошибка API: {response.status_code}")
    except KeyError:
        return "Ключ не найден."



print(filtered_transactions(transaction_data(filepath)))

# def get_currency_rate(currency_code):
#     url = f"https://www.cbr-xml-daily.ru//daily_json.js"
#     response = requests.get(url)
#     if response.status_code != 200:
#         raise ValueError(f"Failed to get currency rate")
#     data = response.json()
#     currency_data = data["Valute"].get(currency_code)
#     if not currency_data:
#         raise ValueError(f"No data for currency {currency_code}")
#     return {
#         "currency_code": currency_code,
#         "rate": currency_data["Value"],




 # elif dictionary["operationAmount"]["currency"]["code"] == "USD" or "EUR":

# print(next(filtered_transactions(transaction_data(filepath))))




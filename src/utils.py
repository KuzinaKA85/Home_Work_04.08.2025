import json
import os
from typing import Any

filepath = r"C:\Users\sysadmin\Desktop\Project_Python\Home_Work_10.1\data\operations.json"


def transaction_data(filepath: Any) -> Any:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях"""
    try:
        with open(filepath, encoding="utf-8") as f:
            if os.path.getsize(filepath) > 0:  # проверка, что файл не пуст
                data = json.load(f)
                if isinstance(data, list):  # проверка, что файл содержит список
                    print("Файл содержит JSON-список.")
                else:
                    print("Файл содержит JSON, но это не список.")
                print(type(data))
                return data
            else:
                print("Файл пустой.")
    except json.JSONDecodeError:
        print("Файл не является валидным JSON.")
    except FileNotFoundError:
        print(f"Файл '{filepath}' не найден.")


print(transaction_data(filepath))

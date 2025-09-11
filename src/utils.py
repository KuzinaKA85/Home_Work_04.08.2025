import json
import os
from typing import Any

filepath = r"C:\Users\sysadmin\Desktop\Project_Python\Home_Work_10.1\data\operations.json"


def transaction_data(file_path: Any) -> Any:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях"""
    try:
        with open(file_path, encoding="utf-8") as f:
            if os.path.getsize(file_path) > 0:  # проверка, что файл не пуст
                data = json.load(f)
                if isinstance(data, list):  # проверка, что файл содержит список
                    print("Файл содержит JSON-список.")
                else:
                    print("Файл содержит JSON, но это не список.")
                return data
            else:
                print("Файл пустой.")
    except json.JSONDecodeError:
        print("Файл не является валидным JSON.")
    except FileNotFoundError:
        print(f"Файл '{file_path}' не найден.")


print(transaction_data(filepath))

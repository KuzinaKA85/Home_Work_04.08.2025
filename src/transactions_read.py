import csv
from pathlib import Path
from pprint import pprint
from typing import Any, Dict, List

import pandas as pd

filepath_csv = Path("..", "data", "transactions.csv")
filepath_xlsx = Path("..", "data", "transactions_excel.xlsx")


def read_transactions_csv(filepath: Path) -> List[Dict[Any, Any]]:
    """Функция для считывания финансовых операций. Принимает на вход файл.csv, возвращает список
    словарей"""
    with open(filepath, mode="r", encoding="utf-8") as csv_file:
        # Создание объекта DictReader, который читает строки как словари
        reader = csv.DictReader(csv_file, delimiter=";")
        # Итерация по строкам и добавление их в список
        list_of_dicts = []
        for row in reader:
            list_of_dicts.append(row)
        return list_of_dicts


def read_transactions_xlsx(filepath: Path) -> List[Dict[Any, Any]]:
    """Функция для считывания финансовых операций. Принимает на вход файл.xlsx, возвращает список
    словарей"""
    # Чтение файла
    reader = pd.read_excel(filepath)
    # Преобразование DataFrame в список словарей
    dict_reader = reader.to_dict(orient="records")
    return dict_reader


if __name__ == "__main__":
    result_csv = read_transactions_csv(filepath_csv)
    pprint(result_csv)
    result_xlsx = read_transactions_xlsx(filepath_xlsx)
    pprint(result_xlsx)

import json
import logging
import os
from pathlib import Path
from typing import Any

file_path_1 = Path("..", "logs", "utils.log")

file_path_2 = Path("..", "data", "operations.json")

logger = logging.getLogger("utils")
logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(file_path_1, "w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def read_transactions(file_path: Path) -> Any:
    """Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными
    о финансовых транзакциях"""
    if not os.path.exists(file_path):
        logger.error("Файл не найден или путь указан неверно.")
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        logger.info("Файл успешно прочитан и выведен в консоль в виде Python-объекта.")
        if not data or not isinstance(data, list):
            logger.error("Файл пустой или содержит не список.")
            return []
        return data


print(read_transactions(file_path_2))

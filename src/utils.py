import json
import os
from typing import Dict, List

filepath = r"C:\Users\sysadmin\Desktop\Project_Python\Home_Work_10.1\data\operations.json"


def read_transactions(file_path: str) -> List[Dict]:
    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as file:
        data = json.load(file)
        if not data or not isinstance(data, list):
            return []
        return data


print(read_transactions(filepath))

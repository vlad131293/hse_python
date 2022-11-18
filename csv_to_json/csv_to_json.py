import csv
import json
from typing import List


class Converter:
    """Работает в парадигме, что заголовок есть всегда"""

    def __init__(self):
        pass

    def get_data(self, csv_file_name: str) -> List[list]:
        rows = []
        with open(csv_file_name, newline='') as f:
            reader = csv.reader(f)
            for row in reader:
                rows.append(row)
        return rows
    
    def transform_data(self, rows: List[list]) -> List[dict]:
        keys = rows[0]
        result = []

        if len(rows) == 1:
            result = {key: None for key in keys}

        else:
            for row in rows[1:]:
                temp = dict()
                for key, val in zip(keys, row):
                    val = val if val != '' else None
                    temp[key] = val
                result.append(temp)
        return result 

    def save_json(self, data: List[dict], json_file_name: str) -> None:
        
        with open(json_file_name, 'w') as file:
            json.dump(data, file)

    def main(self, csv_file_name: str, json_file_name: str) -> None:
        rows = self.get_data(csv_file_name)
        data = self.transform_data(rows)
        self.save_json(data, json_file_name)


def main(csv_file_name: str, json_file_name: str) -> None:
    conv = Converter()
    conv.main(csv_file_name, json_file_name)


if __name__ == "__main__":
    main('data/input.csv', 'data/output.json')
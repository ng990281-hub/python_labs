import csv
import json
from pathlib import Path

def json_to_csv(json_path: str, csv_path: str) -> None:
    """
    Преобразует JSON-файл в CSV.
    Поддерживает список словарей [{...}, {...}], заполняет отсутствующие поля пустыми строками.
    Кодировка UTF-8. Порядок колонок — как в первом объекте или алфавитный (указать в README).
    """
    jp=Path(json_path)
    cp=Path(csv_path)
    
    if not jp.is_file():
        raise FileNotFoundError(f"Файл не найден: {json_path}")
    if jp.suffix.lower() != ".json":
        raise ValueError("Входной файл должен иметь расширение .json")

    if cp.suffix.lower() != ".csv":
        raise ValueError("Выходной файл должен иметь расширение .csv")

    with jp.open('r',encoding='utf-8') as f:
        try:
            data=json.load(f)
        except json.JSONDecodeError:
            raise ValueError("Неверный формат JSON или файл пуст")

    if type(data)!=list or len(data)==0:
        raise ValueError("Пустой JSON или неподдерживаемая структура")
    for item in data:
        if type(item)!=dict:
            raise ValueError("JSON должен содержать список словарей")

    columns=[]
    for item in data:
        for key in item:
            if key not in columns:
                columns.append(key)
    
    if not columns:
        raise ValueError("В JSON отсутствуют поля для CSV")
    
    with cp.open('w',newline="",encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=columns)
        w.writeheader()
        w.writerows(data)

def csv_to_json(csv_path: str, json_path: str) -> None:
    jp=Path(json_path)
    cp=Path(csv_path)
    
    if not cp.is_file():
        raise FileNotFoundError(f"Файл не найден: {csv_path}")
    if cp.suffix.lower() != ".csv":
        raise ValueError("Входной файл должен иметь расширение .csv")

    if jp.suffix.lower() != ".json":
        raise ValueError("Выходной файл должен иметь расширение .json")
    with cp.open("r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise ValueError("Файл CSV пустой")
        data = list(reader)
    if len(data)==0:
        raise ValueError('CSV-файл не содержит данных')
    with jp.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    

if __name__ == '__main__':
    json_to_csv("data/samples/people.json", "data/out/people.csv")
    csv_to_json("data/samples/people.csv", "data/out/people.json")


            

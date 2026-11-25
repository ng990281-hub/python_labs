import json
from pathlib import Path

from src.lab08.models import student_to_dict, student_from_dict


def students_to_json(students, path):
    data = [student_to_dict(s) for s in students]
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path):

    with Path(path).open("r", encoding="utf-8") as f:
        data = json.load(f)

    if not isinstance(data, list):
        raise ValueError("Данные должны быть списком")

    students = []
    errors = []

    for x, i in enumerate(data, start=1):
        try:
            students.append(student_from_dict(i))
        except (ValueError, TypeError, KeyError) as e:
            errors.append(f"Запись №{x}: {e}")

    if errors:
        print("Найдены ошибки:")
        for error in errors:
            print(error)

        print(f"Неправильных записей: {len(errors)}")

    return students
    
if __name__ == "__main__":

    input_file = "data/lab08/samples/students_input.json"
    output_file = "data/lab08/out/students_output.json"
    bad_file = "data/lab08/samples/students_bad.json"

    students = students_from_json(input_file)

    students_to_json(students, output_file)

    print(f"Записано: {len(students)}")

    print("Проверка плохого файла:")

    bad = students_from_json(bad_file)

    


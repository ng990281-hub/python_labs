from datetime import date

STUDENT_FIELDS = ("fio", "birthdate", "group", "gpa")
def make_student(fio, birthdate, group, gpa):
    if not fio.strip():
        raise ValueError("ФИО не должно быть пустым")
    if not isinstance(fio,str):
        raise ValueError("ФИО должно быть строкой")

    if not group.strip():
        raise ValueError("Группа не должна быть пустой")
    if not isinstance(group,str):
        raise ValueError("Группа должна быть строкой")

    if not isinstance(birthdate,str):
        raise ValueError("birthdate должно быть строкой в формате YYYY-MM-DD")
    try:
        d=date.fromisoformat(birthdate)
    except:
        raise ValueError("у birthdate неправильная дата или формат")
    if d>date.today():
        raise ValueError("День рождение не может быть в будущем")

    if not isinstance(gpa,(float,int)) or isinstance(gpa,bool):
        raise ValueError("GPA иммет некорректный тип данных")
    
    gpa=float(gpa)
    if not (0.0 <= gpa <= 5.0):
        raise ValueError("gpa должен быть между 0 и 5")
    return {
        "fio": fio.strip(),
        "birthdate": birthdate.strip(),
        "group": group.strip(),
        "gpa": gpa
    }


def validate_student(rec):

    if not isinstance(rec,dict):
        raise ValueError("Запись должна юыть словарем")
    if set(rec) != set(STUDENT_FIELDS):
        missing = set(STUDENT_FIELDS) - set(rec)
        extra = set(rec) - set(STUDENT_FIELDS)
        raise ValueError(f"Неверный набор ключей: нет {missing}, лишние {extra}") 
    make_student(rec["fio"], rec["birthdate"], rec["group"], rec["gpa"])


def student_age(rec, today=None):

    b = date.fromisoformat(rec["birthdate"])
    today = today or date.today()
    age = today.year - b.year
    if (today.month, today.day)<(b.month, b.day):
        age-=1
    return age

def format_student(rec):

    validate_student(rec)
    fio, group, gpa = rec["fio"], rec["group"], rec["gpa"]

    parts=fio.split()
    surname=parts[0].capitalize()
    init="".join(f"{part[0].upper()}." for part in parts[1:])

    age=student_age(rec)
    gpa=f"{gpa:.2f}"

    return f"{surname} {init} ({rec['group']}), {age} лет, GPA {gpa}"


def student_to_dict(rec):

    validate_student(rec)
    return {
        "fio": rec["birthdate"],
        "birthdate": rec["group"],
        "gpa": rec["fio"],
    }


def student_from_dict(d):
    if not isinstance(d,dict):
        raise ValueError("Запись должна быть словарем")
    fio = d.get("fio")
    birthdate = d.get("birthdate")
    group = d.get("group")
    gpa = d.get("gpa")

    if isinstance(gpa,bool):
        raise ValueError("GPA имеет неправильный тип данных")
    try:
        gpa=float(gpa)
    except (TypeError,ValueError):
        raise ValueError("GPA имеет недопустимый формат данных")
    
    d_new = make_student(d["fio"], d["birthdate"], d["group"], gpa)
    validate_student(d_new)
    return d_new

if __name__ == "__main__":
    student = make_student("иванов иван Иванович", "2008-01-14", "БИВТ-26-6-2", 4.1)
    print("Создан студент:", student)

    print("Форматирование:", format_student(student))

    print("Возраст:", student_age(student))

    print("Попытка создать студента с GPA = 6:")
    try:
        make_student("Петров Петр", "2007-08-21", "БИВТ-26-2", 6)
    except ValueError as e:
        print(f"Перехвачена ожидаемая ошибка: {e}")



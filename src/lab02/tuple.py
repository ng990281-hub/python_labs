def format_record(rec: tuple[str, str, float]) -> str:
    if tuple!=type(rec):
        raise TypeError("Запись должна быть кортежом")
    if len(rec)!=3:
        raise ValueError("В записи должно быть 3 элемента")
    fio=rec[0].strip()
    group=rec[1].strip()
    gpa=rec[2]
    if type(fio)!=str:
        raise TypeError("ФИО должно быть строкой")
    if len(fio.split())<2  or 3<len(fio.split()): 
        raise ValueError("Некорректное ФИО")
    if type(group)!=str:
        raise TypeError("Группа должна быть строкой")
    if len(group.split())==0:
        raise ValueError("Группа пустая")
    if type(gpa)!=float and type(gpa)!=int:
        raise  TypeError("GPA должно быть числом")
    if  0>gpa or gpa>5:
        raise ValueError("Некорректное GPA")
    if len(fio.split())==3:
        s,n,ot=fio.split()
        n_ot=f'{n[0].upper()}.{ot[0].upper()}.,'
    elif len(fio.split())==2:
        s,n=fio.split()
        n_ot=f'{n[0]}.,'
    return f'{s[0].upper()}{s[1:]} {n_ot} гр. {group}, GPA {gpa:.2f}'


print(("Иванов Иван Иванович", "BIVT-25", 4.6),'→',format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(("Петров Пётр", "IKBO-12", 5.0),'→',format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(("Петров Пётр Петрович", "IKBO-12", 5.0),'→',format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(("  сидорова  анна   сергеевна ", "ABB-01", 3.999),'→',format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
print(("Кузнецов Матвей  Алексеевич", "HBD-08", 5.1),'→',format_record(("Кузнецов Матвей  Алексеевич", "HBD-08", 5.1)))
      


    
    

a=input("ФИО: ")
n,s,o=a.split()
print(f'Инициалы: {n[0]}{s[0]}{o[0]}.')
print(f'Длина (символов): {len(' '.join(a.split()))}')

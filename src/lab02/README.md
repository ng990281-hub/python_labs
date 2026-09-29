 ### ЛР2 — Коллекции и матрицы (list/tuple/set/dict)
 ## Задача 1-arrays
 ---
1. Функция min_max
Возвращаю ошибку, если список пустой. Нахожу минимальный и маскимальный элемент в цикле и возвращаю кортеж из них.
 ```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    """
    This function takes list and return pair (min, max) of the list
    """
    mn=10**9
    mx=-10**9
    if len(nums)==0:
        raise ValueError("Список пустой")
    for i in nums:
        if i<mn:
            mn=i
        if i>mx:
            mx=i
    return (mn,mx)

```
![](images\lab02\arrays_minmax.png)

---
2. Функция unique_sorted
Создаю множество из списка. С помощью пузырьковой сортировки получаю из множетсва отсортированный список.
```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    """
    This function takes a list of numbers (integers or floats) and sorts it
    """
    m=set(nums)
    m=list(m)
    for i in range(len(m)):
        for j in range(0, len(m) - i - 1):
            if m[j] > m[j + 1]:
                m[j], m[j + 1] = m[j + 1], m[j]
    return m


```
![](images\lab02\arrays_unique_sorted.png)

---
3. Функция flatten
Проверяю является ли списком или кортежом входные данные. Далее объединяю все в один список.
```python
def flatten(mat: list[list | tuple]) -> list:
    """
    This function returns a flattened version of matrix as a single list.
    """
    a=[]
    for i in mat:
        if i==list(i) or i==tuple(i):
            a+=i
        else:
            raise TypeError("Строка должна являться или списком или кортежом")
    return a
```
![](images\lab02\arrays_flatten.png)
---
### Задание 2-matrix

Функция для проверки прямоугольности матрицы
```python
def check_prmat(mat: list[list[float | int]]):
    for i in range(len(mat)):
        if len(mat[i])!=len(mat[0]):
            return False
    return True

```

---
1. Функция transpose
Проверяю на прямоугольность матрицу. Далее создаю новую  матрицу,заполненную 0, которая уже является транспанированной. Потом в двойном цикле заполняю новую матрицу значениями, меняя местами порядок строки и столбца.
```python
def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat)==0: return mat
    if not check_prmat(mat):
        raise ValueError("Матрица рваная")
    mat2=[[0 for _ in range(len(mat))] for _ in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat2[j][i]=mat[i][j]
    return mat2
```
![](images\lab02\matrix_transpose.png)
---
2. Функция row_sums
Проверяется на прямоугольность матрицы. Далее создаю список размера входной матрицы. В цикле находим сумму каждой строки и добавляем ее в новый список.
```python
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat)==0: return mat
    if not check_prmat(mat):
        raise ValueError("Матрица рваная")
    mat2=[0]*len(mat)
    for i in range(len(mat)):
        row=0
        for j in range(len(mat[i])):
            row+=int(mat[i][j])
        mat2[i]=row
    return mat2
```
![](images\lab02\matrix_rowsum.png)
---
3. Функция col_sums
Проверяется на прямоугольность матрицы. Далее создаю список размера строки входной матрицы. В цикле находим сумму каждого столбца и добавляем ее в новый список.
```python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat)==0: return mat
    if not check_prmat(mat):
       raise ValueError("Матрица рваная")
    mat2=[0]*len(mat[0])
    for i in range(len(mat[0])):
        col=0
        for j in range(len(mat)):
            col+=int(mat[j][i])
        mat2[i]=col
    return mat2
```
![](images\lab02\matrix_colsum.png)
---
### Задание 3-tuple
Разбиваю кортеж на три переменные и удаляю лишние пробелы. Проверяется корректность записи ФИО, группы и GPA. Далле в завиимости от длины ФИО разбиваю на переменные и с помощью upper() создаю f строку.Возвращаю полностью f строку.
```python
def format_record(rec: tuple[str, str, float]) -> str:
    if rec!=tuple(rec):
        raise TypeError("Запись должна быть кортежом")
    if len(rec)!=3:
        raise ValueError("В записи должно быть 3 элемента")
    fio=rec[0].strip()
    group=rec[1].strip()
    gpa=rec[2]
    if str(fio)!=fio:
        raise TypeError("ФИО должно быть строкой")
    if len(fio.split())<2  or 3<len(fio.split()): 
        raise ValueError("Некорректное ФИО")
    if str(group)!=group:
        raise TypeError("Группа должна быть строкой")
    if len(group.split())==0:
        raise ValueError("Группа пустая")
    if gpa!=float(gpa):
        raise  TypeError("GPA должно быть вещественным числом")
    if  0>gpa or gpa>5:
        raise ValueError("Некорректное GPA")
    if len(fio.split())==3:
        s,n,ot=fio.split()
        n_ot=f'{n[0].upper()}.{ot[0].upper()}.,'
    elif len(fio.split())==2:
        s,n=fio.split()
        n_ot=f'{n[0]}.,'
    return f'{s[0].upper()}{s[1:]} {n_ot} гр. {group}, GPA {gpa:.2f}'
```
![](images\lab02\tuple.png)

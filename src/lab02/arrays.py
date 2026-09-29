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

mn_mx=[[3, -1, 5, 5, 0],
      [42],
      [-5,-2,-9],
      [1.5, 2, 2.0, -3.1],
       []]
unq_s=[[3, 1, 2, 1, 3],
       [],
       [-1, -1, 0, 2, 2],
       [1.0, 1, 2.5, 2.5, 0]]

'''for i in mn_mx:
    print(i,'→',min_max(i))
for i in unq_s:
    print(i,'→',unique_sorted(i))'''
print([[1, 2], [3, 4]],'→',flatten([[1, 2], [3, 4]]))
print([[1, 2], (3, 4, 5)],'→',flatten([[1, 2], (3, 4, 5)]))
print([[1], [], [2, 3]],'→',flatten([[1], [], [2, 3]]))
print([[1, 2],"ab"],'→',flatten([[1, 2],"ab"]))

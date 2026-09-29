def check_prmat(mat: list[list[float | int]]):
    for i in range(len(mat)):
        if len(mat[i])!=len(mat[0]):
            return False
    return True

def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat)==0: return mat
    if not check_prmat(mat):
        raise ValueError("Матрица рваная")
    mat2=[[0 for _ in range(len(mat))] for _ in range(len(mat[0]))]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            mat2[j][i]=mat[i][j]
    return mat2
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
'''
print([[1, 2, 3]],'→',transpose([[1, 2, 3]]))
print([[1], [2], [3]],'→',transpose([[1], [2], [3]]))
print([[1, 2], [3, 4]],'→',transpose([[1, 2], [3, 4]]))
print([],'→',transpose([]))
print([[1, 2], [3]],'→',transpose([[1, 2], [3]]))
print([[1, 2, 3], [4, 5, 6]],'→',row_sums([[1, 2, 3], [4, 5, 6]]))
print([[-1, 1], [10, -10]],'→',row_sums([[-1, 1], [10, -10]]))
print([[0, 0], [0, 0]],'→',row_sums([[0, 0], [0, 0]]))
print([[1, 2], [3]],'→',row_sums([[1, 2], [3]]))
'''
print([[1, 2, 3], [4, 5, 6]],'→',col_sums([[1, 2, 3], [4, 5, 6]]))
print([[-1, 1], [10, -10]],'→',col_sums([[-1, 1], [10, -10]]))
print([[0, 0], [0, 0]],'→',col_sums([[0, 0], [0, 0]]))
print([[1, 2], [3]],'→',col_sums([[1, 2], [3]]))
     
    

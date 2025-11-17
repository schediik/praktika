import random
n = int(input())
matrix = []
for i in range(n):
    matrix.append([random.randint(-10, 20) for _ in range(n)])
for row in matrix:
    print(*row)
positiv_st = []
for i in range(len(matrix[0])):
    flag = True
    for j in range(len(matrix)):
        if matrix[j][j] > 0:
            flag = False
        if flag:
            positiv_st.append(i)
if len(matrix) > 0:
    positiv_st
else:
    print('Ничего не найдено')
print('Hello')

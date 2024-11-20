#Задание 2
n = int(input("Введите нечетный порядок матрицы: "))
A = []
print("Введите значения матрицы: ")
for i in range (n):
    B = []
    for i in range (n):
        B.append(int(input()))
    A.append(B)
print("Полученная вами матрица:")
for i in A:
    for j in i:
        print(j, end=' ')
    print()
MP1 = max(A[i+1][i] for i in range (n-1))
MP2= max(A[i][i+1] for i in range (n-1))
MG = max(A[i][i] for i in range (n))
MM = max(MP1, MP2, MG)
print("Максимальный элемент среди главной и побочных дииагоналей (MM):",MM)
for i in range (n):
    for j in range (n):
        if A[i][j] == MM:
            A[i][j] = A[n//2][n//2]
            break
A[n//2][n//2] = MM
print("Матрица полученная после обмена значениями между MM и центральным элементом изначальной матрицы:")
for i in A:
    for j in i:
        print(j, end=' ')
    print()
#Задание 1
matrix = [[1, 4, 5],
          [3, 2, 7],
          [8, 6, 9]]

max_in_rows = [max(row) for row in matrix]
min_in_cols = [min(col) for col in zip(*matrix)]

print("Наибольшие элементы в каждой строке:", max_in_rows)
print("Наименьшие элементы в каждом столбце:", min_in_cols)
# Задача №13

#  Шахматная доска
# На вход программе подаются два натуральных числа n и m. 
# Напишите программу для создания матрицы размером n×m, заполнив ее символами 
# . и * в шахматном порядке. В левом верхнем углу должна стоять точка. 
# Выведите полученную матрицу на экран, разделяя элементы пробелами.

# n = int(input("Enter n: "))
# m = int(input("Enter m: "))

n, m = map(int, input().split())

matrix = list()

for i in range(n):
    row = []
    for j in range(m):
        if i % 2 != 0 and j % 2 == 0:
            row.append('*')
        elif i % 2 == 0 and j % 2 != 0:
            row.append('*')
        else:
            row.append('.')
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Задача №14
# Побочная диагональ
# На вход программе подается натуральное число n. Напишите программу, 
# которая создает матрицу размером n×n и заполняет ее по следующему правилу:

# числа на побочной диагонали равны 1;
# числа, стоящие выше этой диагонали, равны 0;
# числа, стоящие ниже этой диагонали, равны 2.

# Полученную матрицу выведите на экран. Числа в строке разделяйте одним пробелом.

# Формат входных данных
# На вход программе подается натуральное число n – количество строк и столбцов в 
# матрице.

# Формат выходных данных
# Программа должна вывести матрицу в соответствии с условием задачи.

# Примечание. Побочная диагональ – это диагональ, идущая из правого верхнего в 
# левый нижний угол матрицы.


n = int(input("Enter size of matrix: "))
matrix = []

for i in range(n):
    row = []
    for j in range(n):
        row.append('.')
    matrix.append(row)


for i in range(n):
    for j in range(n):
        matrix[i][n - i - 1] = 1
        if (i >= j or i <= j) and i < n - 1 - j:
            matrix[i][j] = 0
        if (i <= j or i >= j) and i > n - 1 - j:
            matrix[i][j] = 2

for i in range(n):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print()

# Вариант 2
n = int(input())
matrix = [[None for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if i + j + 1 == n:
            matrix[i][j] = 1
        elif i + j + 1 < n:
            matrix[i][j] = 0
        else:
            matrix[i][j] = 2

for row in matrix:
    print(*row)
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

# Задача № 15
# Заполнение 1
# На вход программе подаются два натуральных числа n и m. 
# Напишите программу, которая создает матрицу размером n×m и заполняет ее числами 
# от 1 до n⋅m в соответствии с образцом.

# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и 
# m – количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести матрицу в соответствии с образцом.

# Примечание. Для вывода элементов матрицы как в примерах отводите ровно 
# 3 символа на каждый элемент. Для этого используйте строковый метод ljust(). 
# Можно обойтись и без ljust(), система примет и такое решение.

import random

# n = int(input("Enter n: "))
# m = int(input("Enter m: "))

n, m = map(int, input().split())

endOfRange = n * m

matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(random.randrange(1, endOfRange))
    matrix.append(row)

# for row in matrix:
#     print(*row)

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()

# Вариант, где идет по порядку
n, m = map(int, input().split())

matrix = []

count = 1

for i in range(n):
    row = []
    for j in range(m):
        row.append(count)
        count += 1
    matrix.append(row)

for r in range(n):
    for c in range(m):
        print(str(matrix[r][c]).ljust(3), end='')
    print()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
# Задача № 16

# Заполнение 2

# На вход программе подаются два натуральных числа n и m. 
# Напишите программу, которая создает матрицу размером n×m, заполнив ее в соответствии с образцом.

# Формат входных данных
# На вход программе на одной строке подаются два натуральных числа n и m – количество строк и столбцов в матрице.

# Формат выходных данных
# Программа должна вывести указанную матрицу в соответствии с образцом.

matrixOfNums = list()
n, m = map(int, input().split())
count = 1

while count <= n:
    matrix = []
    for i in range(count, n * m + 1, n):
        matrix.append(i)
    
    count += 1
    matrixOfNums.append(matrix)

for row in matrixOfNums:
    print(*row)
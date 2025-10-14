# Задача №1

# Вывести матрицу 1
# На вход программе подаются два натуральных числа n и m, каждое на отдельной строке – количество строк и столбцов в матрице. 
# Далее вводятся сами элементы матрицы – слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, затем второй, 
# и так далее.

# Напишите программу, которая сначала считывает элементы матрицы один за другим, затем выводит их в виде матрицы.

# Формат входных данных
# На вход программе подаются два числа n и m – количество строк и столбцов в матрице, далее идут n×m слов, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести считанную матрицу, разделяя ее элементы одним пробелом.


n = int(input('Enter count of rows: '))
m = int(input('Enter count of colums: '))

my_list = []

for i in range(n*m):

    my_list.append(input())

for i in range(n):
    row = my_list[i * m:(i + 1) * m]
    print(' '.join(row))

# Второй цикл проходит по номерам строк i от 0 до n-1.

# Для каждой строки берётся срез из плоского списка my_list: my_list[i * m:(i + 1) * m].

# i * m — индекс начала строки (сколько элементов нужно пропустить: по m на каждую из предыдущих i строк).

# (i + 1) * m — индекс конца строки (не включая его), то есть взяли ровно m элементов.

# Полученный список row — это элементы одной строки матрицы; print(' '.join(row)) выводит их через пробел.

# Пример при n=2, m=3 и my_list = ['a','b','c','d','e','f']:
# i=0: срез my_list[0:3] → ['a','b','c']
# i=1: срез my_list[3:6] → ['d','e','f']


# Второй вариант

n, m = int(input()), int(input())
matrix = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    matrix.append(row)

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()

#-------------------------------------
# Задача №2
# Вывести матрицу 2
# На вход программе подаются два натуральных числа n и m, каждое на отдельной строке — количество строк и столбцов в матрице. 
# Далее вводятся сами элементы матрицы – слова, каждое на отдельной строке; подряд идут элементы сначала первой строки, 
# затем второй, и так далее.

# Напишите программу, которая считывает элементы матрицы один за другим, выводит их в виде матрицы, выводит пустую строку, и снова ту же матрицу, но уже поменяв местами строки со столбцами: первая строка выводится как первый столбец, и так далее.

# Формат входных данных
# На вход программе подаются два числа n и m – количество строк и столбцов в матрице, далее идут n×m слов, каждое на отдельной строке.

# Формат выходных данных
# Программа должна вывести считанную матрицу, за ней пустую строку и ту же матрицу, но поменяв местами строки со столбцами. 
# Элементы матрицы разделять одним пробелом.


n = int(input("Enter count of row: "))
m = int(input("Enter count of column: "))

my_list = []

for i in range(n):
    row = []
    for j in range(m):
        row.append(input())
    my_list.append(row)

for i in range(len(my_list)):
    print(*my_list[i])

print()

for j in range(m):
    for i in range(n):
        print(my_list[i][j], end=' ')
    print()

#-------------------------------------
# Задача №3

# След матрицы ↘️
# Следом квадратной матрицы называется сумма элементов главной диагонали. Напишите программу, которая выводит след заданной квадратной матрицы.

# Формат входных данных
# На вход программе подается натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы (целые числа) 
# построчно через пробел.

# Формат выходных данных
# Программа должна вывести одно число – след заданной матрицы.

n = int(input('Enter your count of rows: '))

matrix = []

sum_of_num = 0

for i in range(n):
    row = []
    for j in range(n):
        row.append(input())
    matrix.append(row)

for i in range(len(matrix)):
    print(*matrix[i], end='\n')


for i in range(n):
    sum_of_num += int(matrix[i][i])

print(sum_of_num)


# Вариант 2

n = int(input('Enter your count of rows: '))
matrix = []
sum_of_num = 0

for i in range(n):
    str_of_num = input().split(' ')
    for j in range(len(str_of_num)):
        str_of_num[j] = int(str_of_num[j])
    matrix.append(str_of_num)

print(matrix)

for i in range(n):
    sum_of_num += int(matrix[i][i])

print(sum_of_num)

#------------------------------------
# Задача 4
# Больше среднего

# Напишите программу, которая выводит количество элементов квадратной матрицы в каждой строке, больших среднего арифметического 
# элементов данной строки.

# Формат входных данных
# На вход программе подается натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы (целые числа) 
# построчно через пробел.

# Формат выходных данных
# Программа должна вывести n чисел – для каждой строки количество элементов матрицы, больших среднего арифметического элементов данной 
# строки.

import math
num = int(input())
matrix = []
average_sum = 0
final_matrix = []


for i in range(num):
    str_of_num = input().split(' ')
    for j in range(len(str_of_num)):
        str_of_num[j] = int(str_of_num[j])
    matrix.append(str_of_num)

# print(matrix)

for i in range(len(matrix)):
    average_sum = 0
    for j in matrix[i]:
        average_sum += j
    average_value = average_sum // len(matrix[i])
    count = 0
    for z in matrix[i]:
        if z > average_value:
            count += 1
    final_matrix.append(count)

print(*final_matrix, sep='\n')


#------------------------------------
# Задача 5
# Максимальный в области 1

# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.


# Формат входных данных
# На вход программе подается натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы (целые числа) 
# построчно через пробел.

# Формат выходных данных
# Программа должна вывести одно число – максимальный элемент в заштрихованной области квадратной матрицы.

num = int(input("Enter size of matrix: "))

matrix = []

max_num = -100

for i in range(num):
    row = input().split(' ')
    for j in range(len(row)):
        row[j] = int(row[j])
    matrix.append(row)

for i in range(num):
    for j in range(num):
        if i >= j:
            if matrix[i][j] > max_num:
                max_num = matrix[i][j]
print(max_num)

#------------------------------------
# Задача 6
# Суммы четвертей

# Квадратная матрица разбивается на четыре четверти, ограниченные главной и побочной диагоналями: верхнюю, нижнюю, левую и правую.


num = int(input('Enter size of matrix: '))

matrix = []

sum_1 = 0
sum_2 = 0
sum_3 = 0
sum_4 = 0


for i in range(num):

    row = input().split(' ')
    for j in range(len(row)):
        row[j] = int(row[j])
    matrix.append(row)


for i in range(num):
    for j in range(num):
        if i < j and i < num - 1 - j:
            sum_1 += matrix[i][j]
        if i < j and i > num - 1 - j:
            sum_2 += matrix[i][j]
        if i > j and i > num - 1 -j:
            sum_3 += matrix[i][j]
        if i > j and i < num - 1 - j:
            sum_4 += matrix[i][j]


print('Верхняя четверть:',sum_1)
print('Правая четверть:', sum_2)
print('Нижняя четверть:', sum_3)
print('Левая четверть:', sum_4)

#------------------------------------
# Задача 7
# Максимальный в области 2 🌶️
# Напишите программу, которая выводит максимальный элемент в заштрихованной области квадратной матрицы.



# Формат входных данных
# На вход программе подается натуральное число n – количество строк и столбцов в матрице, затем элементы матрицы (целые числа) построчно 
# через пробел.

# Формат выходных данных
# Программа должна вывести одно число – максимальный элемент в заштрихованной области квадратной матрицы.


num = int(input("Enter size of matrix: "))

matrix = []

max_1 = -100
max_2 = -100

for i in range(num):
    row = input().split(' ')
    for j in range(len(row)):
        row[j] = int(row[j])
    matrix.append(row)

for i in range(len(matrix)):
    for j in range(len(matrix)):
        if i >= j and i <= num - 1 - j:
            if max_1 < matrix[i][j]:
                max_1 = matrix[i][j]
            # print(matrix[i][j])
        if i <= j and i >= num - 1 - j:
            if max_2 < matrix[i][j]:
                max_2 = matrix[i][j]
            # print(matrix[i][j])

print(max(max_1, max_2))
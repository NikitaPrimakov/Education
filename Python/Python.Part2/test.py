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
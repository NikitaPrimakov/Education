# Упражнение 1

# Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой, равной n, 
# в соответствии с примером:

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# ...

count = 0
num = int(input("Введите натуральное число: "))

for i in range(1, num + 1):

    print(i)
    
    for j in range(i + 1, num):

        print(j,j + 1)

    break
        
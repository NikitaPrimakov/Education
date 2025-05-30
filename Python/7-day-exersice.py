#####################################################
## День 7. Решение задач                            #
#####################################################

import math
# Задача №1

# Напишите программу, которая считывает одну строку текста и выводит 10 строк, пронумерованных от 0 до 9
# каждая, с указанной строкой текста.

str = input()

for i in range(10):
    print(i, str)

# Задача №2

# На вход программе подаётся натуральное число n. 
# Напишите программу, которая для каждого из чисел от 0 до n (включительно) 
# выводит текст в следующем формате:

# Квадрат числа <текущее число> равен <квадрат текущего числа>

n = int(input("Enter number n: "))

for i in range(n):
    print("Квадрат числа", i, "равен", i**2)


# Задача №3

# На вход программе подаётся натуральное число n (n≥2) – катет прямоугольного равнобедренного треугольника.
# Напишите программу, которая выводит звёздный треугольник в соответствии с примером.

num = int(input("Enter your num: "))
for i in range(num):
    print((num-i) * "*" )


# Задача №4
# На вход программе подаются три натуральных числа m,p,z: 
# m: стартовое количество организмов;
# p: среднесуточное увеличение в %;
# n: количество дней для размножения.

# Напишите программу, которая предсказывает размер популяции организмов с 
# 1-го по n-й день (включительно). # Программа должна выводить номер дня, 
# а затем через пробел размер популяции в этот день.

m = int(input())
p = int(input())
n = int(input())

for i in range(n):
    print(i + 1, m * (p / 100 + 1) ** i)
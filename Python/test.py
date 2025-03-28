# Дано натуральное число n. Напишите программу, которая выводит значение суммы: 
# 1!+2!+3!+…+n!

import math

num = int(input('Введите число: '))

summ = 0

for i in range(1, num + 1):

    factorialOfnum = math.factorial(i)
    summ += factorialOfnum

print(summ)
## Решение задач
import math

# Упражнение 1

# Напишите функцию, которая возвращает длину гипотенузы прямоугольного треугольника по известным 
# значениям его катетов.

def gipotinuza (katet_one, katet_two):

    return (katet_one ** 2 + katet_two ** 2) * 0.5


katet_one = int(input("Enter value of katet #1: "))
katet_two = int(input("Enter value of katet #2: "))

value_of_gipotinuza = gipotinuza(katet_one, katet_two)
print("Значение гипотинузы:", value_of_gipotinuza)


# Упражнение 2


#  Напишите функцию get_distance(x1, y1, x2, y2), вычисляющую расстояние между точками (x1; y1) и
# (x2 ;y2).


def distance(x_1, y_1, x_2, y_2):

    return ((x_1 - x_2)**2 + (y_1 - y_2)**2) * 0.5


x_1 = int(input("Enter x1:"))
y_1 = int(input("Enter y1:"))
x_2 = int(input("Enter x2:"))
y_2 = int(input("Enter y2:"))

value_of_distance = distance(x_1, y_1, x_2, y_2)

print(value_of_distance)



# Упражнение 3


# Напишите функцию sum_digits(n), принимающую в качестве аргумента натуральное число и 
# возвращающую сумму его цифр.


def sum_digits(n):
    
    value_of_summ = 0

    while n > 0:

        last_digit = n % 10
        value_of_summ += last_digit
        n = n // 10
    
    return value_of_summ
    

n = int(input("Enter your number 'n': "))

print(sum_digits(n))


# Упражнение 4


# Напишите функцию compute_average(numbers), принимающую в качестве аргумента список чисел и 
# возвращающую среднее значение элементов списка.

# return [int(number) for number in (input().split())]


def compute_average(number):

    value_of_summ = 0
    count = 0
    for i in number:

        value_of_summ += i
        count += 1

    return value_of_summ // count


number = input().split()

for i in range(len(number)):

    number[i] = int(number[i])

print(compute_average(number))




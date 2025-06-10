# Упражнение 1

# Середина отрезка

# Напишите функцию get_middle_point(x1, y1, x2, y2), которая принимает в качестве аргументов 
# координаты концов отрезка (x1,y1) (x2,y2) и возвращает координаты точки являющейся серединой 
# данного отрезка.

def get_middle_point(x_1, y_1, x_2, y_2):

    return (x_1 + x_2)/2, (y_1 + y_2)/2


# считываем данные
x_1, y_1 = int(input()), int(input())
x_2, y_2 = int(input()), int(input())

# вызываем функцию
x, y = get_middle_point(x_1, y_1, x_2, y_2)
print(x, y)
#-------------------------------------------

# Упражнение 2

# Площадь и длина 📏

# Напишите функцию get_circle(radius), которая принимает в качестве аргумента радиус окружности и 
# возвращает два значения: длину окружности и площадь круга, ограниченного данной окружностью.


import math

def get_circle(radius):

    return math.pi * 2 * radius, math.pi * radius**2

radius = float(input())

C, S = get_circle(radius)
print(C, S)
#-------------------------------------------

# Упражнение 3

# Корни уравнения 🌶️🌶️
import math

# Напишите функцию solve(a, b, c), которая принимает в качестве аргументов три целых числа a, b, c 
# – коэффициенты квадратного уравнения ax2+bx+c=0 и возвращает его корни в порядке возрастания.

def solve(a, b, c):

    print("Посчитаем количество корней в уравнеее")

    D = b ** 2 - 4 * a * c

    if D > 0:
        print("D > 0. Квадратное уровнение имеет 2 корня")
        print()
        print("Решим квадратное уровнеие вида: ax2+bx+c=0")

        x_1 = (-b + math.sqrt(D)) / (2 * a)
        x_2 = (-b - math.sqrt(D)) / (2 * a)

        if x_1 > x_2:
            return x_2, x_1
        else:
            return x_1, x_2

    elif D == 0:
        print("D = 0. Квадратное уровнение имеет два равных корня")
        print()
        print("Решим квадратное уровнеие вида: ax2+bx+c=0")
        x_1 = -b / (2 * a)
        x_2 = -b / (2 * a)
        return x_1, x_2

    else:
        print("D < 0. Квадратное уровнение не имеет корней")


a, b, c = int(input()), int(input()), int(input())
print(solve(a, b, c))
#-------------------------------------------

# Упражнение 4

# Вывод уникальных слов

def unique(answer_text: str) -> str:

    list_one = []
    answer_split = answer_text.split(' ')
    for i in answer_split:
        count_of_word = answer_split.count(i)
        if count_of_word < 2:
            list_one.append(i)
        else:
            continue
    return list_one
    

answer_text = input()
unique_word = unique(answer_text)
print(*unique_word, sep=' ')
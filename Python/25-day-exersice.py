## Упражнение 1

# Звёздный треугольник

# Напишите функцию draw_triangle(fill, base), которая принимает два параметра:

# fill – символ заполнитель;
# base – величина основания равнобедренного треугольника;
# а затем выводит его.

# Примечание. Гарантируется, что основание треугольника – нечётное число.

# *
# 9


# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *


def draw_triangle(fill, base):

    base_part_one = base // 2
    base_part_two = base - base_part_one

    for i in range(1, base_part_one + 1):

        print(fill * i)

    for i in range(base_part_two, 0, -1):

        print(fill * i)

draw_triangle(input(), int(input()))
#------------------------------------

#№ Упражнение 2

# ФИО

# Напишите функцию print_fio(name, surname, patronymic), которая принимает три параметра:

# name – имя человека;
# surname – фамилия человека;
# patronymic – отчество человека;
# а затем выводит на печать ФИО человека.

# Примечание. Предусмотрите тот факт, что все три буквы в ФИО должны иметь верхний регистр.


def print_fio( name, surname, patronymic):

    print(surname.title()[0], name.title()[0], patronymic.title()[0], sep='')

print_fio(input(), input(), input())
#------------------------------------

#№ Упражнение 3

# Сумма цифр

# Напишите функцию print_digit_sum(), которая принимает одно натуральное число num и выводит на печать сумм

def print_digit_sum(num):
    sum_of_num = 0
    if num < 10:
        sum_of_num += num
    else:
        while num > 0:
            last_digit = num % 10
            sum_of_num += last_digit
            num = num // 10
    print(sum_of_num)

print_digit_sum(int(input()))
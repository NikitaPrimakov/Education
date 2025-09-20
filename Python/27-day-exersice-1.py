# Упражнение 1

# Конвертер километров

# Напишите функцию convert_to_miles(km), которая принимает в качестве аргумента расстояние в 
# километрах и возвращает расстояние в милях. Формула для преобразования: 
# 
# мили = километры * 0.6214.


def convert_to_miles(km):

    return km * 0.6214


num = float(input("Enter value of km: "))

print(convert_to_miles(num)) # вывод при 10 -> 6.2139999999999995
                            # нужный вывод 6.214

#----------------------------------------------------------------

# Упражнение 2

# Напишите функцию get_days(month), которая принимает в качестве аргумента номер месяца и 
# возвращает количество дней в данном месяце.

# Примечание 1. Гарантируется, что передаваемый аргумент находится в диапазоне от 1 до 12 
# (включительно).

# Примечание 2. Считайте, что год является невисокосным.


def get_days(month):

    if month in [1, 3, 5, 7, 8, 10, 12]:
        return 31
    if month in [2]:
        return 28
    else:
        return 30
    

month = int(input("Enter num of month: "))
print(get_days(month))

#----------------------------------------------------------------

# Упражнение 3


# Делители 1

# Напишите функцию get_factors(num), принимающую в качестве аргумента натуральное число и 
# возвращающую список всех делителей данного числа.


def get_factors(num):

    list_of_factors = []

    for i in range(1, num + 1):

        if num % i == 0:

            list_of_factors.append(i)

    return list_of_factors



num = int(input("Enter your num: "))
print(get_factors(num))

#----------------------------------------------------------------

# Упражнение 4


# Делители 2

# Напишите функцию number_of_factors(num), принимающую в качестве аргумента число и возвращающую 
# количество делителей данного числа.

# Примечание 1. Используйте уже реализованную функцию get_factors(num) из предыдущей задачи.

def get_factors(num):

    count = 0

    for i in range(1, num + 1):

        if num % i == 0:

            count += 1

    return count

num = int(input("Enter your num: "))

print(get_factors(num))


#----------------------------------------------------------------

# Упражнение 5


# Найти всех

# Напомним, что строковый метод find('a') возвращает местоположение первого вхождения символа a в 
# строке. Проблема заключается в том, что данный метод не находит местоположение всех символов а.

# Напишите функцию с именем find_all(target, symbol), которая принимает два аргумента: строку 
# target и символ symbol и возвращает список, содержащий все местоположения этого символа в 
# строке.

# Примечание 1. Если указанный символ не встречается в строке, то следует вернуть пустой список.

def find_all(target, symbol):

    list_one = []

    for i in range(len(target)):

        if target[i] == symbol:

            list_one.append(i)

    return list_one


target = input()
symbol = input()

print(find_all(target, symbol))
#----------------------------------------------------------------

# Упражнение 6


# Merge lists 1

# Напишите функцию merge(list1, list2), которая принимает в качестве аргументов два 
# отсортированных по возрастанию списка, состоящих из целых чисел, и объединяет их в один 
# отсортированный список.

# Примечание 1. Можно использовать списочный метод sort(), а можно обойтись и без него. 😎

def merge(list1, list2):

    list3 = list1 + list2
    list3.sort()
    return list3



list1 = input().split()
for i in range(len(list1)):
    list1[i] = int(list1[i])

list2 = input().split()
for i in range(len(list2)):
    list2[i] = int(list2[i])

print(merge(list1, list2))
#----------------------------------------------------------------

# Упражнение 7

# Merge lists 2

# На вход программе подаются число n, а затем n строк, содержащих целые числа в порядке 
# возрастания. Из данных строк формируются списки чисел. Напишите программу, которая объединяет 
# указанные списки в один отсортированный список с помощью функции quick_merge(), а затем выводит 
# его.


def quick_merge(n):

    list_one = []
    list_two = []

    for i in range(1, n + 1):

        string = input()

        for i in string:
            list_one.append(i)

    list_two += list_one

    for i in range(len(list_two)):
        list_two[i] = int(list_two[i])

    list_two.sort()
    return list_two

n = int(input())

print(*quick_merge(n))


# 2-ой вариант


def quick_merge(list1, list2):
    result = []
    p1 = 0  # указатель на первый элемент списка list1
    p2 = 0  # указатель на первый элемент списка list2

    while p1 < len(list1) and p2 < len(list2):  # пока не закончился какой-нибудь из списков
        if list1[p1] <= list2[p2]:
            result.append(list1[p1])
            p1 += 1
        else:
            result.append(list2[p2])
            p2 += 1

    if p1 < len(list1):   # прицепление остатка
        result += list1[p1:]
    else:                 # иначе прицепляем остаток другого списка
        result += list2[p2:]
    
    return result


n = int(input())
total_list = []

for _ in range(n):
    num_list = [int(q) for q in input().split()]
    total_list = quick_merge(total_list, num_list)

print(*total_list)


# Основные изменения:

#   Переименовал параметры функции для ясности (total_list и num могут запутывать)
#   В цикле ввода сразу объединяем каждый новый список с аккумулированным результатом
#   Исправил название переменной в цикле ввода с num на num_list для ясности
#   Перенес инициализацию total_list перед циклом ввода
#   Теперь программа будет корректно объединять все введенные отсортированные списки в один отсортированный список.
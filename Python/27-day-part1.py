###########################################################
## День 27. Тема урока: функции с возвратом значения      #
###########################################################

## Функция с возвратом значения
#------------------------------

# Функция с возвратом значения похожа на функцию без возврата значения тем, что:

# это набор инструкций, выполняющий определенную задачу;
# когда нужно выполнить функцию, ее вызывают.


# Однако, когда функция с возвратом значения завершается, она возвращает значение в ту часть 
# программы, которая ее вызвала. Возвращаемое из функции значение используется как любое другое:
#  
# оно может быть присвоено переменной, 
# выведено на экран, 
# использовано в математическом выражении (если это число) и т. д.

#    !!!Функция с возвратом значения возвращает значение обратно в ту часть программы, 
#       которая ее вызвала.

# Мы уже сталкивались со многими функциями с возвратом значений:

#   функция int() – преобразует строку к целому числу и возвращает его;
#   функция float() – преобразует строку к вещественному числу и возвращает его;
#   функция range() – возвращает последовательность целых чисел 0, 1, 2, ...;
#   функция abs() – возвращает абсолютное значение числа (модуль числа);
#   функция len() – возвращает длину строки или списка.

# Функцию с возвратом значения пишут точно так же, как и без, но она должна иметь инструкцию 
# return.

# Вот общий формат определения функции с возвратом значения в Python:

# def название_функции():
#     блок кода
#     return выражение

# В функции должна быть инструкция return, принимающая форму:

# return выражение


# Значение выражения, которое следует за ключевым словом return, будет отправлено в ту часть 
# программы, которая вызвала функцию. Это может быть переменная либо выражение, к примеру, 
# математическое.

#  !!! Функция с возвратом значения имеет инструкцию return, возвращающую значение в ту часть 
#      программы, которая ее вызвала.


# При изучении вещественных чисел мы решали задачу о переводе градусов по шкале Фаренгейта в 
# градусы по шкале Цельсия по формуле


# Напишем функцию, которая осуществляет перевод: 

def convert_to_celsius(temp):
    result = (5 / 9) * (temp - 32)
    return result

# Задача этой функции — принять одно число temp в качестве аргумента – количество градусов по 
# шкале Фаренгейта, и вернуть другое — количество градусов по шкале Цельсия.


# Рассмотрим ее работу. 
# 
# Первая инструкция в блоке функции присваивает значение (5 / 9) * (temp - 32) переменной result. 
# Затем исполняется инструкция return, которая приводит к завершению исполнения функции и 
# отправляет значение из переменной result, назад в ту часть программы, которая вызвала эту функцию.

# функция перевода градусов Фаренгейта в градусы Цельсия
def convert_to_celsius(temp):
    result = (5 / 9) * (temp - 32)
    return result

# основная программа
temp = float(input('Bвeдитe количество градусов по Фаренгейту: '))
celsius = convert_to_celsius(temp)
print(celsius)  # градусы Цельсия

# Основная программа получает от пользователя одно число – значение в градусах Фаренгейта, и 
# вызывает функцию, передавая значение переменной temp в качестве аргумента. Значение, которое 
# возвращается из функции convert_to_celsius, присваивается переменной celsius. 


## Использование инструкции return по максимуму
#----------------------------------------------

# Взглянем еще раз на функцию convert_to_celsius():

def convert_to_celsius(temp):
    result = (5 / 9) * (temp - 32)
    return result

# Обратите внимание, что внутри этой функции происходят две вещи: во-первых, переменной result 
# присваивается значение выражения (5 / 9) * (temp - 32), и во-вторых, значение переменной 
# result возвращается из функции. Эта функция хорошо справляется с поставленной перед ней задачей, 
# но ее можно упростить. Поскольку инструкция return возвращает значение выражения, переменную 
# result устраняем и переписываем функцию так:

def convert_to_celsius(temp):
    return (5 / 9) * (temp - 32)

# Эта версия функции не сохраняет значение (5 / 9) * (temp - 32) в отдельной переменной, а сразу 
# возвращает значение выражения с помощью инструкции return. Делает то же, что и предыдущая версия, 
# но за один шаг.


## Использование нескольких return
#---------------------------------


# В одной функции может быть сколько угодно инструкций return. Рассмотрим функцию convert_grade(), 
# которая переводит стобалльную оценку в пятибалльную:

def convert_grade(grade):
    if grade >= 90:
        return 5
    elif grade >= 80:
        return 4
    elif grade >= 70: 
        return 3
    elif grade >= 60:
        return 2
    else:
        return 1

# основная программа
grade = int(input('Введите вашу отметку по 100-балльной системе: '))
print(convert_grade(grade))

# В функции convert_grade() используется 5 инструкций return. Каждая из них возвращает
# соответствующее значение и завершает работу функции.


# Функцию cxonvert_grade() можно переписать с помощью одной инструкции return:

def convert_grade(grade):
    if grade >= 90:
        result = 5
    elif grade >= 80:
        result = 4
    elif grade >= 70: 
        result = 3
    elif grade >= 60:
        result = 2
    else:
        result = 1
    
    return result


## Примечания
#------------

# Примечание 1. Функции с возвратом значения предоставляют те же преимущества, что функции без 
# возврата значения:

    # упрощают программный код;
    # уменьшают дублирование кода;
    # упрощают тестирование кода;
    # увеличивают скорость разработки;
    # способствуют работе в команде.


# Примечание 2. result – хорошее название для переменной, значение которой возвращается из функции.



## Слияние двух отсортированных списков
#--------------------------------------

# Слияние двух отсортированных списков в один — важная задача в информатике. Она естественно 
# возникает при сортировке списков с использованием сортировки слиянием.

# Пусть даны два отсортированных по возрастанию списка чисел list1 и list2:

list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]

# Простейшее решение задачи слияния списков использует списочный метод sort():

def merge(list1, list2):
    result = list1 + list2   # создаем результирующий список
    result.sort()            # сортируем список встроенным методом sort()
    return result            # возвращаем отсортированный список


list1 = [3, 10, 11, 12, 47, 57, 58, 63, 77, 79, 80, 95]
list2 = [0, 11, 12, 20, 24, 26, 47, 48, 53, 65, 70, 81, 84, 84, 90]
list3 = merge(list1, list2)  # вызываем функцию слияния двух отсортированных списков

print(list3)


# И хотя функция merge() полностью справляется со своей задачей, она абсолютно не учитывает то, 
# что два списка list1 и list2 уже отсортированы.


## Быстрое слияние двух отсортированных списков в один
#-----------------------------------------------------

# Пусть мы имеем два уже отсортированных по возрастанию списка list1 и list2.

# Алгоритм быстрого слияния следующий:
#-------------------------------------

#   Создаем численные указатели p1 = 0 и p2 = 0 на начала обоих списков list1 и list2 
# соответственно;

#   На каждом шаге берем меньший из двух элементов list1[p1] и list2[p2];

#   Записываем его в результирующий список;

#   Увеличиваем на 1 указатель на первый элемент списка (p1 или p2), из которого был взят элемент;

#   Когда один из начальных списков закончился, добавляем все оставшиеся элементы второго списка 
# в результирующий список.


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
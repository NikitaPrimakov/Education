###########################################################
## День 19. Тема урока: основы работы со списками         #
###########################################################


## Основы работы со списками
#---------------------------

# Работа со списками очень сильно напоминает работу со строками, поскольку и списки, и строки содержат 
# отдельные элементы. Однако элементы списка могут иметь произвольный тип, а элементами строк всегда 
# являются символы. Многое из того, что мы делали со строками, доступно и при работе со списками.

## Функция len()
#---------------

# Длиной списка называется количество его элементов. Для того чтобы посчитать длину списка, мы используем 
# встроенную функцию len() (от слова length – длина).

# Приведённый ниже код:

numbers = [2, 4, 6, 8, 10]
languages = ['Python', 'C#', 'C++', 'Java']

print(len(numbers))      # выводим длину списка numbers
print(len(languages))    # выводим длину списка languages

print(len(['apple', 'banana', 'cherry']))   # выводим длину списка, состоящего из 3 элементов

# выводит:

# 5
# 4
# 3

## Оператор принадлежности in
#----------------------------

# Оператор in позволяет проверить, содержит ли список некоторый элемент.

# Рассмотрим следующий код:

numbers = [2, 4, 6, 8, 10]

if 2 in numbers:
    print('Список numbers содержит число 2')
else:
    print('Список numbers не содержит число 2')

# Такой код проверяет, содержит ли список numbers число 2, и выводит соответствующий текст:

# Список numbers содержит число 2


# Мы можем использовать оператор in вместе с логическим оператором not. Например:

numbers = [2, 4, 6, 8, 10]

if 0 not in numbers:
    print('Список numbers не содержит нулей')

## Индексация
#-----------

# При работе со строками мы использовали индексацию, то есть обращение к конкретному символу строки по 
# его индексу. Аналогично, можно индексировать и списки.

# Для индексации списков в Python используются квадратные скобки [], в которых указывается индекс (номер) 
# нужного элемента в списке:

# Пусть numbers = [2, 4, 6, 8, 10].

# Таблица ниже показывает, как работает индексация:

# Выражение	    Результат	Пояснение
# numbers[0]	    2	    первый элемент списка
# numbers[1]	    4	    второй элемент списка
# numbers[2]	    6	    третий элемент списка
# numbers[3]	    8	    четвертый элемент списка
# numbers[4]	    10	    пятый элемент списка


## Срезы
#-------

# Рассмотрим список numbers = [2, 4, 6, 8, 10].

# С помощью среза мы можем получить несколько элементов списка, создав диапазон индексов, разделенных 
# двоеточием numbers[x:y].

# Приведённый ниже код:

print(numbers[1:3])
print(numbers[2:5])

# выводит:

# [4, 6]
# [6, 8, 10]

# При построении среза numbers[x:y] первое число – это то место, где начинается срез (включительно), 
# а второе – это место, где заканчивается срез (невключительно). Разрезая списки, мы создаем новые списки,
# по сути, подсписки исходного.

# При использовании срезов со списками мы также можем опускать второй параметр в срезе numbers[x:] 
# (но поставить двоеточие), тогда срез берется до конца списка. Аналогично если опустить первый параметр 
# numbers[:y], то можно взять срез от начала списка.

# Срез numbers[:] возвращает копию исходного списка.

# Как и в строках, мы можем использовать отрицательные индексы в срезах списков.


## Использование срезов для изменения элементов в заданном диапазоне
#-------------------------------------------------------------------

# Для изменения целого диапазона элементов списка можно использовать срезы. Например, если мы хотим 
# перевести на русский язык названия фруктов 'banana', 'cherry', 'kiwi', то это можно сделать с помощью 
# среза.

# Приведённый ниже код:

fruits = ['apple', 'apricot', 'banana', 'cherry', 'kiwi', 'lemon', 'mango']
fruits[2:5] = ['банан', 'вишня', 'киви']

print(fruits)

# выводит: ['apple', 'apricot', 'банан', 'вишня', 'киви', 'lemon', 'mango']

## Операция конкатенации + и умножения на число *
#------------------------------------------------

# Мы можем применять операторы + и * для списков подобно тому, как мы это делали со строками.

# Приведённый ниже код:

print([1, 2, 3, 4] + [5, 6, 7, 8])
print([7, 8] * 3)
print([0] * 10)
# выводит:

# [1, 2, 3, 4, 5, 6, 7, 8]
# [7, 8, 7, 8, 7, 8]
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# Для генерации списков, состоящих строго из повторяющихся элементов, умножение на число — самый короткий 
# и правильный метод.

# Мы также можем использовать расширенные операторы += и *= при работе со списками.

# Приведённый ниже код:

a = [1, 2, 3, 4]
b = [7, 8]
a += b   # добавляем к списку a список b
b *= 5   # повторяем список b 5 раз 

print(a)
print(b)

# выводит:

# [1, 2, 3, 4, 7, 8]
# [7, 8, 7, 8, 7, 8, 7, 8, 7, 8]


## Встроенные функции sum(), min(), max()
#----------------------------------------

# Встроенная функция sum() принимает в качестве параметра список чисел и вычисляет сумму его элементов.

# Приведённый ниже код:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print('Сумма всех элементов списка =', sum(numbers))
# выводит: Сумма всех элементов списка = 55


# Встроенные функции min() и max() принимают в качестве параметра список и находят минимальный и 
# максимальный элементы соответственно.

# Приведённый ниже код:

numbers = [3, 4, 10, 3333, 12, -7, -5, 4]
print('Минимальный элемент =', min(numbers))
print('Максимальный элемент =', max(numbers))

# выводит:

# Минимальный элемент = -7
# Максимальный элемент = 3333


## Отличие списков от строк
#--------------------------

# Несмотря на всю схожесть списков и строк, есть одно очень важное отличие: 
# строки — неизменяемые объекты, а списки – изменяемые.

# Приведённый ниже код:

s = 'abcdefg'
s[1] = 'x'    # пытаемся изменить 2 символ (по индексу 1) строки 

# приводит к возникновению ошибки:

# object does not support item assignment


# Приведённый ниже код:

numbers = [1, 2, 3, 4, 5, 6, 7]
numbers[1] = 101     # изменяем 2 элемент (по индексу 1) списка
print(numbers)
# выводит:

# [1, 101, 3, 4, 5, 6, 7]


#Запомни: изменять отдельные символы строк нельзя, однако можно изменять отдельные элементы списков. 
# Для этого используем индексатор и оператор присваивания.


##                                  Таблица "методы списков"
#----------------------------------------------------------------------------------------------------

# Метод                             Что делает

# list.append(x)                    Добавляет элемент в конец списка

# list.extend(L)                    Расширяет список list, добавляя в конец все элементы списка L

# list.insert(i, x)                 Вставляет на i-ый элемент значение x

# list.remove(x)                    Удаляет первый элемент в списке, имеющий значение x. ValueError, если 
#                                   такого элемента не существует

# list.pop([i])                     Удаляет i-ый элемент и возвращает его. Если индекс не указан, 
#                                   удаляется последний элемент

# list.index(x, [start [, end]])    Возвращает положение первого элемента со значением x (при этом поиск 
#                                   ведется от start до end)

# list.count(x)                     Возвращает количество элементов со значением x

# list.sort([key=функция])          Сортирует список на основе функции

# list.reverse()                    Разворачивает список

# list.copy()                       Поверхностная копия списка

# list.clear()                      Очищает список
#----------------------------------------------------------------------------------------------------
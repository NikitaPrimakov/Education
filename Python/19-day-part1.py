###############################################
## День 19. Тема урока: введение в списки     #
###############################################

## Списки
#--------


# В предыдущих уроках мы работали с последовательностями чисел, символов, строк, но не сохраняли всю 
# последовательность в памяти компьютера, а обрабатывали ее поэлементно, считывая раз за разом новый 
# элемент. Однако во многих задачах требуется сохранять всю последовательность. Например, классическая 
# задача сортировки (упорядочения) некоторой последовательности требует сохранения всех данных в памяти 
# компьютера. Увы, не сохранив, их невозможно отсортировать. И тут на помощь приходит структура данных, 
# которая в большинстве языков программирования называется массивом. В Python она называется списком.

# Структура данных (data structure) — программная единица, позволяющая хранить и обрабатывать множество 
# однотипных и/или логически связанных данных.

# Список представляет собой последовательность элементов, пронумерованных от 0, как символы в строке.

## Создание списка
#-----------------

# Чтобы создать список, нужно перечислить его элементы через запятую в квадратных скобках:

numbers = [2, 4, 6, 8, 10]
languages = ['Python', 'C#', 'C++', 'Java']
# Список numbers состоит из 5 элементов, и каждый из них — целое число.

# numbers[0] == 2;
# numbers[1] == 4;
# numbers[2] == 6;
# numbers[3] == 8;
# numbers[4] == 10.

# Список languages состоит из 4 элементов, каждый из которых — строка.

# languages[0] == 'Python';
# languages[1] == 'C#';
# languages[2] == 'C++';
# languages[3] == 'Java'.
# 
# Значения, заключенные в квадратные скобки и отделенные запятыми, называются элементами списка.

# Список может содержать значения разных типов данных:

# info = ['Timur', 1992, 61.5]

# Список info содержит строковое значение, целое число и число с плавающей точкой.

# info[0] == 'Timur';
# info[1] == 1992;
# info[2] == 61.5.

# Обычно элементы списка содержат данные одного типа, и на практике редко приходится создавать списки, 
# содержащие элементы разных типов данных.


## Пустой список
#---------------

# Создать пустой список можно двумя способами:

#   1) Использовать пустые квадратные скобки [];
#   2) Использовать встроенную функцию, которая называется list.

# Следующие две строки кода создают пустой список:

mylist = []  # пустой список
mylist = list()  # тоже пустой список


## Вывод списка
#--------------

# Для вывода всего списка можно применить функцию print():

numbers = [2, 4, 6, 8, 10]
languages = ['Python', 'C#', 'C++', 'Java']
print(numbers)
print(languages)

# Функция print() выводит на экран элементы списка, в квадратных скобках, разделенные запятыми:

# [2, 4, 6, 8, 10]
# ['Python', 'C#', 'C++', 'Java']


# Обратите внимание, что вывод списка содержит квадратные скобки. Позже мы научимся выводить элементы 
# списка в более удобном виде с помощью циклов или с помощью распаковки.


## Встроенная функция list
#-------------------------

# Python имеет встроенную функцию list(), которая помимо создания пустого списка может преобразовывать 
# некоторые типы объектов в списки.

# Например, мы знаем, что функция range() создает последовательность целых чисел в заданном диапазоне. Для преобразования этой последовательности в список, мы пишем следующий код:

numbers = list(range(5))

# Во время исполнения этого кода происходит следующее:

# 1) Вызывается функция range(), в которую в качестве аргумента передается число 5;
# 2) Эта функция возвращает последовательность чисел 0, 1, 2, 3, 4;
# 3) Последовательность чисел 0, 1, 2, 3, 4 передается в качестве аргумента в функцию list();
# 4) Функция list() возвращает список [0, 1, 2, 3, 4];
# Список [0, 1, 2, 3, 4] присваивается переменной numbers.


# Вот еще один пример:

# even_numbers = list(range(0, 10, 2))  # список содержит четные числа 0, 2, 4, 6, 8
# odd_numbers = list(range(1, 10, 2))  # список содержит нечетные числа 1, 3, 5, 7, 9
# Точно так же с помощью функции list() мы можем создать список из символов строки. Для преобразования 
# строки в список мы пишем следующий код:

s = 'abcde'
chars = list(s)  # список содержит символы 'a', 'b', 'c', 'd', 'e'

# Во время исполнения этого кода происходит следующее:

# 1) Вызывается функция list(), в которую в качестве аргумента передается строка 'abcde';
# 2) Функция list() возвращает список ['a', 'b', 'c', 'd', 'e'];
# 3) Список ['a', 'b', 'c', 'd', 'e'] присваивается переменной chars.

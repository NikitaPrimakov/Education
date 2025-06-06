########################################################################
## День 19. Тема урока: методы добавления и удаления элементов         #
########################################################################

## Добавление элементов
#----------------------

# Мы научились создавать статические списки, то есть списки, элементы которых известны на этапе создания. 
# Следующий шаг – научиться добавлять элементы в уже существующие списки.


## Метод append()
#----------------

# Для добавления нового элемента в конец списка используется метод append().

# Приведённый ниже код:

numbers = [1, 1, 2, 3, 5, 8, 13]  # создаем список

numbers.append(21)  # добавляем число 21 в конец списка
numbers.append(34)  # добавляем число 34 в конец списка

print(numbers)

# выводит: [1, 1, 2, 3, 5, 8, 13, 21, 34]

# Обратите внимание, для того чтобы использовать метод append(), нужно, чтобы список был создан 
# (при этом он может быть пустым).

# Приведённый ниже код:

numbers = []  # создаем пустой список

numbers.append(1)
numbers.append(2)
numbers.append(3)

print(numbers)

# выводит: [1, 2, 3]

# Важно: мы не можем использовать индексаторы для установки значений элементов списка, если список 
#        пустой.

# Приведённый ниже код:

numbers = []  # создаем пустой список

numbers[0] = 1
numbers[1] = 2
numbers[2] = 3

print(numbers)

# приводит к возникновению ошибки:

# IndexError: list assignment index out of range


## Метод extend()
#---------------

# Можно также расширить список другим списком путём вызова метода extend().

# Приведённый ниже код:

numbers = [0, 2, 4, 6, 8, 10]
odds = [1, 3, 5, 7]

numbers.extend(odds)
print(numbers)

# выводит: [0, 2, 4, 6, 8, 10, 1, 3, 5, 7]

# Метод extend() как бы расширяет один список, добавляя к нему элементы другого списка.

# Отличие между методами append() и extend() проявляется при добавлении строки к списку.

# Приведённый ниже код:

words1 = ['iq option', 'stepik', 'beegeek']
words2 = ['iq option', 'stepik', 'beegeek']

words1.append('python')
words2.extend('python')

print(words1)
print(words2)

# выводит:

# ['iq option', 'stepik', 'beegeek', 'python']
# ['iq option', 'stepik', 'beegeek', 'p', 'y', 't', 'h', 'o', 'n']

# Метод append() добавляет строку 'python' целиком к списку, а метод extend() разбивает строку 'python' 
# на символы 'p', 'y', 't', 'h', 'o', 'n' и их добавляет в качестве элементов списка.


## Удаление элементов
#--------------------

# С помощью оператора del можно удалять элементы списка по определенному индексу.

# Приведённый ниже код:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[5]    # удаляем элемент, имеющий индекс 5

print(numbers)
# выводит: [1, 2, 3, 4, 5, 7, 8, 9]

# Элемент под указанным индексом удаляется, а список перестраивается.

# Обратите внимание на синтаксис удаления, так как он отличается от обычного вызова метода. При удалении 
# элементов не надо передавать аргумент внутри круглых скобок.

# Оператор del работает и со срезами: мы можем удалить целый диапазон элементов списка.

# Приведённый ниже код:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[2:7]    # удаляем элементы с 2 по 6 включительно

print(numbers)
# выводит: [1, 2, 8, 9]

# Мы можем удалить все элементы на чётных позициях (0, 2, 4, ...) исходного списка.

# Приведённый ниже код:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del numbers[::2]

print(numbers)
# выводит: [2, 4, 6, 8]
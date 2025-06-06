###########################################################
## День 21. Тема урока: строковые методы                  #
###########################################################

# В предыдущем модуле мы детально изучили основные строковые методы, однако обошли стороной два важных: 
# split() и join(), имеющих отношение к спискам. Они как бы противоположны по смыслу: метод split() 
# разбивает строку по произвольному разделителю на список слов, а метод join() собирает строку из списка 
# слов через заданный разделитель.

## Метод split()
#---------------

# Метод split() разбивает строку на слова, используя в качестве разделителя последовательность пробельных 
# символов, и возвращает список из этих слов.

# Приведённый ниже код:

s = 'Python is the most powerful language'
words = s.split()
print(words)

# выводит: ['Python', 'is', 'the', 'most', 'powerful', 'language']



# Таким образом, вызов метода split() разбивает строку на слова и возвращает список, содержащий все слова.

# Рассмотрим следующий программный код:

numbers = input().split()

# Если при запуске этой программы ввести строку 1 2 3 4 5, то список numbers будет следующим
# ['1', '2', '3', '4', '5']. Обратите внимание, что список будет состоять из строк (тип str),
# а не из чисел (тип int). Если требуется получить именно список чисел, то затем нужно элементы списка по 
# одному преобразовать в числа с помощью команды int().


# Приведённый ниже код:

numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
print(numbers)

# выводит (если на вход программе была подана строка 1 2 3 4 5): [1, 2, 3, 4, 5]


## Необязательный параметр
#-------------------------

# У метода split() есть необязательный параметр, который определяет, какой набор символов будет 
# использоваться в качестве разделителя между элементами списка. Например, вызов метода split('.') вернёт 
# список, полученный разделением исходной строки по символу '.'.

# Приведённый ниже код:

ip = '192.168.1.24'
numbers = ip.split('.')    # указываем явно разделитель
print(numbers)
# выводит: ['192', '168', '1', '24']



## Метод join()
#--------------


# Метод join() собирает строку из элементов списка, используя в качестве разделителя строку, к которой 
# применяется метод.

# Приведённый ниже код:

words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
s = ' '.join(words)
print(s)
# выводит: Python is the most powerful language

# Обратите внимание: все слова разделены одним пробелом, поскольку метод join() вызывался на строке, состоящей из одного символа пробела  .

# Рассмотрим ещё пару примеров:

words = ['Мы', 'учим', 'язык', 'Python']
print('*'.join(words))
print('-'.join(words))
print('?'.join(words))
print('!'.join(words))
print('*****'.join(words))
print('abc'.join(words))
print('123'.join(words))

# Приведённый выше код выводит:

# Мы*учим*язык*Python
# Мы-учим-язык-Python
# Мы?учим?язык?Python
# Мы!учим!язык!Python
# Мы*****учим*****язык*****Python
# МыabcучимabcязыкabcPython


## Запомни: строковый метод split() служит для преобразования строки в список, 
# а метод join() — для преобразования списка в строку.


## Примечания
#------------

# Примечание 1. Существует большая разница между результатами вызова методов s.split() и s.split(' '). 
# Разница в поведении проявляется, когда строка содержит несколько пробелов между словами.

# Приведённый ниже код:

s = 'I love  Python'
words1 = s.split()
words2 = s.split(' ')
print(words1)
print(words2)
#  выводит:

# ['I', 'love', 'Python']
# ['I', 'love', '', 'Python']


# Если в строке встречаются последовательные разделители, то они будут считаться как отдельные разделители, 
# и между ними будет создана пустая строка ('').


# Примечание 2. Методы split() и join() являются строковыми методами, они не могут применяться к спискам!

# Приведённый ниже код:

print([1, 2].split())
# приводит к возникновению ошибки:

# AttributeError: 'list' object has no attribute 'split'


# Примечание 3. Строковый метод join() не работает для списков, у которых элементы не строкового типа данных.

# Приведённый ниже код:

numbers = [1, 2, 3, 4]  # список чисел
s = '*'.join(numbers)
print(s)
# приводит к возникновению ошибки: TypeError: sequence item 0: expected str instance, int found


# Примечание 4. На самом деле, метод join() в качестве аргумента может принимать не только список, но и 
# строку.

# Приведённый ниже код:

s = '+'.join('pygen')
print(s)
# выводит: p+y+g+e+n
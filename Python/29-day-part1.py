###########################################################
## День 29. Тема урока: модуль random                     #
###########################################################


## Случайные числа
#-----------------

# Случайные числа широко используются в различных задачах программирования:

    # 1) случайные числа используются в играх. Например, компьютерным играм, которые позволяют игроку подбрасывать
    # игральный кубик, нужны случайные числа для представления значений кубика. Программы, которые раскрывают игральные 
    # карты, вынимаемые из перетасованной колоды, используют случайные числа для представления достоинства карт;

    # 2) случайные числа применяются в программах имитационного моделирования. В некоторых симуляциях компьютер должен 
    # случайным образом решить, как будет вести себя человек, животное, насекомое или другое живое существо. Нередко 
    # конструируются формулы, где случайное число используется для определения различных вариантов действий и событий, 
    # происходящих в программе;

    # 3) случайные числа распространены в статистических программах, случайным образом отбирающих данные для анализа;

    # 4) случайные числа используются в компьютерной безопасности для шифрования уязвимых данных.

# Python предлагает встроенные функции для работы со случайными числами. Эти функции хранятся в модуле random в 
# стандартной библиотеке.


## Модуль random
#---------------

# Модуль random предоставляет функции для генерации случайных чисел, букв и случайного выбора элементов 
# последовательности (списка, строки и т.д.).

# Для использования этих функций в начале программы необходимо подключить модуль, что делается командой import:

import random

# После подключения модуля мы можем использовать его функции.

## Функция randint()
#-------------------

# Функция randint() принимает два обязательных аргумента a и b и возвращает случайное целое число из отрезка [a;b].

# Следующий код выводит два случайных целых числа: num1 из отрезка [0; 17] и num2 из отрезка [-5; 5] .

import random

num1 = random.randint(0, 17)
num2 = random.randint(-5, 5)

print(num1)
print(num2)

# !!Важно: левая и правая граница a и b включаются в диапазон генерируемых случайных чисел. Результатом вызова функции 
# random.randint(2, 9) может быть любое число от 2 до 9 включительно.


# Следующий код выводит 10 случайных целых чисел из диапазона [1;100]:

import random

for _ in range(10):
    print(random.randint(1, 100))


# Среди этих чисел возможны повторения, поскольку каждый раз выбирается случайное.


## Функция randrange()
#---------------------

# Если вы помните, как применять функцию range(), то почувствуете себя непринужденно с функцией randrange(). Функция 
# randrange() принимает такие же аргументы, что и функция range(). Различие состоит в том, что функция randrange() 
# не возвращает саму последовательность чисел. Вместо этого она возвращает случайно выбранное число из 
# последовательности чисел.

# Следующий код присваивает переменной num случайное число в диапазоне от 0 до 9:

import random

num = random.randrange(10)
# Аргумент 10 задает конечный предел последовательности значений. Функция возвратит случайно выбранное число из 
# последовательности чисел от 0 до конечного предела, исключая сам предел.

# Следующий код задает начальное значение и конечный предел последовательности:

import random

num = random.randrange(5, 10)

# Таким образом в переменной num будет храниться случайное число в диапазоне от 5 до 9.

# Следующий код задает начальное значение, конечный предел и величину шага:

import random

num = random.randrange(0, 101, 10)

# Таким образом в переменной num будет храниться случайное число из последовательности чисел: 
# 0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100.


## Функция random()
#-----------------

# Функции randint() и randrange() возвращают случайное целое число. А вот функция random() возвращает случайное число с 
# плавающей точкой (вещественное число). В функцию random() никаких аргументов не передается. Функция random() 
# возвращает случайное число с плавающей точкой в диапазоне от 0.0 до 1.0 (исключая 1.0).

# Следующий код выводит случайное число с плавающей точкой из диапазона [0.0;1.0):

import random

num = random.random()
print(num)

## Функция uniform()

# Функция uniform() тоже возвращает случайное число с плавающей точкой, но при этом она позволяет задавать диапазон для 
# отбора значений.

# Следующий код выводит случайное число с плавающей точкой из диапазона [1.5;17.3]:

import random

num = random.uniform(1.5, 17.3)
print(num)


## Начальные значения случайного числа
#-------------------------------------
# Числа, генерируемые функциями модуля random, не являются подлинно случайными. Несмотря на то, что обычно их называют 
# случайными числами, это псевдослучайные числа, вычисляемые на основе формулы. Формула, генерирующая случайные числа, 
# должна быть инициализирована начальным значением. Оно используется в вычислении, возвращающем следующее случайное 
# число в ряду. Когда модуль random импортируется, он получает системное время из внутреннего генератора тактовых 
# импульсов компьютера и использует его как начальное значение. Системное время - целое число, представляющее 
# текущую дату и время вплоть до одной сотой секунды. Если бы всегда использовалось одно и то же начальное значение, 
# функции генерации случайных чисел всегда  возвращали бы один и тот же ряд псевдослучайных чисел. 
# Поскольку системное время меняется каждую сотую долю секунды, можно без опасений утверждать, что всякий раз, когда 
# импортируется модуль random, будет сгенерирована отличающаяся от предыдущих последовательность случайных чисел.

# Вместе с тем, могут иметься некоторые программы, где требуется всегда генерировать одну и ту же последовательность 
# случайных чисел. При необходимости для этого можно вызвать функцию seed(), задав начальное значение.

# Следующий код генерирует 10 случайных чисел, и при этом содержит инструкцию, явно устанавливающую начальное значение 
# для генератора случайных чисел:

import random

random.seed(17)   # явно устанавливаем начальное значение для генератора случайных чисел

for _ in range(10):
    print(random.randint(1, 100))

# Результатом выполнения такого кода может быть:

# 67
# 54
# 39
# 47
# 38
# 23
# 99
# 91
# 91
# 70

# Если выполнить такой код еще раз, то мы получим ту же самую последовательность псевдослучайных чисел.


## Задача 2. В интервью с профессором Тимуром вы выясняете, что он хотел бы использовать программу для имитации нескольких поочередных бросаний кубика.

# Решение. Будем использовать цикл while, который имитирует один бросок кубиков и затем спрашивает пользователя,
# следует ли сделать еще один бросок. Цикл будет повторяться до тех пор, пока пользователь отвечает "да", 
# набирая букву "д":

import random

again = 'д'
while again.lower() == 'д':
    print('Бросаем кубики... ')
    print('Значения граней:')
    print(random.randint(1, 6))
    print(random.randint(1, 6))
    again = input('Бросить кубики еще раз? (д = да, н = нет): ')


# Задача 3. Профессор Тимур был так доволен написанным вами симулятором бросания кубиков, что попросил вас разработать 
# еще одну программу. Он хотел бы иметь симулятор десятикратного поочередного подбрасывания монеты. Всякий раз, когда 
# программа имитирует подбрасывание монеты, она должна случайным образом показывать "орла" или "решку".
import random

for i in range(10):
    up = random.randint(1,3)
    if up == 1:
        print("решка")
    else:
        print("орел")
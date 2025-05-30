###########################################################
## День 25. Тема урока: функции с параметрами             #
###########################################################


## Функции с параметрами
#-----------------------

# В предыдущем уроке мы определили функцию draw_box(), которая выводит звездный прямоугольник с 
# размерами 5×7:

def draw_box():
    for i in range(5):
        print('*' * 7)

# Было бы намного удобнее, если бы функция draw_box() выводила прямоугольник с произвольными 
# размерами. И действительно, функции могут принимать входные параметры, что делает их более 
# гибкими.

# Функции с параметрами объявляются так же как функции без параметров, только с указанием в 
# скобках:

# def название_функции(параметры):
#     блок кода


# Давайте перепишем предыдущую версию функции draw_box() так, чтобы она принимала параметры, 
# задающие высоту и ширину прямоугольника:

def draw_box(height, width):    # функция принимает два параметра
    for i in range(height):
        print('*' * width)

# Теперь наша функция draw_box() принимает два целочисленных параметра height – высота 
# прямоугольника и width – ширина прямоугольника, и для ее вызова нам нужно обязательно их 
# указать.

# Чтобы вывести звездный прямоугольник размерами 5 на 7 мы пишем код:

draw_box(5, 7)


# Результатом такого вызова функции draw_box(5, 7) будет:

# *******
# *******
# *******
# *******
# *******


# Чтобы вывести прямоугольник размерами 10 на 15, мы пишем код:

# draw_box(10, 15)

# Результатом такого вызова функции draw_box(10, 15) будет:

# ***************
# ***************
# ***************
# ***************
# ***************
# ***************
# ***************
# ***************
# ***************
# ***************

# Теперь с помощью нашей новой версии функции draw_box() можем в одной программе выводить 
# прямоугольники разных размеров.

# Приведённый ниже код:

# draw_box(3, 3)
# print()
# draw_box(5, 5)
# print()
# draw_box(4, 10)
# выводит:

# ***
# ***
# ***

# *****
# *****
# *****
# *****
# *****

# **********
# **********
# **********
# **********


# На место параметров мы можем подставлять не только целочисленные константы, но и значения 
# переменных.

# Приведённый ниже код:

# n = 3
# m = 9
# draw_box(n, m)

# выводит:

# *********
# *********
# *********


## Параметры VS аргументы
#------------------------


# Аргумент – это любая порция данных, которая передается в функцию, когда функция вызывается. 
# Параметр – это переменная, которая получает аргумент, переданный в функцию.

# Для функции draw_box(height, width):

# ​def draw_box(height, width):
#     for i in range(height):
#         print('*' * width)

# параметрами являются переменные height и width.

# В момент вызова функции draw_box(height, width):

# height = 10
# draw_box(height, 9)
# аргументами являются height и 9.

## Параметры функций часто называют параметрическими переменными.


## Внесение изменений в параметры
#--------------------------------

# Когда аргумент передается в функцию, параметрическая переменная функции будет ссылаться на 
# значение этого аргумента. Однако любые изменения, которые вносятся в параметрическую 
# переменную, не будут влиять на аргумент.

# Приведённый ниже код:

def draw_box(height, width):
    height = 2
    width = 10
    for i in range(height):
        print('*' * width)

n = 5
m = 7
draw_box(n, m)
print(n, m)

# выводит:

# **********
# **********
# 5 7

# В теле функции вносятся изменения в значения параметрических переменных height и width, 
# однако это никак не повлияло на значение переменных n и m из основной программы, которые 
# передавались в качестве аргументов в функцию draw_box().


#№  Примечание

# Примечание 1. Функции в Python могут принимать сколько угодно параметров.

# Примечание 2. Иногда вместо параметров и аргументов говорят о формальных параметрах и 
# фактических параметрах. Формальные параметры – переменные, которые мы пишем при описании 
# функции. Фактические параметры – то, что реально подставляется при вызове функции.
# Упражнение 6

# Змеиный регистр 🐍
# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в 
# «верблюжьем регистре» и преобразует его в «змеиный регистр».

# Примечание 1. Почитать подробнее о стилях именования можно по ссылке.

# Примечание 2. Приведённый ниже код:

# print(convert_to_python_case('ThisIsCamelCased'))
# print(convert_to_python_case('IsPrimeNumber'))


text = input()

list_one = []

for i in range(len(text)):

    if text[i].islower():
        list_one.append(text[i])

print(list_one)
# Упражнение 1

# Is the Triangle Valid?

# Напишите функцию is_valid_triangle(side1, side2, side3), которая принимает в качестве аргументов 
# три натуральных числа, и возвращает значение True, если существует невырожденный треугольник со 
# сторонами side1, side2, side3, или False в противном случае.

# Примечание 1. С данной задачей мы уже сталкивались при изучении условного оператора.


def is_valid_triangle(side1, side2, side3):

    if (side1 + side2) > side3 and (side1+side3) > side2 and (side2+side3) > side1:
        return True

    else: 
        return False
    

side1 = int(input())
side2 = int(input())
side3 = int(input())

print(is_valid_triangle(side1, side2, side3))

#----------------------------------------------------------------

# Упражнение 2


# Is the Number Prime? 🌶️

# Напишите функцию is_prime(num), которая принимает в качестве аргумента натуральное число и 
# возвращает значение True, если число является простым, или False в противном случае.


def is_prime(num):

    count = 0
    
    if num == 1:
        return False
    
    if num > 1:
        for i in range(1, num + 1):
            if num % i == 0:
                count += 1
    
    if count == 2:
        return True
    else:
        return False

            

num = int(input())
print(is_prime(num))
#----------------------------------------------------------------

# Упражнение 3

# Next Prime 🌶️🌶️

# Напишите функцию get_next_prime(num), которая принимает в качестве аргумента натуральное число 
# num и возвращает первое простое число, большее числа num.
def is_prime(num):
    if num == 1:
        return False
    if num > 1:
        for i in range(2, num): # делится ли число кроме 1 и себя
            if num % i == 0:
                return False
        return True # функция, которая высчитывает, является ли число простым или нет
    

def get_next_prime(num):

    next_num = num + 1

    while num > 0:
        
        if is_prime(next_num):
            return next_num
        else:
            next_num += 1
            continue
    

num = int(input())
print(get_next_prime(num))
#----------------------------------------------------------------

# Упражнение 3

# Напишите функцию is_password_good(password), которая принимает в качестве аргумента строковое 
# значение пароля password и возвращает значение True, если пароль является надёжным, или False в 
# противном случае.

# Пароль является надёжным, если:

    # его длина не менее 8 символов; 
    # он содержит как минимум одну заглавную букву (верхний регистр); 
    # он содержит как минимум одну строчную букву (нижний регистр);
    # он содержит хотя бы одну цифру.

def is_password_good(password):
    if len(password) < 8:
        return False
    
    has_upper = False
    has_lower = False
    has_digit = False
    
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
    
    return has_upper and has_lower and has_digit


password = input()
print(is_password_good(password))
#----------------------------------------------------------------

# Упражнение 4

# Ровно в одном 1️⃣

# Напишите функцию is_one_away(word1, word2), которая принимает в качестве аргументов два слова 
# word1 и word2. Функция должна возвращать значение True, если слова имеют одинаковую длину и 
# отличаются одним символом на одной и той же позиции, или False в противном случае.


def is_one_away(word1, word2):

    count = 0

    if len(word1) == len(word2):
        for i in range(len(word1)):
            if word1[i] == word2[i]:
                count += 1
            
        if count == len(word1) - 1:
            return True
        else:
            return False
    else:
        return False
    
word1 = input()
word2 = input()
print(is_one_away(word1, word2))
#----------------------------------------------------------------

# Упражнение 4


# Палиндром 🌶️

# Напишите функцию is_palindrome(text), которая принимает в качестве аргумента строку text и 
# возвращает значение True, если указанный текст является палиндромом, или False в противном 
# случае.


def is_palindrome(text):

    list_one = []

    for i in range(len(text)):

        text_lower = text.lower()

        if text_lower[i].isalpha():
            list_one.append(text_lower[i])

    if list_one == list_one[-1::-1]:
        return True
    else:
        return False

text = input()
print(is_palindrome(text))
#----------------------------------------------------------------

# Упражнение 5

# BEEGEEK 🐝🌶️

# BEEGEEK наконец-то открыл свой банк, в котором используются специальные банкоматы с необычным 
# паролем.

# Действительный пароль BEEGEEK банка имеет вид a:b:c, где a, b и c – натуральные числа. Поскольку 
# основатель BEEGEEK фанатеет от математики, то он решил:

    # число a – должно быть палиндромом;
    # число b – должно быть простым;
    # число c – должно быть чётным.

# Напишите функцию is_valid_password(password), которая принимает в качестве аргумента строковое 
# значение пароля password и возвращает значение True, если пароль является действительным паролем 
# BEEGEEK банка, или False в противном случае.

def is_valid_password(password):

    if password.count(':') > 2:
        return False
    else:
        password_new = password.split(':')
        a = password_new[0]
        b = password_new[1]
        c = password_new[2]

        if a == a[-1::-1] and int(c) % 2 == 0:
            if int(b) == 1:
                return False
            for i in range(2, int(b)):
                if int(b) % i == 0 and int(b):
                    return False
            return True
        else:
            return False
            
password = input()
print(is_valid_password(password))
#----------------------------------------------------------------

# Упражнение 6


# Правильная скобочная последовательность 🌶️

# Напишите функцию is_correct_bracket(text), которая принимает в качестве аргумента непустую 
# строку text, состоящую из символов ( и ) и возвращает значение True, если поступившая на вход 
# строка является правильной скобочной последовательностью, или False в противном случае.

# Примечание 1. Правильной скобочной последовательностью называется строка, состоящая только из 
# символов ( и ), где каждой открывающей скобке найдётся парная закрывающая скобка (при этом 
# каждая открывающая скобка должна быть левее соответствующей ей закрывающей скобки).

def is_correct_bracket(text):
    count = 0
    
    for i in range(len(text)):
        if text[i] == '(':
            count += 1
        elif text[i] == ')':
            count -= 1
            if count < 0:
                return False

    if count == 0:
        return True
    else:
        return False

text = input()
#----------------------------------------------------------------

# Упражнение 6

# Змеиный регистр 🐍
# Напишите функцию convert_to_python_case(text), которая принимает в качестве аргумента строку в 
# «верблюжьем регистре» и преобразует его в «змеиный регистр».

# Примечание 1. Почитать подробнее о стилях именования можно по ссылке.

# Примечание 2. Приведённый ниже код:

# print(convert_to_python_case('ThisIsCamelCased'))
# print(convert_to_python_case('IsPrimeNumber'))


def convert_to_python_case(text):
    
    string_new = ''
    string_new += text[0].lower()

    for i in range(0, len(text)):

        if text[i].isupper() and i != 0:
            string_new += '_' + text[i].lower()

        if text[i].islower():
            string_new += text[i]
    
        if text[i] in '0123456789':
            string_new += text[i]

    return string_new


text = input()
print(convert_to_python_case(text))



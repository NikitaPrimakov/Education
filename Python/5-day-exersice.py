#####################################################
## День 5. Решение задач                            #
#####################################################

# Задача 1

#  Площадь треугольнака
# Напишите программу, которая считывает длины двух катетов в прямоугольном треугольнике и выводит его площадь.

a = float(input("Введите длину катета a: "))
b = float(input("Введите длину катета b: "))

square  = (1/2) * a * b
print("Площадь прямоугольного треугольника равна:", square)


# Задача 2

# Две старушки идут навстречу друг другу с постоянными скоростями V1 1​  и V2 2​  км/ч. Определите, через какое время (в часах) 
# старушки встретятся, если расстояние между ними равно S км.

# На вход программе подаются три действительных числа S,V1,V2​ каждое на отдельной строке.

S = float(input("Введите расстояние: "))
V_1 = float(input("Скорость первой бабушки: "))
V_2 = float(input("Скорость второй бабушки: "))

t = S / (V_1 + V_2)
print(t)

# Задача 3

# Напишите программу, которая считывает с клавиатуры одно число и выводит обратное ему. 
# Если при этом введённое с клавиатуры число – ноль, то вывести «Обратного числа не существует» (без кавычек).

num = float(input("Введите число: "))

if num > 0 or num < 0:
    num = 1/(num**1)
    print(num)
else:
    print("Обратного числа не существует")
    
    
# Задача 4

# У известного американского писателя Рэя Бредбери есть роман «451 градус по Фаренгейту». Напишите программу, 
# которая определяет, какой температуре по шкале Цельсия соответствует указанное значение по шкале Фаренгейта.

# Для получения градусов по Цельсию из градусов по Фаренгейту используйте следующую формулу:
# t_c = 5/9 * (t_f - 32)

# где t_f – температура в градусах по Фаренгейту.

t_f = float(input("Введите температуру в градусах по Фаренгейту: "))

t_c = (5/9) * (t_f - 32)

print(t_c)

# Задача 5

# На вход программе подаётся число n – количество собачьих лет. Напишите программу, которая вычисляет возраст собаки в 
# человеческих годах по следующему алгоритму: в течение первых двух лет собачий год равен 10.5 человеческим годам, 
# после этого каждый год собаки равен 4 человеческим годам.

ageOfDog = float(input("Введите возраст собаки: "))

if ageOfDog >= 2:
    ageOfDog_1 = ageOfDog - (ageOfDog - 1)
    ageOfDog_2 = ageOfDog - (ageOfDog - 2)
    ageOFDog_for2year = ageOfDog_2 * 10.5 # за первые два года
    ageOFDog_other = (ageOfDog - 2) * 4   # стальные годы
    ageOfDog_final = ageOFDog_for2year + ageOFDog_other
    print(ageOfDog_final)
elif 1 <= ageOfDog < 2:
    ageOfDog_1 = ageOfDog - (ageOfDog - 1)
    ageOFDog_for1year = ageOfDog_1 * 10.5
    print(ageOFDog_for1year)
    

# Альтернатива

age = int(input())
if 0 < age <= 2:
    print(age * 10.5)
else:
    print(2 * 10.5 + (age - 2) * 4)
    

# Задача 6

# Дано положительное действительное число. Выведите его первую цифру после десятичной точки.

num = float(input("Введите число: "))

print(int(num * 10 % 10))


# Задача 7

# Дано положительное действительное число. Выведите его дробную часть.

a = float(input("Введите число: "))

print(a - int(a))

# задача 8

# Напишите программу, которая находит наименьшее и наибольшее из пяти чисел и выводит текст в следующем формате:

# Наименьшее число = <наименьшее число>
# Наибольшее число = <наибольшее число>

firstNum, secondNum, thirdNum, fourthNum, fifthNum = int(input()), int(input()), int(input()), int(input()), int(input())
print("Наименьшее число =", min(firstNum, secondNum, thirdNum, fourthNum, fifthNum))
print("Наибольшее число =", max(firstNum, secondNum, thirdNum, fourthNum, fifthNum))

# Задача 9

# Напишите программу, которая упорядочивает три числа от большего к меньшему.
firstNum, secondNum, thirdNum = int(input()), int(input()), int(input())

if min(firstNum, secondNum, thirdNum) == firstNum and max(firstNum, secondNum, thirdNum) == thirdNum:
    print(thirdNum, secondNum, firstNum, sep='\n')
elif min(firstNum, secondNum, thirdNum) == firstNum and max(firstNum, secondNum, thirdNum) == secondNum:
    print(secondNum, thirdNum, firstNum, sep='\n')
elif min(firstNum, secondNum, thirdNum) == thirdNum and max(firstNum, secondNum, thirdNum) == secondNum:
    print(secondNum, firstNum, thirdNum, sep='\n')
elif min(firstNum, secondNum, thirdNum) == secondNum and max(firstNum, secondNum, thirdNum) == firstNum:
    print(firstNum, thirdNum, secondNum, sep='\n')
elif min(firstNum, secondNum, thirdNum) == thirdNum and max(firstNum, secondNum, thirdNum) == firstNum:
    print(firstNum, secondNum, thirdNum, sep='\n')
elif min(firstNum, secondNum, thirdNum) == secondNum and max(firstNum, secondNum, thirdNum) == thirdNum:
    print(thirdNum, firstNum, secondNum, sep='\n')
    
# Альтернатива

a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(min(a, b, c))


# Задача 10

# Назовём число интересным, если в нём разность максимальной и минимальной цифры равняется средней по величине цифре. 
# Напишите программу, которая определяет, интересное число или нет. Если число интересное, 
# следует вывести текст «Число интересное» (без кавычек), иначе – «Число неинтересное» (без кавычек).

intNum = int(input("Введите исходное 3-х значное число: "))

firstNum = intNum // 100 # первая цифра
secondNum = intNum % 10  # вторая цифра
thirdNum = (intNum // 10) % 10 # третья цифры

minNum = min(firstNum, secondNum, thirdNum)
maxNum = max(firstNum, secondNum, thirdNum)

if (maxNum - minNum) == ((firstNum + secondNum + thirdNum) - minNum - maxNum):
    print("Число интересное")
else:
    print("Число неинтересное")
    

# Задача 11

# Даны пять чисел a1,a2,a3,a4,a5. Напишите программу, которая вычисляет сумму их модулей

a_1 = abs(float(input()))
a_2 = abs(float(input()))
a_3 = abs(float(input()))
a_4 = abs(float(input()))
a_5 = abs(float(input()))

print(abs(a_1 + a_2 + a_3 + a_4 + a_5))


# Задача 12

p_1 = abs(int(input()))
p_2 = abs(int(input()))
q_1 = abs(int(input()))
q_2 = abs(int(input()))

print(abs(p_1 - q_1) + abs(p_2 - q_2))


# Задача 13

# Даны названия трёх городов. Напишите программу, которая определяет самое короткое и самое 
# длинное название города.


city_1 = input()
city_2 = input()
city_3 = input()

len_city_1 = len(city_1)
len_city_2 = len(city_2)
len_city_3 = len(city_3)

if  min(len_city_1, len_city_2, len_city_3) == len_city_1 and max(len_city_1, len_city_2, len_city_3) == len_city_2:
    print(city_1, city_2, sep='\n')
elif  min(len_city_1, len_city_2, len_city_3) == len_city_1 and max(len_city_1, len_city_2, len_city_3) == len_city_3:
    print(city_1, city_3, sep='\n')
elif  min(len_city_1, len_city_2, len_city_3) == len_city_2 and max(len_city_1, len_city_2, len_city_3) == len_city_1:
    print(city_2, city_1, sep='\n')
elif  min(len_city_1, len_city_2, len_city_3) == len_city_2 and max(len_city_1, len_city_2, len_city_3) == len_city_3:
    print(city_2, city_3, sep='\n')
elif  min(len_city_1, len_city_2, len_city_3) == len_city_3 and max(len_city_1, len_city_2, len_city_3) == len_city_2:
    print(city_3, city_2, sep='\n')
elif  min(len_city_1, len_city_2, len_city_3) == len_city_3 and max(len_city_1, len_city_2, len_city_3) == len_city_1:
    print(city_3, city_1, sep='\n')
    
# Альтернатива

first_city = input()
second_city = input()
third_city = input()

# ищем минимальную длину среди всех городов
min_city_len = min(len(first_city), len(second_city), len(third_city))
# ищем максимальную длину среди всех городов
max_city_len = max(len(first_city), len(second_city), len(third_city))

# длину каждого города сравниваем с минимальной длиной
if len(first_city) == min_city_len:
    print(first_city)
elif len(second_city) == min_city_len:
    print(second_city)
else:
    print(third_city)

# длину каждого города сравниваем с максимальной длиной
if len(first_city) == max_city_len:
    print(first_city)
elif len(second_city) == max_city_len:
    print(second_city)
else:
    print(third_city)
    
    
# Задача 14

# Вводятся 3 строки в случайном порядке. Напишите программу, которая выясняет, можно ли из длин этих 
# строк построить арифметическую прогрессию.

first_str = input()
second_str = input()
third_str = input()


len_first_str = len(first_str)
len_second_str = len(second_str)
len_third_str = len(third_str)

min_len_str = min(len(first_str), len(second_str), len(third_str))
max_len_str = max(len(first_str), len(second_str), len(third_str))
average_len_str = len_first_str + len_second_str + len_third_str - min_len_str - max_len_str

if (average_len_str - min_len_str) == max_len_str - average_len_str:
    print("YES")
else:
    print("NO")
    
    
# Задача 15

# Напишите программу, которая считывает одну строку, после чего выводит «YES» (без кавычек), если во введённой строке есть подстрока «синий»,
# или «NO» (без кавычек) # в противном случае.

strOne = input()

if 'синий' in strOne:
    print("YES")
else:
    print("NO")
    
# Задача 16

# Напишите программу, которая считывает одну строку, после чего выводит «YES» (без кавычек), 
# если во введённой строке есть подстрока «суббота» или «воскресенье», или «NO» (без кавычек) в противном случае.

str_One = input()

if 'суббота' in str_One or 'воскресенье' in str_One:
    print("YES")
else:
    print("NO")
    

# Задача 17

str_of_email = input()

if '@' in str_of_email and '.' in str_of_email:
    print("YES")
else:
    print("NO")
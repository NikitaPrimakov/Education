#####################################################
## День 3. Практика                                 #
#####################################################

# Задача 1

# При регистрации на сайтах требуется вводить пароль дважды. 
# Это сделано для безопасности, поскольку такой подход уменьшает возможность неверного ввода пароля.

# Напишите программу, которая сравнивает пароль и его подтверждение. 
# Если они совпадают, то программа выводит текст «Пароль принят» (без кавычек), иначе – «Пароль не принят» (без кавычек).

passwordOne = input("Введите пароль: ")
passwordVerify = input("Подтвердите пароль: ")
if passwordOne == passwordVerify:
    print("Пароль принят")
else:
    print("Пароль не принят")
    
    
    
# Задача 2

# Напишите программу, которая определяет, является число четным или нечетным.

intNum = int(input("Ведите число: "))
if intNum % 2 == 0:
    print("Четное")
else:
    print("Нечетное")
    

# Задача 3

# Напишите программу, которая проверяет, что для заданного четырехзначного числа выполняется следующее соотношение: 
# сумма первой и последней цифр равна разности второй и третьей цифр.

intNum = int(input("Введите четырехзначное число: "))
if intNum < 1000:
    print("Число не четырехзначное")
if (intNum // 1000 + intNum % 10) == (intNum // 100 % 10 - intNum % 100 // 10) :
    print("ДА")
else:
    print("НЕТ")
    
    
# Задача 4

# Напишите программу, которая определяет, разрешён ли пользователю доступ к интернет-ресурсу или нет.

ageOfPerson = int(input("Введите свой возраст: "))

if ageOfPerson >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")
    

# Задача 5

# Напишите программу, которая определяет, являются ли три заданных числа (в указанном порядке) последовательными 
# членами арифметической прогрессии.

intOne = int(input('Введите число №1: '))
intTwo = int(input('Введите число №2: '))
intThree = int(input('Введите число №3: '))

if (intTwo - intOne) == (intThree - intTwo):
    print("YES")
else:
    print("NO")
    

# Задача 6

# Напишите программу, которая определяет наименьшее из двух чисел.

intOne = int(input('Введите число №1: '))
intTwo = int(input('Введите число №2: '))

if intOne > intTwo:
    print(intTwo)
else:
    print(intOne)
    
    
# Задача 7

# Напишите программу, которая определяет наименьшее из четырёх чисел.

intOne = int(input('Введите число №1: '))
intTwo = int(input('Введите число №2: '))
intThree = int(input('Введите число №3: '))
intFour = int(input('Введите число №4: '))

minNumOne = 0
minNumTwo = 0

if intOne < intTwo:
    minNumOne = intOne
else:
    minNumOne = intTwo
    
if intThree < intFour:
    minNumTwo = intThree
else:
    minNumTwo = intFour
    
if minNumOne < minNumTwo or minNumOne == minNumTwo:
    print(minNumOne)
else:
    print(minNumTwo)


# Задача 8

# Напишите программу, которая по введённому возрасту пользователя сообщает, к какой возрастной группе он относится: 
# до 13 (включительно) – детство; 
# от  14 до 24 (включительно) – молодость;от 25 до 59 (включительно) – зрелость; от 60 (включительно) – старость.

ageOfPerson = int(input("Введите свой возраст: "))

if ageOfPerson <= 13:
    print("детство")
if 14 <= ageOfPerson <= 24:
    print("молодость")
if 25 <= ageOfPerson <= 59:
    print("зрелость")
if ageOfPerson >= 60:
    print("старость")
    
# Задача 9

# Напишите программу, которая считывает три числа и подсчитывает сумму только положительных чисел.

intOne = int(input('Введите число №1: '))
intTwo = int(input('Введите число №2: '))
intThree = int(input('Введите число №3: '))

if intOne > 0 and intTwo < 0 and intThree < 0:
    print(intOne)
if intOne > 0 and intTwo > 0 and intThree < 0:
    print(intOne + intTwo)
if intOne > 0 and intTwo > 0 and intThree > 0:
    print(intOne + intTwo + intThree)
if intOne < 0 and intTwo > 0 and intThree < 0:
    print(intTwo)
if intOne < 0 and intTwo < 0 and intThree > 0:
    print(intThree)
if intOne > 0 and intTwo < 0 and intThree > 0:
    print(intOne + intThree)
if intOne < 0 and intTwo > 0 and intThree > 0:
    print(intTwo + intThree)
if intOne < 0 and intTwo < 0 and intThree < 0:
    print(0)
    

# Альтернатива
a, b, c = int(input()), int(input()), int(input())
total = 0
if a > 0:
    total = total + a
if b > 0:
    total = total + b
if c > 0:
    total = total + c
print(total)
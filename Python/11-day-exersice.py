# Упражнение 1

# Дано натуральное число. Напишите программу, которая выводит его цифры в столбик в обратном порядке.

num = int(input("Введите число:"))

total = num

while num != 0:

    last_digit = num % 10
    print(f"Цифры числа {total}: ", last_digit)
    num = num // 10


# Упражнение 2

# Дано натуральное число. Напишите программу, которая меняет порядок цифр числа на обратный.

num = int(input("Введите число: "))

reNum = ''

while num != 0:

    last_digit = num % 10
    reNum += str(last_digit)
    num = num // 10

print("Отфармотированное число:", int(reNum))


# Упражнение 3

# Дано натуральное число n (n≥10). Напишите программу, которая определяет его максимальную и минимальную цифры и 
# выводит текст в следующем формате:

#   - Максимальная цифра равна <максимальная цифра>
#   - Минимальная цифра равна <минимальная цифра>

num = int(input("Введите число > или равно 10: "))

maxOfNum = 0
minOfNum = 9

total = num

flag = False

while num != 0:

    last_digit = num % 10
    num = num // 10
    
    if last_digit > maxOfNum:
        maxOfNum = last_digit
        flag = True
    
    if last_digit < minOfNum:
        minOfNum = last_digit
        flag = True
    
    if  total < 10:
        flag = False


if flag == True:
    print("Максимальная цифра равна", maxOfNum)
    print("Минимальная цифра равна", minOfNum)
else:
    print("Не удовлетворяет условию")


# Упражнение 4

# Дано натуральное число. Напишите программу, которая вычисляет:

#   - сумму его цифр;
#   - количество цифр в нем;
#   - произведение его цифр;
#   - среднее арифметическое его цифр;
#   - его первую цифру;
#   - сумму его первой и последней цифры.

num = int(input("Введите число:"))

summOfNum = 0
counter = 0
multiplication = 1
arithmeticMean = 0
firstOfNum = 0
lastOfNum = num % 10

while num != 0:

    last_digit = num % 10
    
    num = num // 10
    
    summOfNum += last_digit
    
    counter += 1
    
    multiplication *= last_digit
    
    arithmeticMean = summOfNum / counter

    if num ==  0:
        firstOfNum = last_digit

    


print("Сумма чисел:", summOfNum)
print("Количество чисел:", counter)
print("Произведение чисел:", multiplication)
print("Среднее арифметическое:", arithmeticMean)
print("Первое число:", firstOfNum)
print("Сумма первой и последней цифры:", firstOfNum + lastOfNum)


# Упражнение 5

# Дано натуральное число n (n>9). Напишите программу, которая определяет его вторую (с начала) цифру.

num = int(input("Введите число n (n>9): "))

if num <= 9:
    print("Число не удовлетворяет условию")
else:
    # Определяем количество цифр в числе
    temp = num
    count = 0
    while temp != 0:
        temp = temp // 10
        count += 1
    
    # Находим вторую цифру с начала
    second_digit = (num // 10 ** (count - 2)) % 10
    
    print("Вторая цифра с начала:", second_digit)

# АЛЬТЕРНАТИВА

n = int(input())
while n > 9:
    x = n % 10
    n = n // 10
print(x)

# Упражнение 6

# Дано натуральное число. Напишите программу, которая определяет, состоит ли указанное число из одинаковых цифр.

num = int(input("введите число n:"))

flag = True

theSameNum = num % 10

while num != 0:

    last_digit = num % 10

    num = num // 10

    if last_digit != theSameNum:
        flag = False


if flag:
    print("YES")
else:
    print("NO")


# Упражнение 7

# Дано натуральное число. Напишите программу, которая определяет, является ли последовательность его цифр при 
# просмотре справа налево упорядоченной по неубыванию.

num = int(input("Введите число n: "))

newNum = num % 10

flag = True

while num != 0:

    last_digit = num % 10

    num = num // 10

    newNum = num % 10

    if 0 < newNum < last_digit:
        flag = False


if flag:
    print("YES")
else:
    print("NO")
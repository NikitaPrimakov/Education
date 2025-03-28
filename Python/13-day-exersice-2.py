# Упражнение 1

# Дано натуральное число n. Напишите программу, которая печатает численный треугольник с высотой, равной n, 
# в соответствии с примером:

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
# 16 17 18 19 20 21
# ...

# total = 0

# num = int(input("Введите число: "))3


# for i in range(1, num + 1):
#     total += 1
#     print(str(i) * total)


total = 1

num = int(input("Введите число: "))


for i in range(1, num + 1):

    for j in range(1, i + 1):

        print(total, end=' ')
        total += 1

    print()

# Упражнение 2

# Делители-2

# На вход программе подаётся натуральное число n. Напишите программу, выводящую графическое изображение 
# делимости чисел от 1 до n включительно. В каждой строке надо напечатать очередное число и столько символов +, 
# сколько делителей у этого числа.

# Первый вариант

a = int(input("Введите число a: "))
b = int(input("Введите число b: "))

for i in range(a, b + 1):
    if i < 2:
        continue  # 0 и 1 не являются простыми числами
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        print(i)

# Второй вариант

a, b = int(input()), int(input())

for num in range(a, b + 1):
    # явно обрабатываем единицу
    if num == 1:
        continue
    
    for i in range(2, num):
        # если у числа num есть делитель, 
        # то можно завершать цикл, т.к. это число не является простым
        if num % i == 0:
            break
    else:
        # если цикл завершается без break (штатным образом), 
        # то значит делители найдены не были, и число является простым
        print(num)


# Упражнение 3

# На вход программе подаются два натуральных числа a и b (a< b). Напишите программу, которая находит натуральное 
# число из отрезка [a;b] (от a до b включительно) с максимальной суммой делителей. Если чисел с максимальной 
# суммой делителей несколько, то искомым числом является наибольшее из них. Ваша программа должна выводить ответ 
# в следующем формате:


a, b = int(input("Введите число a: ")), int(input("Введите число b: "))

maxNum = 0
maxSumm = 0

for i in range(a, b + 1):
    curentCount = 0
    currentSumm = 0
    for j in range(1, i + 1):
        if i % j == 0:
             currentSumm += j
             if currentSumm > maxSumm or (currentSumm == maxSumm and i > maxNum):
                 maxSumm = currentSumm
                 maxNum = i

print(maxNum, maxSumm)


# Упражнение 4

# Цифровым корнем числа n называется число, получающееся следующим образом: вычисляется сумма цифр числа n, 
# затем сумма цифр у получившегося числа и так далее, пока не получится однозначное число. Например, 
# цифровой корень числа 9875 равен 2: 

# 9+8+7+5=29
# 2+9=11
# 1+1=2

# Мой вариант решения

num = int(input("Введите число: "))

summOne = 0
summSecond = 0
summThree = 0

while num != 0:

    last_digit = num % 10
    num //= 10
    
    summOne += last_digit

if summOne <= 9:
    print(summOne)
else:
    while summOne != 0:
        last_digit = summOne % 10
        summOne //= 10
        summSecond += last_digit

    if summSecond <= 9:
        print(summSecond)

    else:
        while summSecond != 0:
            last_digit = summSecond % 10
            summSecond //= 10
            summThree += last_digit

        if summThree <= 9:
            print(summThree)

# От Python академии

n = int(input())

while n > 9:
    new_n = 0
    while n > 0:
        new_n += n % 10
        n //= 10
    
    n = new_n
    
print(n)
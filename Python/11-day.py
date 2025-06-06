#####################################################
## День 11. Тема урока: цикл while                  #
#####################################################

## Обработка цифр числа
# ----------------------

# При изучении целых чисел (тип данных int), мы говорили про операцию целочисленного 
# деления // и операцию нахождения остатка от деления одного целого числа на другое %. 
# Используя цикл while и две данных операции, можно обработать цифры числа с произвольным количеством разрядов (цифр).

# Пусть дано натуральное число n. Тогда:

#   - результатом операции n % 10 – является последняя цифра числа;
#   - результатом операции n // 10 – является число с удаленной последней цифрой.

# Напишем программу, которая считывает натуральное число (целое положительное) и обрабатывает его цифры.

num = int(input("Введите целое число: "))

while num != 0:  # пока в числе есть цифры
    last_digit = num % 10  # получить последнюю цифру
    print("Получение последей цифры: ", last_digit)
    # код обработки последней цифры
    num = num // 10  # удалить последнюю цифру из числа
    print("Удаление последней цифры из числа: ", num)


# Цикл while работает до тех пор, пока в числе есть необработанные цифры. Тело цикла содержит:

#   - процедуру получения последней цифры last_digit = n % 10;
#   - код обработки последней цифры;
#   - процедуру удаления последней цифры из числа n = n // 10.

# В качестве процедуры обработки может быть все что угодно: вывод цифр, нахождение суммы, произведения цифр, 
# нахождение наибольшей или наименьшей цифры, подсчет цифр удовлетворяющих некоторому условию и т.д.

# Напишем программу, которая определяет, есть ли в числе цифра 7.

num = int(input("Введите число: "))
flag = False

while num != 0:

    last_digit = num % 10 # нашли последнюю цифру числа

    num = num // 10 # удаляем последнюю цифру, уменьшая перебор

    if last_digit == 7:
        flag = True

if flag == True:
    print("Цифра '7' присутсвтует")
else:
    print("Цифра '7' отсутсвует")


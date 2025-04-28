# Упражнение 1

# Дополните приведённый ниже код так, чтобы он вывел сумму квадратов элементов списка numbers.


numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

summ = 0

list_one = list()

for i in numbers:

  list_one.append(int(i) * int(i))

print(sum(list_one))
#--------------------------------------------------------------------------------------------------


# Упражнение 2

# Значение функции 
# На вход программе подаются натуральное число n, а затем n целых чисел. Напишите программу, 
# которая для каждого введённого числа x выводит значение функции f(x)=x^2+2x+1, каждое на отдельной 
# строке.

n = int(input("Enter your number: "))

list_one = list()

list_two = list()

for i in range(n):

    num = int(input("Enter interger: "))

    list_one.append(num)

    our_func = num**2 + 2 * num + 1

    list_two.append(our_func)

print(*list_one, sep='\n')
print()
print(*list_two, sep='\n')
#--------------------------------------------------------------------------------------------------


# Упражнение 3

# Remove outliers

# При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и 
# самое маленькое значение.

# На вход программе подаются натуральное число n, а затем n различных натуральных чисел. 
# Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, 
# а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.

n = int(input("Enter your number: "))

list_one = list()

for i in range(n):

    num = int(input("Enter integer: "))

    list_one.append(num)


list_one.remove(max(list_one))
list_one.remove(min(list_one))

print(*list_one, sep='\n')
#--------------------------------------------------------------------------------------------------


# Упражнение 4

# Без дубликатов

# На вход программе подаются натуральное число n, а затем n строк. Напишите программу, которая выводит 
# только уникальные строки, в том же порядке, в котором они были введены.

n = int(input("Enter your number: "))

# str_one = input("Enter your string: ")

list_one = list()

for i in range(n):

    str_one = input("Enter your string: ")

    if str_one not in list_one:
        
        list_one.append(str_one)

print(*list_one, sep='\n')
#--------------------------------------------------------------------------------------------------


# Упражнение 5

# Google search - 1

# На вход программе подаются натуральное число n, затем n строк, затем ещё одна строка – поисковый 
# запрос. Напишите программу, которая выводит все введённые строки, в которых встречается поисковый 
# запрос.

n = int(input())

list_one = list()

list_two = list()

for i in range(n):

    str_one = input()


    list_one.append(str_one)


str_two = input()

for i in range(len(list_one)):

    if str_two.lower() in list_one[i].lower():

        list_two.append(list_one[i])
    

print(*list_two, sep='\n')
#--------------------------------------------------------------------------------------------------


# Упражнение 6

# Negatives, Zeros and Positives

# На вход программе подаются натуральное число n, а затем n целых чисел. Напишите программу, которая 
# сначала выводит все отрицательные числа, затем нули, а затем все положительные числа, каждое на 
# отдельной строке. Числа должны быть выведены в том же порядке, в котором они были введены.

n = int(input("Enter n: "))

list_one = list()
list_two = list()
list_three = list()

for i in range(n):

    num = int(input("Enter your num: "))

    if num > 0:

        list_one.append(num)

    elif num == 0:

        list_two.append(num)

    else:

        list_three.append(num)

print(*list_three, sep='\n')
print(*list_two, sep='\n')
print(*list_one, sep='\n')


#--------------------------------------------------------------------------------------------------

# Упражнение 7


## Google search - 2 🌶️🌶️

# На вход программе подаются натуральное число n, затем n строк, затем число k – количество поисковых 
# запросов, затем k строк – поисковые запросы. Напишите программу, которая выводит все введённые строки, 
# в которых встречаются одновременно все поисковые запросы.

n = int(input("Enter your n: "))

list_one = list()
list_two = list()
list_three = list()

for i in range(n):

    str_one = input("Enter your string: ")
    list_one.append(str_one)

num_k = int(input("Enter number of search queries: "))

for i in range(num_k):

    str_of_k = input("Enter strings (k): ")
    list_two.append(str_of_k)

for i in list_one:

    count = 0

    for j in list_two:

        if j.lower() in i.lower():

            count += 1

            if count == len(list_two):

                list_three.append(i)

print(*list_three, sep='\n')
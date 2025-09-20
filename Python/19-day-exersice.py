# Упражнение 1

# Список чисел

# На вход программе подаётся одно число n. Напишите программу, которая выводит список [1, 2, 3, ..., n].

n = int(input("Enter your number: "))

list_n = list(range(1, n + 1))

print(list_n)

#--------------------------------------
# Упражнение 2


# Список букв

# На вход программе подаётся натуральное число n. Напишите программу, которая выводит список, состоящий 
# из n букв английского алфавита ['a', 'b', 'c', ...] в нижнем регистре.

alphavit_eng = 'abcdefghijklmnopqrstuvwxyz'

n = int(input("Enter your number: "))

list_alphavit = list()

for i in range(n):

    list_alphavit += list(alphavit_eng[i])

print(list_alphavit)
#--------------------------------------
# Упражнение 3

# Дополните приведённый ниже код так, чтобы он вывел сумму минимального и максимального элементов 
# списка numbers.

numbers = [12.5, 3.1415, 2.718, 9.8, 1.414, 1.1618, 1.324]

print(min(numbers) + max(numbers))
#--------------------------------------
# Упражнение 4

# Дополните приведённый ниже код так, чтобы элемент списка имеющий значение Green заменился на значение 
# Зеленый, а элемент Violet – на Фиолетовый. Далее необходимо вывести полученный список.

rainbow = ['Red', 'Orange', 'Yellow', 'Green', 'Blue', 'Indigo', 'Violet']

for i in range(len(rainbow)):

    if rainbow[i] == 'Green':

        rainbow[i] = 'Зеленый'
    
    if rainbow[i] == 'Violet':

        rainbow[i] = 'Фиолетовый'
    
print(rainbow)

#--------------------------------------
# Упражнение 5

# Дополните приведённый ниже код так, чтобы он вывел "перевёрнутый" список languages (то есть элементы 
# будут идти в обратном порядке).

# Примечание. Для вывода списка воспользуйтесь функцией print().


languages = ['Chinese', 'Spanish', 'English', 'Hindi', 'Arabic', 'Bengali', 'Portuguese', 'Russian', 
             'Japanese', 'Lahnda']

print(languages[-1::-1])

#--------------------------------------
# Упражнение 6

# Все сразу 1 🌶️

# Дополните приведённый ниже код, чтобы он:

# Вывел длину списка;
# Вывел последний элемент списка;
# Вывел список в обратном порядке (вспоминаем срезы);
# Вывел «YES» (без кавычек), если список содержит числа 5 и 17, или «NO» (без кавычек) в противном случае;
# Вывел список с удалёнными первым и последним элементами.

numbers = [2, 6, 3, 14, 10, 4, 11, 16, 12, 5, 4, 16, 1, 0, 8, 16, 10, 10, 8, 5, 1, 11, 10, 10, 12, 0, 0, 
           6, 14, 8, 2, 12, 14, 5, 6, 12, 1, 2, 10, 14, 9, 1, 15, 1, 2, 14, 16, 6, 7, 5]

print(len(numbers))
print(numbers[-1])
print(numbers[-1::-1])

if 17 in numbers and 5 in numbers:
    print("YES")
else:
    print("NO")

del numbers[0]
del numbers[-1]
print(numbers)

#--------------------------------------
# Упражнение 7

# Список строк

# На вход программе подаются натуральное число n, а затем n строк. 
# Напишите программу, которая создаёт из указанных строк список, а затем выводит его.

n = int(input("Enter your number: "))

list_one = []

for i in range(n):

    str_one = input("Enter your string: ")

    list_one.append(str_one)

print(list_one)

#--------------------------------------
# Упражнение 8

# Алфавит

# Напишите программу, выводящую следующий список:

# ['a', 'bb', 'ccc', 'dddd', 'eeeee', 'ffffff', ...]


alphavit_eng = 'abcdefghijklmnopqrstuvwxyz'

list_one = []

for i in range(len(alphavit_eng)):

    
    list_one.append(alphavit_eng[i] * (i + 1))

print(list_one)


#--------------------------------------
# Упражнение 9

# Список кубов
# На вход программе подаются натуральное число n, а затем n целых чисел. Напишите программу, 
# которая создаёт из указанных чисел список их кубов, а затем выводит его.


n = int(input("Enter your n: "))

list_one = []

for i in range(n):

    str_of_int = input(f"Enter number {i}: ")
    list_one.append(int(str_of_int) ** 3)

print(list_one)

#--------------------------------------
# Упражнение 10

# Список делителей

# На вход программе подаётся натуральное число n. Напишите программу, которая создаёт список, состоящий 
# из делителей введённого числа, а затем выводит его.


n = int(input())

list_one = list()

for i in range(1, n+1):

    if n % i == 0:

        list_one.append(i)

print(list_one)

#--------------------------------------
# Упражнение 11

# Суммы двух

# На вход программе подаётся натуральное число n(n≥2). Затем поступают n целых чисел. Напишите программу, 
# которая создаёт из указанных чисел список, состоящий из сумм соседних чисел (0 и 1, 1 и 2, 2 и 3 и так 
# далее).


n = int(input("Enter your n: "))

list_one = list()

number_new = int(input())

for i in range(n-1):

    number_old = number_new

    number_new = int(input())

    number_final = number_old + number_new

    list_one.append(number_final)

print(list_one)

#--------------------------------------
# Упражнение 12

# Удалите нечётные индексы

# На вход программе подаются натуральное число n, а затем n целых чисел. Напишите программу, которая 
# создаёт из указанных чисел список, затем удаляет все элементы, стоящие по нечётным индексам, а затем 
# выводит полученный список.

n = int(input("Enter your number: "))

list_one = list()

for i in range(n):

    num = int(input())

    if i % 2 == 0:

        list_one.append(num)

print(list_one)

# Альтернативный код (del)

n = int(input())
seq = []

for _ in range(n):
    cur = int(input())
    seq.append(cur)

del seq[1::2]
    
print(seq)

#--------------------------------------
# Упражнение 13

#  k-ая буква слова 🌶️

# На вход программе подаются натуральное число n и n строк, а затем число k. Напишите программу, 
# которая выводит k-ую букву из введённых строк на одной строке без пробелов.

n = int(input("Enter n: "))

list_one = list()

str_three = ''
str_four = ''

for  i in range(n):

    str_one = input("Enter your strings: ")

    list_one.append(str_one)

k = int(input("Enter number K: "))

for i in range(len(list_one)):

    str_two = list_one[i]

    if k <= len(str_two):

       str_three += str_two[k - 1]

print(str_three)

#--------------------------------------
# Упражнение 14

# Символы всех строк

# На вход программе подаются натуральное число n, а затем n строк. Напишите программу, которая создает 
# список из символов всех строк, а затем выводит его.

n = int(input("Enter number: "))

list_one = list()

for i in range(n):

    str_one = input("Enter your string: ")

    list_one.extend(str_one)

print(list_one)
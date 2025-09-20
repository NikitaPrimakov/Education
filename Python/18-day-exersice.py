# Упражнение 1

# Строковые минимум и максимум

# На вход программе подаётся последовательность строк, каждая строка на отдельной строке. Концом 
# последовательности является слово «КОНЕЦ» (без кавычек). При этом само слово «КОНЕЦ» не входит в 
# последовательность, лишь символизируя ее окончание. Напишите программу, которая находит в данной 
# последовательности максимальную и минимальную строки (в лексикографическом порядке) и выводит их в следующем 
# формате:

# Минимальная строка ⬇️: <минимальная строка>
# Максимальная строка ⬆️: <максимальная строка>


str_one = ''

max_str = ' '

min_str = 'я'

while True:

    str_one = input()

    if str_one == "КОНЕЦ":
        break

    elif str_one > max_str:
        max_str = str_one

    if str_one < min_str:
        min_str = str_one

print(f"Минимальная строка ⬇️: {min_str}")
print(f"Максимальная строка ⬆️: {max_str}")

#-------------------------------------------

# Упражнение 2

# Волшебное число ✨

# В некотором наборе слов Сэм находит "волшебное" число по следующему алгоритму: берет самую "маленькую" и самую 
# "большую" строки, перемножает Unicode-коды последних символов этих строк и возводит полученное число в квадрат. 
# Результатом и является "волшебное" число.

# На вход программе подаются 4 слова. Найдите "волшебное" число в этом наборе слов.

max_str = ''
min_str_eng = 'z'
min_str_ru = 'я'

# for i in range(1,5):

#     str_one = input("Enter your string: ")

#     if str_one > max_str:
#         max_str = str_one

#     if str_one < min_str:
#         min_str = str_one

# answer = (ord(max_str[-1]) * ord(min_str[-1])) ** 2

# print(answer)

for i in range(1,5):

    str_one = input("Enter your string: ")

    if str_one > max_str:
        max_str = str_one

    if str_one in 'абвгдежзийклмнопрстуфхцчшщъыьэюяAБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ' or str_one < min_str_ru:
        min_str_ru = str_one
        flag = False

    if str_one in 'abcdefghIjklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' or str_one < min_str_eng:
        min_str_eng = str_one
        flag = True

if flag == False:
    answer = (ord(max_str[-1]) * ord(min_str_ru[-1])) ** 2
    print(answer)
else:
    answer = (ord(max_str[-1]) * ord(min_str_eng[-1])) ** 2
    print(answer)

# Альтернатива

s1 = input()
s2 = input()
s3 = input()
s4 = input()

min_string = min(s1, s2, s3, s4)
max_string = max(s1, s2, s3, s4)
res = ord(min_string[-1]) * ord(max_string[-1])
res **= 2

print(res)

#-------------------------------------------

# Упражнение 3

# Название класса 👩‍🏫🌶️

# В школе BEEGEEK названия учебных классов необычные. Они имеют следующий формат: <номер класса><буква класса>
# где <номер класса> должен находиться в диапазоне от 0 (как и все у программистов) до  9 включительно, а буквой 
# класса могут быть все буквы в диапазоне от «А» до «П» включительно.

# Напишите программу, которая принимает натуральное число n, а далее n названий классов, каждое на новой строке. 
# Для каждого названия класса ваша программа должна выводить на отдельной строке «YES» (без кавычек), 
# если название класса корректное, или «NO» (без кавычек) в противном случае.

num = int(input())
for _ in range(num):
    class_name = input().strip()
    if len(class_name) == 2 and class_name[0] in '0123456789' and class_name[1] in 'АБВГДЕЖЗИЙКЛМНОП':
        print("YES")
    else:
        print("NO")

#-------------------------------------------

# Упражнение 4

# Сортируем слова 📶

# На вход программе подаются 3 различных слова. Вам необходимо отсортировать эти слова по возрастанию
# в лексикографическом порядке и вывести их на одной строке, разделяя символом пробела.

str_one = input()
str_two = input()
str_three = input()

max_str = max(str_one, str_two, str_three)
min_str = min(str_one, str_two, str_three)

if min_str == str_one and max_str == str_two:
    print(str_one, str_three, str_two)
elif min_str == str_one and max_str == str_three:
    print(str_one, str_two, str_three)
elif min_str == str_two and max_str == str_one:
    print(str_two, str_three, str_one)
elif min_str == str_two and max_str == str_three:
    print(str_two, str_one, str_three)
elif min_str == str_three and max_str == str_one:
    print(str_three, str_two, str_one)
elif min_str == str_three and max_str == str_two:
    print(str_three, str_one, str_two)

# Лучший вариант

a, b, c = input(), input(), input()
general_string = a + b + c

min_word = min(a, b, c)
max_word = max(a, b, c)
middle_word = general_string.replace(min_word, '').replace(max_word, '')

print(min_word, middle_word, max_word)


#-------------------------------------------

# Упражнение 5

# Порядок книг 📚🌶️

# Все книги в домашней библиотеке Душнилы, друга Сэма, должны быть обязательно отсортированы по возрастанию: 
# сначала по фамилиям авторов, а в случае совпадения фамилий – по названиям. Напишите программу, 
# которая проверяет, верно ли отсортированы книги.

# На вход вашей программе поступает число n, а затем – n строк, каждая строка представляет собой книгу в 
# следующем формате: <фамилия автора> <инициалы автора>, «<название книги>»

# Программа должна вывести «YES» (без кавычек), если книги отсортированы в соответствии с пожеланиями Душнилы, 
# или «NO» (без кавычек) в противном случае.

n = int(input("Введите количество книг: "))

if n == 0 or n == 1:
    flag = True

flag = True

name_of_book_1 = input("Введите название книги: ")
autor_surname_1 = (name_of_book_1[ : name_of_book_1.find(" ")])
autor_initials_1 = (name_of_book_1[name_of_book_1.find("«") : ])

for i in range(n-1):

    name_of_book_2 = input("Введите название книги: ")
    autor_surname_2 = (name_of_book_2[ : name_of_book_2.find(" ")])
    autor_initials_2 = (name_of_book_2[name_of_book_2.find("«") : ])

    if autor_surname_2 < autor_surname_1:
        flag = False
        

    elif autor_surname_2 == autor_surname_1:

        if autor_initials_2 < autor_initials_1:
            flag = False
            

    autor_surname_1 = autor_surname_2
    autor_initials_1 = autor_initials_2

if flag:
    print("YES")
else:
    print("NO")

#-------------------------------------------

# Упражнение 6

# Необычное сравнение 📊


# На вход программе подаются 2 строки. Вам необходимо сравнить эти строки посимвольно, не учитывая регистр 
# игнорируя все небуквенные символы. Программа должна вывести «YES» (без кавычек), если строки окажутся равны 
# в результате такой проверки, или «NO» (без кавычек) в противном случае.

str_one = input("Enter string №1: ")
str_two = input("Enter string №2: ")

new_str_one = ''
new_str_two = ''

for i in str_one:
    if i.isalpha():
        new_str_one += i

for j in str_two:
    if j.isalpha():
        new_str_two += j

if new_str_one.lower() == new_str_two.lower():
    print("YES")
else:
    print("NO")
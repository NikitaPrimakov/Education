# Упражнение 1

# Количество слов

# На вход программе подаётся строка текста, состоящая из слов, разделённых ровно одним пробелом. Напишите 
# программу, которая подсчитывает количество слов в ней.

str_one = input("Enter your string: ")

count_of_word = str_one.count(' ') + 1

print(count_of_word)
# --------------------------------------

# Упражнение 2

# Минутка генетики 🧬

# На вход программе подаётся строка генетического кода, состоящая из букв А (аденин), Г (гуанин), Ц (цитозин) и 
# Т (тимин). Напишите программу, которая подсчитывает сколько аденина, гуанина, цитозина и тимина входит в 
# данную строку генетического кода.

str_one = input("Enter your string: ")

count_a = 0
count_g = 0
count_c = 0
count_t = 0

for i in range(len(str_one)):

    if  str_one[i] == 'А' or str_one[i] == 'а':
        count_a += 1
        
    if str_one[i] == 'Г'or str_one[i] == 'г':
        count_g += 1
        
    if str_one[i] == 'Ц'or str_one[i] == 'ц':
        count_c += 1

    if str_one[i] == 'Т'or str_one[i] == 'т':
        count_t += 1

print("Аденин:", count_a)
print("Гуанин:", count_g)
print("Цитозин:", count_c)
print("Тимин:", count_t)


# Альтернатива

genetic_code = input()  # Ввод строки генетического кода
adenine_count = genetic_code.count('А') + genetic_code.count('а')  # Подсчет количества аденина
guanine_count = genetic_code.count('Г') + genetic_code.count('г')  # Подсчет количества гуанина
cytosine_count = genetic_code.count('Ц') + genetic_code.count('ц')  # Подсчет количества цитозина
thymine_count = genetic_code.count('Т') + genetic_code.count('т')  # Подсчет количества тимина

# Вывод результатов
print('Аденин:', adenine_count)
print('Гуанин:', guanine_count)
print('Цитозин:', cytosine_count)
print('Тимин:', thymine_count)


# --------------------------------------

# Упражнение 3

# Количество цифр

# На вход программе подаётся строка текста. Напишите программу, которая подсчитывает количество цифр в данной 
# строке.

str_one = input("Enter your string: ")

count = 0

for i in range(len(str_one)):

    if str_one[i] in '0123456789':

        count += 1

print(count)

# Альтернатива

n = input()
count = 0
for i in range(10):
    count += n.count(str(i))
print(count)

# --------------------------------------

# Упражнение 4

# .com or .ru 🌐
# На вход программе подаётся строка текста. Напишите программу, которая проверяет, что строка заканчивается 
# подстрокой .com или .ru.

str_one = input("Enter your string: ")

flag = False

if str_one.endswith('.com') or str_one.endswith('.ru'):

    flag = True

if flag:
    print('YES')
else:
    print('NO')


# --------------------------------------

# Упражнение 5

# Самый частотный символ

# На вход программе подаётся строка текста. Напишите программу, которая выводит на экран символ, который 
# появляется наиболее часто.

str_one = input("Enter your string: ")

max_count = 0

str_two = ''

for i in str_one:

    if str_one.count(i) >= max_count:

        max_count = str_one.count(i)
        str_two = i

print(max_count)
print(str_two)

# Альтернатива

s = input()

most_common = s[0]
for el in s:
    if s.count(el) >= s.count(most_common):
        most_common = el
        
print(most_common)


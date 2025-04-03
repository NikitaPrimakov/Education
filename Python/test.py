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
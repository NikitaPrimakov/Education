# Упаковка дубликатов 🌶️

# На вход программе подается строка текста, содержащая символы. Напишите программу, 
# которая упаковывает последовательности одинаковых символов заданной строки в подсписки.

# Sample Input 2:

# # w w w o r l d g g g g r e a t t e c c h e m g g p w w
# Sample Output 2:

# [['w', 'w', 'w'], ['o'], ['r'], ['l'], ['d'], ['g', 'g', 'g', 'g'], ['r'], ['e'], ['a'], ['t', 't'], ['e'], ['c', 'c'], ['h'], ['e'], ['m'], ['g', 'g'], ['p'], ['w', 'w']]

str_one = input('Enter your string: ').split(' ')
my_list = list()

for i in str_one:
    my_list.append(list(i))

print(my_list)
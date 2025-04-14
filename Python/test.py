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
# Символы всех строк

# На вход программе подаются натуральное число n, а затем n строк. Напишите программу, которая создает 
# список из символов всех строк, а затем выводит его.

n = int(input("Enter number: "))

list_one = list()

for i in range(n):

    str_one = input("Enter your string: ")

    list_one.extend(str_one)

print(list_one)
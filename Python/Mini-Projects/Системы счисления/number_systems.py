num = input(("Введите число в двоичной системе счисления: "))

powers_of_two = len(num)
result = 0

for i in range(powers_of_two + 1):

    last_digit = (int(num) % 10) * i
    result += last_digit
    int(num) //= 10

print(result)

# Перевод в систему счисления из шестнадцатиричной в десятичную систему счисления
print(int('1AF2', 16))



# Перевод в систему счисления из десятичной в двоичную систему счисления

num = int(input("Введите число в десятичной системе счисления: "))

list_one = list()
list_two = list()

while num // 2 > 1:
    integer_number = num // 2
    remains = num % integer_number
    list_two.append(remains) 
    num = num // 2

list_two_reverse = list_two[::-1]

if num - 2 == 1 or num - 2 == 0:
    list_one.append(num // 2)
    list_one.append(num -2)
    
list_final = list_one + list_two_reverse
print(*list_final, sep='')

# Перевод в систему счисления из десятичной в восьмеричную систему счисления
num = int(input("Введите число в десятичной системе счисления: "))

list_one = list()
list_two = list()


while num // 8 > 1:
    integer_number = num // 8
    remains = num % integer_number
    list_two.append(remains)
    num = num // 8

list_two_reverse = list_two[::-1]

if num - 8 == 7:
    list_one.append(num // 8)
    list_one.append(num - 8)

list_final = list_one + list_two_reverse
print(*list_final, sep='')


# BOH
#----

# На вход программе подается натуральное число в десятичной системе счисления. Напишите программу, которая переводит его в двоичную, 
# восьмеричную и шестнадцатеричную системы счисления.


num = int(input())

print(bin(num)[2:])
print(oct(num)[2:])
print(hex(num)[2:].upper())
# Упражнение 1
#-------------


# Заглавные буквы 🔠
# На вход программе подаётся строка, состоящая из имени и фамилии человека, разделённых одним пробелом. 
# Напишите программу, которая проверяет, что имя и фамилия начинаются с заглавной буквы.

name_of_people = input()

if name_of_people == name_of_people.title():
    print("YES")
else:
    print("NO")

# Упражнение 2
#-------------

# sWAP cASE 🔃

# На вход программе подаётся строка. Напишите программу, которая меняет регистр символов – заменяет все 
# строчные символы заглавными и наоборот.

str_one = input()

print(str_one.swapcase())


# Упражнение 3
#-------------

# Хороший оттенок 👍

# На вход программе подаётся строка текста. Напишите программу, которая определяет, является ли оттенок текста 
# хорошим или нет. Текст имеет хороший оттенок, если содержит подстроку «хорош» (без кавычек) во всевозможных 
# регистрах.

str_one = input("Enter your string: ")
str_one = str_one.lower() # изначально преобразовали строку к нижнему регистру
str_two = 'хорош'
# upper_str_two = str_two.upper()
lower_str_two = str_two.lower()
# print(upper_str_two, lower_str_two, sep='\n')
if lower_str_two in str_one :

    print("YES")
else:
    print("NO")

# Упражнение 3
#-------------

# Нижний регистр 🔽

# На вход программе подаётся строка. Напишите программу, которая подсчитывает количество буквенных символов в 
# нижнем регистре.

str_one = input("Enter your string: ")

count = 0

for i in range(len(str_one)):
    if str_one[i] in '0123456789@#$%^&':
        continue
    elif str_one[i] == str_one[i].lower():
        count += 1

print(count)

# альтернатива

s, counter = input(), 0
for i in s:
    if i != i.upper():  # условие выполняется только для букв в нижнем регистре
        counter += 1
print(counter)



# Задача №1

# Список по образцу 1
# На вход программе подается число n. Напишите программу, которая создает и выводит построчно список, состоящий из n списков 
# [[1, 2, ..., n], [1, 2, ..., n], ..., [1, 2, ..., n]].


n = int(input("Enter n: "))

our_list = list()
final_list = list()

for i in range(1, n + 1):

    our_list.append(i)

for i in range(1, n + 1):

    final_list.append(our_list)    

print(*final_list, sep='\n')


# Вариант 2

n = int(input())
result = []

for _ in range(n):
    result.append(list(range(1, n + 1)))

print(*result, sep='\n')


#-----------------------------------

# Задача №2

# Список по образцу 2
# На вход программе подается число n. Напишите программу, которая создает и выводит построчно 
# вложенный список, состоящий из n списков [[1], [1, 2], [1, 2, 3], ..., [1, 2, ..., n]].


n = int(input("Enter n: "))

our_list = []

for i in range(1, n + 1):
    result.append(list(range(1, n + 1)))

print(result)
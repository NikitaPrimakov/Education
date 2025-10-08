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
    our_list.append(list(range(1, i + 1)))


print(our_list)

for row in our_list:
    print(row)


## Глоссарий
#------------

# ✅ Способы создания вложенных списков:

# my_list = []

# for _ in range(n):
#     my_list.append([0] * m)

                  
# my_list = [0] * n

# for i in range(n):
#     my_list[i] = [0] * m

                  
# my_list = [[0] * m for _ in range(n)]

                  
# ✅ Для перебора и обработки всех элементов вложенных списков обычно используются вложенные циклы:

# перебор индексов
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(my_list[i][j], end=' ')
#     print()

                  
# перебор элементов
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for row in my_list:
#     for elem in row:
#         print(elem, end=' ')
#     print()


# Задача №3
# На вход программе подается натуральное число n. Напишите программу, которая выводит первые n строк треугольника Паскаля.

# На вход программе подается число n(n≥1).


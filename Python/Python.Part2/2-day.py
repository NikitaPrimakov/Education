# Координатные четверти

# Дан набор точек на координатной плоскости. Необходимо подсчитать и вывести количество точек, 
# лежащих в каждой координатной четверти.

count_of_points = int(input("Enter count of points: "))

count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0

for i in range(1, count_of_points + 1):
    coordinates = input("Enter x and y: ").split(' ')
    for i in range(len(coordinates)):
        coordinates[i] = int(coordinates[i])
    if coordinates[0] > 0 and coordinates[1] > 0:
        count_1 += 1
    elif coordinates[0] < 0 and coordinates[1] > 0:
        count_2 += 1
    elif coordinates[0] < 0 and coordinates[1] < 0:
        count_3 += 1
    elif coordinates[0] > 0 and coordinates[1] < 0:
        count_4 += 1
    
print(f"Первая четверть: {count_1}")
print(f"Вторая четверть: {count_2}")
print(f"Третья четверть: {count_3}")
print(f"Четрвертая четверть: {count_4}")


#------------------------------------------
# Больше предыдущего
# На вход программе подается строка текста из натуральных чисел. Из нее формируется список чисел. 
# Напишите программу подсчета количества чисел, которые больше предшествующего им в этом списке числа,
# то есть, стоят вслед за меньшим числом. 

list_of_num = input("Enter your split of num: ").split(' ')

count = 0

for i in range(len(list_of_num)):

    list_of_num[i] = int(list_of_num[i])

for i in range(len(list_of_num)-1):

    if list_of_num[i+1] > list_of_num[i]:

        count += 1

print(count)



# Вариант №2
# Сохраняем входящую строку как список целых чисел.
x = list(map(int, input().split()))

# Задаём начальное значение счётчика.
count = 0

# В цикле проверяем условие и изменяем значение счётчика.
for i in range(1, len(x)):
	if x[i] > x[i-1]:
		count += 1
  
# Выводим результат.
print(count)

#------------------------------------------
# Назад, вперед и наоборот

# На вход программе подается строка текста из неотрицательных чисел. Из элементов строки формируется список чисел. 
# Напишите программу, которая меняет местами соседние элементы списка (a[0] c a[1], a[2] c a[3] и так далее). 
# Если в списке нечетное количество элементов, то последний остается на своем месте.

str_of_num = input("Enter your string of numbers: ").split(' ')

if len(str_of_num) % 2 == 0:

    for i in range(0, len(str_of_num), 2):

        str_of_num[i], str_of_num[i + 1] = str_of_num[i + 1], str_of_num[i]
else:
    
    for i in range(0, len(str_of_num) - 1, 2):

        str_of_num[i], str_of_num[i + 1] = str_of_num[i + 1], str_of_num[i]

        
print(*str_of_num)


# Вариант №2
numbers = input().split()

for i in range(0, len(numbers) - 1, 2):
    numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]
    
print(*numbers)


#------------------------------------------
# Сдвиг в развитии ↩️
# На вход программе подается строка текста из натуральных чисел. Из элементов строки формируется список чисел. 
# Напишите программу циклического сдвига элементов списка направо, когда последний элемент становится первым, а остальные сдвигаются на одну позицию вперед, 
# в сторону увеличения индексов.

our_list = input("Enter your string of numbers: ").split(" ")

removed = our_list.pop(-1)
our_list.insert(0, removed)

for i in range(len(our_list)):
    
    our_list[i] = int(our_list[i])


print(*our_list)

#------------------------------------------
# Различные элементы

# На вход программе подается строка текста, содержащая натуральные числа, расположенные по неубыванию. Из строки формируется список чисел. 
# Напишите программу для подсчета количества разных элементов в списке.

our_str = input("Enter your string of numbers: ").split(" ")

new_list = list()

for i in range(len(our_str)):

    if our_str[i] not in new_list:

        new_list.append(our_str[i])

for i in range(len(new_list)):

    new_list[i] = int(new_list[i])

print(len(new_list))


#------------------------------------------
# Произведение чисел

# Напишите программу для определения, является ли число произведением двух чисел из данного набора. 
# Программа должна выводить результат в виде ответа ДА или НЕТ.

n = int(input("Количество чисел: "))
list_of_num = []
flag = False

for i in range(1, n + 1):
    num = int(input(f"Число № {i}: "))
    list_of_num.append(num)


our_num = int(input("Искомое произведение двух чисел: "))


for i in range(len(list_of_num)):
    for j in range(1, len(list_of_num)):
        if list_of_num[i] * list_of_num[j] == our_num and i != j:
            flag = True

if flag is True:
    print("ДА")
else:
    print("НЕТ")


#------------------------------------------
# Камень, ножницы, бумага

# Тимур и Руслан пытаются разделить фронт работы по курсу "Python для профессионалов". Для этого они решили сыграть в камень, ножницы и бумагу. 
# Помогите ребятам бросить честный жребий и определить, кто будет делать очередной модуль нового курса.


str_Tumur = input("Введите выбор Тимура: камень, ножницы, бумага: ")

str_Ruslan = input("Введите выбор Руслана: камень, ножницы, бумага: ")

if str_Tumur == 'камень' and str_Ruslan == 'ножницы':
    print('Тимур')

elif str_Tumur == 'ножницы' and str_Ruslan == 'бумага':
    print('Тимур')

elif str_Tumur == 'бумага' and str_Ruslan == 'камень':
    print('Тимур')

elif str_Tumur == str_Ruslan :
    print('ничья')
else:
    print("Руслан")


# Вариант 2
moves = ["камень", "ножницы", "бумага"]
outcomes = ["ничья", "Руслан", "Тимур"]

timur_move = input()
ruslan_move = input()

difference = moves.index(timur_move) - moves.index(ruslan_move)
result = outcomes[difference]

print(result)


#------------------------------------------
# Камень, ножницы, бумага, ящерица, Спок 🌶️
# Проиграв 10 раз Тимуру, Руслан понял, что так дело дальше не пойдет, и решил усложнить игру. 
# Теперь Тимур и Руслан играют в игру Камень, ножницы, бумага, ящерица, Спок. Помогите ребятам вновь бросить честный жребий и определить, 
# кто будет делать следующий модуль в новом курсе.


Timur = input()
Ruslan = input()

if Timur == 'камень' and Ruslan == 'ножницы' or Timur == 'камень' and Ruslan == 'ящерица':
    print('Тимур')

elif Timur == 'ножницы' and Ruslan == 'бумага' or Timur == 'ножницы' and Ruslan == 'ящерица':
    print('Тимур')

elif Timur == 'бумага' and Ruslan == 'камень':
    print('Тимур')

elif Timur == Ruslan :
    print('ничья')

elif Timur == 'ящерица' and Ruslan == 'Спок' or Timur == 'ящерица' and Ruslan == 'бумага':
    print('Тимур')

elif Timur == 'Спок' and Ruslan == 'ножницы' or Timur == 'Спок' and Ruslan == 'камень':
    print('Тимур')
else:
    print("Руслан")

# Вариант 2
options = ["камень", "ящерица", "Спок", "ножницы", "бумага"]
results = ["ничья", "Руслан", "Тимур", "Руслан", "Тимур"]

timur_move = input()
ruslan_move = input()

case = options.index(timur_move) - options.index(ruslan_move)
res = results[case]

print(res)

#------------------------------------------
# Орел и решка

# Дана строка текста, состоящая из букв русского алфавита "О" и "Р". 
# Буква "О" соответствует выпадению Орла, а буква "Р" – выпадению Решки. 
# Напишите программу, которая подсчитывает наибольшее количество подряд выпавших Решек.


our_str = input().split('О')

print(len(max(our_str)))

#------------------------------------------
# Роскомнадзор запретил букву а 🚫🌶️🌶️

# Необходимо написать программу, реализующую алгоритм написания этой песни. 
# Алгоритм выводит в конце предложения следующую в алфавитном порядке букву, 
# если она встречается в строке текста, а очередную строку отображает уже без этой буквы.


# word = input() + ' запретил букву'

alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 
            'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
word = input() + ' запретил букву'

for i in range(len(alphabet)):
    if alphabet[i] in word:
        print(word.strip(), alphabet[i])
        word = word.replace(alphabet[i], '')
        word = ' '.join(word.split())

# Кремниевая долина 🤖🌶️

# Искусственный интеллект Антон, созданный Гилфойлом, взломал сеть умных холодильников. 
# Теперь он использует их в качестве серверов "Пегого дудочника". Помогите владельцу фирмы отыскать 
# все зараженные холодильники. Для каждого холодильника существует строка с данными, состоящая из 
# строчных букв и цифр, и если в ней присутствует слово "anton" (необязательно рядом стоящие буквы, 
# главное наличие последовательности букв), то холодильник заражен и нужно вывести номер холодильника,
# нумерация начинается с единицы.

num = int(input("Введите количество холодильников: "))
infected = []

for i in range(1, num + 1):
    s = input(f"Введите строку холодильника № {i}: ")
    
    # Проверяем наличие последовательности "anton"
    target = "anton"
    index = 0
    
    for char in s:
        if char == target[index]:
            index += 1
            if index == len(target):
                infected.append(i)
                break

print("Зараженные холодильники:", infected)
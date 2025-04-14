# Упражнение 1

# Дополните приведённый ниже код так, чтобы он вывел сумму квадратов элементов списка numbers.


numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

summ = 0

list_one = list()

for i in numbers:

  list_one.append(int(i) * int(i))

print(sum(list_one))


#--------------------------------------------------------------------------------------------------


# Упражнение 2

# Значение функции 
# На вход программе подаются натуральное число n, а затем n целых чисел. Напишите программу, 
# которая для каждого введённого числа x выводит значение функции f(x)=x^2+2x+1, каждое на отдельной 
# строке.

n = int(input("Enter your number: "))

list_one = list()

list_two = list()

for i in range(n):

    num = int(input("Enter interger: "))

    list_one.append(num)

    our_func = num**2 + 2 * num + 1

    list_two.append(our_func)

print(*list_one, sep='\n')
print()
print(*list_two, sep='\n')

#--------------------------------------------------------------------------------------------------


# Упражнение 3

# Remove outliers

# При анализе данных, собранных в рамках научного эксперимента, бывает полезно удалить самое большое и 
# самое маленькое значение.

# На вход программе подаются натуральное число n, а затем n различных натуральных чисел. 
# Напишите программу, которая удаляет наименьшее и наибольшее значение из указанных чисел, 
# а затем выводит оставшиеся числа каждое на отдельной строке, не меняя их порядок.

n = int(input("Enter your number: "))

list_one = list()

for i in range(n):

    num = int(input("Enter integer: "))

    list_one.append(num)


list_one.remove(max(list_one))
list_one.remove(min(list_one))

print(*list_one, sep='\n')


#--------------------------------------------------------------------------------------------------


# Упражнение 4

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


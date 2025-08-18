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


#####################################################
## День 4. Тема урока: логические операторы         #
#####################################################

## Логические операторы
#---------------------------

# Как быть в ситуации, когда у нас есть несколько условий? В Python есть три логических оператора, которые позволяют создавать сложные условия:

# and — логическое умножение;
# or — логическое сложение;
# not — логическое отрицание.

# Оператор and
# Предположим, мы написали программу для учеников от двенадцати лет, которые учатся по крайней мере в 7 классе. 
# Доступ к ней тем, кто младше, надо запретить. Следующий код решает поставленную задачу:

age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
if age >= 12 and grade >= 7:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    
# Мы объединили два условия при помощи оператора and. Он означает, что в этом ветвлении блок кода выполняется только при 
# выполнении обоих условий одновременно!

# Оператор and может объединять произвольное количество условий:

age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and city == 'Москва':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    
# Оператор or
# Оператор or также применяется для объединения условий. Однако, в отличие от and, для выполнения блока кода достаточно выполнения хотя бы одного из условий.

city = input('В каком городе вы живете?: ')
if city == 'Москва' or city == 'Санкт-Петербург' or city == 'Екатеринбург':
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    
# Доступ будет разрешен в случае, если хотя бы одно из условий выполнится.

# Мы можем использовать оба логических оператора одновременно:

age = int(input('Сколько вам лет?: '))
grade = int(input('В каком классе вы учитесь?: '))
city = input('В каком городе вы живете?: ')
if age >= 12 and grade >= 7 and (city == 'Москва' or city == 'Санкт-Петербург'):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    

# Оператор not
# Оператор not позволяет инвертировать (т.е. заменить на противоположный) результат логического выражения. 
# Например, следующий код:

age = int(input('Сколько вам лет?: '))
if not (age < 12):
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    
# полностью эквивалентен коду:

age = int(input('Сколько вам лет?: '))
if age >= 12:
    print('Доступ разрешен.')
else:
    print('Доступ запрещен.')
    
# В первом примере мы поместили выражение age < 12 в скобки для того, чтобы было чётко видно, что мы применяем оператор 
# not к значению выражения age < 12, а не только к переменной age.

# Приоритеты логических операторов

# Логические операторы, подобно арифметическим операторам (+, -, *, /), имеют приоритет выполнения. Приоритет выполнения следующий: 
#   в первую очередь выполняется логическое отрицание not; 
#   далее выполняется логическое умножение and;
#   далее выполняется логическое сложение or.


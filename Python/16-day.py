#####################################################
## День 14. Тема урока: строки                      #
#####################################################

## Классификация символов
#------------------------

# Методы в этой группе классифицируют строку на основе содержащихся в ней символов.

## Метод isalnum()
#-----------------

# Метод isalnum() определяет, состоит ли исходная строка из буквенно-цифровых символов. Метод возвращает значение 
# True, если исходная строка является непустой и состоит только из буквенно-цифровых символов, или False 
# в противном случае.

# Приведённый ниже код:

s1 = 'abc123'
s2 = 'abc$*123'
s3 = ''

print(s1.isalnum())
print(s2.isalnum())
print(s3.isalnum())
# выводит:
#       True
#       False
#       False

# Обратите внимание, что метод isalnum() возвращает значение True даже в том случае, когда строка состоит только 
# из буквенных или только из цифровых символов.

# Приведённый ниже код:

s1 = 'BEEGEEK'
s2 = '2202'

print(s1.isalnum())
print(s2.isalnum())
# выводит:
#       True
#       True

## Метод isalpha()
#-----------------

# Метод isalpha() определяет, состоит ли исходная строка из буквенных символов. Метод возвращает значение True, 
# если исходная строка является непустой и состоит только из буквенных символов, или False в противном случае.

# Приведённый ниже код:

s1 = 'ABCabc'
s2 = 'abc123'
s3 = ''

print(s1.isalpha())
print(s2.isalpha())
print(s3.isalpha())
# выводит:
    # True
    # False
    # False

## Метод isdigit()
#-----------------

# Метод isdigit() определяет, состоит ли исходная строка только из цифровых символов. Метод возвращает значение 
# True, если исходная строка является непустой и состоит только из цифровых символов, или False в противном 
# случае.

# Приведённый ниже код:

s1 = '1234567'
s2 = 'abc123'
s3 = ''

print(s1.isdigit())
print(s2.isdigit())
print(s3.isdigit())
# выводит:
#       True
#       False
#       False


## Метод islower()
#-----------------

# Метод islower() определяет, являются ли все буквенные символы исходной строки строчными (имеют нижний регистр). 
# Метод возвращает значение True, если все буквенные символы исходной строки являются строчными, или False в 
# противном случае.

# Приведённый ниже код:

s1 = 'abc'
s2 = 'abc1$d'
s3 = 'Abc1$D'

print(s1.islower())
print(s2.islower())
print(s3.islower())
# выводит:
#       True
#       True
#       False

# Обратите внимание, что метод islower() игнорирует все небуквенные символы.

# Приведённый ниже код:

print('1234'.islower())
print('+-*/'.islower())
print('ab#%'.islower())

# выводит:
#       False
#       False
#       True

# В первом и втором случаях у нас в строках отсутствуют буквенные символы в нижнем регистре, поэтому метод 
# islower() и возвращает значение False.


## Метод isupper()
#-----------------

# Метод isupper() определяет, являются ли все буквенные символы исходной строки заглавными (имеют верхний регистр). 
# Метод возвращает значение True, если все буквенные символы исходной строки являются заглавными, или False в 
# противном случае.

# Приведённый ниже код:

s1 = 'ABC'
s2 = 'ABC1$D'
s3 = 'Abc1$D'

print(s1.isupper())
print(s2.isupper())
print(s3.isupper())
# выводит:
#       True
#       True
#       False

# Обратите внимание, что метод isupper() игнорирует все небуквенные символы.

# Приведённый ниже код:

print('5678'.isupper())
print('!?_&'.isupper())
print('AB%$'.isupper())
# выводит:
#       False
#       False
#       True

# В первом и втором случаях у нас в строках отсутствуют буквенные символы в верхнем регистре, поэтому метод 
# isupper() и возвращает значение False.

## Метод isspace()
#----------------

# Метод isspace() определяет, состоит ли исходная строка только из пробельных символов. Метод возвращает значение 
# True, если строка состоит только из пробельных символов, или False в противном случае.

# Приведённый ниже код:

s1 = '       '
s2 = 'abc1$d'

print(s1.isspace())
print(s2.isspace())
# выводит:
#       True
#       False

# Для пустой строки метод isspace() также возвращает False, так как в этом случае строка не состоит из пробельных 
# символов.

# Приведённый ниже код:

s1 = ''
print(s1.isspace())
# выводит:
#       False
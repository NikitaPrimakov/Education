# На вход программе подаётся строка текста. Если в этой строке буква «f» встречается только один раз, выведите 
# её индекс. Если она встречается два и более раза, выведите индексы её первого и последнего вхождения на одной 
# строке, разделённые символом пробела. Если буква «f» в данной строке не встречается, следует вывести «NO» 
# (без кавычек).

str_one = input("Enter your string: ")

flag = False

if str_one.count('f') == 1:
    
    index = str_one.find('f')
    flag = True

elif str_one.count('f') > 1:

    index_find = str_one.find('f')
    index_rfind = str_one.rfind('f')
    flag = True


if flag and str_one.count('f') == 1:
    print(index)
elif flag and str_one.count('f') > 1:
    print(index_find, index_rfind)
else:
    print("NO")

# альтернатива

s = input()
cnt = s.count("f")

if cnt == 0:
    print("NO")
elif cnt == 1:
    print(s.index("f"))
else:
    print(s.index("f"), s.rindex("f"))
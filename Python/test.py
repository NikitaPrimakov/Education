# Цифровым корнем числа n называется число, получающееся следующим образом: вычисляется сумма цифр числа n, 
# затем сумма цифр у получившегося числа и так далее, пока не получится однозначное число. Например, 
# цифровой корень числа 9875 равен 2: 

# 9+8+7+5=29
# 2+9=11
# 1+1=2

num = int(input("Введите число: "))

summOne = 0
summSecond = 0
summThree = 0

while num != 0:

    last_digit = num % 10
    num //= 10
    
    summOne += last_digit

if summOne <= 9:
    print(summOne)
else:
    while summOne != 0:
        last_digit = summOne % 10
        summOne //= 10
        summSecond += last_digit

    if summSecond <= 9:
        print(summSecond)

    else:
        while summSecond != 0:
            last_digit = summSecond % 10
            summSecond //= 10
            summThree += last_digit

        if summThree <= 9:
            print(summThree)
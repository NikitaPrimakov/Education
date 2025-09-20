import math
import random
import time

# Функция приветствия                       - done
# Функция получения числа попыток           - done
# Функция получения диапазона чисел         - done
# Функция игры пользователя                 - done
# Функция продолжения игры                  - done
# Функция прощания                          - done
# Функция выбора типа игры                  - done
# Компьютер угадывает ваше число 🤖         - done
# Секция основного кода игры пользователя   - done
# Секция основного кода игры компьютера     - done
# Запуск программы                          - done
#-------------------------------------------------

# Функция приветствия_1
def the_welcome_func_1():
    
    print("\n 🎲 Привет! Давай поиграем в игру Угадай число 🎲. \n")
    time.sleep(1)
    print("\n Ты загадываешь число, а я должен попробовать угадать его. 🤔 \n")
    time.sleep(1)

# Функция приветствия_2
def the_welcome_func_2():
    
    print("\n 🎲 Привет! Давай поиграем в игру Угадай число 🎲. \n")
    time.sleep(1)
    print("\n Я загадываю число, а ты должен попробовать угадать его. 🤔 \n")
    time.sleep(1)

# Функция получения числа попыток
def num_of_attempts():
    while True:
        try:
            attempts = int(input("\n Сколько попыток, чтобы разгадать число? 🤔 "))
            if attempts > 0:
                return attempts
            else:
                time.sleep(1)
                print("\n Попыток должно быть больше 0. Попробуй еще раз. 😔  ")
        except ValueError:
            time.sleep(1)
            print("\n Это не число. Попробуй еще раз. 😔 \n")

# Функция получения диапазона чисел
def choice_range():
    while True:
        try:
            time.sleep(1)
            range_start = int(input("\n 💭-- Выбери начало диапазона чисел: "))
            time.sleep(1)
            range_end = int(input("\n Выбери конец диапазона чисел: --💭 "))
            if range_start > range_end:
                time.sleep(1)
                print("\nКоненчное число должно быть больше начального.")
            else:
                return range_start, range_end
        except ValueError:
            time.sleep(1)
            print("\n Это не число. Попробуй еще раз. 😔 \n")

# Функция прощания
def the_goodbyes_func():

    time.sleep(1)
    print("\n Спасибо за игру! Приходи еще. \n")
    time.sleep(1)
    print("\n 👋👋👋👋👋👋👋👋👋👋👋👋👋👋 \n")

# Функция выбора типа игры
def choice_game():
    while True:
        try:
            time.sleep(1)
            choice = int(input("\n ---=== Выберите режим игры: ===--- \n '1' Для игры Угадай число против компьютера 🤖 " \
                    ": \n '2' для игры Угадай число в которой угадываешь ты: \n '3' Выйти из игры: \n"))
            if choice == 1:
                base_computer_game()
            elif choice == 2:
                base_users_play()
            elif choice == 3:
                the_goodbyes_func()
                break
            else:
                time.sleep(1)
                print("\n Некорректный выбор.")
        except ValueError:
            time.sleep(1)
            print("\n Это не число. Попробуй еще раз. 😔 \n")

# Функция игры пользователя
def users_play(range_start, range_end, attempts):

    the_desired_number = random.randint(range_start, range_end)

    for i in range(1, attempts + 1):

        users_number = int(input("\n Угадай число 🙂: "))

        if users_number == the_desired_number:
            time.sleep(1)
            print(f"\n Восхитительно! Ты угадал число за {i} попыток. \n")
            return
        if users_number > the_desired_number:
            time.sleep(1)
            print("\n Неверно ❌. Твое число больше искомого.")
            continue
        if users_number < the_desired_number:
            time.sleep(1)
            print("\n Неверно ❌. Твое число меньше искомого.")
            continue
    time.sleep(1)
    print("\n К сожалению, ты не угадал число. Все попытки были использованы.")
    print(f" Было загадано число {the_desired_number} 🤷‍♀️")

# Компьютер угадывает ваше число 🤖 
def computer_game(range_start, range_end, attempts):

    users_num = int(input("\n Загадайте число: "))
    left = range_start
    right = range_end
    time.sleep(3)
    for i in range(1, attempts + 1):
        middle = (left + right) // 2
        time.sleep(1)
        print(f"\n Я предполагаю, что число, которое вы загадали - это {middle}.")
        time.sleep(1)
        if middle == users_num:
            time.sleep(1)
            if i == 1:
                print(f"\n Восхитительно! Угадал число за {i} попытку. \n")
            elif i in [2, 3, 4]:
                print(f"\n Восхитительно! Угадал число за {i} попытки. \n")
            elif i > 4:
                print(f"\n Восхитительно! Угадал число за {i} попыток. \n")
            time.sleep(1)
            print(f" Искомое число: {middle}")
            break
        elif middle > users_num:
            time.sleep(1)
            print("\n Угу, вижу, что ваше число меньше моего...Думаю дальше")
            right = middle - 1
        else:
            time.sleep(1)
            print("\n Угу, вижу, что ваше число больше моего...Напрягаю микросхемы!")
            left = middle + 1
    time.sleep(3)
    if  users_num != middle:
        print("\n 🤖 К сожалению, компьютер не угадал число. Было загадано", users_num, "🤖" )

  

# Функция продолжения игры
def continue_game():
    time.sleep(1)
    answer = input("\n Хочешь продолжить игру? (да/нет): ")
    time.sleep(1)
    if answer in ['да', 'y', 'yes', 'д']:
        return True
    elif answer in ['нет', 'n', 'no', 'н']:
        return False
    else:
        time.sleep(1)
        print("\n 🚨 🚧 ☔ Некорректный ввод данных ❌. Попробуйте заново.")

# Компьютер угадывает ваше число 🤖 
def base_computer_game():

    the_welcome_func_1()

    while True:

        attempts = num_of_attempts()
        
        range_start, range_end = choice_range()

        computer_game(range_start, range_end, attempts)

        if continue_game():
            print(" Отлично! Начинаем игру заново.")
            time.sleep(1)
            print(" Загрузка...5%")
            time.sleep(1)
            print(" Загрузка...25%")
            time.sleep(1)
            print(" Загрузка...35%")
            time.sleep(1)
            print(" Загрузка...47%")
            time.sleep(1)
            print(" Загрузка...70%")
            time.sleep(1)
            print(" Загрузка...91%")
        else:
            break

    the_goodbyes_func()



# Секция основного кода игры пользователя
def base_users_play():

    the_welcome_func_2()

    while True:
        
        attempts = num_of_attempts()
        
        range_start, range_end = choice_range()
        
        users_play(range_start, range_end, attempts)
        
        if continue_game():
            print(" Отлично! Начинаем игру заново.")
            time.sleep(1)
            print(" Загрузка...5%")
            time.sleep(1)
            print(" Загрузка...25%")
            time.sleep(1)
            print(" Загрузка...35%")
            time.sleep(1)
            print(" Загрузка...47%")
            time.sleep(1)
            print(" Загрузка...70%")
            time.sleep(1)
            print(" Загрузка...91%")
        else:
            break

    the_goodbyes_func()

# Выбор игры
choice_game()
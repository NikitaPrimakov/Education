import random
import time


DIGITS = '0123456789'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_'


def welcom_func():
    time.sleep(1)
    print("\nПривет! Я генератор безопасных паролей. Давай начнем!")
    time.sleep(1)
    print("\nБезопасный пароль - это это комбинация уникальных символов, которую сложно угадать другим или взломать с " \
    "помощью современных технологий. Надежные пароли состоят из случайной комбинации букв, отличающихся по написанию, а " \
    "также содержат цифры и символы")
    time.sleep(1)


def start_generation():

    ask_users = input("\nХотите сгенерировать пароль да/нет? ")
    time.sleep(1)
    if ask_users in ['да', 'y', 'yes', 'д']:
        print("\nТода начнем!")
        time.sleep(1)
        print("\nЗагрузка...5%")
        time.sleep(1)
        print("Загрузка...25%")
        time.sleep(1)
        print("Загрузка...35%")
        time.sleep(1)
        print("Загрузка...47%")
        time.sleep(1)
        print("Загрузка...70%")
        time.sleep(1)
        print("Загрузка...91%")
    elif ask_users in ['нет', 'n', 'no', 'н']:
        goodbye()
    else:
        print("Некорректный ввод данных.")
    


def goodbye():
    time.sleep(1)
    print("\nЯ больше не нужен? Хорошо! До скорой встречи\n")
    time.sleep(1)


def password_option():
    time.sleep(1)
    print("\nО! Отлично! Тогда начнем с параметров Вашего пароля.")

    try:
        quantity_of_passwords = int(input("Введите необходимое количество паролей: "))
        time.sleep(1)
        print("\nНеобходимо ввести длину пароля. Минимальная длина пароля не менее 8 символов.")
        len_of_password = int(input("Введите длину пароля: "))
        time.sleep(1)
        return quantity_of_passwords, len_of_password
    except ValueError:
        print("\nНекорректный ввод данных.")


def generation_password(quantity_of_passwords, len_of_password):
        chars = ''

        include_digits = input("\nВключать ли символы '0123456789'? (да/нет): ")
        include_lowercase_letters = input("\nВключать ли символы 'abcdefghijklmnopqrstuvwxyz'? (да/нет): ")
        include_uppercase_letters = input("\nВключать ли символы 'abcdefghijklmnopqrstuvwxyz'? (да/нет): ")
        include_punctuation = input("\nВключать ли символы '!#$%&*+-=?@^_'? (да/нет): ")

        if include_digits in ['да', 'y', 'yes', 'д']:
            chars += chars + DIGITS

        if include_lowercase_letters in ['да', 'y', 'yes', 'д']:
            chars += chars + LOWERCASE_LETTERS
    

        if include_uppercase_letters in ['да', 'y', 'yes', 'д']:
            chars += chars + UPPERCASE_LETTERS

        if include_punctuation in ['да', 'y', 'yes', 'д']:
            chars += chars + PUNCTUATION

        list_of_passwords = list()

        password = ''

        while quantity_of_passwords > 0:
    
            for i in range(len_of_password):

                password += random.choice(chars)
    
            quantity_of_passwords -= 1
            list_of_passwords.append(password)
            password = ''

        print(*list_of_passwords, sep='\n')


def start():
   
    welcom_func()

    while True:
    
        start_generation()

        quantity_of_passwords, len_of_password = password_option()

        generation_password(quantity_of_passwords, len_of_password)


start()
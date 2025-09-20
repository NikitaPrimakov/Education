import time

UPPER_ENG_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_ENG_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
UPPER_RUS_ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
LOWER_RUS_ALPHABET = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'

def welcom_func():
    print("\nПривет! Запускаем программу 'Шифр Цезаря'.")
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
    time.sleep(1)
    print("Запуск...")


def choice_direction():
    while True:
        time.sleep(1)
        users_choice = input("\nЧто интересует шифрование/дешифрование: ")
        if users_choice == 'шифрование':
            time.sleep(1)
            choice_language_encryption()
        elif users_choice == 'дешифрование':
            time.sleep(1)
            choice_language_decryption()
        else:
            time.sleep(1)
            print('\nНеобходимо ввести "шифрование" или "дешифрование".')


def step():
    while True:
        try:
            time.sleep(1)
            step = int(input("\nВведите шаг сдвига: "))
            print("\nПроверка...")
            time.sleep(1)
            print("Все верно!")
            return(step)
        except ValueError:
            time.sleep(1)
            print("\nПроверка...")
            time.sleep(1)
            print("Введите целое число!")
            

#----------------------------шифрование----------------------------
def choice_language_encryption():
    while True:
        time.sleep(1)
        language_encryption = input("\nВведите какой язык будем использовать rus/eng: ")
        if language_encryption == 'rus':
            text = checker_encryption_rus()
            encryption_rus(text, step)
            break
        elif language_encryption == 'eng':
            text = checker_encryption_eng()
            encryption_eng(text)
            break
        else:
            time.sleep(1)
            print('\nНеобходимо ввести "rus" или "eng".')


def checker_encryption_rus():
    while True:
        print("\nВы выбрали: шифрование на русском языке!")
        text = input("Введите текст, который необходимо зашифровать: ")

        has_english = False
        for char in text:
            if char in UPPER_ENG_ALPHABET or char in LOWER_ENG_ALPHABET:
                has_english = True
                break

        if has_english:
            print("\nПроверяю введенные данные на ошибки...")
            time.sleep(3)
            print("Неверно!")
            print('\nОшибка: обнаружены английские буквы')
            continue 

        print("\nПроверяю введенные данные на ошибки...")
        time.sleep(3)
        print("Все верно!")
        return text
    

def checker_encryption_eng():
    while True:
        print("\nВы выбрали: шифрование на английском языке!")
        text = input("Введите текст, который необходимо зашифровать: ")
        
        has_russian = False
        for char in text:
            if char in UPPER_RUS_ALPHABET or char in LOWER_RUS_ALPHABET:
                has_russian = True
                break
        
        if has_russian:
            print("\nПроверяю введенные данные на ошибки...")
            time.sleep(3)
            print("Неверно!")
            print('Ошибка: обнаружены русские буквы')
            continue

        print("\nПроверяю введенные данные на ошибки...")
        time.sleep(3)
        print("Все верно!")
        return text 


def encryption_rus(text, step):
    while True:
        try:
            time.sleep(1)
            step = int(input("\nВведите шаг сдвига: "))
            print("\nПроверка...")
            time.sleep(1)
            print("Все верно!")

            alphas = 32
            low_alphabet = LOWER_RUS_ALPHABET
            upp_alphabet = UPPER_RUS_ALPHABET

            for i in range(len(text)):
                if text[i].isalpha():
                    if text[i] == text[i].lower():
                        place = low_alphabet.index(text[i])
                        index = (place + int(step)) % alphas
                    if text[i] == text[i].upper():
                        place = upp_alphabet.index(text[i])
                        index = (place + int(step)) % alphas
                    
                    if text[i] == text[i].lower():
                        print(low_alphabet[index], end='')
                    if text[i] == text[i].upper():
                        print(upp_alphabet[index], end='')
                else:
                    print(text[i], end='')

        except ValueError:
            time.sleep(1)
            print("\nПроверка...")
            time.sleep(1)
            print("Введите целое число!")

def encryption_eng(text):
    while True:
        try:
            time.sleep(1)
            step = int(input("\nВведите шаг сдвига: "))
            print("\nПроверка...")
            time.sleep(1)
            print("Все верно!")

            alphas = 26
            low_alphabet = LOWER_ENG_ALPHABET
            upp_alphabet = UPPER_ENG_ALPHABET

            for i in range(len(text)):
                if text[i].isalpha():
                    if text[i] == text[i].lower():
                        place = low_alphabet.index(text[i])
                        index = (place + int(step)) % alphas
                    if text[i] == text[i].upper():
                        place = upp_alphabet.index(text[i])
                        index = (place + int(step)) % alphas
                    
                    if text[i] == text[i].lower():
                        print(low_alphabet[index], end='')
                    if text[i] == text[i].upper():
                        print(upp_alphabet[index], end='')
                else:
                    print(text[i], end='')            


        except ValueError:
            time.sleep(1)
            print("\nПроверка...")
            time.sleep(1)
            print("Введите целое число!")
#----------------------------шифрование----------------------------



#----------------------------дешифрование----------------------------
def choice_language_decryption():
    while True:
        time.sleep(1)
        language_encryption = input("\nВведите какой язык будем использовать rus/eng: ")
        if language_encryption == 'rus':
            text = checker_decryption_rus()
            decryption_rus(text,step)
            break
        elif language_encryption == 'eng':
            text = checker_decryption_eng()
            decryption_eng(text,step)
            break
        else:
            time.sleep(1)
            print('\nНеобходимо ввести "rus" или "eng".')


def checker_decryption_rus():
    while True:
        print("\nВы выбрали: дешифрование на русском языке!")
        text = input("Введите текст, который необходимо зашифровать: ")
        
        has_english = False
        for char in text:
            if char in UPPER_ENG_ALPHABET or char in LOWER_ENG_ALPHABET:
                has_english = True
                break
        
        if has_english:
            print("\nПроверяю введенные данные на ошибки...")
            time.sleep(3)
            print("Неверно!")
            print('Ошибка: обнаружены английские буквы')
            continue

        print("\nПроверяю введенные данные на ошибки...")
        time.sleep(3)
        print("Все верно!\n")
        return text
    

def checker_decryption_eng():
    while True:
        print("\nВы выбрали: дешифрование на английском языке!")
        text = input("Введите текст, который необходимо зашифровать: ")
        
        has_english = False
        for char in text:
            if char in UPPER_RUS_ALPHABET or char in LOWER_RUS_ALPHABET:
                has_english = True
                break
        
        if has_english:
            print("\nПроверяю введенные данные на ошибки...")
            time.sleep(3)
            print("Неверно!")
            print('Ошибка: обнаружены английские буквы')
            continue

        print("\nПроверяю введенные данные на ошибки...")
        time.sleep(3)
        print("Все верно!")
        return text
    

def decryption_rus(text,step):
    while True:
        try:
            time.sleep(1)
            step = int(input("\nВведите шаг сдвига: "))
            print("\nПроверка...")
            time.sleep(1)
            print("Все верно!")

            alphas = 32
            low_alphabet = LOWER_RUS_ALPHABET
            upp_alphabet = UPPER_RUS_ALPHABET

            for i in range(len(text)):
                if text[i].isalpha():
                    if text[i] == text[i].lower():
                        place = low_alphabet.index(text[i])
                        index = (place - int(step)) % alphas
                    if text[i] == text[i].upper():
                        place = upp_alphabet.index(text[i])
                        index = (place - int(step)) % alphas
                    
                    if text[i] == text[i].lower():
                        print(low_alphabet[index], end='')
                    if text[i] == text[i].upper():
                        print(upp_alphabet[index], end='')
                else:
                    print(text[i], end='')

        except ValueError:
            time.sleep(1)
            print("\nПроверка...")
            time.sleep(1)
            print("Введите целое число!")

    
def decryption_eng(text, step):
    while True:
        try:
            time.sleep(1)
            step = int(input("\nВведите шаг сдвига: "))
            print("\nПроверка...")
            time.sleep(1)
            print("Все верно!")

            alphas = 26
            low_alphabet = LOWER_ENG_ALPHABET
            upp_alphabet = UPPER_ENG_ALPHABET

            for i in range(len(text)):
                if text[i].isalpha():
                    if text[i] == text[i].lower():
                        place = low_alphabet.index(text[i])
                        index = (place - int(step)) % alphas
                    if text[i] == text[i].upper():
                        place = upp_alphabet.index(text[i])
                        index = (place - int(step)) % alphas
                    
                    if text[i] == text[i].lower():
                        print(low_alphabet[index], end='')
                    if text[i] == text[i].upper():
                        print(upp_alphabet[index], end='')
                else:
                    print(text[i], end='')

        except ValueError:
            time.sleep(1)
            print("\nПроверка...")
            time.sleep(1)
            print("Введите целое число!")
#----------------------------дешифрование----------------------------

def continue_prog():
    time.sleep(1)
    answer = input("\n Хочешь начать заново? (да/нет): ")
    time.sleep(1)
    if answer in ['да', 'y', 'yes', 'д']:
        return True
    elif answer in ['нет', 'n', 'no', 'н']:
        return False
    else:
        time.sleep(1)
        print("\n 🚨 🚧 ☔ Некорректный ввод данных ❌. Попробуйте заново.")

def the_goodbyes_func():

    time.sleep(1)
    print("\n Спасибо! Приходи еще. \n")
    time.sleep(1)
    print("\n 👋👋👋👋👋👋👋👋👋👋👋👋👋👋 \n")


def start():

    welcom_func()

    while True:
        
        choice_direction()

        if continue_prog():
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

start()
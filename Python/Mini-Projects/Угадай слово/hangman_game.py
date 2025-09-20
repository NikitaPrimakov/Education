# Игра "Угадай слово"


import random
import time

UPPER_RUS_ALPHABET = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

LIST_OF_WORDS = ['КЛЮЧ', 'КНИГА', 'ЕНОТ', 'МАШИНКА', 'КОРОВА', 'ТЕЛЕЖКА', 'ШЛЕМ', 'КНОПКА', 'ШНУР', 'ЧЕРНЫЙ', 
'ВЛАСТЕЛИН', 'СКАЙП', 'ДУБ', 'ЧАСЫ', 'ТРУБА', 'ЕЛКА', 'ИНСТИТУТ', 'КОРОБКА', 'ТАБЛИЧКА', 'ВОДА', 'СКОВОРОДА', 
'МНОГОНОЖКА', 'ЕВРЕЙ', 'ТЕРМИТ', 'КАЧЕК', 'РУЛОН', 'МАГНИТОФОН', 'НОГА', 'СЛОН', 'МИКРОВОЛНОВКА', 'ТОРТ', 'МАК', 
'ДЫМ', 'ЧАЙКА', 'ВАЛЕТ', 'ПЛИНТУС', 'ШАПКА', 'ДИНОЗАВР', 'ТОРШЕР', 'БАЛАЛАЙКА', 'БАНКА', 'ЯХТА', 'ОВЦА', 'БАНАН', 
'ДУБ', 'АНИМЕ', 'РАДУГА', 'БУКВА', 'ВЕЛОСИПЕД', 'БАНДЖО', 'ГОЛУБЬ', 'ВИНТОВКА', 'КУБОК', 'ЖАСМИН', 'ТЕЛЕФОН', 
'АНДРОИД', 'ГОРА', 'ХАЛАТ', 'ЖЕТОН', 'ОБОД', 'МЫЛО', 'ЙОГ', 'ШИШКА', 'ДОЛЛАР', 'КОЛОНКА', 'КУБИК', 'ОМАР', 
'РАКЕТА', 'МОРКОВКА', 'ЗЕРКАЛО', 'МОЛОТ', 'ВОЗДУХ', 'ЗМЕЙ', 'ЁЖ', 'ПАЛЬМА', 'МАСЛО', 'ДИДЖЕЙ', 'МЕШОК', 'ТЮБИК', 
'МОЗГ', 'ПОЕЗД', 'РОЗЕТКА', 'ПАРАШЮТИСТ', 'БЕЛКА', 'ШПРОТЫ', 'САМОСВАЛ', 'ПАЗЛ', 'БУТЫЛКА', 'КРЕМЛЬ', 'ПИЦЦА', 
'МАКАРОНЫ', 'КОВЕР', 'ЗУБЫ', 'ЯРЛЫК', 'КАШАЛОТ', 'МАРС', 'ШАКАЛ', 'ПОМАДА', 'ДЖИП', 'ЛЕЩ', 'КАМЕНЬ', 'ДИСК']

 
# Функция приветствия
def welcome_of_game():

    print('\nПриветстувую тебя в игре "Угадай слово"')
    time.sleep(1)
    print('Принцип игры: я загадываю слово, а ты (пользователь) должен угадать!')
    while True:
        time.sleep(1)
        name_of_user = input("\nНачнем со знакомства. Как тебя зовут? ")
        if name_of_user:
            time.sleep(1)
            print(f"Очень приятно, {name_of_user}!")
            return True
        else:
            time.sleep(1)
            print("\nВаше имя не задано! Прошу его написать!")
            time.sleep(1)
            return False

# Функция прощания
def the_goodbyes_func():

    time.sleep(1)
    print("\nСпасибо за игру! Приходи еще.")
    print("👋👋👋👋👋👋👋👋👋👋👋👋👋👋 \n")


def choice_game():
    while True:
        try:
            time.sleep(1)
            choice = int(input('\nВыберите режим игры:\n"1" Игра "Угадай слов" 🤖 ' \
                    '\n"2" Выйти из игры \n'))
            if choice == 1:
                play_game()
            elif choice == 2:
                the_goodbyes_func()
                break
            else:
                time.sleep(1)
                print("\n Некорректный выбор.")
        except ValueError:
            time.sleep(1)
            print("\n Это не число. Попробуй еще раз. 😔 \n")
            

def guessing_a_word():
    time.sleep(1)
    print("\nЗагадываю слово")
    time.sleep(3)
    print("Ухты! Очень интересное слово!")
    random_word = random.choice(LIST_OF_WORDS).upper()
    word_completion = '_' * len(random_word)          # строка, содержащая символы _ на каждую букву задуманного слова
    time.sleep(1)
    print(f"\nА вот и само слово: {word_completion}. Оно состоит из {len(random_word)} букв.")
    print("У тебя есть 6 попыток, чтобы его отгадать!")
    return random_word, word_completion

def hangman_game(random_word, word_completion):
    
    word_completion_list = list(word_completion)

    random_word_list = list(random_word)

    tries = 6

    while tries != 0:

        some_letter = input("\nВведите букву, которая может быть в данном слове: ").upper()

        if some_letter in random_word:
            for i in range(len(random_word_list)):
                if some_letter == random_word_list[i]:
                    word_completion_list[i] = some_letter
                    print(*word_completion_list)
            if word_completion_list == random_word_list:
                break
        elif some_letter not in random_word:
            tries -= 1
            if tries == 5:
                print(                '''
                --------
                |      |
                |      O
                |    
                |      
                |     
                -
                ''')

            elif tries == 4:
                print(                '''
                --------
                |      |
                |      O
                |      |
                |      |
                |     
                -
                ''')

            elif tries == 3:
                print(                '''
                --------
                |      |
                |      O
                |     \\|
                |      |
                |     
                -
                ''')

            elif tries == 2:
                print(                '''
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |      
                -
                ''')

            elif tries == 1:
                print(                '''
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / 
                -
                ''')

            elif tries == 0:
                print(                '''
                --------
                |      |
                |      O
                |     \\|/
                |      |
                |     / \\
                -
                ''')

                print("Ты проиграл!\n")
                return False
        
def continue_game():
    time.sleep(1)
    answer = input("\nХочешь продолжить игру? (да/нет): ")
    time.sleep(1)
    if answer in ['да', 'y', 'yes', 'д']:
        return True
    elif answer in ['нет', 'n', 'no', 'н']:
        return False
    else:
        time.sleep(1)
        print("\n🚨 🚧 ☔ Некорректный ввод данных ❌. Попробуйте заново.")


def play_game():

    welcome_of_game()

    while True:

        random_word, word_completion = guessing_a_word()
        
        hangman_game(random_word, word_completion)

        if continue_game():
            print("Отлично! Начинаем игру заново.")
            time.sleep(1)
            print("Загрузка...5%")
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
        else:
            break

    the_goodbyes_func()


choice_game()  
# Magic ball 8
import random
import time


def welcome_func():

    time.sleep(1)
    print("\nПривет!👋 Я магический шар.🎱 Отвечу на любой твой вопрос.😎")
    print("Давай знакомиться.🙂\n")

    name_of_users = input("Как тебя зовут?🙂 ")

    if name_of_users:
        time.sleep(1)
        print(f"\nОчень приятно познакомиться, {name_of_users}❤️❤️❤️")
        time.sleep(1)
        users_questions()
    return name_of_users
    


def users_questions():

    ask_me = input("\nСпроси меня, на что хочешь узнать ответ: ")

    if ask_me:
        time.sleep(1)
        print(random.choice(['\nУхты! Очень интересный вопрос🤔', '\nХммм, давай попробую ответить🤔', '\nОтличный вопрос!🤔',
                            '\nНа этот вопрос будет трудно ответить, но я попробую.🤔']))
    else:
        print("\nНекоторректный вопрос.❌\n")
    


def magic_ball_8(name_of_users):

    positive_ones = {1: 'Бесспорно ✅', 2: 'Предрешено ✅', 3: 'Никаких сомнений ✅', 4: 'Определённо да ✅', 
                     5: 'Можешь быть уверен в этом ✅'}
    
    hesitantly_positive = {6: 'Мне кажется - да ☑️', 7: 'Вероятнее всего ☑️', 8: 'Хорошие перспективы ☑️', 
                           9: 'Знаки говорят - да ☑️', 10: 'Да ☑️'}
    
    neutral = {11: 'Пока неясно, попробуй снова 🙁', 12: 'Спроси позже 🙁', 13: 'Лучше не рассказывать 🙁', 
                           14: 'Сейчас нельзя предсказать 🙁', 15: 'Сконцентрируйся и спроси опять 🙁'}

    negative = {16: 'Даже не думай ❌', 17: 'Мой ответ - нет ❌', 18: 'По моим данным - нет ❌', 
                           19: 'Перспективы не очень хорошие ❌', 20: 'Весьма сомнительно ❌'}
    
    num_of_answer = random.randint(1, 21)

    if num_of_answer in [1, 2, 3, 4, 5]:
        time.sleep(3)
        print(f"\nОтвет: {positive_ones[num_of_answer]}, {name_of_users}\n")
    
    elif num_of_answer in [6, 7, 8, 9, 10]:
        time.sleep(3)
        print(f"\nОтвет: {hesitantly_positive[num_of_answer]}, {name_of_users}\n")
    
    elif num_of_answer in [11, 12, 13, 14, 15]:
        time.sleep(3)
        print(f"\nОтвет: {neutral[num_of_answer]}, {name_of_users}\n")
    
    elif num_of_answer in [16, 17, 18, 19, 20]:
        time.sleep(3)
        print(f"\nОтвет: {negative[num_of_answer]}, {name_of_users}\n")
    return num_of_answer


def repeat_game(num_of_answer):
    if num_of_answer in [11, 12, 13, 14, 15]:
        answer = input("\nХочешь продолжить игру? (да/нет): ")
        time.sleep(1)
        if answer in ['да', 'y', 'yes', 'д']:
            return True
        elif answer in ['нет', 'n', 'no', 'н']:
            return False
    else:
        return False


def goodbye():
    time.sleep(1)
    print("\nСпасибо за игру! Приходи еще. \n")
    time.sleep(1)
    print("\n👋👋👋👋👋👋👋👋👋👋👋👋👋👋 \n")


def start_game():

        while True:

            name_of_users = welcome_func()

            num_of_answer = magic_ball_8(name_of_users)

            if repeat_game(num_of_answer):

                time.sleep(1)
                print("\nСбрасываю предыдущий результат...5%")
                time.sleep(1)
                print("Сбрасываю предыдущий результат...9%")
                time.sleep(1)
                print("Сбрасываю предыдущий результат...14%")
                time.sleep(1)
                print("Сбрасываю предыдущий результат...25%")
                time.sleep(1)
                print("Сбрасываю предыдущий результат...56%")
                time.sleep(1)
                print("Сбрасываю предыдущий результат...75%")
                time.sleep(1)
                print("Сбрасываю предыдущий результат...88%")
                time.sleep(1)
                print("Запуск...")
            else:
                break

        goodbye()


start_game()
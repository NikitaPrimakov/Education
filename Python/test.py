# Аве, Цезарь 🌶️
# На вход программе подаётся строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными. Гарантируется, что между различными словами присутствует один пробел.

# Формат входных данных 
# На вход программе подаётся строка текста на английском языке.

# Формат выходных данных
# Программа должна вывести зашифрованный текст в соответствии с условием задачи.

def encription(text):

    for i in range(len(text)):

        for j in text[i]:

            print(len(text[i]))

text = input("Введите текст, который необходимо зашифровать ").split(' ')

encription(text)
#----
def unique(answer_text: str) -> str:

    list_one = []
    answer_split = answer_text.split(' ')
    for i in answer_split:
        count_of_word = answer_split.count(i)
        if count_of_word < 2:
            list_one.append(i)
        else:
            continue
    return list_one
    

answer_text = input()
unique_word = unique(answer_text)
print(*unique_word, sep=' ')
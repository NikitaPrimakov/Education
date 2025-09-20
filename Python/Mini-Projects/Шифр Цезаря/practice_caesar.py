# Аве, Цезарь 🌶️
# На вход программе подаётся строка текста на английском языке, в которой нужно зашифровать все слова. Каждое слово строки следует зашифровать с помощью шифра Цезаря (циклического сдвига на длину этого слова). Строчные буквы при этом остаются строчными, а прописные – прописными. Гарантируется, что между различными словами присутствует один пробел.

# Формат входных данных 
# На вход программе подаётся строка текста на английском языке.

# Формат выходных данных
# Программа должна вывести зашифрованный текст в соответствии с условием задачи.

UPPER_ENG_ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWER_ENG_ALPHABET = 'abcdefghijklmnopqrstuvwxyz'         

def encription(text):

    alphas = 26
    low_alphabet = LOWER_ENG_ALPHABET
    upp_alphabet = UPPER_ENG_ALPHABET

    for word in text:
    
        step = 0
        count = 0
        encrypted_words = list()

        for i in word:

            if i.isalpha():
                count += 1
                step = count

        for char in word:
            if char.isalpha():
                if char.islower():
                    place = low_alphabet.index(char)
                    index = (place + step) % alphas
                    encrypted_words.append(low_alphabet[index])
                if char.isupper():
                    place = upp_alphabet.index(char)
                    index = (place + step) % alphas
                    encrypted_words.append(upp_alphabet[index])
            else:
                encrypted_words.append(char)
        print(''.join(encrypted_words), end=' ')

text = input().split(' ')

encription(text)
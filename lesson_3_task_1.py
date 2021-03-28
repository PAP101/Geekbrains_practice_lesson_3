list_words = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре', 'five': 'пять', 'six': 'шесть',
              'seven': 'семь', 'eight': 'восемь', 'nine': 'девять', 'ten': 'десять'}
word = input('Введите число от одного до десяти на английском языке')


def num_translate():
    print(list_words[word])


num_translate()

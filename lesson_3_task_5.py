nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]


def get_jokes():
    from random import randrange

    random_nouns_idx = randrange(len(nouns))
    # Объявлем случайное число в предела длинны списка существительных
    random_nouns = nouns[random_nouns_idx]
    # Присваиваем аргументу существителбного существительное под данным номером из списка.
    nouns.remove(random_nouns)
    # Вырезаем это слово из списка

    from random import randrange

    random_adverbs_idx = randrange(len(adverbs))
    # Объявлем случайное число в предела длинны списка наречий
    random_adverbs = adverbs[random_adverbs_idx]
    # Присваиваем аргументу наречия наречие под данным номером из списка.
    adverbs.remove(random_adverbs)
    # Вырезаем это слово из списка

    from random import randrange

    random_adjectives_idx = randrange(len(adjectives))
    # Объявлем случайное число в предела длинны списка прилагательных
    random_adjectives = adjectives[random_adjectives_idx]
    # Присваиваем аргументу прилагательного прилагательное под данным номером из списка.
    adjectives.remove(random_adjectives)
    # Вырезаем это слово из списка

    print(random_nouns, random_adverbs, random_adjectives)
    # Выводим переменные на экран.


get_jokes()

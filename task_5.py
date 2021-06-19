from random import choice, sample


def get_jokes(quantity=1, flag=False):
    """
    joke making function
    :param quantity: quantity of jokes
    :param flag: allow a repeat of words in joke
    :return: list of jokes
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    jokes = []
    if flag:
        nouns.extend(adverbs)
        nouns.extend(adjectives)
        for _ in range(quantity):
            jokes.append(' '.join([choice(nouns), choice(nouns), choice(nouns)]))
        return jokes
    else:

        for _ in range(quantity):
            jokes.append(' '.join([choice(nouns), choice(adverbs), choice(adjectives)]))
        return jokes


print(get_jokes(2, True))

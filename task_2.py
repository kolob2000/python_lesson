def num_translate(digit_name: str):
    digits = {
        'zero': 'ноль',
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if digit_name.istitle():
        if digits.get(digit_name.lower()) is None:
            return None
        else:
            return digits.get(digit_name.lower()).title()
    else:
        return digits.get(digit_name)


translation = num_translate(input('Введете английское название цифры: '))
print(f'Перевод вашей цифы: {translation}')

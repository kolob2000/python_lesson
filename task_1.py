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
    return digits.get(digit_name)


translation = num_translate(input('Введете название числа буквами: '))
print(f'Перевод вашего числа: {translation}')

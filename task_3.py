class ListDigitException(Exception):
    def __init__(self, text):
        self.txt = text

    def __str__(self):
        return self.txt


if __name__ == '__main__':
    digit_list = []
    while True:
        try:
            digit = input('Введите число или для конца ввода ведите стоп - ')
            if digit.isdigit():
                digit_list.append(int(digit))
            elif digit.lower() == 'стоп':
                break
            else:
                raise ListDigitException('Ошибка. Вводится должны только числа или слово стоп')
        except ListDigitException as err:
            print(err)

    print(digit_list)

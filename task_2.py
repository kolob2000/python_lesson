class DivisionByZero(Exception):
    def __init__(self, text):
        self.txt = text

    def __str__(self):
        return self.txt


def div_true(a: float, b: float) -> float:
    try:
        if b == 0:
            raise DivisionByZero('На ноль делить нельзя.')
    except ValueError:
        print('Вы ввели не число')
    except DivisionByZero as err:
        print(err)
    else:
        print(f'Результа - {a / b}')


if __name__ == '__main__':
    div_true(int(input('Введите делимое - ')), int(input('Введите делитель -')))

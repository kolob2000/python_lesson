class Cell:
    def __init__(self, nucleus):
        self.nucleus = nucleus

    def __add__(self, other):
        return Cell(self.nucleus + other.nucleus)

    def __sub__(self, other):
        result = self.nucleus - other.nucleus
        if result > 0:
            return Cell(result)
        else:
            print('Невозможно выполнить вычитание, общая разность меньше нуля')

    def __mul__(self, other):
        return Cell(self.nucleus * other.nucleus)

    def __truediv__(self, other):
        return Cell(self.nucleus // other.nucleus)

    def __str__(self):
        return str(self.nucleus)

    def make_order(self, cls, row):
        quantity = cls.nucleus // row
        for i in range(quantity):
            if i < quantity - 1:
                print('*' * row, end='\\n')
            else:
                if cls.nucleus % row > 0:
                    print('*' * row, end='')
                    print('\\n' + '*' * (cls.nucleus % row))
                else:
                    print('*' * row, end='')
        print()


if __name__ == '__main__':
    cell = Cell(63)
    cell.make_order(cell, 7)
    cell_2 = Cell(34)
    print(cell + cell_2)
    print(cell - cell_2)
    print(cell * cell_2)
    print(cell / cell_2)

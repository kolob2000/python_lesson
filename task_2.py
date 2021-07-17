from abc import ABC, abstractmethod
import abc


class Clothes(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @property# пайчарм пишет что abstractproperty больше не поддерживается
    @abstractmethod
    def size(self):
        pass

    @abstractmethod
    def __add__(self, other):
        pass

class Costume(Clothes):
    def __init__(self, h):
        self.h = h

    @property
    def size(self):
        return 2 * self.h + 0.3

    def __add__(self, other):
        return self.size + other.size




class Coat(Clothes):
    def __init__(self, v):  # только я так и не понял какой английское слово на v имели ввиду🤔
        self.v = v

    @property
    def size(self):
        return self.v / 6.5 + 0.5 #Какие то странные формулы нереальные расчеты дают

    def __add__(self, other):
        return self.size + other.size


if __name__ == '__main__':
    costume = Costume(174)
    print(f'Расход ткани для костюма: {costume.size}')

    coat = Coat(105)
    print(f'Расход ткани для пальто: {coat.size}')

    print(f'Общий размер: {coat + costume}')

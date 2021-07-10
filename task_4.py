def car_count_static_method():
    print(f'В городе теперь {Car.car_count} автомобиля(ей)')


class Car:
    car_count = 0
    is_go = False
    is_stop = True

    def __init__(self, speed: int, color: str, name: str, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        Car.car_count += 1
        if self.speed > 0:
            self.show_speed()
            self.go(self.speed)

    def go(self, speed: int):
        if self.is_go:
            print(f'Чего спишь то? {self.name} полчаса, как едет!')
        else:
            self.is_go = True
            self.is_stop = False
            print(f'Заводи - {self.name} поехал!')
            self.speed = speed
            print(f'Скорость {self.name} {self.speed} км')

    def stop(self):
        if self.is_stop:
            print(f'Даааа... Тяжелый случай.  {self.name} и так стоит!')
        else:
            print(f'{self.name} останавливается')
            self.is_go = False
            self.is_stop = True

    def turn(self, direction=''):
        if direction == '':
            print(f'{self.name} едет прямо')
        else:
            print(f'Повернул  {direction}')

    def show_speed(self):
        if self.speed > 120:
            print(f'Вот это драйв) {self.name} летит!')
        else:
            print(f'Скорость {self.name} {self.speed} км')


class TownCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Потише бручку {self.name}! Не завывай вокруг пешеходы.')


class SportCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police=False):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police=False):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Не спеши {self.name}- работа не волк в лес не убежит)')


class PoliceCar(Car):
    def __init__(self, speed: int, color: str, name: str, is_police=True):
        super().__init__(speed, color, name, is_police)


police = PoliceCar(0, 'black', 'Nissan Skyline')
police.go(120)

family = TownCar(65, 'blue', 'VW Polo')

deliver = WorkCar(45, 'white', 'Газель')

driver = SportCar(180, 'red', 'Mitsubishi GTO')

driver.stop()
driver.stop()

car_count_static_method()

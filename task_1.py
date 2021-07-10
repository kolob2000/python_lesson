import time
from colorama import Back, Fore


class TrafficLight:
    __color = ('red', 'yellow', 'green', 'yellow')

    def running(self):
        while True:
            for i in self.__color:
                color = Fore.BLACK
                if i == 'red':
                    timer = 7
                    bg_color = Back.RED
                elif i == 'yellow':
                    timer = 2
                    bg_color = Back.YELLOW
                else:
                    timer = 10
                    bg_color = Back.GREEN
                print(f'{bg_color}{color}{i}', end='')
                time.sleep(timer)
                print(end='\r')


TrafficLightObject = TrafficLight()

TrafficLightObject.running()

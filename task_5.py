class Stationery:
    def __init__(self):
        self.name = 'stationery'

    def draw(self):
        print(f"I'm just a {self.name}. I must draw now but i don't no how i can draw, yet (")


class Pen(Stationery):
    def __init__(self):
        self.name = 'pen'

    def draw(self):
        print(f"I'm a {self.name}. I draw with grey color and thin writing")


class Pencil(Stationery):
    def __init__(self):
        self.name = 'pencil'

    def draw(self):
        print(f"I'm a {self.name}. I draw with blue color and thin writing")


class Handle(Stationery):
    def __init__(self):
        self.name = 'handle'

    def draw(self):
        print(f"I'm a {self.name}. I draw with black color and thick writing")


stationery = Stationery()
stationery.draw()
pencil = Pencil()
pencil.draw()
pen = Pen()
pen.draw()
handle = Handle()
handle.draw()

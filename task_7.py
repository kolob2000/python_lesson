class ComplexNumbers:
    def __init__(self, real: float, image: float):
        self.real = real
        self.image = image

    def __add__(self, other):
        real = self.real + other.real
        image = self.image + other.image
        return ComplexNumbers(real, image)

    def __sub__(self, other):
        real = self.real - other.real
        image = self.image - other.image
        return ComplexNumbers(real, image)

    def __str__(self):
        return f'{self.real} + {self.image}i'


z_1 = ComplexNumbers(1, 2)
z_2 = ComplexNumbers(2, 3)

print(z_1)
print(z_1 + z_2)
print(z_2 - z_1)

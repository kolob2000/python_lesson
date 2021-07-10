class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_asphalt_calc(self, thickness=1) -> int:
        mass = self._width * self._length * 25 * thickness
        return mass


m8_way = Road(1271000, 7)

print(f'Расход асфальта для трассы М-8 при толщине покрытия 5 см = {m8_way.mass_asphalt_calc(5)} тон.')

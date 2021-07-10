def get_worker_count() -> str:
    """
    static method for Worker class
    :return: quantity of workers
    """
    return Worker.worker_count


class Worker:
    worker_count = 0
    _income = {}

    def __init__(self, name: str, surname: str, position: str):
        self.name = name
        self.surname = surname
        self.position = position
        Worker.worker_count += 1

    def set_income(self, wage=0, bonus=0):
        self._income = {
            'wage': wage,
            'bonus': bonus,
        }

    def get_income(self) -> dict:
        return self._income


class Position(Worker):
    def __init__(self, name: str, surname: str, position: str):
        super().__init__(name, surname, position)

    def get_full_name(self) -> str:
        return f'{self.name.title()} {self.surname.title()}'

    def get_total_income(self) -> int:
        return self._income['wage'] + self._income['bonus']


staff = list()
staff.append(Position('Николай', 'Щербаков', 'Python Senior'))
staff.append(Position('Евгения', 'Набиева', 'Web-editor'))
staff.append(Position('Марат', 'Набиева', 'Python Middle'))


def get_staff_info(workers: list):
    wage = 120000
    bonus = 80000
    for i in workers:
        i.set_income(wage, bonus)
        print(f'{i.get_full_name()} - {i.position}')
        print(f'Заробатная плата - {i.get_total_income()}\n')
        wage -= 20000
        bonus -= 20000
    print(f'В "Kolabizz web studio" работают {get_worker_count()} сотрудник(ов)')


get_staff_info(staff)

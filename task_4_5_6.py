from abc import ABC, abstractmethod


class OfficeEquipment(ABC):
    def __init__(self, brand, model, weight, color):
        self.brand = brand
        self.model = model
        self.weight = weight
        self.color = color

    @abstractmethod
    def set_model_quantity(self, model_quantity):
        pass

    @property
    @abstractmethod
    def get_model_quantity(self):
        pass

    @property
    @abstractmethod
    def quantity(self):
        pass

    def __str__(self):
        return f'name: {self.brand}\n' \
               f'model: {self.model}\n' \
               f'weight: {self.weight}\n' \
               f'color: {self.color}'


class Printer(OfficeEquipment):
    common_quantity = 0

    def __init__(self, brand, model, weight, color):
        super(Printer, self).__init__(brand, model, weight, color)
        self.model_quantity = 0
        Printer.common_quantity += 1

    def set_model_quantity(self, model_quantity):
        self.model_quantity = model_quantity

    @property
    def get_model_quantity(self):
        return self.model_quantity

    @property
    def quantity(self):
        return Printer.common_quantity


class Scanner(OfficeEquipment):
    common_quantity = 0

    def __init__(self, brand, model, weight, color):
        super(Scanner, self).__init__(brand, model, weight, color)
        self.model_quantity = 0
        Scanner.common_quantity += 1

    def set_model_quantity(self, model_quantity):
        self.model_quantity = model_quantity

    @property
    def get_model_quantity(self):
        return self.model_quantity

    @property
    def quantity(self):
        return Scanner.common_quantity


class Xerox(OfficeEquipment):
    common_quantity = 0

    def __init__(self, brand, model, weight, color):
        super(Xerox, self).__init__(brand, model, weight, color)
        self.model_quantity = 0
        Xerox.common_quantity += 1

    def set_model_quantity(self, model_quantity):
        self.model_quantity = model_quantity

    @property
    def get_model_quantity(self):
        return self.model_quantity

    @property
    def quantity(self):
        return Xerox.common_quantity


class Storage:
    common_quantity = 0
    data_base = {
        'printer': {},
        'scanner': {},
        'xerox': {}
    }

    def add_item(self, item: OfficeEquipment):
        Storage.common_quantity += 1

        if isinstance(item, Printer):
            if item.brand in self.data_base['printer']:
                self.data_base['printer'][item.brand].append(item)
            else:
                self.data_base['printer'].setdefault(item.brand, [item])
        if isinstance(item, Scanner):
            if item.brand in self.data_base['scanner']:
                self.data_base['scanner'][item.brand].append(item)
            else:
                self.data_base['scanner'].setdefault(item.brand, [item])
        if isinstance(item, Xerox):
            if item.brand in self.data_base['xerox']:
                self.data_base['xerox'][item.brand].append(item)
            else:
                self.data_base['xerox'].setdefault(item.brand, [item])
        print('Добавлен: \n', item)
        self.send_to_subdivision(item)
        print('*' * 50)

    def send_to_subdivision(self, item):
        if isinstance(item, Printer):
            print('Отправленно в отдел принтеров')
        if isinstance(item, Scanner):
            print('Отправленно в отдел сканнеров')
        if isinstance(item, Xerox):
            print('Отправленно в отдел МФУ')

    def __str__(self):
        return str(self.data_base)


xerox = Xerox('hp', 's-21', '3.5', 'grey')
printer = Printer('hp', 's-21', '3.5', 'grey')
scanner = Scanner('hp', 's-21', '3.5', 'grey')

storage = Storage()
storage.add_item(xerox)
storage.add_item(printer)
storage.add_item(scanner)

print(f'Общее количество техники на складе {Storage.common_quantity} едениц(ы)')

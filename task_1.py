import re


class Data:
    def __init__(self, date):
        if re.match(re.compile(r'^(\d{2}-){2}\d{4}$'), date):
            self.date = date
        else:
            print('Неверный формат даты.')

    def __str__(self):
        try:
            return self.date
        except AttributeError:
            return 'Атрибута не существует.'

    @staticmethod
    def extract_date(date_str: str) -> list:
        return list(map(int, date_str.split('-')))

    @classmethod
    def validate_date(cls, date):
        date_list = Data.extract_date(date)
        if 0 < date_list[0] < 31 and 0 < date_list[1] < 13 and 0 < date_list[2] < 2022:
            print('Дата коректна.')
        else:
            print('Дата не существует.')


if __name__ == '__main__':
    obj = Data('21-11-2020')
    print(obj)

    print(Data.extract_date(obj.date))
    obj.validate_date(obj.date)

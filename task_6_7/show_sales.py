# coding=utf-8
from sys import argv

with open('sales.csv', 'r', encoding='utf-8') as f:
    try:
        if len(argv) == 1:
            print(f.read())
        elif len(argv) == 2:
            for index, line in enumerate(f, 1):
                if index >= int(argv[1]):
                    print(line, end='')
        elif len(argv) == 3:
            for index, line in enumerate(f, 1):
                if int(argv[1]) <= index < int(argv[2]):
                    print(line, end='')
        else:
            print('Вы ввели слишком много значений')
    except:
        print('Неверные значения!')

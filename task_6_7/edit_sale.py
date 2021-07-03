# coding=utf-8
from sys import argv


def str_file_len(file_name):
    length = 0
    with open(file_name) as f:
        for _ in f:
            length += 1
    return length


def edit_sales(number, sale):
    try:
        if int(number) > str_file_len('sales.csv'):
            print('Такого номера строки не существует')
            exit(1)
        with open('sales.csv', 'r', encoding='utf-8') as f:
            with open('temp.csv', 'w', encoding='utf-8') as d:
                for val, line in enumerate(f, 1):
                    if val == int(number):
                        d.write(f'{sale}\n')
                    else:
                        d.write(line)
        with open('sales.csv', 'w', encoding='utf-8') as f:
            with open('temp.csv', 'r', encoding='utf-8') as d:
                for line in d:
                    f.write(line)
    except ValueError as e:
        print(f'Ошибка {e}. Строка должна быть числом!')

edit_sales(argv[1], argv[2])
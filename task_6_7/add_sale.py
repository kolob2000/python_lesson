# coding=utf-8
import sys

try:
    with open('sales.csv', 'a') as f:
        f.seek(2)
        f.writelines(sys.argv[1] + '\n')
except IndexError:
    print('Вы не ввели сумму продажи!')
else:
    print('Запись внесена.')

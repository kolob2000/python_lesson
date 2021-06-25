from utils import currency_rates
import sys

if len(sys.argv) > 1:
    data = currency_rates(sys.argv[1])
    if isinstance(data, list):
        print(f'Курс фунта: {data[1]} \n{data[0]}')
    else:
        print(data)
else:
    print('Вы не ввели код валюты!')
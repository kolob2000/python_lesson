from utils import currency_rates

data = currency_rates("gbp")
if isinstance(data, list):
    print(f'Курс фунта: {data[1]} \n{data[0]}')
else:
    print(data)

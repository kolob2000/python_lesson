prices = [83.73, 47.8, 39.22, 51.0, 62, 45.24, 87, 88.77, 32.1, 80.12]
# можно было создать генератором [ round(random.uniform(0,100)) for _ in range(10)]
print('Первичный список: \n', prices)
###################################################
print('Цены: ')
for index, price in enumerate(prices):
    if index == len(prices) - 1:
        sign = ''
    else:
        sign = ','
    if len(str(price).split('.')) == 1:
        price = str(price) + '.0'

    print(f'{str(price).split(".")[0]} руб. '
          f'{str(price).split(".")[1] if not len(str(price).split(".")[1]) == 1 else "0" + str(price).split(".")[1]} коп.',
          end=f'{sign}')
######################################################
print('\nЦены по возрастанию:')
for index, price in enumerate(sorted(prices)):
    if index == len(prices) - 1:
        sign = ''
    else:
        sign = ','
    if len(str(price).split('.')) == 1:
        price = str(price) + '.0'

    print(f'{str(price).split(".")[0]} руб. '
          f'{str(price).split(".")[1] if not len(str(price).split(".")[1]) == 1 else "0" + str(price).split(".")[1]} коп.',
          end=f'{sign}')
print('\nСписок не изменился:\n', prices)
##################################################
new_prices = sorted(prices, reverse=True)
print(f'Создан новый список отсортированный по убыванию:\n{new_prices}')
########################################################
print('Пять самых дорогих товаров: ')
for index, price in enumerate(sorted(prices, reverse=True)[:5]):
    if index == len(prices[:5]) - 1:
        sign = ''
    else:
        sign = ','

    if len(str(price).split('.')) == 1:
        price = str(price) + '.0'

    print(f'{str(price).split(".")[0]} руб. '
          f'{str(price).split(".")[1] if not len(str(price).split(".")[1]) == 1 else "0" + str(price).split(".")[1]} коп.',
          end=f'{sign}')
"""
    Задание про минимум кода - мне кажется у меня и так минимум кода?!
    Еще меньше я придумать не смог
"""

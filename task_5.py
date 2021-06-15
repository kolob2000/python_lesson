prices = [83.73, 47.8, 39.22, 51.0, 62, 45.24, 87, 88.77, 32.1, 80.12]
# можно было создать генератором [ round(random.uniform(0,100)) for _ in range(10)]
print('Первичный список: \n', prices)
###################################################
print('Цены: ')
for price in prices:
    if len(str(price).split('.')) == 1:
        price = str(price) + '.0'

    print(f'{str(price).split(".")[0]} руб. '
          f'{str(price).split(".")[1] if not len(str(price).split(".")[1]) == 1 else "0" + str(price).split(".")[1]} коп.',
          end=', ')
######################################################
print('\nЦены по возрастанию:')
for price in sorted(prices):
    if len(str(price).split('.')) == 1:
        price = str(price) + '.0'

    print(f'{str(price).split(".")[0]} руб. '
          f'{str(price).split(".")[1] if not len(str(price).split(".")[1]) == 1 else "0" + str(price).split(".")[1]} коп.',
          end=', ')
print('\nСписок не изменился:\n', prices)
##################################################
new_prices = sorted(prices, reverse=True)
print(f'Создан новый список отсортированный по убыванию:\n{new_prices}')
########################################################
print('Пять самых дорогих товаров: ')
for price in sorted(prices, reverse=True)[:5]:
    if len(str(price).split('.')) == 1:
        price = str(price) + '.0'

    print(f'{str(price).split(".")[0]} руб. '
          f'{str(price).split(".")[1] if not len(str(price).split(".")[1]) == 1 else "0" + str(price).split(".")[1]} коп.',
          end=', ')
"""
    Задание про минимум кода - мне кажется у меня и так минимум кода?!
    Еще меньше я придумать не смог
"""

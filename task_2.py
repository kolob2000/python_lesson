i = 0
cubes = []
# НЕ ПОНЯТНО ДО 1000 ИЛИ ВКЛЮЧИТЕЛЬНО, ХОТЯ НАВЕРНОЕ РАЗНИЦЫ НЕТ - 1000 ЧЕТНАЯ
while i < 1000:
    if i % 2:
        cubes.append(i ** 3)
    i += 1
num_sum = 0  # общая сумма
num_sum_17 = 0  # общая сумма с 17
for num in cubes:
    # расчет суммы для первичного списка
    digit = num
    digit_sum = 0  # сумма разрядов
    while digit:
        digit_sum += digit % 10
        digit = digit // 10
    if not digit_sum % 7:
        num_sum += num
    # расчет суммы для +17
    digit_17 = num + 17
    digit_sum_17 = 0  # сумма разрядов
    while digit_17:
        digit_sum_17 += digit_17 % 10
        digit_17 = digit_17 // 10
    if not digit_sum_17 % 7:
        num_sum_17 += (num + 17)

print(f'Сумма элементов для первичного списка: {num_sum}')
print(f'Сумма элементов для списка элементов с + 17: {num_sum_17}')

percent = int(input('Введите количество процентов от 0 до 20: '))
if percent == 0 or 21 > percent > 4:
    print(percent, 'процентов')
elif percent == 1:
    print(percent, 'процент')
elif percent > 20:
    print('Не верный ввод')
else:
    print(percent, 'процента')

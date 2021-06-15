weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print('Первоначальный список: ')
print(weather_list)
print('Строка:')
for index, value in enumerate(weather_list):
    try:

        if weather_list[index + 1] == 'градусов':
            print(f'"{value[0]}{int(value[-1]):02d}"', end=' ')
        else:
            print(f'"{int(value):02d}"', end=' ')
    except:
        print(f'{value}', end=' ')
print('\n Список не изменился: \n', weather_list)
print('*' * 100)
print('*' * 100)
print('*' * 100)
#################################################################
#################################################################
########################## ВТОРОЙ ВАРИАНТ########################
weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print('Первоначальный список: ')
print(weather_list)
print('Строка:')
new_weather_list = []
for i in weather_list:
    if i.isdigit():
        if len(i) == 1:
            print(f'"0{i}"', end=' ')
        else:
            print(f'"{i}"', end=' ')
    elif i.find('-') != -1 or i.find('+') != -1:
        print(f'"{i[0]}{int(i[1:]):02d}"', end=' ')
    else:
        print(i, end=' ')
print('\n Список не изменился: \n', weather_list)

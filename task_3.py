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
for element in weather_list:
    if element.isdigit():
        if len(element) == 1:
            print(f'"0{element}"', end=' ')
        else:
            print(f'"{element}"', end=' ')
    elif element.find('-') != -1 or element.find('+') != -1:
        print(f'"{element[0]}{int(element[1:]):02d}"', end=' ')
    else:
        print(element, end=' ')
print('\n Список не изменился: \n', weather_list)

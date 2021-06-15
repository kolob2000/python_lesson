weather_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print('Первоначальный список: ')
print(weather_list)
new_weather_list = []
for i in weather_list:
    if i.isdigit():
        if len(i) == 1:
            new_weather_list.append('"')
            new_weather_list.append(f'{int(i):02d}')
            new_weather_list.append('"')
        else:
            new_weather_list.append('"')
            new_weather_list.append(f'{i}')
            new_weather_list.append('"')
    elif i.find('-') != -1 or i.find('+') != -1:
        new_weather_list.append('"')
        new_weather_list.append(f'{i[0]}{int(i[1:]):02d}')
        new_weather_list.append('"')
    else:
        new_weather_list.append(i)

print('Новый список: \n',new_weather_list)
print('Строка:')
print(' '.join(new_weather_list))

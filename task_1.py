duration = int(input('Введите продолжительность времени в секундах: '))
MIN = 60
HOUR = MIN * 60
DAY = HOUR * 24
MONTH = DAY * 31
YEAR = DAY * 365
years = duration // YEAR
monthes = (duration % YEAR) // MONTH
days = ((duration % YEAR) % MONTH) // DAY
hours = (((duration % YEAR) % MONTH) % DAY) // HOUR
minutes = ((((duration % YEAR) % MONTH) % DAY) % HOUR) // MIN
seconds = (((((duration % YEAR) % MONTH) % DAY) % HOUR) % MIN) % 60
if duration < MIN:
    print(f'Ваше время в секундах:  {seconds} сек. ')
elif MIN < duration < HOUR - 1:
    print(f'Ваше время в минутах: {minutes} мин. {seconds} сек. ')
elif HOUR < duration < DAY - 1:
    print(f'Ваше время в часах: {hours} час. {minutes} мин. {seconds} сек. ')
elif DAY < duration < MONTH - 1:
    print(f'Ваше время в днях: {days} дн. {hours} час. {minutes} мин. {seconds} сек. ')
elif MONTH < duration < YEAR - 1:
    print(f'Ваше время в месяцах: {monthes} мес. {days} дн. {hours} час. {minutes} мин. {seconds} сек. ')
else:
    print(f'Ваше время в годах:{years} лет {monthes} мес. {days} дн. {hours} час. {minutes} мин. {seconds} сек. ')

employees = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй',
             'директор аэлита']
for employee in employees:
    print(f'Привет, {employee.split()[-1].title()}!')  # или capitalize()
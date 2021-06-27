from itertools import zip_longest

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А',
]

pupils = (a for a in zip_longest(tutors, klasses, fillvalue=None))
print(type(pupils))
for i in pupils:
    print(i)

def thesaurus_adv(*args):
    names = {}
    for name in args:
        if name[name.find(' ') + 1] in names:
            if name[0] in names[name[name.find(' ') + 1]]:
                names[name[name.find(' ') + 1]][0].append(name)
            else:
                names[name[name.find(' ') + 1]].setdefault(name[0], name)
        else:
            temp_name = {}
            temp_name.setdefault(name[0], name)
            names.setdefault(name[name.find(' ') + 1], temp_name)
    return names


dict_names = thesaurus_adv('Сергей Омский', 'Андрей Лихавцов', 'Олег Леонов', 'Ольга Щербакова', 'Николай Щербаков',
                           'Евгения Набиева', 'Марат Набиев', 'Роман Смирнов', 'Елена Орлова')

print(dict_names, '\n')
for item in dict_names.items():
    print(item)

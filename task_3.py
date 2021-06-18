def thesaurus(*args):
    names = {}
    for name in args:
        if name[0].lower() in names:
            names[name[0].lower()].append(name)
        else:
            names.setdefault(name[0].lower(), [name])
    # return names # при необходимости не отсортирванный словарь
    return dict(sorted(names.items()))  # возвращаем отсортированный словарь. использовать можно


names = thesaurus('Сергей', 'Андрей', 'Олег', 'Ольга', 'Николай', 'Евгенмя', 'Роман', 'Елена')
print(names)

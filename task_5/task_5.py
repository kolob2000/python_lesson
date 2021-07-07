import os


def files_size_folder_info(folder_name: str) -> dict:
    file_size_quantity = {
        '100': [0, ],
        '1000': [0, ],
        '10000': [0, ],
        '100000': [0, ],
    }
    set_100 = set()
    set_1000 = set()
    set_10000 = set()
    set_100000 = set()

    for i in os.scandir(folder_name):
        if i.stat().st_size <= 100:
            file_size_quantity['100'][0] += 1
            set_100.add(i.name.split('.')[-1])
        if 100 < i.stat().st_size <= 1000:
            file_size_quantity['1000'][0] += 1
            set_1000.add(i.name.rsplit('.')[-1])
        if 1000 < i.stat().st_size <= 10000:
            file_size_quantity['10000'][0] += 1
            set_10000.add(i.name.rsplit('.')[-1])
        if 10000 < i.stat().st_size <= 100000:
            file_size_quantity['100000'][0] += 1
            set_100000.add(i.name.rsplit('.')[-1])

    file_size_quantity.setdefault('100', file_size_quantity['100'].append(list(set_100)))
    file_size_quantity['100'] = tuple(file_size_quantity['100'])

    file_size_quantity.setdefault('1000', file_size_quantity['1000'].append(list(set_1000)))
    file_size_quantity['1000'] = tuple(file_size_quantity['1000'])

    file_size_quantity.setdefault('10000', file_size_quantity['10000'].append(list(set_10000)))
    file_size_quantity['10000'] = tuple(file_size_quantity['10000'])

    file_size_quantity.setdefault('100000', file_size_quantity['100000'].append(list(set_100000)))
    file_size_quantity['100000'] = tuple(file_size_quantity['100000'])



    return file_size_quantity


print(files_size_folder_info('some_data'))

#

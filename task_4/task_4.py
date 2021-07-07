import os


def files_size_folder_info(folder_name: str) -> dict:
    file_size_quantity = {
        '100': 0,
        '1000': 0,
        '10000': 0,
        '100000': 0,
    }
    for i in os.scandir(folder_name):
        if i.stat().st_size <= 100:
            file_size_quantity['100'] += 1
        if 100 < i.stat().st_size <= 1000:
            file_size_quantity['1000'] += 1
        if 1000 < i.stat().st_size <= 10000:
            file_size_quantity['10000'] += 1
        if 10000 < i.stat().st_size <= 100000:
            file_size_quantity['100000'] += 1

    return file_size_quantity


print(files_size_folder_info('some_data'))

import _io
import json
import os.path
"""
    програма хранит структуру проекта в json файле.
    можно создавать несколько проектов и добавлять папки только на тот же уровень вложенности,
    поскольку рекурсию не добавлял - реализую её во второй задаче.
"""

def json_to_dict(file_name: str) -> dict:
    with open(file_name, 'r', encoding='utf-8') as f:
        return json.load(f)


def struct_project_maker(file_name: str) -> str:
    project_structure = json_to_dict(file_name)
    for folder in project_structure:
        if os.path.exists(folder):
            print(f'Такое уж есть - {folder}')
            print('Измените название проекта в файле конфигурации!')
            exit(1)
        else:
            os.mkdir(folder)
        for sub_folder in project_structure[folder]:
            os.mkdir(f'{folder}/{sub_folder}')
        print(f'{folder} создан.')
    return 'Успешное Выполнение.'


struct_project_maker('task_1.json')

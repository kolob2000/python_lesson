import os
import yaml


def valid_yaml_file(file_name: str) -> dict:
    with open(file_name, 'r', encoding='utf-8') as f:
        folders = yaml.safe_load(f)
    if folders is None:
        print("File is empty. Can't create project.")
        exit(1)
    else:
        return folders


def yaml_project_maker(structure: dict, path=os.getcwd()) -> int:
    for key, value in structure.items():
        if not os.path.exists(f'{path}/{key}'):
            os.mkdir(f'{path}/{key}')
        else:
            return print('Folder exsists. Rename your project.')
        if isinstance(value, dict):
            yaml_project_maker(value, f'{path}/{key}')
        if isinstance(value, str):
            if not os.path.exists(f'{path}/{key}/{value}'):
                with open(f'{path}/{key}/{value}', 'w', encoding='utf-8') as f:
                    pass
        if isinstance(value, list):
            for element in value:
                if isinstance(element, str):
                    if not os.path.exists(f'{path}/{key}/{element}'):
                        with open(f'{path}/{key}/{element}', 'w', encoding='utf-8') as f:
                            pass
                if isinstance(element, dict):
                    yaml_project_maker(element, f'{path}/{key}')
    return 1


def main(file_name):
    folder_structure = valid_yaml_file(file_name)
    if yaml_project_maker(folder_structure) == 1:
        print('Project created')


main('config.yaml')

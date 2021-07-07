import os
import shutil
from project_creator import tree_creator


def html_to_template_folder(directory=os.getcwd(), project_name=''):
    if project_name == '':
        project_name = os.path.basename(directory)
    for i in os.listdir(directory):
        if os.path.isdir(f'{directory}/{i}'):
            html_to_template_folder(f'{directory}/{i}', project_name)
        elif os.path.isfile(f'{directory}/{i}') and i.endswith('.html'):
            if not os.path.exists(f'{project_name}/template/{os.path.basename(directory)}'):
                os.makedirs(f'{project_name}/template/{os.path.basename(directory)}')
            if not os.path.exists(f'{project_name}/template/{os.path.basename(directory)}/{i}'):
                shutil.copy(f'{directory}/{i}', f'{project_name}/template/{os.path.basename(directory)}/{i}')
    return 1


tree_creator('config.yaml')
if html_to_template_folder('my_project') == 1:
    print('Все файлы собраны')

import yaml

structures = {
    'my_project': {
        'setting': [
            '__init__.py',
            'dev.py',
            'prod.py',
        ],
        'mainapp': [
            '__init__.py',
            'models.py',
            'views.py',
            {
                'templates': {
                    'mainapp': [
                        'base.html',
                        'index.html',
                    ]
                }
            }
        ],
        'authapp': [
            '__init__.py',
            'models.py',
            'views.py',
            {
                'templates': {
                    'authapp': [
                        'base.html',
                        'index.html',
                    ],
                }
            }
        ],
    }
}

with open('config.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(structures, f)

def valid_yaml_file(file_name: str):
    with open(file_name, 'r', encoding='utf-8') as f:



def yaml_structure_maker(file_name: str, root_path=''):

        for i in yaml.safe_load(f).values():
            if isinstance(i, dict):
                pass
            if isinstance(i, list):
                pass
            if isinstance(i, str):
                pass

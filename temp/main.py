import yaml

with open('temp.yaml', 'r', encoding='utf-8') as f:
    print(yaml.safe_load(f))

import requests

r = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
with open('nginx_logs.txt', 'wb') as f:
    f.write(r.content)

parsed_list = []
with open('nginx_logs.txt', 'r') as f:
    for line in f:
        parsed_list.append((line.split()[0], line.split()[5].strip('"'), line.split()[6]))
parsed_dict = {}
for i in parsed_list:
    if i[0] in parsed_dict:
        parsed_dict[i[0]] += 1
    else:
        parsed_dict[i[0]] = 1
count = 0
hacker = tuple()
print(f'Всего запросов: {len(parsed_list)}')

for index, value in parsed_dict.items():
    if value > count:
        count = value
        hacker = (index, value)

print(f'Хакер:  {hacker}')

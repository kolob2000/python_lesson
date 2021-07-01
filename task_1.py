import requests

r = requests.get('https://github.com/elastic/examples/raw/master/Common%20Data%20Formats/nginx_logs/nginx_logs')
with open('nginx_logs.txt', 'wb') as f:
    f.write(r.content)

parsed_list = []
with open('nginx_logs.txt', 'r') as f:
    for line in f:
        parsed_list.append((line.split()[0], line.split()[5].strip('"'), line.split()[6]))

for i in parsed_list:
    print(i)


import os
import re
import time
import requests

URL = 'https://raw.githubusercontent.com/elastic/examples/master/Common%20Data%20Formats/nginx_logs/nginx_logs'
TEMPLATE = r'([\d\.]+)*.*([\d]{2}/[A-Za-z]*/[\d:]*\s[\+\d]+).*"([A-Z]+).*(/[\w]+/[\w]+).*"\s([\d]+)\s(\d*)'


def get_log_from_server(url: str, file_name='log.txt'):
    if not os.path.exists(file_name):
        html = requests.get(URL)
        with open(file_name, 'w') as f:
            f.write(html.text)
        return file_name
    else:
        print('File exists. Input another name.')
        exit(1)


def string_to_tuple_parser(template: str, file_name: str):
    match = re.compile(template)
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f.readlines():
            if match.search(line) is None:
                print(line)
                continue
            print(match.search(line).groups())
            time.sleep(0.5)


def main(url: str, template: str, file_name=''):
    if file_name == '':
        file = get_log_from_server(url)
    else:
        file = get_log_from_server(url, file_name)
    string_to_tuple_parser(template, file)


main(URL, TEMPLATE, file_name='log.txt')

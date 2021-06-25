from datetime import datetime
from typing import Union
import xml.etree.ElementTree as et
import requests


def currency_rates(currency_code: str) -> Union[str, float, None]:
    if not isinstance(currency_code, str):
        return 'Код должен быть строкой'
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    with open('file.xml', 'w') as f:
        f.write(r.text)
    tree = et.parse('file.xml')
    root = tree.getroot()
    for child in root:
        if child.find('CharCode').text == currency_code.upper():
            return float(child.find('Value').text.replace(',', '.'))
    return None


if __name__ == '__main__':
    print('Курс евро: ', currency_rates('eur'))
    print('Курс доллара: ', currency_rates('usd'))

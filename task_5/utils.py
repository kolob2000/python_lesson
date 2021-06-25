from datetime import datetime
from typing import Union
import xml.etree.ElementTree as et
import requests


def currency_rates(currency_code: str) -> Union[str, list, None]:
    if not isinstance(currency_code, str):
        return 'Код должен быть строкой'
    r = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')
    with open('file.xml', 'w') as f:
        f.write(r.text)
    tree = et.parse('file.xml')
    root = tree.getroot()
    for child in root:
        if child.find('CharCode').text == currency_code.upper():
            parsed_data = datetime.date(datetime.strptime(' '.join(r.headers['Date'].split()[1:4]), '%d %b %Y'))
            data = [parsed_data, float(child.find('Value').text.replace(',', '.'))]

            return data
    return None

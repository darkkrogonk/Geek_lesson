from requests import get, utils
import datetime
from decimal import Decimal


def currency_rates(name):
    response = get('http://www.cbr.ru/scripts/XML_daily.asp')
    encodings = utils.get_encoding_from_headers(response.headers)
    content = response.content.decode(encoding=encodings)
    total1 = []
    total2 = []
    content = content.split('</')
    for element_xml in content:
        xml_coppy = element_xml
        xml_coppy = xml_coppy.split('>')
        for finish in xml_coppy:
            if finish.isupper():
                total1.append(finish)
        finish = finish.replace(',', '.')
        finish = finish.lower()
        if finish.isdigit() == False and finish.islower() == False and finish != '':
            total2.append(Decimal(finish).quantize(Decimal('1.00')))
    result = dict(zip(total1, total2))

    for key, value in result.items():
        if key == name.upper():
            return f'{name.upper()} {result[name.upper()]} \n{datetime.datetime.now().strftime("Дата: %d.%m.%Y")}'


if __name__ == "__main__":
    print(f'{currency_rates(input("Введите валюту: "))}')
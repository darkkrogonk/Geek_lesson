from utils import currency

i = input('Введите валюту: ')
while i != 'stop':
    print(currency.currency_rates(i))
    i = input('Введите валюту (stop - для выхода): ')
print('До свидания!')
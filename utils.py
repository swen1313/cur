import json
from config import keys
import requests



class ConvertionException(Exception):
    pass



class CurrencyConverter:
    @staticmethod
    
    def convert(quote: str, base: str, amount: str):
        
        if quote == base:
            raise ConvertionException(f'невозможно перевести одинаковые валюты{base}')
        try:
            quote_tiker = keys[quote]
        except KeyError:
            raise ConvertionException(f'не удалось обработать валюту{quote}')

        try:
            base_tiker = keys[base]
        except KeyError:
            raise ConvertionException(f'не удалось обработать валюту{base}')


        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'не удалось обработать колличество{amount}')       
        
        r = requests.get('https://currate.ru/api/?get=rates&pairs={base_tiker}{qoute_tiker},{base_tiker}{qoute_tiker}&key=a3721bb9160f48af8a99bbd1defbd16f')
        
        total_base = json.loads(r.content)[keys[base]]
        return total_base

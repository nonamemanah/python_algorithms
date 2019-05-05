import requests

from api.BaseApi import BaseApi
from business_objects import Currency
import json


class OpenExchangeRatesApi(BaseApi):
    _baseurl = 'https://openexchangerates.org/api'
    _currencies = []

    def __init__(self):
        super().__init__()

    def load_currencies(self):
        try:
            response = requests.get(f'{self._baseurl}/currencies.json')
            if not response.ok:
                print('Wrong response')
                return

            json_response = json.loads(response.text)
            for item in json_response:
                self._currencies.append(Currency.Currency(item, json_response[item]))
        except Exception as err:
            print(f'Can not do request to {self._baseurl}: {err.response.content}')

    @property
    def currencies(self):
        return self._currencies

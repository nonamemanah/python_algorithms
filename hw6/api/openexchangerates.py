import requests

from api.BaseApi import BaseApi
from business_objects import Currency
import json
from operator import attrgetter


class OpenExchangeRatesApi(BaseApi):
    _baseurl = 'https://openexchangerates.org/api'
    _api_key = 'e8e66dc9ca0243899dc6e71d5e86af4e'
    _currencies = []

    def __init__(self):
        super().__init__()

    def load(self):
        self._load_currencies()
        self._load_exchanges()

    def _load_currencies(self):
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

    def _load_exchanges(self):
        try:
            response = requests.get(f'{self._baseurl}/latest.json?app_id={self._api_key}')
            if not response.ok:
                print('Wrong response')
                return

            json_response = json.loads(response.text)
            for item in self._currencies:
                rate_value = json_response['rates'][item.label]
                self._set_rate(item.label, rate_value)
        except Exception as err:
            print(f'Can not do request to {self._baseurl}: {err.response.content}')

    def _set_rate(self, label: str, rate: int):
        element = [item for item in self.currencies if item.label == label]
        if element is None:
            return

        element[0].set_rate(rate)

    @property
    def currencies(self):
        return self._currencies

    @property
    def sorted_currency(self):
        return sorted(self.currencies, key=lambda x: x.rate)

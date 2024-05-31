import requests
from requests import Response


def convert_response_to_json(response: Response):
    try:
        json = response.json()
    except requests.exceptions.JSONDecodeError:
        print("JSONDecodeError has occurred")
    else:
        return json


class Client:

    def __init__(self, api_key, base):
        self.auth_header = {'apikey': api_key}
        self.base = base

    def status(self):
        requests_get = requests.get(self.base + '/status', headers=self.auth_header)
        return convert_response_to_json(requests_get)

    def latest(self, base_currency=None, currencies=None):
        if type(base_currency) is not str:
            raise Exception("Base currency needs to be a string")
        if type(currencies) is not list:
            raise Exception("Currencies needs to be a list")

        requests_get = requests.get(self.base + '/latest',
                                    {'base_currency': base_currency, 'currencies': ','.join(currencies)},
                                    headers=self.auth_header)
        return convert_response_to_json(requests_get)

    def historical(self, date, base_currency=None, currencies=None):
        if type(base_currency) is not str:
            raise Exception("Base currency needs to be a string")
        if type(currencies) is not list:
            raise Exception("Currencies needs to be a list")

        requests_get = requests.get(self.base + '/historical',
                           {'date': str(date), 'base_currency': base_currency, 'currencies': ','.join(currencies)},
                           headers=self.auth_header)
        return convert_response_to_json(requests_get)

    def currencies(self, currencies=None):
        if type(currencies) is not list:
            raise Exception("Currencies needs to be a list")

        requests_get = requests.get(self.base + '/currencies', {'currencies': ','.join(currencies)}, headers=self.auth_header)
        return convert_response_to_json(requests_get)

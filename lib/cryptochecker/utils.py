from typing import Any

import requests


class Binance:
    URL = 'https://api.binance.com/api/v3'

    def get_price(self, symbol: str) -> dict[str, Any]:
        url = f'{self.URL}/ticker/price'
        response = requests.get(url=url, params={'symbol': f'{symbol.upper()}USDT'})
        return response.json()


class Kucoin:
    URL = 'https://api.kucoin.com/api/v1'

    def get_price(self, symbol: str) -> dict[str, Any]:
        url = f'{self.URL}/market/orderbook/level1'
        response = requests.get(url=url, params={'symbol': f'{symbol.upper()}-USDT'})
        return response.json()

from lib.cryptochecker.utils import Binance, Kucoin

e = Binance()
print(e.get_price('SOL'))
k = Kucoin()
print(k.get_price('SOL'))
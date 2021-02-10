from binance.client import Client
import math

class TradingBot:
    def __init__(self, api_key, secret_key, fee=0.02, profit=2.0):
        self.client = Client(api_key, secret_key)
        self.fee = 1.00 - fee
        self.profit = profit

    def SetCoin(self, coin):
        self.coin = coin.upper()
        self.symbol = coin.upper()+'BTC'
        self.price = float(self.client.get_symbol_ticker(symbol=self.symbol)['price'])
        self.filters = self.client.get_symbol_info(self.symbol)['filters']

        for filter in self.filters:
            if filter['filterType'] == 'LOT_SIZE':
                self.step_size = float(filter['stepSize'])

        self.precision = int(round(-math.log(self.step_size,10),0))

    def Buy(self):
        balance = float(self.client.get_asset_balance(asset = 'BTC')['free'])
        factor = 10 ** self.precision

        quantity = (balance / self.price) * self.fee
        quantity = float(math.trunc(quantity * factor) / factor)

        try:
            self.client.create_order(symbol=self.symbol, side='BUY', type='MARKET', quantity=quantity)
        except Exception as e:
            print(e)

    def Sell(self):
        balance = float(self.client.get_asset_balance(asset = self.coin)['free'])
        factor = 10**self.precision

        quantity = float(math.trunc(balance * factor) / factor)
        ideal_price = self.price * self.profit
        try:
            order = self.client.create_order(symbol=self.symbol, side='SELL', type="LIMIT", quantity=quantity, price=ideal_price, timeInForce='GTC')
        except Exception as e:
            print(e)


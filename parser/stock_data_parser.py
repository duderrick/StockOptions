import logging
from typing import Any

from model.stock_models import MetaData, StockPriceVolume
from util import logging_util

LOG = logging_util.setup_logging(__name__, logging.DEBUG)
class StockParser(object):
    def __init__(self):
        pass

    def parse(self, json: Any):
        symbol = json['Meta Data']['2. Symbol']
        interval = json['Meta Data']['4. Interval']
        information = json['Meta Data']['1. Information']
        metadata = MetaData(symbol, interval, information)

        stock_prices = list()
        for ts, v in json[f'Time Series ({interval})'].items():
            open = float(v['1. open'])
            high = float(v['2. high'])
            low = float(v['3. low'])
            close = float(v['4. close'])
            volume = int(v['5. volume'])
            stock_prices.append(StockPriceVolume(ts, open, high, low, close, volume))
        return metadata, stock_prices

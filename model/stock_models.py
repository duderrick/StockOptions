class MetaData(object):
    def __init__(self, symbol: str, interval: str, information: str):
        self.symbol = symbol
        self.interval = interval
        self.information = information

    def __str__(self):
        return f'Symbol: {self.symbol}, Interval: {self.interval}, Information: {self.information}'


class StockPriceVolume:
    def __init__(self, ts: str, open: float, high: float, low: float, close: float, volume: int):
        self.timestamp = ts
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __str__(self):
        return f'open: {self.open}, high: {self.high}, low: {self.low}, volume: {self.volume}'


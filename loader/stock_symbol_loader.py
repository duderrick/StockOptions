import logging

import requests

from util import logging_util
from util.commons import HOST, API_KEY

LOG = logging_util.setup_logging(__name__, logging.DEBUG)


class StockPriceLoader:
    def __init__(self):
        pass

    def load(self, function: str, symbol: str, interval: str):
        url = f'{HOST}/query?function={function}&apikey={API_KEY}&interval={interval}&symbol={symbol}'
        LOG.debug('Requesting url: %s', url)
        LOG.debug('fetching %s stock price ...', symbol.upper())
        rsp = requests.get(url)
        LOG.debug('response status code: %d', rsp.status_code)
        # print(rsp.text)
        return rsp.json()
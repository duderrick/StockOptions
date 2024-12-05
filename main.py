import json
import logging

from PySide6 import QtWidgets

from util.commons import SAMPLE_STOCK_DATA
from parser.stock_data_parser import StockParser
from views.stock_line_chart_view import StockLineChartView
from util import logging_util

LOG = logging_util.setup_logging(__name__, logging.DEBUG)

if __name__ == '__main__':
    jsonObj = json.loads(SAMPLE_STOCK_DATA)
    parser = StockParser()
    metadata, stock_prices = parser.parse(jsonObj)

    app = QtWidgets.QApplication([])

    stock_line_viewer = StockLineChartView()
    stock_line_viewer.resize(1200, 1000)
    stock_line_viewer.build()
    stock_line_viewer.show()

    app.exec()

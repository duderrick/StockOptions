import json
import sys
from PySide6.QtCore import Qt, QDateTime, QPointF, Slot
from PySide6.QtGui import QFont, QPainter
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QGridLayout, QHBoxLayout, QLineEdit, QComboBox
from PySide6.QtCharts import QChart, QChartView, QLineSeries, QValueAxis, QDateTimeAxis

from model.stock_models import MetaData, StockPriceVolume
from loader.stock_symbol_loader import StockPriceLoader
from parser.stock_data_parser import StockParser
from util.commons import INTRADAY_TS, COMMON_FONT, LABEL_FONT, \
    SAMPLE_STOCK_DATA, AXIS_TITLE_FONT


class StockLineChartView(QWidget):
    def __init__(self):
        super().__init__()
        self.quit_button = self._create_close_button()
        self.stock_symbol_text_box = self._create_search_text_box()
        self.search_button = self._create_search_button()
        self.interval_dropdown = self._create_interval_dropdown()

    def build(self):
        symbol_layout = QHBoxLayout()
        label = self._create_label('Symbol: ')
        symbol_layout.addWidget(label)
        symbol_layout.addWidget(self.stock_symbol_text_box)
        symbol_layout.addWidget(self.search_button)

        interval_layout = QHBoxLayout()
        label = self._create_label('Interval: ')
        interval_layout.addWidget(label)
        interval_layout.addWidget(self.interval_dropdown)

        self.setWindowTitle('Stock Price Line Chart')
        self.main_layout = QGridLayout(self)
        self.main_layout.addLayout(symbol_layout, 0, 0)

        self.main_layout.addLayout(interval_layout, 1, 0, 1, 3)
        self.main_layout.setAlignment(interval_layout, Qt.AlignTop | Qt.AlignLeft)

        self.main_layout.addWidget(self.quit_button, 3, 1)

    def _create_line_chart_view(self, metadata: MetaData, stock_prices: list[StockPriceVolume]):
        series = QLineSeries()
        for stock_price in stock_prices:
            timestamp = QDateTime.fromString(stock_price.timestamp,
                                             'yyyy-MM-dd HH:mm:ss').toMSecsSinceEpoch()
            series.append(QPointF(timestamp, stock_price.open))

        chart = QChart()
        chart.legend().hide()
        chart.addSeries(series)
        chart.setTitle(f'{metadata.symbol.upper()} Opening Prices Over Time')

        axis_x = QDateTimeAxis()
        axis_x.setTitleText('Time')
        axis_x.setFormat('HH:mm:ss')
        axis_x.setTickCount(10)
        axis_x.setTitleFont(AXIS_TITLE_FONT)
        axis_x.setLabelsFont(LABEL_FONT)
        axis_x.setLabelsAngle(-45)
        chart.addAxis(axis_x, Qt.AlignBottom)
        series.attachAxis(axis_x)

        axis_y = QValueAxis()
        axis_y.setTitleText('Opening Price')
        axis_y.setLabelFormat('%.2f')
        axis_y.setTickCount(10)
        axis_y.setTitleFont(AXIS_TITLE_FONT)
        axis_y.setLabelsFont(LABEL_FONT)
        chart.addAxis(axis_y, Qt.AlignLeft)
        series.attachAxis(axis_y)

        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        return chart_view

    def _create_interval_dropdown(self):
        dropdown = QComboBox(self)
        dropdown.addItems(['1min', '5min', '15min', '30min', '60min'])
        dropdown.setCurrentIndex(1)
        dropdown.currentTextChanged.connect(self._on_interval_dropdown_change_event_handler)
        return dropdown

    def _create_search_text_box(self):
        search_input = QLineEdit(self)
        search_input.setPlaceholderText('Enter a company ticker symbol')
        return search_input

    def _create_search_button(self):
        button = QPushButton('Search', self)
        button.setFixedSize(80, 30)
        button.setFont(COMMON_FONT)
        button.clicked.connect(self._search_on_click_event_handler)
        return button

    def _create_close_button(self):
        close_button = QPushButton('Quit', self)
        close_button.setFixedSize(70, 30)
        close_button.setFont(COMMON_FONT)
        close_button.clicked.connect(self._quit_on_click_event_handler)
        return close_button

    def _create_label(self, text: str) -> QLabel:
        label = QLabel(text)
        label.setFont(COMMON_FONT)
        return label

    def _on_interval_dropdown_change_event_handler(self):
        self._search_stock_and_show(self.interval_dropdown.currentText(), self.stock_symbol_text_box.text().upper())

    def _search_on_click_event_handler(self):
        self._search_stock_and_show(self.interval_dropdown.currentText(), self.stock_symbol_text_box.text().upper())

    def _search_stock_and_show(self, interval: str, symbol: str):
        stockLoader = StockPriceLoader()
        stockData = stockLoader.load(INTRADAY_TS, symbol, interval)

        # stockData = json.loads(SAMPLE_STOCK_DATA)
        parser = StockParser()
        metadata, stock_prices = parser.parse(stockData)

        view = self._create_line_chart_view(metadata, stock_prices)
        self.main_layout.addWidget(view, 2, 0, 1, 3)

    def _quit_on_click_event_handler(self):
        sys.exit(0)
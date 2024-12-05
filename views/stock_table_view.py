import sys

from PySide6 import QtWidgets, QtCore
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import QTableWidget, QTableWidgetItem, QWidget, QGridLayout

from model.stock_models import MetaData, StockPriceVolume


HEADERS = ['Timestamp', 'Open', 'High', 'Low', 'Close', 'Volume']
class StockDetailWidget(QWidget):
    def __init__(self, metadata: MetaData, stock_prices: list[StockPriceVolume]):
        super().__init__()
        self.metadata = metadata
        self.stock_prices = stock_prices
        self.table = self.__create_table_view()
        self.quitButton = self.__create_close_button()

    def build(self):
        symbol_layout = QtWidgets.QHBoxLayout()
        label = self.__create_label('Symbol: ')
        symbol_layout.addWidget(label)
        symbol_layout.addWidget(QtWidgets.QLabel(self.metadata.symbol.upper()))

        interval_layout = QtWidgets.QHBoxLayout()
        label = self.__create_label('Interval: ')
        interval_layout.addWidget(label)
        interval_layout.addWidget(QtWidgets.QLabel(self.metadata.interval))

        self.setWindowTitle('Stock Details')
        main_layout = QGridLayout(self)
        main_layout.addLayout(symbol_layout, 0, 0, 1, 1)
        main_layout.addLayout(interval_layout, 1, 0)

        self.__construct_table()
        main_layout.addWidget(self.table, 2, 0, 1, 3)
        main_layout.addWidget(self.quitButton, 3, 1)

    def __construct_table(self):
        self.table.setColumnWidth(0, 160)
        for i, stock_price in enumerate(self.stock_prices):
            self.table.setItem(i, 0, QTableWidgetItem(stock_price.timestamp))
            self.table.setItem(i, 1, QTableWidgetItem(str(stock_price.open)))
            self.table.setItem(i, 2, QTableWidgetItem(str(stock_price.high)))
            self.table.setItem(i, 3, QTableWidgetItem(str(stock_price.low)))
            self.table.setItem(i, 4, QTableWidgetItem(str(stock_price.close)))
            self.table.setItem(i, 5, QTableWidgetItem(str(stock_price.volume)))

    def __create_table_view(self):
        table = QTableWidget()
        table.setRowCount(len(self.stock_prices))
        table.setColumnCount(6)
        table.setHorizontalHeaderLabels(HEADERS)

        font = QFont('Arial', 14, QFont.Bold)
        table.horizontalHeader().setFont(font)
        return table

    def __create_close_button(self):
        button = QtWidgets.QPushButton('Close')
        button.setFixedSize(50, 30)
        font = QFont('Arial', 14, QFont.Bold)
        button.setFont(font)
        button.clicked.connect(self.quit)
        return button

    def __create_label(self, text: str):
        label = QtWidgets.QLabel(text)
        font = QFont('Arial', 14, QFont.Bold)
        label.setFont(font)
        return label

    @QtCore.Slot()
    def quit(self):
        sys.exit(0)
import pybithumb
import time

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import uic
from PyQt5.QtCore import *


form_class = uic.loadUiType("test01.ui")[0]
tickers = ['BTC', 'ETH', 'XRP', 'BCH']

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tw_bull.setRowCount(len(tickers))

        timer = QTimer(self)
        timer.start(5000)
        timer.timeout.connect(self.timeout)

    def bull_market(self, ticker, num):
        dayData = pybithumb.get_ohlcv(ticker)
        ma = dayData["close"].rolling(num).mean()
        last_ma = ma[-2]
        price = pybithumb.get_current_price(ticker)
        state = None
        if price > last_ma:
            state = "상승장"
        else:
            state = "하락장"
        return price, last_ma, state

    def timeout(self):
        for i, ticker in enumerate(tickers):
            price, last_ma5, state = self.bull_market(ticker, 5)
            self.tw_bull.setItem(i, 0, QTableWidgetItem(ticker))
            self.tw_bull.setItem(i, 1, QTableWidgetItem(str(price)))
            self.tw_bull.setItem(i, 2, QTableWidgetItem(str(last_ma5)))
            self.tw_bull.setItem(i, 3, QTableWidgetItem(state))






app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()



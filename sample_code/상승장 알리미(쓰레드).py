import pybithumb
import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
import time


form_class = uic.loadUiType("test01.ui")[0]
tickers = ['BTC', 'ETH', 'XRP', 'BCH']

class Worker(QThread):
    finished = pyqtSignal(dict)

    def run(self):
        while True:
            data = {}
            for ticker in tickers:
                data[ticker] = self.bull_market(ticker, 5)
            print(data)

            self.finished.emit(data)
            time.sleep(2)


    def bull_market(self, ticker, num):
        try:
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
        except:
            return None, None, None


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.tw_bull.setRowCount(len(tickers))


        self.worker = Worker()
        self.worker.finished.connect(self.update_table_widget)
        self.worker.start()

    @pyqtSlot(dict)
    def update_table_widget(self, data):
        try:
            for ticker, infos in data.items():
                index = tickers.index(ticker)

                self.tw_bull.setItem(index, 0, QTableWidgetItem(ticker))
                self.tw_bull.setItem(index, 1, QTableWidgetItem(str(infos[0])))
                self.tw_bull.setItem(index, 2, QTableWidgetItem(str(infos[1])))
                self.tw_bull.setItem(index, 3, QTableWidgetItem(str(infos[2])))
        except:
            pass

app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()



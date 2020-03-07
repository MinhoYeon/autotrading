import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import *
# import pykorbit

form_class = uic.loadUiType("실시간 가격 조회.ui")[0]


class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.timer = QTimer(self)
        self.timer.start(1000)
        self.timer.timeout.connect(self.timeout)

    def timeout(self):
        cur_time = QTime.currentTime()
        str_time = cur_time.toString("hh:mm:ss")
        self.statusBar().showMessage(str_time)
        # price_BTC = pykorbit.get_current_price("BTC")
        self.lineEdit.setText("hello")



app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
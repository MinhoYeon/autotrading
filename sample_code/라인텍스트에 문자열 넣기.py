import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
# import pykorbit

form_class = uic.loadUiType("price_btc.ui")[0]

class MyWindow(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_clicked)

    def btn_clicked(self):
        # price_BTC = pykorbit.get_current_price("BTC")
        self.lineEdit.setText("hello")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
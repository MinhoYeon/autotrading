import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(100, 200, 300, 200)
        self.setWindowTitle("PyQt")
        self.setWindowIcon(QIcon("icon_increase_money.png"))

        btn1 = QPushButton("button1", self)
        btn1.move(10, 10)
        btn1.clicked.connect(self.btn1_clicked)
        btn2 = QPushButton("button2", self)
        btn2.move(10, 40)

    def btn1_clicked(self):
        print("button1 clicked")


app = QApplication(sys.argv)
window = MyWindow()
window.show()
app.exec_()
import sys
from PyQt5.QtWidgets import *

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)

        self.label1= QLabel("매도수량:", self)
        self.label1.move(10, 20)

        self.spinBox1 = QSpinBox(self)
        self.spinBox1.move(80, 25)
        self.spinBox1.resize(80, 22)
        self.spinBox1.valueChanged.connect(self.spinBoxState)

        self.statusBar = QStatusBar(self)
        self.setStatusBar(self.statusBar)

    def spinBoxState(self):
        value = self.spinBox1.value()
        msg = '%d 주를 매도합니다.' % (value)
        self.statusBar.showMessage(msg)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
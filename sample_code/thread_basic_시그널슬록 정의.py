import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time

class Worker(QThread):
    finished = pyqtSignal(dict) #시그널 생성시 딕셔너리 전달함

    def run(self):
        while True:
            data = {}
            self.finished.emit(data) #시그널 생성시 data 변수를 전달함
            time.sleep(2)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.worker = Worker()
        self.worker.finished.connect(self.update_table_widget) #시그널과 슬롯(함수) 연결
        self.worker.start()

    @pyqtSlot(dict)
    def update_table_widget(self, data): #슬롯 정의
        try:
            기능
        except:
            pass

app = QApplication(sys.argv)
mywindow = MyWindow()
mywindow.show()
app.exec_()
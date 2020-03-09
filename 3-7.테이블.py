import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

# 데이터프레임
kospi_top5 = {
    'code': ['005930', '015760', '005380', '090430', '012330'],
    'name': ['삼성전자', '한국전력', '현대차', '아모레퍼시픽', '현대모비스'],
    'cprice': ['1,269,000', '60,100', '132,000', '414,500', '243,500']
}
column_idx_lookup = {'code': 0, 'name': 1, 'cprice': 2}


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setGeometry(800, 200, 300, 300)
        #테이블 생성, 아이템 항목 수정 불가
        self.table = QTableWidget(self)
        self.table.resize(290, 290)
        self.table.setRowCount(5)
        self.table.setColumnCount(3)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        #아이템 채우는 함수호출
        self.input_tableWidger()

    def input_tableWidger(self):
        #컬럼의 라벨을 설정
        column_headers = ['종목코드', '종목명', '종가']
        self.table.setHorizontalHeaderLabels(column_headers)

        for k, v in kospi_top5.items():
            #열에 대한 인덱스
            col = column_idx_lookup[k]
            for row, value in enumerate(v):
                #아이템 객체를 생성
                item = QTableWidgetItem(value)
                # '종가'에 해당하는 열 데이터는 setTextAlignment 메서드를 사용해 우측 정렬
                if col == 2:
                    item.setTextAlignment(Qt.AlignVCenter | Qt.AlignRight)
                self.table.setItem(row, col, item)
                
        #각 행과 열의 크기를 아이템 길이에 맞춰 조정
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mywindow = MyWindow()
    mywindow.show()
    app.exec_()
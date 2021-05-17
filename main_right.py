import os
import sys
import pandas as pd
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class MainRightArea(QWidget):
    """ 오른쪽 디스플레이 위젯 """
    qss = """
        QWidget {
            background: rgb(10, 10, 10);
        }
        QLabel {
            background: rgb(131, 131, 131);
            border-radius: 6px;
            color: rgb(255, 255, 255);
        }
        QTableWidget {
            background: rgb(131, 131, 131)
        }
    """
    # background: rgb(14, 22, 24);
    # background: rgb(31, 39, 42);


    def __init__(self, parent = None):
        super(MainRightArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        self.setMinimumHeight(1000)
        self.setMinimumWidth(int(1900 * (1 / 4)))

        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        label1 = MainParaArea(self)
        label2 = EndCondArea(self)

        layout.addWidget(label1)
        layout.addWidget(label2)
        self.setLayout(layout)

# ======================================================================================================================

class MainParaArea(QWidget):
    def __init__(self, parent=None):
        super(MainParaArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)

        # 타이틀 레이어 셋업 ----------------------------------------------------------------------------------------------
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # 1. 절차서 Table
        label = QLabel('CTMT 중대사고 위협 변수 감시')
        # procedure_label.setMinimumHeight(30)
        label.setFixedHeight(30)
        label.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)  # 텍스트 정렬


        para_table = ParaTable(self)

        layout.addWidget(label)
        layout.addWidget(para_table)

        self.setLayout(layout)

class ParaTable(QTableWidget):
    def __init__(self, parent):
        super(ParaTable, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setObjectName('ParaTable')

        # 테이블 프레임 모양 정의
        self.verticalHeader().setVisible(False)     # Row 넘버 숨기기

        # 테이블 셋업
        col_info = [('주요 발전소 변수', 158), ('현재 발전소 변수', 158), ('추이', 147)] # 475

        self.setColumnCount(len(col_info))
        self.setRowCount(9)

        col_names = []
        for i, (l, w) in enumerate(col_info):
            self.setColumnWidth(i, w)
            col_names.append(l)

        cell_height = self.rowHeight(0)
        print(cell_height)

        self.setHorizontalHeaderLabels(col_names)

# ======================================================================================================================

class EndCondArea(QWidget):
    def __init__(self, parent=None):
        super(EndCondArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedHeight(500)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel('SAMG 종결 조건 감시')
        label.setFixedHeight(30)
        label.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)

        label2 = EndCondTable(self)

        layout.addWidget(label)
        layout.addWidget(label2)

        self.setLayout(layout)

class EndCondTable(QTableWidget):
    def __init__(self, parent):
        super(EndCondTable, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setObjectName('EndCondTable')

        # 테이블 프레임 모양 정의
        self.verticalHeader().setVisible(False)     # Row 넘버 숨기기

        # 테이블 셋업
        col_info = [('SAMG 종료 조건', 263), ('추이', 200)] # 475

        self.setColumnCount(len(col_info))
        self.setRowCount(5)

        col_names = []
        for i, (l, w) in enumerate(col_info):
            self.setColumnWidth(i, w)
            col_names.append(l)

        self.setHorizontalHeaderLabels(col_names)






if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MainRightArea()
    window.show()
    app.exec_()

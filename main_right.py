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

        # 기본 속성
        self.setMinimumHeight(900-40)
        self.setFixedWidth(int(1900 * (1 / 4)))

        # 레이아웃
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

        # 레이아웃
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # 1. 절차서 Table
        label = QLabel('CTMT 중대사고 위협 변수 감시')
        label.setFixedHeight(30)
        label.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)  # 텍스트 정렬
        label.setStyleSheet("Color : white; font-size: 14pt; font-weight: bold")

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
        col_info = [('주요 발전소 변수', 231), ('현재 상태', 231)] # 475

        self.setColumnCount(len(col_info))
        self.setRowCount(8)

        # 테이블 행 높이 조절
        for each in range(self.rowCount()):
            self.setRowHeight(each, 54)

        col_names = []
        for i, (l, w) in enumerate(col_info):
            self.setColumnWidth(i, w)
            col_names.append(l)

        cell_height = self.rowHeight(0)
        print(cell_height)

        # 테이블 헤더
        self.setHorizontalHeaderLabels(col_names)
        self.horizontalHeader().setStyleSheet("::section {background-color : lightGray;font-size:13pt;}")

        self.setItem(0, 0, QTableWidgetItem('SG Narrow Level'))
        self.setItem(1, 0, QTableWidgetItem('RCS Pressure'))
        self.setItem(2, 0, QTableWidgetItem('CET Temperature'))
        self.setItem(3, 0, QTableWidgetItem('Radiation in Plant'))
        self.setItem(4, 0, QTableWidgetItem('CTMT Level'))
        self.setItem(5, 0, QTableWidgetItem('CTMT Pressure'))
        self.setItem(6, 0, QTableWidgetItem('CTMT Hyd. R'))
        self.setItem(7, 0, QTableWidgetItem('SFP L'))

        # 테이블 셀 내용 가운데 정렬
        delegate = AlignDelegate()
        self.setItemDelegateForColumn(0, delegate)

        fnt = self.font()
        fnt.setPointSize(12)
        self.setFont(fnt)


# ======================================================================================================================

class EndCondArea(QWidget):
    def __init__(self, parent=None):
        super(EndCondArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setFixedHeight(340)
        # 레이아웃
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        label = QLabel('SAMG 종결 조건 감시')
        label.setFixedHeight(30)
        label.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        label.setStyleSheet("Color : white; font-size: 14pt; font-weight: bold")

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
        col_info = [('SAMG 종료 조건 변수', 231), ('현재 상태', 231)] # 475

        self.setColumnCount(len(col_info))
        self.setRowCount(5)

        col_names = []
        for i, (l, w) in enumerate(col_info):
            self.setColumnWidth(i, w)
            col_names.append(l)

        # 테이블 헤더
        self.setHorizontalHeaderLabels(col_names)
        # self.table.horizontalHeader().setFixedHeight(60)
        self.horizontalHeader().setStyleSheet("::section {background-color : lightGray;font-size:13pt;}")

        # 테이블 행 높이 조절
        for each in range(self.rowCount()):
            self.setRowHeight(each, 54)

        self.setItem(0, 0, QTableWidgetItem('CET Temperature'))
        self.setItem(1, 0, QTableWidgetItem('Rad. in Plant'))
        self.setItem(2, 0, QTableWidgetItem('CTMT Pressure'))
        self.setItem(3, 0, QTableWidgetItem('CTMT Hyd. R'))
        self.setItem(4, 0, QTableWidgetItem('SFP L'))

        # 테이블 셀 내용 가운데 정렬
        delegate = AlignDelegate()
        self.setItemDelegateForColumn(0, delegate)

        fnt = self.font()
        fnt.setPointSize(12)
        self.setFont(fnt)


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MainRightArea()
    window.show()
    app.exec_()

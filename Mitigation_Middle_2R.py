import os
import sys
import pandas as pd
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from PyQt5.QtChart import *

# from button2 import custom_button




class MitigationMiddleArea_2R(QWidget):

    qss = """
        QWidget {
            background: rgb(128, 128, 128);
        }
        QLabel {
            background: rgb(131, 131, 131);
            border-radius: 6px;
            color: rgb(255, 255, 255);
        }
        QTableWidget {
            background: rgb(221, 221, 221)
        }
        QPushButton{
            background: rgb(221, 221, 221)
        }
        QScrollBar::sub-line:vertical {
    padding-top: 50px;
    height: 20px;
    background-color: blue;
}
QScrollBar::vertical {
    margin-top: 50px;
    padding-top: 20px;
}
    """


    def __init__(self, parent = None):
        super(MitigationMiddleArea_2R, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 기본 속성
        self.setMinimumHeight(1000)
        self.setFixedWidth(int(1920 * (1 / 3)))
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        # 1. 절차서 Table
        # label = QLabel('CTMT 중대사고 위협 변수 감시')
        # label.setFixedHeight(30)
        # label.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)  # 텍스트 정렬
        # label.setStyleSheet("Color : white; font-size: 14pt; font-weight: bold")
        layout = QVBoxLayout(self)
        # layout.setContentsMargins(5, 5, 5, 5)
        para_table = ParaTable(self)
        self.scroll.setWidget(para_table)
        # layout.addWidget(label)


        layout.addWidget(self.scroll)
        # layout.addWidget(para_table)
        self.setLayout(layout)
# ======================================================================================================================

class ParaTable(QTableWidget):
    def __init__(self, parent):
        super(ParaTable, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setObjectName('ParaTable')
        self.setGeometry(0, 0, 900, 1100)  # 1900*(3/4) = 1425
        # 테이블 프레임 모양 정의
        self.verticalHeader().setVisible(False)     # Row 넘버 숨기기

        # 테이블 셋업
        col_info = [('주요 발전소 변수', 360), ('현재 발전소 변수', 268)] # 475
        self.setColumnCount(len(col_info))
        self.setRowCount(7)
        self.horizontalHeader().setFixedHeight(60)
        # 테이블 행 높이 조절
        for each in range(self.rowCount()):
            self.setRowHeight(each, 60)

        col_names = []
        for i, (l, w) in enumerate(col_info):
            self.setColumnWidth(i, w)
            col_names.append(l)

        cell_height = self.rowHeight(0)
        print(cell_height)

        # 테이블 헤더
        self.setHorizontalHeaderLabels(col_names)
        self.horizontalHeader().setStyleSheet("::section {background: rgb(221, 221, 221);font-size:13pt;}")
        self.horizontalHeader().sectionPressed.disconnect()
        # self.setItem(0, 0, QTableWidgetItem('발전소 부지 경계 선량'))
        # self.setItem(1, 0, QTableWidgetItem('격납건물 압력'))
        # self.setItem(2, 0, QTableWidgetItem('격납건물 압력'))
        # self.setItem(3, 0, QTableWidgetItem('격납건물 압력'))
        # self.setItem(4, 0, QTableWidgetItem('SG 1 수위 NR'))
        # self.setItem(5, 0, QTableWidgetItem('SG 2 수위 NR'))
        # self.setItem(6, 0, QTableWidgetItem('격납건물 수위'))

        item = [0*i for i in range(7)]
        item2 = [0*i for i in range(7)]
        item[0] = QTableWidgetItem('발전소 부지 경계 선량')
        item[1] = QTableWidgetItem('격납건물 압력')
        item[2] = QTableWidgetItem('격납건물 압력')
        item[3] = QTableWidgetItem('격납건물 압력')
        item[4] = QTableWidgetItem('SG 1 수위 NR')
        item[5] = QTableWidgetItem('SG 2 수위 NR')
        item[6] = QTableWidgetItem('격납건물 수위')

        for i in range(7):
            item[i].setFlags(Qt.NoItemFlags)
            item[i].setForeground(QBrush(QColor(0, 0, 0)))
            self.setItem(i, 0, item[i])

        for i in range(7):
            item2[i] = QTableWidgetItem('value')
            self.setItem(i, 1, item2[i])
        # self.doubleClicked.connect(self.popup)

        # self.item1 = QPushButton("value1")
        # self.setCellWidget(0, 1, self.item1)

        # self.cellClicked.connect(self.__mycell_clicked)
        # mycom.currentTextChanged.connect(self.__mycom_text_changed)

        # 테이블 셀 내용 가운데 정렬
        delegate = AlignDelegate()
        self.setItemDelegateForColumn(0, delegate)
        self.setItemDelegateForColumn(1, delegate)
        fnt = self.font()
        fnt.setPointSize(12)
        self.setFont(fnt)



# ======================================================================================================================


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MitigationMiddleArea_2R()
    window.show()
    app.exec_()
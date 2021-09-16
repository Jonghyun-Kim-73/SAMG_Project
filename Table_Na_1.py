import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class tableNa_1(QWidget):
    qss = """
            QWidget {
                background: rgb(221, 221, 221);

            }
            QLabel {
                background: rgb(131, 131, 131);
                border-radius: 6px;
                color: rgb(255, 255, 255);
            }
            QTableWidget {
                background: rgb(221, 221, 221);

            }
            QPushButton{
                background: rgb(221, 221, 221)
            }

QScrollBar::vertical {
    height:0px;
    margin-top: 0px;
    padding-top: 0px;
}
        """

    def __init__(self, parent=None):
        super(tableNa_1, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.setContentsMargins(0, 0, 0, 0)
        # 기본 속성
        layout = QVBoxLayout(self)

        self.setLayout(layout)

        self.scrollTop = QScrollArea()
        self.scrollTop.setFixedHeight(84)
        self.scrollTop.setWidgetResizable(True)
        self.scrollTop.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollTop.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scrollBottom = QScrollArea()
        self.scrollBottom.setWidgetResizable(True)
        self.scrollBottom.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        table_header = TableHeader_Na_1(self)
        para_table = ParaTable_Na_1(self)

        self.scrollTop.setWidget(table_header)
        self.scrollBottom.setWidget(para_table)
        # layout.addWidget(label)

        layout.addWidget(self.scrollTop)
        layout.addWidget(self.scrollBottom)
        # layout.addWidget(para_table)


class TableHeader_Na_1(QTableWidget):
    def __init__(self, parent):
        super(TableHeader_Na_1, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)

        # 테이블 프레임 모양 정의
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)  # Row 넘버 숨기기
        self.setContentsMargins(0, 0, 0, 0)

        self.setColumnCount(4)
        self.setRowCount(2)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setRowHeight(0, 40)
        self.setRowHeight(1, 40)
        self.setColumnWidth(0, 208)
        for i in range(1, self.columnCount()):
            self.setColumnWidth(i, 210)

        # SPAN 생성
        self.setSpan(0, 1, 1, 3)

        # 테이블 헤더
        self.setItem(0, 1, QTableWidgetItem("급수 승압 펌프"))

        self.setItem(1, 1, QTableWidgetItem("1"))
        self.setItem(1, 2, QTableWidgetItem("2"))
        self.setItem(1, 3, QTableWidgetItem("3"))

        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegate(delegate)

        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)
        self.setFont(fnt)


class ParaTable_Na_1(QTableWidget):
    def __init__(self, parent):
        super(ParaTable_Na_1, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)  # Row 넘버 숨기기
        self.setContentsMargins(0, 0, 0, 0)
        # self.setStyleSheet(self.qss)
        self.setColumnCount(4)
        self.setRowCount(17)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setColumnWidth(0, 208)
        for i in range(1, self.columnCount()):
            self.setColumnWidth(i, 210)
        for i in range(0, self.rowCount()):
            self.setRowHeight(i, 40)

        # SPAN 생성(타이틀)
        self.setSpan(0, 0, 1, 4)
        self.setSpan(4, 0, 1, 4)
        self.setSpan(8, 0, 1, 4)
        self.setSpan(10, 0, 1, 4)
        self.setSpan(12, 0, 1, 4)
        self.setSpan(13, 0, 1, 4)

        # SPAN 생성(이용 가능한 수단)
        self.setSpan(14, 1, 1, 4)
        self.setSpan(15, 1, 1, 4)
        self.setSpan(16, 1, 1, 4)

        # 행
        self.setItem(0, 0, QTableWidgetItem("펌프 이용 가능성"))
        self.setItem(4, 0, QTableWidgetItem("펌프 제한 조건"))
        self.setItem(8, 0, QTableWidgetItem("급수원 이용 가능성"))
        self.setItem(10, 0, QTableWidgetItem("급수 주입 경로"))
        self.setItem(13, 0, QTableWidgetItem("이용 가능한 수단"))

        # 열
        self.setItem(1, 0, QTableWidgetItem("손상 상태"))
        self.setItem(2, 0, QTableWidgetItem("교류 전원"))
        self.setItem(3, 0, QTableWidgetItem("증기발생기 압력"))

        self.setItem(5, 0, QTableWidgetItem("밀봉 냉각"))
        self.setItem(6, 0, QTableWidgetItem("전동기 냉각"))
        self.setItem(7, 0, QTableWidgetItem("윤활유 냉각"))

        self.setItem(9, 0, QTableWidgetItem("탈기 저장 탱크"))

        self.setItem(11, 0, QTableWidgetItem("주급수 배관"))

        self.setItem(14, 0, QTableWidgetItem("급수펌프"))
        self.setItem(15, 0, QTableWidgetItem("급수원"))
        self.setItem(16, 0, QTableWidgetItem("급수 주입 경로"))

        # N/A표시

        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegate(delegate)

        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)
        self.item(13, 0).setFont(fnt)
        self.item(14, 0).setFont(fnt)
        self.item(15, 0).setFont(fnt)
        self.item(16, 0).setFont(fnt)


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = tableNa_1()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
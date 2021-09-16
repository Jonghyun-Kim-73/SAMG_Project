import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class tableNa_2(QWidget):
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
        super(tableNa_2, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.setContentsMargins(0, 0, 0, 0)
        # 기본 속성
        layout = QVBoxLayout(self)

        self.setLayout(layout)
        self.scrollTop = QScrollArea()
        self.scrollTop.setFixedHeight(104)
        self.scrollTop.setWidgetResizable(True)
        self.scrollTop.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollTop.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scrollBottom = QScrollArea()
        self.scrollBottom.setWidgetResizable(True)
        self.scrollBottom.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        table_header = TableHeader_Na_2(self)
        para_table = ParaTable_Na_2(self)

        self.scrollTop.setWidget(table_header)
        self.scrollBottom.setWidget(para_table)
        # layout.addWidget(label)

        layout.addWidget(self.scrollTop)
        layout.addWidget(self.scrollBottom)
        # layout.addWidget(para_table)


class TableHeader_Na_2(QTableWidget):
    def __init__(self, parent):
        super(TableHeader_Na_2, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)

        # 테이블 프레임 모양 정의
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)  # Row 넘버 숨기기
        self.setContentsMargins(0, 0, 0, 0)

        self.setColumnCount(13)
        self.setRowCount(2)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setRowHeight(0, 60)
        self.setRowHeight(1, 40)
        self.setColumnWidth(0, 82)
        for i in range(1, self.columnCount()):
            self.setColumnWidth(i, 63)

        # SPAN 생성
        self.setSpan(0, 1, 1, 4)
        self.setSpan(0, 5, 1, 6)
        self.setSpan(0, 11, 1, 2)

        # 테이블 헤더
        self.setItem(0, 1, QTableWidgetItem("주증기 대기 방출 밸브"))
        self.setItem(0, 5, QTableWidgetItem("터빈 우회 복수기 밸브"))
        self.setItem(0, 11, QTableWidgetItem("터빈 우회 대기 밸브"))

        self.setItem(1, 1, QTableWidgetItem("1"))
        self.setItem(1, 2, QTableWidgetItem("2"))
        self.setItem(1, 3, QTableWidgetItem("3"))
        self.setItem(1, 4, QTableWidgetItem("4"))

        self.setItem(1, 5, QTableWidgetItem("1"))
        self.setItem(1, 6, QTableWidgetItem("2"))
        self.setItem(1, 7, QTableWidgetItem("3"))
        self.setItem(1, 8, QTableWidgetItem("4"))
        self.setItem(1, 9, QTableWidgetItem("5"))
        self.setItem(1, 10, QTableWidgetItem("6"))

        self.setItem(1, 11, QTableWidgetItem("1"))
        self.setItem(1, 12, QTableWidgetItem("2"))

        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegate(delegate)

        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)
        self.setFont(fnt)


class ParaTable_Na_2(QTableWidget):
    def __init__(self, parent):
        super(ParaTable_Na_2, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)  # Row 넘버 숨기기
        self.setContentsMargins(0, 0, 0, 0)
        # self.setStyleSheet(self.qss)
        self.setColumnCount(13)
        self.setRowCount(10)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setColumnWidth(0, 82)
        for i in range(1, self.columnCount()):
            self.setColumnWidth(i, 63)

        self.setRowHeight(1, 60)
        self.setRowHeight(4, 80)
        # SPAN 생성(타이틀)
        self.setSpan(0, 0, 1, 13)
        self.setSpan(5, 0, 1, 13)
        self.setSpan(7, 0, 1, 13)
        self.setSpan(8, 0, 1, 13)

        # SPAN 생성(이용 가능한 수단)
        self.setSpan(9, 0, 1, 3)
        self.setSpan(9, 4, 1, 13)

        # 행
        self.setItem(0, 0, QTableWidgetItem("밸브 이용 가능성"))
        self.setItem(5, 0, QTableWidgetItem("복수기 이용 가능성"))
        self.setItem(8, 0, QTableWidgetItem("이용 가능한 수단"))

        # 열
        self.setItem(1, 0, QTableWidgetItem("계측용\n압축 공기"))
        self.setItem(2, 0, QTableWidgetItem("직류 전원"))
        self.setItem(3, 0, QTableWidgetItem("차단 밸브"))
        self.setItem(4, 0, QTableWidgetItem("MSIV\n또는\n우회 밸브"))

        self.setItem(6, 0, QTableWidgetItem("복수기"))

        self.setItem(9, 0, QTableWidgetItem("선정된 밸브"))

        # N/A표시

        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegate(delegate)

        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)
        self.item(8, 0).setFont(fnt)
        self.item(9, 0).setFont(fnt)


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = tableNa_2()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class table_5_4(QWidget):
    qss = """
            QWidget {
                background: rgb(221, 221, 221);
                border:0px solid;
            }
            QTableWidget {
                background: rgb(221, 221, 221);
            }
            QPushButton{
                background: rgb(221, 221, 221)
            }
            QTableWidget {
                background: rgb(221, 221, 221);
            }
            QPushButton{
                background: rgb(221, 221, 221)
            }
            QCheckBox {
                margin-left:0px;
                font-size:15px;
            }
            QCheckBox::indicator {
                width:  60px;
                height: 40px;
            }
            QCheckBox::indicator::unchecked {
                width:  60px;
                height: 40px;
                border : 0px solid;
            }
            QCheckBox::indicator::checked {
                image : url(./check.png);
                height:30px;
                width:60px;
            }
            QScrollBar::vertical {
                height:0px;
                margin-top: 0px;
                padding-top: 0px;
            }
           QTableView {
                gridline-color : black;
            }
            QHeaderView::section {
                background: black;
            }
            QTextEdit{
                font-size: 16pt;
                Color : black;
                border : 0px solid
            }
        """

    def __init__(self, parent=None):
        super(table_5_4, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.setContentsMargins(0, 0, 0, 0)
        # 기본 속성
        layout = QVBoxLayout(self)
        label = QTextEdit("10. 추가적인 완화 조치들이 필요한 지를 결정한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10,10,10,20)
        label.setFixedHeight(40)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)
        label.setDisabled(True)

        label1 = QTextEdit("<p style=\"line-height:130%\">&nbsp;&nbsp;가. 실제로 발생한 부정적 영향을 파악한다.<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;나. 실제로 발생한 부정적 영향을 완화할 수 있는 조치들을 평가한다.<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;다. 부정적 영향을 완화할 수 있는 조치들이 있으면 수행하도록 주제어실에 지시한다.<p>")
        label1.setStyleSheet("font-size: 14pt;font-weight: bold")
        label1.setContentsMargins(10, 10, 10, 20)
        label1.setFixedHeight(120)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)
        label1.setDisabled(True)

        self.setLayout(layout)
        self.scrollTop = QScrollArea()
        self.scrollTop.setFixedHeight(45)
        self.scrollTop.setWidgetResizable(True)
        self.scrollTop.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollTop.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        self.scrollBottom = QScrollArea()
        self.scrollBottom.setWidgetResizable(True)
        self.scrollBottom.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        table_header = TableHeader(self)
        para_table = ParaTable(self)
        self.scrollTop.setWidget(table_header)
        self.scrollBottom.setWidget(para_table)

        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(self.scrollTop)
        layout.addWidget(self.scrollBottom)


class TableHeader(QTableWidget):
    def __init__(self, parent):
        super(TableHeader, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)

        # 테이블 프레임 모양 정의
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)
        self.setContentsMargins(0, 0, 0, 0)

        self.setColumnCount(4)
        self.setRowCount(1)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setRowHeight(0, 40)
        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 160)
        self.setColumnWidth(2, 505)
        self.setColumnWidth(3, 60)

        # 테이블 헤더
        self.setItem(0, 0, QTableWidgetItem("부정적 영향"))
        self.setItem(0, 1, QTableWidgetItem("탐지방법"))
        self.setItem(0, 2, QTableWidgetItem("완화조치"))
        self.setItem(0, 3, QTableWidgetItem("선택"))

        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegate(delegate)

        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)
        self.setFont(fnt)


class ParaTable(QTableWidget):
    def __init__(self, parent):
        super(ParaTable, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)
        self.setContentsMargins(0, 0, 0, 0)
        self.setColumnCount(4)
        self.setRowCount(6)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setColumnWidth(0, 100)
        self.setColumnWidth(1, 160)
        self.setColumnWidth(2, 505)
        self.setColumnWidth(3, 60)
        for i in range(0, self.rowCount()):
            self.setRowHeight(i, 60)
        self.setRowHeight(1, 80)
        self.setRowHeight(3, 80)
        self.setRowHeight(4, 80)
        # SPAN 생성(부정적영향)
        self.setSpan(0, 0, 3, 1)
        self.setSpan(0, 1, 3, 1)
        self.setSpan(3, 0, 3, 1)
        self.setSpan(3, 1, 3, 1)

        self.setItem(0, 0, QTableWidgetItem("증기발생기\n열충격"))
        self.setItem(3, 0, QTableWidgetItem("증기발생기\n튜브 크립\n파손"))

        self.setItem(0, 1, QTableWidgetItem("예기치 않은\n증기발생기 압력\n감소"))
        self.setItem(3, 1, QTableWidgetItem("2차측 방사선\n계측기에서\n핵분열 생성물의\n큰 증가가 감지됨"))

        self.setItem(0, 2, QTableWidgetItem("건전한 증기발생기 사용이 가능하다면 고장난 증기발생기로의 급수 주입을 중단한다."))
        self.setItem(1, 2, QTableWidgetItem("다른 증기발생기로 급수를 주입한다.\n열응력을 최소화하기 위하여 급수 주입 초기에는 주입량을 적게 제한한다."))
        self.setItem(2, 2, QTableWidgetItem("고장난 증기발생기로 급수의 주입이 종결되었다면 고장난 증기발생기를 격리한다."))

        self.setItem(3, 2, QTableWidgetItem("모든 증기발생기의 튜브가 파손되었다면 튜브가 급수로 가득 찰 때까지 현재 급수를 주입하고 있는 증기발생기로 급수 주입량을 최대로 한다."))
        self.setItem(4, 2, QTableWidgetItem("다른 증기발생기에 급수를 주입을 시작한다.\n열응력을 최소화하기 위해서 급수 주입량을 적게 제한할 필요가 있다."))
        self.setItem(5, 2, QTableWidgetItem("튜브가 파열된 증기발생기를 격리한다."))

      # 체크박스
        for i in range(0, self.rowCount()):
            self.checkbox = QCheckBox(self)
            self.setCellWidget(i, 3, self.checkbox)

        # 테이블 정렬
        delegate = AlignDelegate2()
        self.setItemDelegate(delegate)

        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter
class AlignDelegate2(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate2, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignTop


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = table_5_4()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
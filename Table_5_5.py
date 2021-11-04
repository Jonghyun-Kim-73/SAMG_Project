import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class table_5_5(QWidget):
    """ 중간 디스플레이 위젯 """
    qss = """
            QWidget {
                background: rgb(221, 221, 221);   
                border:0px solid;
            }
            QPushButton{
                background-color: rgb(221,221,221);
                border: 1px solid rgb(0,0,0);       
                font-size: 14pt;
                font-weight: bold
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
        super(table_5_5, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(self.qss)
        self.setContentsMargins(0, 0, 0, 0)

        # 기본 속성
        layout = QVBoxLayout(self)
        label = QTextEdit("11. 추가적인 증기발생기 급수 주입이 필요한지를 결정한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10, 10, 10, 20)
        label.setDisabled(True)
        label.setFixedHeight(40)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        label1 = QTextEdit("<p style=\"line-height:130%\">가. 현재의 급수 주입율이 적절한가 평가한다.<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;1) 계산표-05, “장기붕괴열 제거를 위한 냉각재 주입율” 참조<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;2) 발전소 반응 감시<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;• 증기발생기 수위 점검 – 안정적이거나 증가함.<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;• 증기발생기 압력 점검 – 안정적이거나 증기발생기로 급수하는 펌프의<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;  체결수두 이하임.<p>")
        label1.setStyleSheet("font-size: 14pt;font-weight: bold")
        label1.setContentsMargins(10, 10, 10, 20)
        label1.setDisabled(True)
        label1.setFixedHeight(300)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        label2 = QTextEdit("나. 현재의 급수주입 경로가 적절하지 않고 추가적인 급수 주입 경로가 있다면\n단계 3으로 돌아간다.")
        label2.setStyleSheet("font-size: 14pt;font-weight: bold")
        label2.setContentsMargins(10, 10, 10, 20)
        label2.setDisabled(True)
        label2.setFixedHeight(80)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        self.setLayout(layout)

        para_table = ParaTable(self)

        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(para_table)
        layout.addWidget(label2)
        layout.addStretch()

class ParaTable(QTableWidget):
    def __init__(self, parent):
        super(ParaTable, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedHeight(300)
        self.setColumnCount(2)
        self.setRowCount(6)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 너비 조절
        self.setColumnWidth(0, 150)
        self.setColumnWidth(1, 686)
        for i in range(0, 6):
            self.setRowHeight(i, 40)

        self.setSpan(0, 0, 1, 2)

        self.setItem(0, 0, QTableWidgetItem("증기발생기 현재 값"))
        self.setItem(1, 0, QTableWidgetItem("증기발생기"))
        self.setItem(1, 1, QTableWidgetItem("변수값"))

        self.setItem(2, 0, QTableWidgetItem("증기발생기 1 수위"))
        self.setItem(3, 0, QTableWidgetItem("증기발생기 2 수위"))
        self.setItem(4, 0, QTableWidgetItem("증기발생기 1 압력"))
        self.setItem(5, 0, QTableWidgetItem("증기발생기 2 압력"))

        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegate(delegate)

        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)
        self.setFont(fnt)

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = table_5_5()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
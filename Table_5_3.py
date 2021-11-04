import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class table_5_3(QWidget):
    """ 중간 디스플레이 위젯 """
    qss = """
            QWidget {
                background: rgb(221, 221, 221);   
                border : 0px solid;
            }
            QPushButton{
                background-color: rgb(221,221,221);
                border: 1px solid rgb(0,0,0);       
                font-size: 14pt;
                font-weight: bold
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
                width:  40px;
                height: 40px;
            }
            QCheckBox::indicator::unchecked {
                width:  90px;
                height: 40px;
                border : 0px solid;
            }
            QCheckBox::indicator::checked {
                image : url(./check.png);
                height:30px;
                width:90px;
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
        super(table_5_3, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(self.qss)
        self.setContentsMargins(0, 0, 0, 0)

        # 기본 속성
        layout = QVBoxLayout(self)
        label = QTextEdit("9. 주제어실에서 증기발생기 급수 주입을 성공적으로 실시하였는가를 확인한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10, 10, 10, 20)
        label.setFixedHeight(40)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)
        label.setDisabled(True)
        label1 = QTextEdit("<p style=\"line-height:130%\">&nbsp;&nbsp;가. 감시하여야 할 변수는 다음과 같다.<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;• 증기발생기 수위<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;• 증기발생기 압력<p>")
        label1.setStyleSheet("font-size: 14pt;font-weight: bold")
        label1.setContentsMargins(10, 10, 10, 20)
        label1.setFixedHeight(120)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)
        label1.setDisabled(True)
        self.setLayout(layout)

        para_table = ParaTable(self)

        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(para_table)
        layout.addStretch()

class ParaTable(QTableWidget):
    def __init__(self, parent):
        super(ParaTable, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)

        self.setContentsMargins(0, 0, 0, 0)
        self.setColumnCount(2)
        self.setRowCount(5)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 너비 조절
        self.setColumnWidth(0, 150)
        self.setColumnWidth(1, 686)
        for i in range(0, 5):
            self.setRowHeight(i, 40)

        self.setSpan(0, 0, 1, 2)

        self.setItem(0, 0, QTableWidgetItem("증기발생기 현재 값"))
        self.setItem(1, 0, QTableWidgetItem("증기발생기 1 수위"))
        self.setItem(2, 0, QTableWidgetItem("증기발생기 2 수위"))
        self.setItem(3, 0, QTableWidgetItem("증기발생기 1 압력"))
        self.setItem(4, 0, QTableWidgetItem("증기발생기 2 압력"))

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
    window = table_5_3()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
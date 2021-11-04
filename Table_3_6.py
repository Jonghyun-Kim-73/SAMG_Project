import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class table_3_6(QWidget):
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
            QCheckBox::indicator {
                width:  38px;
                height: 60px;
            }
            QCheckBox::indicator::unchecked {
                width:  38px;
                height: 60px;
                border : 0px solid;
            }
            QCheckBox::indicator::checked {
                image : url(./check.png);
                height:30px;
                width:38px;
            }
            QTextEdit{
                font-size: 18pt;
                Color : black;
                border : 0px solid
            }
            QTextEdit#button{
                font-size: 12pt;
                font-weight:bold;
                Color : black;
                border : 0px solid
            }
            QTableView {
                gridline-color : black;
            }
            QHeaderView::section {
                background: black;
            }
        """

    def __init__(self, parent=None):
        super(table_3_6, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(self.qss)
        # 기본 속성
        layout = QVBoxLayout(self)
        label = QTextEdit("5. 증기발생기 급수 주입 실시 여부를 결정한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10, 10, 10, 20)
        label.setDisabled(True)
        label.setFixedHeight(80)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        label1 = QTextEdit("가. 증기발생기 급수 주입을 실시하지 않았을 때의 결과를 평가한다.")
        label1.setStyleSheet("font-size: 18pt;font-weight: bold")
        label1.setContentsMargins(10, 10, 10, 20)
        label1.setDisabled(True)
        label1.setFixedHeight(80)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        label2 = QTextEdit("<p style=\"line-height:130%\">나. 증기발생기 급수 주입을 실시하지 않았을 때 결과와 증기발생기 급수<p>"
                           "<p style=\"line-height:130%\">주입을 실시하였을 떄의 부정적 영향을 비교한다.<p>")
        label2.setStyleSheet("font-size: 18pt;font-weight: bold")
        label2.setContentsMargins(10, 10, 10, 20)
        label2.setDisabled(True)
        label2.setFixedHeight(160)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        label3 = QTextEdit("<p style=\"line-height:130%\">다. 증기발생기 급수 주입을 실시하지 않기로 결정되었다면 전략수행<p>"
                           "<p style=\"line-height:130%\">제어도 또는 이 전략 수행 직전에 주행중이든 전략으로 되돌아간다.<p>")
        label3.setStyleSheet("font-size: 18pt;font-weight: bold")
        label3.setContentsMargins(10, 10, 10, 20)
        label3.setDisabled(True)
        label3.setFixedHeight(160)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        self.setLayout(layout)

        para_table = ParaTable(self)

        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(para_table)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addStretch(1)

class ParaTable(QTableWidget):
    def __init__(self, parent):
        super(ParaTable, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)

        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedHeight(200)
        self.setColumnCount(2)
        self.setRowCount(4)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 너비 조절
        self.setColumnWidth(0, 798)
        self.setColumnWidth(1, 38)
        for i in range(0, 5):
            self.setRowHeight(i, 40)

        self.setItem(0, 0, QTableWidgetItem("  증기발생기가 RCS의 열제거원 역할을 할 수 없음"))
        self.setItem(1, 0, QTableWidgetItem("  증기발생기 튜브의 건전성이 위협받을 수 있음"))
        self.setItem(2, 0, QTableWidgetItem("  RCS를 감압하는 데 증기발생기를 사용할 수 없음"))
        self.setItem(3, 0, QTableWidgetItem("  증기발생기 튜브 파손부로 부터 누출된 핵분열 생성물을 세정할 수 없음"))

        # 체크박스
        for i in range(0, self.rowCount()):
            self.checkbox = QCheckBox(self)
            self.setCellWidget(i, 1, self.checkbox)

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
    window = table_3_6()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
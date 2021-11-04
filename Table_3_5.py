import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Flag import Flag


class table_3_5(QWidget):
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
            QScrollBar::vertical {
                height:0px;
                margin-top: 0px;
                padding-top: 0px;
            }
            QCheckBox {
                margin-left:0px;
                font-size:15px;
            }
            QTableWidget {
               gridline-color : black;
            }
            QCheckBox::indicator {
                width:  60px;
                height: 60px;
            }
            QCheckBox::indicator::unchecked {
                width:  60px;
                height: 60px;
                border : 0px solid;
            }
            QCheckBox::indicator::checked {
                image : url(./check.png);
                height:30px;
                width:60px;
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
        super(table_3_5, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(self.qss)
        # 기본 속성
        layout = QVBoxLayout(self)
        label = QTextEdit("4.다. 부정적 영향을 완화하기 위한 조치들을 평가한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10, 10, 10, 20)
        label.setDisabled(True)
        label.setFixedHeight(60)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        label2 = QTextEdit("  - 발생 가능한 부정적 영향")
        label2.setStyleSheet("font-size: 18pt;font-weight: bold")
        label2.setContentsMargins(10, 10, 10, 20)
        label2.setDisabled(True)
        label2.setFixedHeight(45)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)
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
        layout.addWidget(label2)
        layout.addWidget(self.scrollTop)
        layout.addWidget(self.scrollBottom)

class TableHeader(QTableWidget):
    def __init__(self, parent):
        super(TableHeader, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)

        # 테이블 프레임 모양 정의
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)

        self.setColumnCount(4)
        self.setRowCount(1)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setRowHeight(0, 40)
        self.setColumnWidth(0, 120)
        self.setColumnWidth(1, 220)
        self.setColumnWidth(2, 436)
        self.setColumnWidth(3, 60)

        # 테이블 헤더
        self.setItem(0, 0, QTableWidgetItem("부정적 영향"))
        self.setItem(0, 1, QTableWidgetItem("적용시점"))
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
        # 테이블 프레임 모양 정의
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)
        self.setContentsMargins(0, 0, 0, 0)
        self.setColumnCount(4)
        self.setRowCount(9)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setColumnWidth(0, 120)
        self.setColumnWidth(1, 220)
        self.setColumnWidth(2, 436)
        self.setColumnWidth(3, 60)

        # SPAN 생성(부정적영향)
        self.setSpan(0, 0, 3, 1)
        self.setSpan(0, 1, 3, 1)
        self.setSpan(3, 0, 3, 1)
        self.setSpan(3, 1, 3, 1)
        self.setSpan(6, 0, 3, 1)
        self.setSpan(6, 1, 3, 1)

        self.setItem(0, 0, QTableWidgetItem("증기발생기\n열충격"))
        self.setItem(3, 0, QTableWidgetItem("증기발생기\n튜브 누설로\n핵분열 생성물\n방출"))
        self.setItem(6, 0, QTableWidgetItem("증기발생기\n튜브 크립 파열"))

        self.setItem(0, 1, QTableWidgetItem("급수가 고갈된 고온의 S/G에\n급수할 때\nS/G 광역수위가 [L02] 이하\n"))
        self.setItem(3, 1, QTableWidgetItem("튜브가 파손되거나 누출이\n있는 S/G로 급수할 때"))
        self.setItem(6, 1, QTableWidgetItem("급수가 고갈된 고온의 S/G를\n감압할 때\n감압중인 S/G\n광역수위가 [L02]이하\n일 떄와 RCS 압력이 S/G\n압력 이상일 때"))

        #QTextEdit enter 안먹음
        t1 = QTextEdit()
        t1.setPlainText("급수가 고갈된 고온의 S/G에\n급수할 때\nS/G 광역수위가 [L02] 이하\n\n\n\nSG1 L : \nSG2 L : ")
        t1.setObjectName("button")
        t2 = QTextEdit()
        t2.setPlainText("튜브가 파손되거나 누출이\n있는 S/G로 급수할 때\n\n\n\n\nSG1 R : \nSG2 R : ")
        t2.setObjectName("button")
        t3 = QTextEdit()
        t3.setPlainText("급수가 고갈된 고온의 S/G를\n감압할 때\n감압중인 S/G\n광역수위가 [L02]이하\n일 떄와 RCS 압력이 S/G\n압력 이상일 때\n\nSG1 L : \nSG2 L :\nRCS T : \nCET T :\nPZR T : \nRCS Hot-leg T :  \nRCS Cold-leg 1 T :\nRCS Cold-leg 2 T :")
        t3.setObjectName("button")

        self.setCellWidget(0, 1, t1)
        self.setCellWidget(3, 1, t2)
        self.setCellWidget(6, 1, t3)


        self.setItem(0, 2, QTableWidgetItem("급수 주입의 초기에는 주입량을 적게 제한함"))
        self.setItem(1, 2, QTableWidgetItem("S/G 튜브 파손의 영향이 최소화되는 시간에 S/G\n광역수위가 최소로 지시될때까지 급수가 고갈된 단\n1개의 S/G에 급수를 주입함"))
        self.setItem(2, 2, QTableWidgetItem("S/G 튜브 파손의 영향을 최소화하기 위해 격리가\n가능한 S/G에만 급수를 주입함."))

        self.setItem(3, 2, QTableWidgetItem("건전한 S/G에만 급수하고 비등시킴"))
        self.setItem(4, 2, QTableWidgetItem("S/G 일차측에서 이차측으로 냉각재 누설을\n최소화하기 위하여 RCS를 감압함\n(완화-05, “원자로냉각재계통 감압“ 참조)"))
        self.setItem(5, 2, QTableWidgetItem("복수기로 증기를 배출하여 S/G를 감압함"))

        self.setItem(6, 2, QTableWidgetItem("S/G 튜브 파손의 영향이 최소화되는 시간에 급수가\n고갈되고 고온인 S/G 1개만 감압함"))
        self.setItem(7, 2, QTableWidgetItem("S/G 압력이 급수원의 체결수두 이하일 때 가능한 빨리\n급수 주입량을 복구함. S/G에 급수 주입 초기에는\n주입략을 적게 제한함"))
        self.setItem(8, 2, QTableWidgetItem("RCS를 감압함\n(완화-05, “원자로냉각재계통 감압“ 참조)"))

        # 체크박스
        count = 0
        self.checkbox = []
        for i in range(0, self.rowCount()):
            self.checkbox.append(QCheckBox())
            self.setCellWidget(i, 3, self.checkbox[count])
            count = count + 1
        # 테이블 정렬
        delegate = AlignDelegate2()
        self.setItemDelegate(delegate)

        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)
        self.setFont(fnt)

        # timer section
        timer = QTimer(self)
        timer.setInterval(1000)
        timer.timeout.connect(self.dis_update)
        timer.start()

    def dis_update(self):
        for i in range(9):
            if Flag.s3_3[i]:
                self.setRowHidden(i, True)
            else:
                self.setRowHidden(i, False)
        count = [0] * 3
        for i in range(9):
            if i < 3:
                if not Flag.s3_3[i]:
                    count[0] += 1
            elif i < 6:
                if not Flag.s3_3[i]:
                    count[1] += 1
            else:
                if not Flag.s3_3[i]:
                    count[2] += 1

        for i in range(3):
            if count[i] == 1:
                for j in range(i * 3, i * 3 + 3):
                    self.setRowHeight(j, 190)
                    if i == 2:
                        self.setRowHeight(j, 330)
            elif count[i] == 2:
                for j in range(i * 3, i * 3 + 3):
                    self.setRowHeight(j, 90)
                    if i == 2:
                        self.setRowHeight(j, 165)
            elif count[i] == 3:
                for j in range(i * 3, i * 3 + 3):
                    self.setRowHeight(j, 65)
                    if i == 2:
                        self.setRowHeight(j, 110)

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
    window = table_3_5()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
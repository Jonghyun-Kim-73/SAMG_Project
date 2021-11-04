import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Flag import Flag


class table_4_2(QWidget):
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
            QCheckBox {
                margin-left:0px;
                font-size:15px;
            }
            QCheckBox::indicator {
                width:  45px;
                height: 40px;
            }
            QTableWidget {
               gridline-color : black;
            }
            QCheckBox::indicator::unchecked {
                width:  45px;
                height: 40px;
                border : 0px solid black;
            }
            QCheckBox::indicator::checked {
                image : url(./check.png);
                height:30px;
                width:40px;
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
        super(table_4_2, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(self.qss)
        # self.setFixedHeight(800)
        # 기본 속성
        layout = QVBoxLayout(self)
        label = QTextEdit("6. 증기발생기 급수 주입 경로를 선정한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10, 20, 10, 20)
        label.setDisabled(True)
        label.setFixedHeight(40)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        layout.addWidget(label)
        self.layout_first = QHBoxLayout(self)
        self.layout_first2 = QVBoxLayout(self)
        self.s1 = []
        self.s1.append(QTextEdit('&nbsp;&nbsp;&nbsp;&nbsp;가. 급수 주입을 할 증기발생기는 다음 순서에 따라 선정한다.'))
        self.s1.append(QTextEdit('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1) 건전한 증기발생기(들)'))
        self.s1.append(QTextEdit('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2) 고장난 증기발생기(들)'))
        self.s1.append(QTextEdit('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3) 튜브가 파손된 증기발생기(들)'))

        for i in range(4):
            self.s1[i].setDisabled(True)
            self.s1[i].setFixedHeight(40)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        self.layout1 = []
        for i in range(4):
            self.layout1.append(QHBoxLayout())
            self.layout1[i].addWidget(self.s1[i])

            self.layout_first2.addLayout(self.layout1[i])
        self.layout_first.addLayout(self.layout_first2)
        a = ParaTable3(self)
        a.setMaximumWidth(80)
        self.layout_first.addWidget(a, 0, Qt.AlignRight)
        layout.addLayout(self.layout_first)
        layout.addWidget(ParaTable(self))

        self.s2 = []
        self.s2.append(QTextEdit('&nbsp;&nbsp;&nbsp;&nbsp;나. 선정된 계통의 배열을 확인한다.'))
        self.s2.append(QTextEdit('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1) 펌프'))
        self.s2.append(QTextEdit('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2) 펌프 전단 배열 상태'))
        self.s2.append(QTextEdit('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3) 펌프 후단 배열 상태'))

        for i in range(4):
            self.s2[i].setDisabled(True)
            self.s2[i].setFixedHeight(40)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        self.layout2 = []
        for i in range(4):
            self.layout2.append(QHBoxLayout())
            self.layout2[i].addWidget(self.s2[i])
            layout.addLayout(self.layout2[i])
        self.setLayout(layout)
        layout.addWidget(ParaTable2(self))
        layout.setSizeConstraint(QLayout.SetNoConstraint)
        self.setStyleSheet(self.qss)

class ParaTable(QTableWidget):
    def __init__(self, parent):
        super(ParaTable, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 테이블 프레임 모양 정의
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)
        self.setFixedHeight(200)
        self.setColumnCount(2)
        self.setRowCount(3)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 너비 조절
        self.setColumnWidth(0, 250)
        self.setColumnWidth(1, 586)
        for i in range(0, 4):
            self.setRowHeight(i, 40)

        self.setSpan(0, 0, 1, 2)

        self.setItem(0, 0, QTableWidgetItem("선정된 증기발생기"))
        self.setItem(1, 0, QTableWidgetItem("선정된 증기발생기 번호"))
        self.setItem(1, 1, QTableWidgetItem("선정된 증기발생기 상태"))

        self.text = []
        for i in range(2):
            self.text.append(QTextEdit(''))
        self.setCellWidget(2, 0, self.text[0])
        self.setCellWidget(2, 1, self.text[1])

        # timer section
        timer = QTimer(self)
        timer.setInterval(100)
        timer.timeout.connect(self.dis_update)
        timer.start()

        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegate(delegate)

        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)
        self.setFont(fnt)

    def dis_update(self):
        self.text[0].setPlainText(Flag.s4_2_1_backup)
        self.text[1].setPlainText(Flag.s4_2_2_backup)
        self.text[0].setStyleSheet("font-size:16px;")
        self.text[1].setStyleSheet("font-size:16px;")

class ParaTable2(QTableWidget):
    def __init__(self, parent):
        super(ParaTable2, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 테이블 프레임 모양 정의
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedHeight(200)
        self.setColumnCount(2)
        self.setRowCount(3)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 너비 조절
        self.setColumnWidth(0, 250)
        self.setColumnWidth(1, 586)
        for i in range(0, 3):
            self.setRowHeight(i, 40)
        self.setRowHeight(1, 80)
        self.setRowHeight(2, 50)
        self.setSpan(0, 0, 1, 2)

        self.setItem(0, 0, QTableWidgetItem("이용가능한 수단"))
        self.setItem(1, 0, QTableWidgetItem("급수펌프"))
        self.setItem(2, 0, QTableWidgetItem("급수 주입 경로"))

        self.text = []
        for i in range(2):
            self.text.append(QTextEdit(''))
        self.setCellWidget(1, 1, self.text[0])
        self.setCellWidget(2, 1, self.text[1])

        # timer section
        timer = QTimer(self)
        timer.setInterval(100)
        timer.timeout.connect(self.dis_update)
        timer.start()

        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegate(delegate)

        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)
        self.setFont(fnt)

    def dis_update(self):
        self.text[0].setPlainText(Flag.s2_1_1_backup)
        self.text[1].setPlainText(Flag.s2_1_3_backup)
        self.text[0].setStyleSheet("font-size:16px;")
        self.text[1].setStyleSheet("font-size:16px;")

class ParaTable3(QTableWidget):
    def __init__(self, parent):
        super(ParaTable3, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 테이블 프레임 모양 정의
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)
        self.setContentsMargins(0, 0, 0, 0)
        self.setColumnCount(2)
        self.setRowCount(4)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 너비 조절
        self.setColumnWidth(0, 39)
        self.setColumnWidth(1, 39)
        for i in range(0, 4):
            self.setRowHeight(i, 39)

        self.setItem(0, 0, QTableWidgetItem("SG1"))
        self.setItem(0, 1, QTableWidgetItem("SG2"))

        # # 체크박스
        count = 0
        self.checkbox = []
        for i in range(1, 4):
            for j in range(0, 2):
                self.checkbox.append(QCheckBox())
                self.setCellWidget(i, j, self.checkbox[count])
                count = count + 1

        for checkbox in self.checkbox:
            checkbox.stateChanged.connect(self.write_text)

        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegate(delegate)

        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(9)
        self.setFont(fnt)

    def write_text(self):
        check1 = [False] * 2 #SG1 / SG2
        check2 = [True] * 3
        for i in range(3):
            check1[0] += self.checkbox[i * 2].isChecked()
            check1[1] += self.checkbox[i * 2 + 1].isChecked()

        for i in range(2):
            if check1[i]:
                Flag.s4_2_1[i][1] = True
            else:
                Flag.s4_2_1[i][1] = False

        for i in range(2):
            if Flag.s4_2_1[i][1]:
                Flag.s4_2_1_final += Flag.s4_2_1[i][0]
                Flag.s4_2_1_final += ", "

        for i in range(3):
            check2[i] = self.checkbox[i * 2].isChecked() + self.checkbox[i * 2 + 1].isChecked()

        for i in range(3):
            if check2[i]:
                Flag.s4_2_2[i][1] = True
            else:
                Flag.s4_2_2[i][1] = False

        for i in range(3):
            if Flag.s4_2_2[i][1]:
                Flag.s4_2_2_final += Flag.s4_2_2[i][0]
                Flag.s4_2_2_final += ", "

        # 마지막 문자 제거
        Flag.s4_2_1_final = Flag.s4_2_1_final[:-2]
        Flag.s4_2_2_final = Flag.s4_2_2_final[:-2]

        # 마지막 데이터 다른 클래스에서 사용
        Flag.s4_2_1_backup = Flag.s4_2_1_final
        Flag.s4_2_2_backup = Flag.s4_2_2_final

        Flag.s4_2_1_final = ""
        Flag.s4_2_2_final = ""


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = table_4_2()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Flag import Flag


class tableNa_1(QWidget):
    qss = """
            QWidget {
                background: rgb(221, 221, 221);
                border : 0px solid black;
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
            QCheckBox {
                margin-left:0px;
                font-size:15px;
            }
            QCheckBox::indicator {
                width:  210px;
                height: 40px;
            }
            QCheckBox::indicator::unchecked {
                width:  210px;
                height: 40px;
                border : 0px solid;
            }
            QCheckBox::indicator::checked {
                image : url(./check.png);
                height:30px;
                width:210px;
            }
            QTableView {
                gridline-color : black;
            }
            QHeaderView::section {
                background: black;
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

        layout.addWidget(self.scrollTop)
        layout.addWidget(self.scrollBottom)


class TableHeader_Na_1(QTableWidget):
    def __init__(self, parent):
        super(TableHeader_Na_1, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)

        # 테이블 프레임 모양 정의
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)

        self.setColumnCount(4)
        self.setRowCount(2)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setRowHeight(0, 40)
        self.setRowHeight(1, 40)
        for i in range(0, self.columnCount()):
            self.setColumnWidth(i, 209)

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
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)
        self.setContentsMargins(0, 0, 0, 0)
        self.setColumnCount(4)
        self.setRowCount(17)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        for i in range(0, self.columnCount()):
            self.setColumnWidth(i, 209)
        for i in range(0, self.rowCount()):
            self.setRowHeight(i, 40)
        self.setRowHeight(14, 70)
        self.setRowHeight(15, 30)
        self.setRowHeight(16, 30)

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

        # 이용가능한 수단
        self.text = []
        for i in range(3):
            self.text.append(QTextEdit(''))

        self.setCellWidget(14, 2, self.text[0])
        self.setCellWidget(15, 2, self.text[1])
        self.setCellWidget(16, 2, self.text[2])

        # # 체크박스
        count = 0
        self.checkbox = []
        for i in range(1, self.columnCount()):
            for j in range(1, self.rowCount()):
                if self.item(j, i) or (j in [0, 4, 8, 10, 12, 13, 14, 15, 16]):
                    pass
                else:
                    self.checkbox.append(QCheckBox())
                    self.setCellWidget(j, i, self.checkbox[count])
                    count = count + 1

        # click together
        for checkbox in self.checkbox:
            if checkbox in [self.checkbox[3], self.checkbox[11], self.checkbox[19]]:
                checkbox.stateChanged.connect(self.onStateChange1)
                checkbox.stateChanged.connect(self.onStateChangePrincipal1)
            if checkbox in [self.checkbox[6], self.checkbox[14], self.checkbox[22]]:
                checkbox.stateChanged.connect(self.onStateChange2)
                checkbox.stateChanged.connect(self.onStateChangePrincipal2)
            if checkbox in [self.checkbox[7], self.checkbox[15], self.checkbox[23]]:
                checkbox.stateChanged.connect(self.onStateChange3)
                checkbox.stateChanged.connect(self.onStateChangePrincipal3)

        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegate(delegate)

        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)
        self.setFont(fnt)

        for checkbox in self.checkbox:
            checkbox.stateChanged.connect(self.write_text)

    def write_text(self):
        check1 = [True] * 3
        for j in range(3):
            for i in range(6):
                check1[j] *= self.checkbox[i + j * 8].isChecked()
        count1 = 1
        count2 = 1
        count3 = 1

        for i in range(3):
            if check1[i]:
                Flag.s2_2_1[i][1] = True
            else:
                Flag.s2_2_1[i][1] = False

        for i in range(3):
            if Flag.s2_2_1[i][1]:
                Flag.s2_2_1_final += "%d. " % count1
                Flag.s2_2_1_final += Flag.s2_2_1[i][0]
                Flag.s2_2_1_final += "\n"
                count1 += 1

        for i in range(1):
            if Flag.s2_2_2[i][1]:
                Flag.s2_2_2_final += "%d. " % count2
                Flag.s2_2_2_final += Flag.s2_2_2[i][0]
                Flag.s2_2_2_final += "\n"
                count2 += 1

        for i in range(1):
            if Flag.s2_2_3[i][1]:
                Flag.s2_2_3_final += "%d. " % count3
                Flag.s2_2_3_final += Flag.s2_2_3[i][0]
                Flag.s2_2_3_final += "\n"
                count3 += 1

        # 마지막 공백 제거
        Flag.s2_2_1_final = Flag.s2_2_1_final[:-1]
        Flag.s2_2_2_final = Flag.s2_2_2_final[:-1]
        Flag.s2_2_3_final = Flag.s2_2_3_final[:-1]

        # 마지막 데이터 다른 클래스에서 사용
        Flag.s2_2_1_backup = Flag.s2_2_1_final
        Flag.s2_2_2_backup = Flag.s2_2_2_final
        Flag.s2_2_3_backup = Flag.s2_2_3_final
        self.text[0].setPlainText(Flag.s2_2_1_final)
        self.text[1].setPlainText(Flag.s2_2_2_final)
        self.text[2].setPlainText(Flag.s2_2_3_final)
        Flag.s2_2_1_final = ""
        Flag.s2_2_2_final = ""
        Flag.s2_2_3_final = ""

    # 밀봉냉각
    @pyqtSlot(int)
    def onStateChangePrincipal1(self, state):
        if state == Qt.Checked:  # 체크
            for checkbox in [self.checkbox[3], self.checkbox[11], self.checkbox[19]]:
                checkbox.blockSignals(True)
                checkbox.setCheckState(state)
                checkbox.blockSignals(False)
    @pyqtSlot(int)
    def onStateChange1(self, state):
        for checkbox in [self.checkbox[3], self.checkbox[11], self.checkbox[19]]:
            checkbox.blockSignals(True)
            checkbox.setChecked(Qt.Unchecked)
            checkbox.blockSignals(False)

    # 탈기 저장 탱크
    @pyqtSlot(int)
    def onStateChangePrincipal2(self, state):
        if state == Qt.Checked:
            Flag.s2_2_2[0][1] = True
            for checkbox in [self.checkbox[6], self.checkbox[14], self.checkbox[22]]:
                checkbox.blockSignals(True)
                checkbox.setCheckState(state)
                checkbox.blockSignals(False)
    @pyqtSlot(int)
    def onStateChange2(self, state):
        Flag.s2_2_2[0][1] = False
        for checkbox in [self.checkbox[6], self.checkbox[14], self.checkbox[22]]:
            checkbox.blockSignals(True)
            checkbox.setChecked(Qt.Unchecked)
            checkbox.blockSignals(False)

    # 주급수 배관
    @pyqtSlot(int)
    def onStateChangePrincipal3(self, state):
        if state == Qt.Checked:
            Flag.s2_2_3[0][1] = True
            for checkbox in [self.checkbox[7], self.checkbox[15], self.checkbox[23]]:
                checkbox.blockSignals(True)
                checkbox.setCheckState(state)
                checkbox.blockSignals(False)
    @pyqtSlot(int)
    def onStateChange3(self, state):
        Flag.s2_2_3[0][1] = False
        for checkbox in [self.checkbox[7], self.checkbox[15], self.checkbox[23]]:
            checkbox.blockSignals(True)
            checkbox.setChecked(Qt.Unchecked)
            checkbox.blockSignals(False)

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = tableNa_1()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
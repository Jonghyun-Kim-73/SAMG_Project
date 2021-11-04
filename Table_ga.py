import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Flag import Flag

class tableGa(QWidget):
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
        """

    def __init__(self, parent=None):
        super(tableGa, self).__init__()
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
        table_header = TableHeader(self)
        para_table = ParaTable(self)
        self.scrollTop.setWidget(table_header)
        self.scrollBottom.setWidget(para_table)
        layout.addWidget(self.scrollTop)
        layout.addWidget(self.scrollBottom)


class TableHeader(QTableWidget):
    def __init__(self, parent):
        super(TableHeader, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 테이블 프레임 모양 정의
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)

        self.setColumnCount(9)
        self.setRowCount(2)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setRowHeight(0, 60)
        self.setRowHeight(1, 40)
        self.setColumnWidth(0, 124)
        for i in range(1, self.columnCount()):
            self.setColumnWidth(i, 89)
        # SPAN 생성
        self.setSpan(0, 0, 2, 1)
        self.setSpan(0, 1, 1, 2)
        self.setSpan(0, 3, 1, 2)
        self.setSpan(0, 5, 1, 2)
        self.setSpan(0, 7, 2, 1)
        self.setSpan(0, 8, 2, 1)

        # 테이블 헤더
        self.setItem(0, 1, QTableWidgetItem("터빈 구동\n보조급수 펌프"))
        self.setItem(0, 3, QTableWidgetItem("모터 구동\n보조급수 펌프"))
        self.setItem(0, 5, QTableWidgetItem("터빈 구동\n주급수 펌프"))
        self.setItem(0, 7, QTableWidgetItem("모터 구동\n주급수펌프"))
        self.setItem(0, 8, QTableWidgetItem("기동용\n급수 펌프"))

        self.setItem(1, 1, QTableWidgetItem("1A"))
        self.setItem(1, 2, QTableWidgetItem("1B"))
        self.setItem(1, 3, QTableWidgetItem("1A"))
        self.setItem(1, 4, QTableWidgetItem("1B"))
        self.setItem(1, 5, QTableWidgetItem("1A"))
        self.setItem(1, 6, QTableWidgetItem("1B"))

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
        self.setColumnCount(9)  # 현재 qt 버그로 span 설정시 table border 표시x
        self.setRowCount(21)

        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setColumnWidth(0, 124)
        for i in range(1, self.columnCount()):
            self.setColumnWidth(i, 89)
        for i in range(0, self.rowCount()):
            self.setRowHeight(i, 40)
        self.setRowHeight(3, 50)
        self.setRowHeight(10, 50)
        self.setRowHeight(18, 180)
        self.setRowHeight(19, 90)
        self.setRowHeight(20, 50)

        # SPAN 생성(타이틀)
        self.setSpan(0, 0, 1, 9)
        self.setSpan(4, 0, 1, 9)
        self.setSpan(8, 0, 1, 9)
        self.setSpan(13, 0, 1, 9)
        self.setSpan(16, 0, 1, 9)
        self.setSpan(17, 0, 1, 9)

        # SPAN 생성(이용 가능한 수단)
        self.setSpan(18, 0, 1, 2)
        self.setSpan(18, 2, 1, 7)
        self.setSpan(19, 0, 1, 2)
        self.setSpan(19, 2, 1, 7)
        self.setSpan(20, 0, 1, 2)
        self.setSpan(20, 2, 1, 7)

        # 행
        self.setItem(0, 0, QTableWidgetItem("급수펌프 이용가능성"))
        self.setItem(4, 0, QTableWidgetItem("펌프 작동 제한 조건"))
        self.setItem(8, 0, QTableWidgetItem("급수원"))
        self.setItem(13, 0, QTableWidgetItem("급수 주입 경로"))
        self.setItem(17, 0, QTableWidgetItem("이용 가능한 수단"))

        # 열
        self.setItem(1, 0, QTableWidgetItem("손상 상태"))
        self.setItem(2, 0, QTableWidgetItem("교류 전원"))
        self.setItem(3, 0, QTableWidgetItem("증기발생기\n압력"))

        self.setItem(5, 0, QTableWidgetItem("밀봉 냉각"))
        self.setItem(6, 0, QTableWidgetItem("전동기 냉각"))
        self.setItem(7, 0, QTableWidgetItem("윤활유 냉각"))

        self.setItem(9, 0, QTableWidgetItem("복수 저장 탱크"))
        self.setItem(10, 0, QTableWidgetItem("탈염수\n저장 탱크"))
        self.setItem(11, 0, QTableWidgetItem("원수 저장 탱크"))
        self.setItem(12, 0, QTableWidgetItem("탈기 저장 탱크"))

        self.setItem(14, 0, QTableWidgetItem("주급수 배관"))
        self.setItem(15, 0, QTableWidgetItem("보조급수 배관"))

        self.setItem(18, 0, QTableWidgetItem("급수펌프"))
        self.setItem(19, 0, QTableWidgetItem("급수원"))
        self.setItem(20, 0, QTableWidgetItem("급수 주입 경로"))

        self.text = []
        for i in range(3):
            self.text.append(QTextEdit(''))

        self.setCellWidget(18, 2, self.text[0])
        self.setCellWidget(19, 2, self.text[1])
        self.setCellWidget(20, 2, self.text[2])

        # N/A표시
        self.setItem(2, 1, QTableWidgetItem("N/A"))
        self.setItem(2, 2, QTableWidgetItem("N/A"))
        self.setItem(3, 3, QTableWidgetItem("N/A"))
        self.setItem(3, 4, QTableWidgetItem("N/A"))
        self.setItem(2, 5, QTableWidgetItem("N/A"))
        self.setItem(2, 6, QTableWidgetItem("N/A"))
        self.setItem(3, 7, QTableWidgetItem("N/A"))
        self.setItem(5, 3, QTableWidgetItem("N/A"))
        self.setItem(5, 4, QTableWidgetItem("N/A"))

        for i in range(1, self.columnCount()):
            self.setItem(6, i, QTableWidgetItem("N/A"))

        self.setItem(7, 3, QTableWidgetItem("N/A"))
        self.setItem(7, 4, QTableWidgetItem("N/A"))

        for i in range(5, self.columnCount()):
            for j in range(9, 12):
                self.setItem(j, i, QTableWidgetItem("N/A"))

        for i in range(1, 5):
            self.setItem(12, i, QTableWidgetItem("N/A"))

        for i in range(1, 5):
            self.setItem(14, i, QTableWidgetItem("N/A"))

        for i in range(5, 9):
            self.setItem(15, i, QTableWidgetItem("N/A"))

        # 체크박스
        count = 0
        self.checkbox = []
        for i in range(0, self.columnCount()):
            for j in range(1, 16):
                if self.item(j, i) or j == 4 or j == 8 or j == 13:
                    pass
                else:
                    self.checkbox.append(QCheckBox())
                    self.setCellWidget(j, i, self.checkbox[count])
                    count = count + 1

        # click together
        for checkbox in self.checkbox:
            if checkbox in [self.checkbox[4], self.checkbox[12], self.checkbox[18], self.checkbox[24]]:
                checkbox.stateChanged.connect(self.onStateChange1)
                checkbox.stateChanged.connect(self.onStateChangePrincipal1)
            if checkbox in [self.checkbox[5], self.checkbox[13], self.checkbox[19], self.checkbox[25]]:
                checkbox.stateChanged.connect(self.onStateChange2)
                checkbox.stateChanged.connect(self.onStateChangePrincipal2)
            if checkbox in [self.checkbox[6], self.checkbox[14], self.checkbox[20], self.checkbox[26]]:
                checkbox.stateChanged.connect(self.onStateChange3)
                checkbox.stateChanged.connect(self.onStateChangePrincipal3)
            if checkbox in [self.checkbox[32], self.checkbox[38], self.checkbox[44], self.checkbox[51]]:
                checkbox.stateChanged.connect(self.onStateChange4)
                checkbox.stateChanged.connect(self.onStateChangePrincipal4)
            if checkbox in [self.checkbox[33], self.checkbox[39], self.checkbox[45], self.checkbox[52]]:
                checkbox.stateChanged.connect(self.onStateChange5)
                checkbox.stateChanged.connect(self.onStateChangePrincipal5)
            if checkbox in [self.checkbox[7], self.checkbox[15], self.checkbox[21], self.checkbox[27]]:
                checkbox.stateChanged.connect(self.onStateChange6)
                checkbox.stateChanged.connect(self.onStateChangePrincipal6)

        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegate(delegate)

        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)
        self.item(17, 0).setFont(fnt)
        self.item(18, 0).setFont(fnt)
        self.item(19, 0).setFont(fnt)
        self.item(20, 0).setFont(fnt)

        for checkbox in self.checkbox:
            checkbox.stateChanged.connect(self.write_text)


    def write_text(self):
        check1 = [True] * 8
        for i in range(4):
            check1[0] *= self.checkbox[i].isChecked()
            check1[1] *= self.checkbox[i + 8].isChecked()
        check1[2] = self.checkbox[16].isChecked() * self.checkbox[17].isChecked()
        check1[3] = self.checkbox[22].isChecked() * self.checkbox[23].isChecked()
        for j in range(4, 7):
            for i in range(4):
                check1[j] *= self.checkbox[i + 16 + (j - 2) * 6].isChecked()
        for i in range(5):
            check1[7] *= self.checkbox[i + 46].isChecked()
        for i in range(8):
            if check1[i]:
                Flag.s2_1_1[i][1] = True
            else:
                Flag.s2_1_1[i][1] = False
        count1 = 1
        count2 = 1
        count3 = 1
        for i in range(8):
            if Flag.s2_1_1[i][1]:
                Flag.s2_1_1_final += "%d. " % count1
                Flag.s2_1_1_final += Flag.s2_1_1[i][0]
                Flag.s2_1_1_final += "\n"
                count1 += 1

        for i in range(4):
            if Flag.s2_1_2[i][1]:
                Flag.s2_1_2_final += "%d. " % count2
                Flag.s2_1_2_final += Flag.s2_1_2[i][0]
                Flag.s2_1_2_final += "\n"
                count2 += 1

        for i in range(2):
            if Flag.s2_1_3[i][1]:
                Flag.s2_1_3_final += "%d. " % count3
                Flag.s2_1_3_final += Flag.s2_1_3[i][0]
                Flag.s2_1_3_final += "\n"
                count3 += 1

        # 마지막 공백 제거
        Flag.s2_1_1_final = Flag.s2_1_1_final[:-1]
        Flag.s2_1_2_final = Flag.s2_1_2_final[:-1]
        Flag.s2_1_3_final = Flag.s2_1_3_final[:-1]

        # 마지막 데이터 다른 클래스에서 사용
        Flag.s2_1_1_backup = Flag.s2_1_1_final
        Flag.s2_1_2_backup = Flag.s2_1_2_final
        Flag.s2_1_3_backup = Flag.s2_1_3_final
        self.text[0].setPlainText(Flag.s2_1_1_final)
        self.text[1].setPlainText(Flag.s2_1_2_final)
        self.text[2].setPlainText(Flag.s2_1_3_final)
        Flag.s2_1_1_final = ""
        Flag.s2_1_2_final = ""
        Flag.s2_1_3_final = ""

    # 복수 저장 탱크
    @pyqtSlot(int)
    def onStateChangePrincipal1(self, state):
        if state == Qt.Checked:  # 체크
            Flag.s2_1_2[0][1] = True
            for checkbox in [self.checkbox[4], self.checkbox[12], self.checkbox[18], self.checkbox[24]]:
                checkbox.blockSignals(True)
                checkbox.setCheckState(state)
                checkbox.blockSignals(False)

    @pyqtSlot(int)
    def onStateChange1(self, state):
        Flag.s2_1_2[0][1] = False
        for checkbox in [self.checkbox[4], self.checkbox[12], self.checkbox[18], self.checkbox[24]]:
            checkbox.blockSignals(True)
            checkbox.setChecked(Qt.Unchecked)
            checkbox.blockSignals(False)

    # 탈염수 저장 탱크
    @pyqtSlot(int)
    def onStateChangePrincipal2(self, state):
        if state == Qt.Checked:
            Flag.s2_1_2[1][1] = True
            for checkbox in [self.checkbox[5], self.checkbox[13], self.checkbox[19], self.checkbox[25]]:
                checkbox.blockSignals(True)
                checkbox.setCheckState(state)
                checkbox.blockSignals(False)

    @pyqtSlot(int)
    def onStateChange2(self, state):
        Flag.s2_1_2[1][1] = False
        for checkbox in [self.checkbox[5], self.checkbox[13], self.checkbox[19], self.checkbox[25]]:
            checkbox.blockSignals(True)
            checkbox.setChecked(Qt.Unchecked)
            checkbox.blockSignals(False)

    # 원수 저장탱크
    @pyqtSlot(int)
    def onStateChangePrincipal3(self, state):
        if state == Qt.Checked:
            Flag.s2_1_2[2][1] = True
            for checkbox in [self.checkbox[6], self.checkbox[14], self.checkbox[20], self.checkbox[26]]:
                checkbox.blockSignals(True)
                checkbox.setCheckState(state)
                checkbox.blockSignals(False)

    @pyqtSlot(int)
    def onStateChange3(self, state):
        Flag.s2_1_2[2][1] = False
        for checkbox in [self.checkbox[6], self.checkbox[14], self.checkbox[20], self.checkbox[26]]:
            checkbox.blockSignals(True)
            checkbox.setChecked(Qt.Unchecked)
            checkbox.blockSignals(False)

    # 탈기 저장탱크
    @pyqtSlot(int)
    def onStateChangePrincipal4(self, state):
        if state == Qt.Checked:
            Flag.s2_1_2[3][1] = True
            for checkbox in [self.checkbox[32], self.checkbox[38], self.checkbox[44], self.checkbox[51]]:
                checkbox.blockSignals(True)
                checkbox.setCheckState(state)
                checkbox.blockSignals(False)

    @pyqtSlot(int)
    def onStateChange4(self, state):
        Flag.s2_1_2[3][1] = False
        for checkbox in [self.checkbox[32], self.checkbox[38], self.checkbox[44], self.checkbox[51]]:
            checkbox.blockSignals(True)
            checkbox.setChecked(Qt.Unchecked)
            checkbox.blockSignals(False)

    # 주급수 배관
    @pyqtSlot(int)
    def onStateChangePrincipal5(self, state):
        if state == Qt.Checked:
            Flag.s2_1_3[0][1] = True
            for checkbox in [self.checkbox[33], self.checkbox[39], self.checkbox[45], self.checkbox[52]]:
                checkbox.blockSignals(True)
                checkbox.setCheckState(state)
                checkbox.blockSignals(False)

    @pyqtSlot(int)
    def onStateChange5(self, state):
        Flag.s2_1_3[0][1] = False
        for checkbox in [self.checkbox[33], self.checkbox[39], self.checkbox[45], self.checkbox[52]]:
            checkbox.blockSignals(True)
            checkbox.setChecked(Qt.Unchecked)
            checkbox.blockSignals(False)

    # 보조급수 배관
    @pyqtSlot(int)
    def onStateChangePrincipal6(self, state):
        if state == Qt.Checked:
            Flag.s2_1_3[1][1] = True
            for checkbox in [self.checkbox[7], self.checkbox[15], self.checkbox[21], self.checkbox[27]]:
                checkbox.blockSignals(True)
                checkbox.setCheckState(state)
                checkbox.blockSignals(False)

    @pyqtSlot(int)
    def onStateChange6(self, state):
        Flag.s2_1_3[1][1] = False
        for checkbox in [self.checkbox[7], self.checkbox[15], self.checkbox[21], self.checkbox[27]]:
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
    window = tableGa()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()

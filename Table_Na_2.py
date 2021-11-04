import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Flag import Flag


class tableNa_2(QWidget):
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
            QTableWidget {
               gridline-color : black;
            }
            QCheckBox::indicator {
                width:  63px;
                height: 80px;
            }
            QCheckBox::indicator::unchecked {
                width:  63px;
                height: 80px;
                border : 0px solid;
            }
            QCheckBox::indicator::checked {
                image : url(./check.png);
                height:30px;
                width:63px;
            }
            QTableView {
                gridline-color : black;
            }
            QHeaderView::section {
                background: black;
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

        layout.addWidget(self.scrollTop)
        layout.addWidget(self.scrollBottom)


class TableHeader_Na_2(QTableWidget):
    def __init__(self, parent):
        super(TableHeader_Na_2, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)

        # 테이블 프레임 모양 정의
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)

        self.setColumnCount(13)
        self.setRowCount(2)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setRowHeight(0, 60)
        self.setRowHeight(1, 40)
        self.setColumnWidth(0, 80)
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
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)
        self.setContentsMargins(0, 0, 0, 0)
        self.setColumnCount(13)
        self.setRowCount(10)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setColumnWidth(0, 80)
        for i in range(1, self.columnCount()):
            self.setColumnWidth(i, 63)
        self.setRowHeight(1, 60)
        self.setRowHeight(4, 80)
        self.setRowHeight(9, 260)
        # SPAN 생성(타이틀)
        self.setSpan(0, 0, 1, 13)
        self.setSpan(5, 0, 1, 13)
        self.setSpan(7, 0, 1, 13)
        self.setSpan(8, 0, 1, 13)

        # SPAN 생성(이용 가능한 수단)
        self.setSpan(9, 0, 1, 3)
        self.setSpan(9, 3, 1, 13)

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
        self.setItem(3, 11, QTableWidgetItem("N/A"))
        self.setItem(3, 12, QTableWidgetItem("N/A"))
        self.setItem(4, 1, QTableWidgetItem("N/A"))
        self.setItem(4, 2, QTableWidgetItem("N/A"))
        self.setItem(4, 3, QTableWidgetItem("N/A"))
        self.setItem(4, 4, QTableWidgetItem("N/A"))
        self.setItem(6, 1, QTableWidgetItem("N/A"))
        self.setItem(6, 2, QTableWidgetItem("N/A"))
        self.setItem(6, 3, QTableWidgetItem("N/A"))
        self.setItem(6, 4, QTableWidgetItem("N/A"))
        self.setItem(6, 11, QTableWidgetItem("N/A"))
        self.setItem(6, 12, QTableWidgetItem("N/A"))

        # 이용가능한 수단
        self.text = []
        self.text.append(QTextEdit(''))
        self.setCellWidget(9, 3, self.text[0])

        # 체크박스
        count = 0
        self.checkbox = []
        for i in range(0, self.columnCount()):
            for j in range(0, self.rowCount()):
                if self.item(j, i) or (j in [0, 5, 7, 8, 9]):
                    pass
                else:
                    self.checkbox.append(QCheckBox())
                    self.setCellWidget(j, i, self.checkbox[count])
                    count = count + 1

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
        check1 = [True] * 12
        for i in range(0, 4):
            for j in range(3):
                check1[i] *= self.checkbox[i * 3 + j].isChecked()
        for i in range(4, 10):
            for j in range(5):
                check1[i] *= self.checkbox[(i - 4) * 5 + j + 12].isChecked()
        for i in range(10, 12):
            for j in range(3):
                check1[i] *= self.checkbox[(i - 10) * 3 + j + 42].isChecked()

        for i in range(12):
            if check1[i]:
                Flag.s2_3_1[i][1] = True
            else:
                Flag.s2_3_1[i][1] = False
        count1 = 1

        for i in range(12):
            if Flag.s2_3_1[i][1]:
                Flag.s2_3_1_final += "%d. " % count1
                Flag.s2_3_1_final += Flag.s2_3_1[i][0]
                Flag.s2_3_1_final += "\n"
                count1 += 1
        # 마지막 공백 제거
        Flag.s2_3_1_final = Flag.s2_3_1_final[:-1]

        # 마지막 데이터 다른 클래스에서 사용
        Flag.s2_3_1_backup = Flag.s2_3_1_final
        self.text[0].setPlainText(Flag.s2_3_1_final)
        Flag.s2_3_1_final = ""

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = tableNa_2()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
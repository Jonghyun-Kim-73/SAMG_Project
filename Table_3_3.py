import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Mitigation_button import Custom
from arrow import Arrow

StyleSheet = '''
QCheckBox {
    spacing: 5px;
    font-size:25px;
}

QCheckBox::indicator {
    width:  40px;
    height: 40px;
}
'''

class table_3_3(QWidget):
    qss = """
            QWidget {
                background: rgb(221, 221, 221);

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
        super(table_3_3, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.raise_()
        self.setStyleSheet(self.qss)
        self.setContentsMargins(0, 0, 0, 0)
        # 기본 속성
        layout = QVBoxLayout(self)
        label = QLabel("4.가. 발생가능한 부정적 영향을 파악하고 평가한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10,10,10,20)
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
        # layout.addWidget(label)
        layout.addWidget(label)
        layout.addWidget(self.scrollTop)
        layout.addWidget(self.scrollBottom)
        # layout.addWidget(para_table)


class TableHeader(QTableWidget):
    def __init__(self, parent):
        super(TableHeader, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)

        # 테이블 프레임 모양 정의
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)  # Row 넘버 숨기기
        self.setContentsMargins(0, 0, 0, 0)

        self.setColumnCount(4)
        self.setRowCount(1)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setRowHeight(0, 40)
        self.setColumnWidth(0, 120)
        self.setColumnWidth(1, 200)
        self.setColumnWidth(2, 478)
        self.setColumnWidth(3, 40)

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
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)  # Row 넘버 숨기기
        self.setContentsMargins(0, 0, 0, 0)
        # self.setStyleSheet(self.qss)
        self.setColumnCount(4)
        self.setRowCount(9)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setColumnWidth(0, 120)
        self.setColumnWidth(1, 200)
        self.setColumnWidth(2, 478)
        self.setColumnWidth(3, 40)
        for i in range(0, self.rowCount()):
            self.setRowHeight(i, 60)

        # SPAN 생성(부정적영향)
        self.setSpan(0, 0, 3, 1)
        self.setSpan(0, 1, 3, 1)
        self.setSpan(3, 0, 3, 1)
        self.setSpan(3, 1, 3, 1)
        self.setSpan(6, 0, 3, 1)
        self.setSpan(6, 1, 3, 1)

        self.setItem(0, 0, QTableWidgetItem("증기발생기 열충격"))
        self.setItem(3, 0, QTableWidgetItem("증기발생기 튜브 누설로 핵분열 생성물 방출"))
        self.setItem(6, 0, QTableWidgetItem("증기발생기 튜브 크립 파열"))

        self.setItem(0, 1, QTableWidgetItem("급수가 고갈된 고온의 S/G에 급수할 때S/G 광역수위가 [L02] 이하"))
        self.setItem(3, 1, QTableWidgetItem("튜브가 파손되거나 누출이 있는 S/G로 급수할 때"))
        self.setItem(6, 1, QTableWidgetItem("급수가 고갈된 고온의 S/G를 감압할 때 감압중인 S/G 광역수위가 [L02]이하 일 떄와 RCS 압력이 S/G 압력 이상일 때"))

        self.setItem(0, 2, QTableWidgetItem("급수 주입의 초기에는 주입량을 적게 제한함"))
        self.setItem(1, 2, QTableWidgetItem("S/G 튜브 파손의 영향이 최소화되는 시간에 S/G 광역수위가 최소로 지시될때까지 급수가 고갈된 단 1개의 S/G에 급수를 주입함"))
        self.setItem(2, 2, QTableWidgetItem("S/G 튜브 파손의 영향을 최소화하기 위해 격리가 가능한 S/G에만 급수를 주입함."))

        self.setItem(3, 2, QTableWidgetItem("건전한 S/G에만 급수하고 비등시킴"))
        self.setItem(4, 2, QTableWidgetItem("S/G 일차측에서 이차측으로 냉각재 누설을 최소화하기 위하여 RCS를 감압함 (완화-05, “원자로냉각재계통 감압“ 참조)"))
        self.setItem(5, 2, QTableWidgetItem("복수기로 증기를 배출하여 S/G를 감압함"))

        self.setItem(6, 2, QTableWidgetItem("S/G 튜브 파손의 영향이 최소화되는 시간에 급수가 고갈되고 고온인 S/G 1개만 감압함"))
        self.setItem(7, 2, QTableWidgetItem("S/G 압력이 급수원의 체결수두 이하일 때 가능한 빨리 급수 주입량을 복구함. S/G에 급수 주입 초기에는 주입략을 적게 제한함"))
        self.setItem(8, 2, QTableWidgetItem("RCS를 감압함 (완화-05, “원자로냉각재계통 감압“ 참조)"))

        # 체크박스
        for i in range(0, self.rowCount()):
            self.checkbox = QCheckBox(self)
            self.setCellWidget(i, 3, self.checkbox)

        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegate(delegate)

        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    app.setStyle("fusion")  # +++
    app.setStyleSheet(StyleSheet)
    window = table_3_3()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
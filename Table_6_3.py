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

class table_6_3(QWidget):
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
        super(table_6_3, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.raise_()
        self.setStyleSheet(self.qss)
        self.setContentsMargins(0, 0, 0, 0)
        # 기본 속성
        layout = QVBoxLayout(self)
        label = QLabel("12. 증기발생기 급수 주입으로 인한 장기관심사항을 확인한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10,10,10,20)

        label1 = QLabel("<p style=\"line-height:130%\">가. 장기 관심사항들은 첨부 E를 참조한다.<p>")
        label1.setStyleSheet("font-size: 14pt;font-weight: bold")
        label1.setContentsMargins(10, 10, 10, 20)

        self.setLayout(layout)
        self.scrollTop = QScrollArea()
        self.scrollTop.setFixedHeight(90)
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
        layout.addWidget(label1)
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
        self.setRowCount(2)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setRowHeight(0, 40)
        self.setRowHeight(1, 40)
        self.setColumnWidth(0, 120)
        self.setColumnWidth(1, 200)
        self.setColumnWidth(2, 478)
        self.setColumnWidth(3, 40)

        #span
        self.setSpan(0, 0, 1, 4)

        # 테이블 헤더
        self.setItem(0, 0, QTableWidgetItem("첨부 E, 증기발생기 급수 주입으로 인한 장기 관심사항"))
        self.setItem(1, 0, QTableWidgetItem("감시할 변수"))
        self.setItem(1, 1, QTableWidgetItem("관심사항"))
        self.setItem(1, 2, QTableWidgetItem("회복 조치"))
        self.setItem(1, 3, QTableWidgetItem("선택"))

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
        self.setRowCount(6)
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
            if i==3:
                self.setRowHeight(i, 80)

        # SPAN 생성(부정적영향)
        self.setSpan(0, 0, 3, 1)
        self.setSpan(0, 1, 3, 1)
        self.setSpan(4, 0, 2, 1)
        self.setSpan(4, 1, 2, 1)

        self.setItem(0, 0, QTableWidgetItem("흡입원 수위 - 적당함"))
        self.setItem(3, 0, QTableWidgetItem("증기발생기 수위 – [L01]과 50% 사이"))
        self.setItem(4, 0, QTableWidgetItem("증기발생기 압력 – 흡입원의 체결수두보다 낮음"))

        self.setItem(0, 1, QTableWidgetItem("증기발생기 급수 주입원 사용 불가능"))
        self.setItem(3, 1, QTableWidgetItem("증기발생기 급수 과주입"))
        self.setItem(4, 1, QTableWidgetItem("증기발생기 급수 주입 불가능"))

        self.setItem(0, 2, QTableWidgetItem("흡입원 보충"))
        self.setItem(1, 2, QTableWidgetItem("다른 급수 흡입원 찾음"))
        self.setItem(2, 2, QTableWidgetItem("펌프 공동현상(Cavitation)을 방지하기 위해 급수량을 조절함"))

        self.setItem(3, 2, QTableWidgetItem("증기발생기 협역수위를 [L01]과 50% 사이를 유지하기 위해 급수량을 조절함"))
        self.setItem(4, 2, QTableWidgetItem("추가 증기발생기 방출을 사용"))
        self.setItem(5, 2, QTableWidgetItem("추가 급수 흡입원을 사용"))

      # 체크박스
        for i in range(0, self.rowCount()):
            self.checkbox = QCheckBox(self)
            self.setCellWidget(i, 3, self.checkbox)

        # 테이블 정렬
        #delegate = AlignDelegate()
        #self.setItemDelegate(delegate)

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
    window = table_6_3()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
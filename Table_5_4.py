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

class table_5_4(QWidget):
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
        super(table_5_4, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.raise_()
        self.setStyleSheet(self.qss)
        self.setContentsMargins(0, 0, 0, 0)
        # 기본 속성
        layout = QVBoxLayout(self)
        label = QLabel("10. 추가적인 완화 조치들이 필요한 지를 결정한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10,10,10,20)

        label1 = QLabel("<p style=\"line-height:130%\">가. 실제로 발생한 부정적 영향을 파악한다.<p>"
                        "<p style=\"line-height:130%\">나. 실제로 발생한 부정적 영향을 완화할 수 있는 조치들을 평가한다.<p>"
                        "<p style=\"line-height:130%\">다. 부정적 영향을 완화할 수 있는 조치들이 있으면 수행하도록 주제어실에 지시한다.<p>")
        label1.setStyleSheet("font-size: 14pt;font-weight: bold")
        label1.setContentsMargins(10, 10, 10, 20)

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
        self.setItem(0, 1, QTableWidgetItem("탐지방법"))
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

        # SPAN 생성(부정적영향)
        self.setSpan(0, 0, 3, 1)
        self.setSpan(0, 1, 3, 1)
        self.setSpan(3, 0, 3, 1)
        self.setSpan(3, 1, 3, 1)

        self.setItem(0, 0, QTableWidgetItem("증기발생기 열충격"))
        self.setItem(3, 0, QTableWidgetItem("증기발생기 튜브 크립 파손"))

        self.setItem(0, 1, QTableWidgetItem("예기치 않은 증기발생기 압력 감소"))
        self.setItem(3, 1, QTableWidgetItem("2차측 방사선 계측기에서 핵분열 생성물의 큰 증가가 감지됨"))

        self.setItem(0, 2, QTableWidgetItem("건전한 증기발생기 사용이 가능하다면 고장난 증기발생기로의 급수 주입을 중단한다."))
        self.setItem(1, 2, QTableWidgetItem("다른 증기발생기로 급수를 주입한다.\n열응력을 최소화하기 위하여 급수 주입 초기에는 주입량을 적게 제한한다."))
        self.setItem(2, 2, QTableWidgetItem("고장난 증기발생기로 급수의 주입이 종결되었다면 고장난 증기발생기를 격리한다."))

        self.setItem(3, 2, QTableWidgetItem("모든 증기발생기의 튜브가 파손되었다면 튜브가 급수로 가득 찰 때까지 현재 급수를 주입하고 있는 증기발생기로 급수 주입량을 최대로 한다."))
        self.setItem(4, 2, QTableWidgetItem("다른 증기발생기에 급수를 주입을 시작한다.\n열응력을 최소화하기 위해서 급수 주입량을 적게 제한할 필요가 있다."))
        self.setItem(5, 2, QTableWidgetItem("튜브가 파열된 증기발생기를 격리한다."))

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
    window = table_5_4()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
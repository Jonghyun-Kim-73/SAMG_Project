import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Mitigation_button import Custom
from arrow import Arrow
StyleSheet = '''
QCheckBox {
    margin-left:24px;
    spacing: 5px;
    font-size:25px;
}

QCheckBox::indicator {
    width:  40px;
    height: 40px;
}
'''
class tableGa(QWidget):
    qss = """
            QWidget {
                background: rgb(221, 221, 221);

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
        """

    def __init__(self, parent=None):
        super(tableGa, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.raise_()
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
        # layout.addWidget(label)

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
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)  # Row 넘버 숨기기
        self.setContentsMargins(0, 0, 0, 0)
        # self.setStyleSheet(self.qss)
        self.setColumnCount(9)
        self.setRowCount(21)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setColumnWidth(0, 124)
        for i in range(1, self.columnCount()):
            self.setColumnWidth(i, 89)
        for i in range(1, self.rowCount()):
            self.setRowHeight(i, 40)
        self.setRowHeight(3, 50)
        self.setRowHeight(10, 50)
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

        for i in range(5, self.columnCount()):
            self.setItem(15, i, QTableWidgetItem("N/A"))

            # 체크박스
            for i in range(0, self.columnCount()):
                for j in range(1, 16):
                    if self.item(j, i) or j == 4 or j == 8 or j == 13:
                        pass
                    else:
                        self.checkbox = QCheckBox(self)
                        self.setCellWidget(j, i, self.checkbox)

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

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    app.setStyle("fusion")  # +++
    app.setStyleSheet(StyleSheet)
    window = tableGa()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
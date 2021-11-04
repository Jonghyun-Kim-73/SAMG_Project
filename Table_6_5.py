import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class table_6_5(QWidget):
    """ 중간 디스플레이 위젯 """
    qss = """
            QWidget {
                background: rgb(221, 221, 221);   
                border:0px solid;
            }
            QPushButton{
                background-color: rgb(221,221,221);
                border: 1px solid rgb(0,0,0);       
                font-size: 14pt;
                font-weight: bold
            }
            QTableView {
                gridline-color : black;
            }
            QHeaderView::section {
                background: black;
            }
            QTextEdit{
                font-size: 12pt;
                Color : black;
                border : 0px solid
            }
        """
    def __init__(self, parent=None):
        super(table_6_5, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(self.qss)
        self.setContentsMargins(0, 0, 0, 0)

        # 기본 속성
        layout = QVBoxLayout(self)
        label = QTextEdit("12. 증기발생기 급수 주입으로 인한 장기관심사항을 확인한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10, 10, 10, 20)
        label.setDisabled(True)
        label.setFixedHeight(40)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        label1 = QTextEdit("<p style=\"line-height:130%\">다. 추가적인 장기 관심사항을 파악한다.<p>")
        label1.setStyleSheet("font-size: 14pt;font-weight: bold")
        label1.setContentsMargins(10, 10, 10, 20)
        label1.setDisabled(True)
        label1.setFixedHeight(80)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        self.setLayout(layout)

        para_table = ParaTable(self)

        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(para_table)
        layout.addStretch()


class ParaTable(QTableWidget):
    def __init__(self, parent):
        super(ParaTable, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedHeight(300)
        self.setColumnCount(1)
        self.setRowCount(3)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 너비 조절
        self.setColumnWidth(0, 836)
        for i in range(0, 3):
            self.setRowHeight(i, 60)

        self.setItem(0, 0, QTableWidgetItem("추가적인 장기 관심사항(들)"))
        self.setCellWidget(1, 0, QTextEdit(""))
        self.setCellWidget(2, 0, QTextEdit(""))
        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegate(delegate)

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
    window = table_6_5()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class table_4_3(QWidget):
    qss = """
            QWidget {
                background: rgb(221, 221, 221);   
                border : 0px solid;
            }
            QPushButton {
                background-color: rgb(221, 221, 221);
                border: 1px solid rgb(0, 0, 0);       
                font-size: 14pt;
                font-weight: bold
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
                width:  80px;
                height: 80px;
            }
            QCheckBox::indicator::unchecked {
                width:  80px;
                height: 80px;
                border : 0px solid;
            }
            QCheckBox::indicator::checked {
                image : url(./check.png);
                height:30px;
                width:80px;
            }
            QTextEdit{
                font-size: 18pt;
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
        super(table_4_3, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 레이어 셋업
        layout = QVBoxLayout(self)

        label1 = QTextEdit("7. 증기발생기에 급수를 실시할 때의 제한사항들을 파악한다.")
        label1.setStyleSheet("font-size: 18pt;font-weight: bold")
        label1.setDisabled(True)
        label1.setContentsMargins(10, 10, 10, 20)
        label1.setFixedHeight(45)
        layout.addWidget(label1)
        layout.addWidget(ParaTable(self))
        self.setLayout(layout)

class ParaTable(QTableWidget):
    def __init__(self, parent):
        super(ParaTable, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        # 테이블 프레임 모양 정의
        self.horizontalHeader().setFixedHeight(1)
        self.verticalHeader().setFixedWidth(1)
        self.setColumnCount(3)
        self.setRowCount(8)

        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        self.setColumnWidth(0, 130)
        self.setColumnWidth(1, 626)
        self.setColumnWidth(2, 80)
        for i in range(1, self.rowCount()):
            self.setRowHeight(i, 40)
        self.setRowHeight(1, 60)
        self.setRowHeight(4, 60)
        self.setRowHeight(7, 60)
        # SPAN 생성(부정적영향)
        self.setSpan(0, 0, 1, 3)
        self.setSpan(2, 0, 2, 1)
        self.setSpan(5, 0, 2, 1)

        self.setItem(0, 0, QTableWidgetItem("급수 주입시 제한사항"))
        self.setItem(1, 0, QTableWidgetItem("변수"))
        self.setItem(1, 1, QTableWidgetItem("제한사항"))
        self.setItem(1, 2, QTableWidgetItem("예상되는\n제한사항"))

        self.setItem(2, 0, QTableWidgetItem("유량"))
        self.setItem(2, 1, QTableWidgetItem("열응력 (급수 주입의 초기에는 열응력 떄문에 주입량을 적게 제한함)"))
        self.setCellWidget(2, 2, QCheckBox(self))
        self.setItem(3, 1, QTableWidgetItem("흡입원의 재충수율"))
        self.setCellWidget(3, 2, QCheckBox(self))
        self.setItem(4, 0, QTableWidgetItem("급수가 고갈된\n증기발생기 수"))
        self.setItem(4, 1, QTableWidgetItem("증기발생기 1개 이상에 급수가 고갈되었을 때 증기발생기 광역 수위가\n지시할 때까지 하나의 증기발생기에만 급수를 시작"))
        self.setCellWidget(4, 2, QCheckBox(self))

        self.setItem(5, 0, QTableWidgetItem("급수 주입 기간"))
        self.setItem(5, 1, QTableWidgetItem("흡입원 재고량"))
        self.setCellWidget(5, 2, QCheckBox(self))
        self.setItem(6, 1, QTableWidgetItem("펌프 성능유지를 위한 조건"))
        self.setCellWidget(6, 2, QCheckBox(self))

        self.setItem(7, 0, QTableWidgetItem("증기발생기 감압"))
        self.setItem(7, 1, QTableWidgetItem("증기발생기가 완전히 감압되면 즉시 급수 주입을 시작"))
        self.setCellWidget(7, 2, QCheckBox(self))

        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegateForRow(0, delegate)
        self.setItemDelegateForRow(1, delegate)
        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)
        self.setFont(fnt)

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
    window = table_4_3()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
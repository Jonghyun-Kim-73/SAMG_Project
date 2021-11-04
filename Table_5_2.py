import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Flag import Flag


class table_5_2(QWidget):
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
        super(table_5_2, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(self.qss)
        self.setContentsMargins(0, 0, 0, 0)

        # 기본 속성
        layout = QVBoxLayout(self)
        label = QTextEdit("8. 증기발생기 급수 주입을 실시하도록 주제어실에 지시한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10, 10, 10, 20)
        label.setFixedHeight(45)
        label1 = QTextEdit("<p style=\"line-height:130%\">&nbsp;&nbsp;가. 주제어실에 다음과 같은 정보를 제공한다.<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;• 급수 주입시 제한 사항<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;• 특별히 감시해야 하는 변수들<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;• 기타 정보<p>")
        label1.setStyleSheet("font-size: 14pt;font-weight: bold")
        label1.setContentsMargins(10, 10, 10, 20)
        label1.setFixedHeight(180)
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
        self.setFixedHeight(600)
        self.setColumnCount(2)
        self.setRowCount(7)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 너비 조절
        self.setColumnWidth(0, 150)
        self.setColumnWidth(1, 686)
        for i in range(0, 7):
            self.setRowHeight(i, 40)
        self.setRowHeight(2, 150)
        self.setRowHeight(3, 50)
        self.setRowHeight(4, 150)

        self.setSpan(0, 0, 1, 3)

        self.setItem(0, 0, QTableWidgetItem("선정된 급수주입 기기(들)"))
        self.setItem(1, 0, QTableWidgetItem("선정된 증기발생기"))
        self.setItem(2, 0, QTableWidgetItem("고압급수주입펌프"))
        self.setItem(3, 0, QTableWidgetItem("고압급수주입유로"))
        self.setItem(4, 0, QTableWidgetItem("감압수단"))
        self.setItem(5, 0, QTableWidgetItem("저압급수주입경로"))
        self.setItem(6, 0, QTableWidgetItem("저압급수주입유로"))

        self.text = []
        for i in range(6):
            self.text.append(QTextEdit(''))

        self.setCellWidget(1, 1, self.text[0])
        self.setCellWidget(2, 1, self.text[1])
        self.setCellWidget(3, 1, self.text[2])
        self.setCellWidget(4, 1, self.text[3])
        self.setCellWidget(5, 1, self.text[4])
        self.setCellWidget(6, 1, self.text[5])

        # timer section
        timer = QTimer(self)
        timer.setInterval(100)
        timer.timeout.connect(self.dis_update)
        timer.start()

        # 테이블 정렬
        delegate = AlignDelegate()
        self.setItemDelegateForRow(0, delegate)
        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(12)
        self.setFont(fnt)

    def dis_update(self):
        self.text[0].setPlainText(Flag.s4_2_1_backup)
        self.text[1].setPlainText(Flag.s2_1_1_backup)
        self.text[2].setPlainText(Flag.s2_1_3_backup)
        self.text[3].setPlainText(Flag.s2_3_1_backup)
        self.text[4].setPlainText(Flag.s2_2_1_backup)
        self.text[5].setPlainText(Flag.s2_2_3_backup)

        for i in range(6):
            self.text[i].setStyleSheet("font-size:16px;")

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = table_5_2()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
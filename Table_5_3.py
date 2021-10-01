import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

StyleSheet = '''
QCheckBox {
    spacing: 5px;
    font-size:25px;
}

QCheckBox::indicator {
    width:  33px;
    height: 33px;
}


'''

class table_5_3(QWidget):
    """ 중간 디스플레이 위젯 """
    qss = """
            QWidget {
            background: rgb(221, 221, 221);   

        }

        QPushButton{
            background-color: rgb(221,221,221);
            border: 1px solid rgb(0,0,0);       
            font-size: 14pt;
            font-weight: bold
        }
        """

    def __init__(self, parent=None):
        super(table_5_3, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 크기 조정
        # self.setFixedHeight(550)

        # 레이어 셋업
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        self.setGeometry(100, 100, 700, 400)
        self.scroll = QScrollArea()
        # self.scroll.setFixedHeight(45)
        self.scroll.setWidgetResizable(True)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        label1 = ConditionArea()
        self.scroll.setWidget(label1)
        # layout.addWidget(label1)

        layout.addWidget(self.scroll)


class ConditionArea(QWidget):
    qss = """
             QWidget {
                background: rgb(221, 221, 221);
            }
            QLabel{
                font-size: 18pt;
                Color : black;
            }
 QTableWidget{
  border: 0px solid rgb(0,0,0);     
 }

        """

    def __init__(self):
        super(ConditionArea, self).__init__()
        # self.setGeometry(0, 0, int(1900/2), 2000)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(self.qss)
        self.setContentsMargins(0, 0, 0, 0)



        # 기본 속성
        layout = QVBoxLayout(self)
        label = QLabel("9. 주제어실에서 증기발생기 급수 주입을 성공적으로 실시하였는가를 확인한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10, 10, 10, 20)

        label1 = QLabel("<p style=\"line-height:130%\">가. 감시하여야 할 변수는 다음과 같다.<p>"
                        "<p style=\"line-height:130%\">• 증기발생기 수위<p>"
                        "<p style=\"line-height:130%\">• 증기발생기 압력p>")
        label1.setStyleSheet("font-size: 14pt;font-weight: bold")
        label1.setContentsMargins(10, 10, 10, 20)

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
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)  # Row 넘버 숨기기
        self.setContentsMargins(0, 0, 0, 0)
        self.setFixedHeight(200)
        self.setColumnCount(2)
        self.setRowCount(5)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 너비 조절
        self.setColumnWidth(0, 150)
        self.setColumnWidth(1, 680)
        for i in range(0, 5):
            self.setRowHeight(i, 40)

        self.setSpan(0, 0, 1, 2)

        self.setItem(0, 0, QTableWidgetItem("증기발생기 현재 값"))
        self.setItem(1, 0, QTableWidgetItem("증기발생기 1 수위"))
        self.setItem(2, 0, QTableWidgetItem("증기발생기 2 수위"))
        self.setItem(3, 0, QTableWidgetItem("증기발생기 1 압력"))
        self.setItem(4, 0, QTableWidgetItem("증기발생기 2 압력"))

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
    print('test')
    app = QApplication(sys.argv)
    app.setStyle("fusion")  # +++
    app.setStyleSheet(StyleSheet)
    window = table_5_3()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
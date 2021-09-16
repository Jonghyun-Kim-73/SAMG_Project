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

class table_3_6(QWidget):
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
        super(table_3_6, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 크기 조정
        # self.setFixedHeight(550)

        # 레이어 셋업
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        self.setGeometry(100, 100, 700, 400)

        label1 = ConditionArea()
        layout.addWidget(label1)

        self.setLayout(layout)


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
        label = QLabel("5. 증기발생기 급수 주입 실시 여부를 결정한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10, 10, 10, 20)

        label1 = QLabel("가. 증기발생기 급수 주입을 실시하지 않았을 때의 결과를 평가한다.")
        label1.setStyleSheet("font-size: 18pt;font-weight: bold")
        label1.setContentsMargins(10, 10, 10, 20)

        label2 = QLabel("<p style=\"line-height:130%\">나. 증기발생기 급수 주입을 실시하지 않았을 때 결과와 증기발생기 급수<p>"
                        "<p style=\"line-height:130%\">주입을 실시하였을 떄의 부정적 영향을 비교한다.<p>")
        label2.setStyleSheet("font-size: 18pt;font-weight: bold")
        label2.setContentsMargins(10, 10, 10, 20)

        label3 = QLabel("<p style=\"line-height:130%\">다. 증기발생기 급수 주입을 실시하지 않기로 결정되었다면 전략수행<p>"
                        "<p style=\"line-height:130%\">제어도 또는 이 전략 수행 직전에 주행중이든 전략으로 되돌아간다<p>.")
        label3.setStyleSheet("font-size: 18pt;font-weight: bold")
        label3.setContentsMargins(10, 10, 10, 20)
        self.setLayout(layout)

        para_table = ParaTable(self)

        # layout.addWidget(label)
        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addWidget(para_table)
        layout.addWidget(label2)
        layout.addWidget(label3)
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
        self.setRowCount(4)
        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 너비 조절
        self.setColumnWidth(0, 790)
        self.setColumnWidth(1, 38)
        for i in range(0, 4):
            self.setRowHeight(i, 40)

        self.setItem(0, 0, QTableWidgetItem("  증기발생기가 RCS의 열제거원 역할을 할 수 없음"))
        self.setItem(1, 0, QTableWidgetItem("  증기발생기 튜브의 건전성이 위협받을 수 있음"))
        self.setItem(2, 0, QTableWidgetItem("  RCS를 감압하는 데 증기발생기를 사용할 수 없음"))
        self.setItem(3, 0, QTableWidgetItem("  증기발생기 튜브 파손부로 부터 누출된 핵분열 생성물을 세정할 수 없음"))

        # 체크박스
        for i in range(0, self.rowCount()):
            self.checkbox = QCheckBox(self)
            self.setCellWidget(i, 1, self.checkbox)

        # 테이블 정렬
        # delegate = AlignDelegate()
        # self.setItemDelegate(delegate)

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
    window = table_3_6()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
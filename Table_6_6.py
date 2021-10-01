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

class table_6_6(QWidget):
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
        super(table_6_6, self).__init__()
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
        label = QLabel("12. 증기발생기 급수 주입으로 인한 장기관심사항을 확인한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10, 10, 10, 20)

        label1 = QLabel("<p style=\"line-height:130%\">라. 가능한 회복 조치를 평가한다.<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;1) 권고된 범위를 벗어난 변수들에 대한 가능성 회복조치를 파악한다.<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;2) 적절한 회복 조치를 선정한다.<p>")
        label1.setStyleSheet("font-size: 14pt;font-weight: bold")
        label1.setContentsMargins(10, 10, 10, 20)

        self.setLayout(layout)

        layout.addWidget(label)
        layout.addWidget(label1)
        layout.addStretch()


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    app.setStyle("fusion")  # +++
    app.setStyleSheet(StyleSheet)
    window = table_6_6()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
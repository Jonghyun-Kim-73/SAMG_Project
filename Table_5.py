import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class table5(QWidget):
    """ 중간 디스플레이 위젯 """
    qss = """
            QWidget {
                background: rgb(221, 221, 221);   
            }
            QTextEdit{
                font-size: 18pt;
                Color : black;
                border : 0px solid;
            }
            QPushButton{
                background-color: rgb(221,221,221);
                border: 1px solid rgb(0,0,0);       
                font-size: 14pt;
                font-weight: bold
            }
            QCheckBox {
                margin-top:0px;
                font-size:15px;
            }
            QCheckBox::indicator {
                width:  40px;
                height: 40px;
            }
            QCheckBox::indicator::unchecked {
                width:  40px;
                height: 40px;
                border : 1px solid;
            }
            QCheckBox::indicator::checked {
                image : url(./check.png);
                height:40px;
                width:40px;
            }        
        """

    def __init__(self, parent=None):
        super(table5, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 레이어 셋업
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        self.setMinimumHeight(800)

        label1 = ConditionArea(self)
        layout.addWidget(label1)

        self.setLayout(layout)


class ConditionArea(QWidget):
     def __init__(self, parent):
        super(ConditionArea, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setGeometry(0, 0, 850, 400)  # 1900*(3/4) = 1425
        layout = QVBoxLayout(self)
        # para 1
        self.label1 = QTextEdit('1. 다. 증기발생기에 급수를 주입할 수단이 전혀 없으면 다음을 수행한다.')
        self.label1.setStyleSheet("font-weight: bold;")
        self.label1.setDisabled(True)
        self.label1.setFixedHeight(50)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)
        layout.addWidget(self.label1)

        self.s1 = []
        self.checkbox = []
        self.s1.append(QTextEdit('1) 증기발생기에 급수를 주입할 수 없는 원인을 밝힌다.'))
        self.s1.append(QTextEdit('2) 증기발생기에 급수를 주입할 수 있는 수단을 복구할 수 있는 조치들의 우선순위를 정하고, 적절한 복구조치를 시작하도록 주제어실에 지시한다.'))
        self.s1.append(QTextEdit('3) 전략수행 제어도 또는 이 전략 수행 직전에 수행중이던 전략으로 되돌아간다.'))

        for i in range(3):
            self.s1[i].setDisabled(True)
        self.s1[0].setFixedHeight(50)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)
        self.s1[1].setFixedHeight(105)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)
        self.s1[2].setFixedHeight(75)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        self.layout1 = []
        for i in range(3):
            self.layout1.append(QHBoxLayout())
            self.layout1[i].setContentsMargins(20, 5, 0, 25)
            self.layout1[i].addWidget(self.s1[i])
            self.layout1[i].addWidget(QCheckBox(self))
            layout.addLayout(self.layout1[i])
        self.layout1[1].setContentsMargins(20, 5, 0, 30)
        layout.addStretch(1)
        layout.setSizeConstraint(QLayout.SetMinimumSize)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = table5()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
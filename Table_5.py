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

class table5(QWidget):
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
        super(table5, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 크기 조정
        self.setFixedHeight(550)

        # 레이어 셋업
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        self.setGeometry(100, 100, 600, 400)

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
 

        """

    def __init__(self):
        super(ConditionArea, self).__init__()
        # self.setGeometry(0, 0, int(1900/2), 2000)
        self.setStyleSheet(self.qss)


        self.check1 = QCheckBox(self)
        self.check2 = QCheckBox(self)
        self.check3 = QCheckBox(self)
        self.check1.move(30,30)
        self.purpose1 = QLabel("<p style=\"line-height:130%\">&nbsp;&nbsp;1. 다. 증기발생기에 급수를 주입할 수단이 전혀 없으면 다음을 수행한다.<p>")
        # purpose.setMinimumHeight(30)
        self.purpose1.setStyleSheet("font-weight: bold;")
        self.purpose2 = QLabel("<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1) 증기발생기에 급수를 주입할 수 없는 원인을 밝힌다.<p>")
        self.purpose3 = QLabel("<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2) 증기발생기에 급수를 주입할 수 있는 수단을 복구할 수 있는<p>"
                          "<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;조치들의 우선순위를 정하고, 적절한 복구조치를 시작하도록<p>"
                          "<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;주제어실에 지시한다.<p>")
        self.purpose4 = QLabel("<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3) 전략수행 제어도 또는 이 전략 수행 직전에 수행중이던 전략으로<p>"
                          "<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;되돌아간다.<p>")

        # purpose1 = QLabel("  1. 다. 증기발생기에 급수를 주입할 수단이 전혀 없으면 다음을 수행한다.")
        # purpose1.setStyleSheet("font-weight: bold;")
        #
        # purpose2 = QLabel("     1) 증기발생기에 급수를 주입할 수 없는 원인을 밝힌다.")
        #
        # purpose3 = QLabel("     2) 증기발생기에 급수를 주입할 수 있는 수단을 복구할 수 있는")
        # purpose3_1 = QLabel("        조치들의 우선순위를 정하고, 적절한 복구조치를 시작하도록")
        # purpose3_2 = QLabel("        주제어실에 지시한다.")
        #
        # purpose4 = QLabel("     3) 전략수행 제어도 또는 이 전략 수행 직전에 수행중이던 전략으로")
        # purpose4_1 = QLabel("        되돌아간다.")



        # 레이어 셋업

        self.layout_m = QVBoxLayout(self)
        self.layout_c = QHBoxLayout(self)

        self.layoutl = QVBoxLayout(self)
        self.layoutr = QVBoxLayout(self)
        self.layoutr.setContentsMargins(10,0,0,0)
        self.layout_m.addWidget(self.purpose1)

        self.layoutl.addWidget(self.purpose2)
        self.layoutl.addWidget(self.purpose3)
        self.layoutl.addWidget(self.purpose4)

        self.layoutr.addWidget(self.check1)
        self.layoutr.addStretch(1)
        self.layoutr.addWidget(self.check2)
        self.layoutr.addStretch(1)
        self.layoutr.addWidget(self.check3)
        self.layoutr.addStretch(1)

        self.layout_c.addLayout(self.layoutl)
        self.layout_c.addLayout(self.layoutr)
        self.layout_m.addLayout(self.layout_c)

        # layout.setSizeConstraint(QLayout.SetMinimumSize)
        self.setLayout(self.layout_m)


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    app.setStyle("fusion")  # +++
    app.setStyleSheet(StyleSheet)
    window = table5()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
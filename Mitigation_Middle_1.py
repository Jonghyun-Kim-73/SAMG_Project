import os
import sys
import pandas as pd
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
#from PyQt5.QtChart import *

# from button2 import custom_button




class MitigationMiddleArea_1(QWidget):
    """ 중간 디스플레이 위젯 """
    qss = """
            QWidget {
                background: rgb(128, 128, 128);
            }
            QTableWidget {
                background: rgb(221, 221, 221);
            }
        """

    def __init__(self, parent=None):
        super(MitigationMiddleArea_1, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 크기 조정
        # self.setMinimumHeight(860)
        # self.setMinimumWidth(int(1900/2))

        # 레이어 셋업
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        label1 = M_MiddleArea()

        layout.addWidget(label1)

        self.setLayout(layout)


class M_MiddleArea(QWidget):
    qss = """
            QWidget {
                background: rgb(221, 221, 221);
                border: 0px solid rgb(0, 0, 0); 
            }
        """

    def __init__(self):
        super(M_MiddleArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(self.qss)

        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)

        condition = ConditionArea()

        scroll.setWidget(condition)

        layout = QVBoxLayout()
        layout.addWidget(scroll)
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
        # self.setGeometry(0, 0, 1920, 1080)
        # QString
        # template = "<p style=\"line-height:%1%\">%2<p>";
        # QString
        # targetText = template.arg(myPercentage).arg(myTex);
        # QLabel * l = new
        # QLabel(targetText, this);
        # < p style = ' line-height:150% ' >
        # & ensp , emsp;
        self.label1 = QLabel('<u>목적</u>\n')
        self.label1_1 = QLabel('<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;증기발생기 급수 주입의 목적은 다음과 같다.\n<p>'
                               '<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• RCS 열 제거\n<p>'
                               '<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• RCS를 감압하여 RCS 내로 냉각재 공급을 가능하게 함\n'
                               '<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• 증기발생기 튜브의 크립 파열 방지\n<p>'
                               '<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• 증기발생기로 생성된 핵분열 생성물의 세정\n<p>'
                               '<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• 증기발생기 튜브 파손시 파손부를 통하여 RCS 내에 냉각재 공급\n<p>'
                               )
        self.label1.setStyleSheet("font-weight: bold;")
        self.label2 = QLabel('<u>수행 조건</u>\n')
        self.label2_1 = QLabel('<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• 증기발생기 수위가 튜브 최상부 이하일 때\n<p>'
                               '<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• 증기발생기 튜브 파손시 RCS 압력이 증기발생기 압력보다 낮을 떄\n<p>'
                               )
        self.label2.setStyleSheet("font-weight: bold;")

        self.label3 = QLabel('<u>종결 조건</u>\n')
        self.label3_1 = QLabel('<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• 증기발생기 튜브가 과도하게 가열되어 열충격 발생으로 파손이 예상될 때\n<p>'
                               '<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• 증기발생기 튜브 파손시 급수 주입이 증기발생기를 감압하여 RCS 냉각재가 파손부를 통하여 누설이 증가할 때\n<p>'
                               '<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• 증기발생기 수위가 복구 되었을 때\n<p>')
        self.label3.setStyleSheet("font-weight: bold;")

        self.label4 = QLabel('<u>예상 발전소 거동</u>\n')
        self.label4_1 = QLabel('<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• 증기발생기 수위 상승\n<p>'
                               '<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• 증기발생기 증기 유량 증가\n<p>'
                               '<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• 노심 출구와 고온관의 온도 감소\n<p>'
                               '<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• U 튜브 상부에 수소 축적\n<p>')
        self.label4.setStyleSheet("font-weight: bold;")

        self.label5 = QLabel('<u>비상운전절차와의 관계</u>\n')
        self.label5_1 = QLabel('<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• 상충성\n<p>'
                               '<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;비상운전절차서에는 급수가 있는 증기발생기가 있을 경우에 급수가 없는 증기발생기에는 급수를 주입하지 않고 있으나, 사고관리지침서에서는 증기발생기'
                               '<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;U 튜브의 크립 파열을 방지하기 위하여 급수가 없는 증기발생기에도 급수 주입을 고려한다.\n<p>'
                               '<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• 일치성\n<p>'
                               '<p style=\"line-height:130%\">&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;이전략은 기능회복지침 회복-06, “노심 및 원자로냉각재계통 열제거＂와 일치한다. 증기발생기의 급속한 감압으로 발생할 수 있는 증기발생기에서의'
                               '<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;불필요한 열응력 증가를 피하기 위하여 세심한 주의가 필요하며 정상적인 증기발생기 운전 절차는 이 지침에 적용될 수 있다.\n<p>')
        self.label5.setStyleSheet("font-weight: bold;")

        self.label6 = QLabel('<u>계산 보조 도구</u>\n')
        self.label6_1 = QLabel('        • 계산표-05, “장기 붕괴열 제거를 위한 냉각재 주입율＂\n')
        self.label6.setStyleSheet("font-weight: bold;")

        # 레이어 셋업
        layout = QVBoxLayout(self)

        layout.addWidget(self.label1)
        layout.addWidget(self.label1_1)

        layout.addWidget(self.label2)
        layout.addWidget(self.label2_1)

        layout.addWidget(self.label3)
        layout.addWidget(self.label3_1)

        layout.addWidget(self.label4)
        layout.addWidget(self.label4_1)

        layout.addWidget(self.label5)
        layout.addWidget(self.label5_1)

        layout.addWidget(self.label6)
        layout.addWidget(self.label6_1)

        layout.setSizeConstraint(QLayout.SetMinimumSize)

        self.setLayout(layout)

        self.setStyleSheet(self.qss)

if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MitigationMiddleArea_1()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()


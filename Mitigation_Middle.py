import os
import sys
import pandas as pd
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *

from button import custom_button

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class MitigationMiddleArea(QWidget):
    """ 중간 디스플레이 위젯 """
    qss = """
            QWidget {
                background: rgb(10, 10, 10);
            }
            QLabel {
                background: rgb(131, 131, 131);
                border-radius: 6px;
                color: rgb(255, 255, 255);
            }
            QTableWidget {
                background: rgb(131, 131, 131)
            }
        """

    def __init__(self, parent=None):
        super(MitigationMiddleArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 크기 조정
        self.setMinimumHeight(860)
        self.setMinimumWidth(int(1900/2))

        # 레이어 셋업
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        label1 = M_MiddleArea()

        layout.addWidget(label1)

        self.setLayout(layout)


class M_MiddleArea(QWidget):
    qss = """
            QWidget {
                background: rgb(255, 255, 255);
                border-radius: 6px;
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
                background: rgb(20, 39, 42);
                border-radius: 6px;
            }
        """

    def __init__(self):
        super(ConditionArea, self).__init__()
        self.setGeometry(0, 0, int(1900/2), 2000)
        self.setStyleSheet(self.qss)

        self.btn_dot_1 = custom_button(self, x=0, y=0, w=20, h=20, text='●', type=2)
        self.btn_purpose = custom_button(self, x=30, y=30, w=300, h=60, text='목적', type=1)

        self.btn_purpose_1 = custom_button(self, x=60, y=110, w=700, h=60, text='Reactor Coolant System (RCS) 열 제거', type=1)
        self.btn_purpose_2 = custom_button(self, x=60, y=190, w=700, h=60, text='RCS를 감압하여 RCS 내로 냉각재 공급을 가능하게 함', type=1)
        self.btn_purpose_3 = custom_button(self, x=60, y=270, w=700, h=60, text='증기발생기 튜브의 크립 파손 방지', type=1)
        self.btn_purpose_4 = custom_button(self, x=60, y=360, w=700, h=60, text='증기발생기로 방출된 핵분열생성물의 세정(Scrubbing)', type=1)
        self.btn_purpose_5 = custom_button(self, x=60, y=440, w=700, h=60, text='증기발생기 튜브 파손시 파손부를 통하여 RCS 내에 냉각재 공급', type=1)



if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MitigationMiddleArea()
    window.show()
    app.exec_()


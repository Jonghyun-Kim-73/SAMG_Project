import os
import sys

import PyQt5.QtWidgets
import pandas as pd
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from test_button import custom_button

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class MainLeftArea(QWidget):
    """ 왼쪽 디스플레이 위젯 """
    qss = """
        QWidget {
            background: rgb(0, 0, 0);    
        }
        QPushButton {
            background: rgb(62, 74, 84);
            border-radius: 3px;
            border: 2px inset rgb(62, 74, 84);
            font: bold 12px;
            color: rgb(255, 255, 255);          
        }
    """

    def __init__(self, parent=None):
        super(MainLeftArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)  # 상위 스타일 상속
        self.parent = parent
        self.setStyleSheet(self.qss)

        self.setMinimumHeight(1000 - 40)
        self.setMinimumWidth(int(1900*(3/4)))
        # self.setMinimumHeight(self.parent.height() - 40)
        # self.setMinimumWidth(int(self.parent.width() * (2/3))

        # 레이어 셋업
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        label1 = FlowChartArea(self)

        layout.addWidget(label1)
        self.setLayout(layout)


class FlowChartArea(QWidget):
    qss = """
            QWidget {
                background: rgb(131, 131, 131);
                border-radius: 6px;
            }
        """

    def __init__(self, parent=None):
        super(FlowChartArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        flowchart = FlowChart(self)

        scroll.setWidget(flowchart)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)


class FlowChart(QWidget):
    qss = """
               QWidget {
                   background: rgb(20, 39, 42);
                   border-radius: 6px;
               }
           """

    def __init__(self, parent=None):
        super(FlowChart, self).__init__()
        self.setGeometry(0, 0, 2000, 2000)  # 1900*(3/4) = 1425
        self.setStyleSheet(self.qss)
        self.parent = parent

        # 커스텀버튼 3 dia 2 cir 1 rec
        self.btn_8 = custom_button(self, x=1040, y=390, w=300, h=60, text='완화-01\n"증기발생기 급수 주입" 수행', type=1)
        self.btn_7 = custom_button(self, x=710, y=390, w=300, h=60, text='모든 SG 수위 > 68% NR', type=3,
                                   msg_text="모든 SG 수위 > 68% NR", connected_btn=self.btn_8)

        self.btn_6 = custom_button(self, x=380, y=300, w=300, h=100, text='RCS 대형 개구부\n(PZR MW 개방 또는\nRV head 제거)',
                                   type=3, msg_text="RCS 대형 개구부", connected_btn=self.btn_7)

        self.btn_4 = custom_button(self, x=380, y=210, w=300, h=60, text='발전소 안전변수\n감시 시작', type=2,
                                   msg_text="발전소 안전변수 감시를 시작합니다.", connected_btn=self.btn_6)
        self.btn_5 = custom_button(self, x=1240, y=210, w=300, h=60, text='원자로건물 중대위협 변수\n감시 시작', type=2)

        self.btn_3 = custom_button(self, x=1240, y=120, w=300, h=60, text='"비상전원 공급절차" 수행\n(확인표-1. 계속 확인 단계', type=1)

        self.btn_2 = custom_button(self, x=810, y=120, w=300, h=60, text='전력공급', type=3,
                                   msg_text="전원 공급이 가능합니까?", connected_btn=self.btn_4, connected_btn_2=self.btn_3,
                                   connected_btn_3=self.btn_5)

        self.btn_1 = custom_button(self, x=810, y=30, w=300, h=60, text='TSC "전략수행도" 사용 시작',
                                   msg_text='TSC "전략수행도"를 시작합니다.', type=2, connected_btn=self.btn_2)


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MainLeftArea()
    window.show()
    app.exec_()
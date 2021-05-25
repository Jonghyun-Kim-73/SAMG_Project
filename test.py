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

        # 레이어 셋업 ====================================================================================================
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

        # 커스텀버튼추가===================================================================================================
        # 3 dia 2 cir 1 rec
        self.btn_1 = custom_button(self, x=810, y=30, w=300, h=60, text='TSC "전략수행도" 사용 시작', type=2)
        # self.btn_1.color = Qt.black


        self.btn_2 = custom_button(self, x=810, y=120, w=300, h=60, text='전력공급', type=3, connected_btn=self.btn_1)
        self.btn_3 = custom_button(self, x=1240, y=120, w=300, h=60, text='"비상전원 공급절차" 수행\n(확인표-1. 계속 확인 단계', type=1)



        self.btn_1.clicked.connect(self.btn_1_clicked)



    def btn_1_clicked(self, state):
        # self.btn_1.setStyleSheet('QPushButton {background-color: yellow; color: blue}')

        # self.btn_1.setStyleSheet("color: red;"
        #                          "border-style: solid;"
        #                          "border-width: 2px;"
        #                          "border-color: #FA8072;"
        #                          "border-radius: 3px")

        print(state)
        if state == True:
            self.btn_1.setStyleSheet("color: red;"              # self.btn_1에 접근을 못하거나, setStyleSheet이 작동안함..
                                     "border-style: solid;"
                                     "border-width: 2px;"
                                     "border-color: yellow;"
                                     "border-radius: 3px")
            print('bb')


        QMessageBox.about(self, "message", "clicked")



if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MainLeftArea()
    window.show()
    app.exec_()
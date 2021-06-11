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
                background: rgb(0, 0, 0);
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
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        condition = ConditionArea()

        scroll.setWidget(condition)

        layout = QVBoxLayout()
        layout.addWidget(scroll)
        self.setLayout(layout)


class ConditionArea(QWidget):
    qss = """
            QWidget {
                background: rgb(255, 255, 255);
                border-radius: 6px;
            }
        """

    def __init__(self):
        super(ConditionArea, self).__init__()
        self.setGeometry(0, 0, int(1900/2), 2000)
        self.setStyleSheet(self.qss)

        # self.purpose = QLabel('우뿌뿌')

        purpose = QLabel('● 목적\n'
                         '     - Reactor Coolant System (RCS) 열 제거\n'
                         '     - RCS를 감압하여 RCS 내로 냉각재 공급을 가능하게 함\n'
                         '     - 증기발생기 튜브의 크립 파손 방지\n'
                         '     - 증기발생기로 방출된 핵분열생성물의 세정(Scrubbing)\n'
                         '     - 증기발생기 튜브 파손시 파손부를 통하여 RCS 내에 냉각재 공급\n'
                         '\n'
                         '\n'
                         '● 수행 조건\n'
                         '     - 발전소 상태가 A 또는 B이고 어느 하나라도 증기발생기 수위가 협역수위 지시기로 68% 이하일 때\n'
                         '     - 발전소 상태가 C이고 핵분열생성물의 방출이 있는 증기발생기 수위가 협역수위 지시기로68% 이하일 때'
                         '\n'
                         '\n'
                         '\n'
                         '● 예상 발전소 거동\n'
                         '     - 증기발생기 수위 상승\n'
                         '     - 증기발생기 증기 유량 증가\n'
                         '     - 노심 출구와 고온관의 온도 감소\n'
                         '     - 증기발생기 튜브 상부에 수소 축적\n'
                         '\n'
                         '\n'
                         '● 비상운전절차서와의 관계\n'
                         '     - 상충성: 비상운전절차서에는 급수가 있는 증기발생기가 있을 경우에 급수가 없는 증기발생기에는\n'
                         '       급수를 주입하지 않고 있으나,중대사고관리지침서에서는 증기발생기 튜브의 크립 파손을 방지하기 위하여\n'
                         '       급수가 없는 증기발생기에도 급수 주입을 고려한다.\n'
                         '     - 일치성: 이 전략은 기능회복절차서 회복-06, “노심 및 RCS 열 제거”와 일치한다.\n'
                         '       증기발생기의 급속한 감압으로 발생할 수 있는 증기발생기에서의 불필요한 열응력 증가를 피하기 위하여\n'
                         '       세심한 주의가 필요하며 정상적인 증기발생기 운전 절차도 이 지침에 적용될 수 있다.'
                         '\n'
                         '\n'
                         '● 계산보조도구\n'
                         '     - 계산표-01, 장기 붕괴열 제거를 위한 냉각수 주입률'
                         )
        purpose.setMinimumHeight(30)
        purpose.setStyleSheet("Color : black; font-size: 14pt; font-weight: bold")

        condition = QLabel('\n')
        condition.setFixedHeight(1300)
        condition.setStyleSheet("Color : black; font-size: 14pt; font-weight: bold")

        # 레이어 셋업
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        layout.addWidget(purpose)
        layout.addWidget(condition)

        self.setLayout(layout)


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MitigationMiddleArea()
    window.show()
    app.exec_()


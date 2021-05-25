import os
import sys

import PyQt5.QtWidgets
import pandas as pd
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from button import custom_button

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
    # background: rgb(14, 22, 24);

    def __init__(self, parent=None):
        super(MainLeftArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)  # 상위 스타일 상속
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 크기 조정
        # self.setFixedHeight(1000)
        # self.setFixedWidth(500)

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
        # scroll.setWidgetResizable(True)

        flowchart = FlowChart()

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

        # 커스텀버튼추가===================================================================================================
        # 3 dia 2 cir 1 rec
        self.btn_1 = custom_button(self, x=810, y=30, w=300, h=60, text='TSC "전략수행도" 사용 시작', type=2)

        self.btn_2 = custom_button(self, x=810, y=120, w=300, h=60, text='전력공급', type=3)
        self.btn_3 = custom_button(self, x=1240, y=120, w=300, h=60, text='"비상전원 공급절차" 수행\n(확인표-1. 계속 확인 단계', type=1)

        self.btn_4 = custom_button(self, x=380, y=210, w=300, h=60, text='발전소 안전변수\n감시 시작', type=2)
        self.btn_5 = custom_button(self, x=1240, y=210, w=300, h=60, text='원자로건물 중대위협 변수\n감시 시작', type=2)

        self.btn_6 = custom_button(self, x=380, y=300, w=300, h=100, text='RCS 대형 개구부\n(PZR MW 개방 또는\nRV head 제거)', type=3)

        self.btn_7 = custom_button(self, x=710, y=390, w=300, h=60, text='모든 SG 수위 > 68% NR', type=3)
        self.btn_8 = custom_button(self, x=1040, y=390, w=300, h=60, text='완화-01\n"증기발생기 급수 주입" 수행', type=1)

        self.btn_9 = custom_button(self, x=30, y=480, w=300, h=80, text='원자로건물 방사선준위\n'
                                                                        '그림3의"노심손상 미발생"영역 또는\n'
                                                                        '노심출구온도<371.1℃', type=3)
        self.btn_10 = custom_button(self, x=380, y=480, w=300, h=60, text='완화-03\n'
                                                                          '"원자로냉각재계통 냉각수 주입"\n'
                                                                          '수행', type=1)
        self.btn_11 = custom_button(self, x=710, y=480, w=300, h=60, text='RCS 압력 < 29.2kg/㎠', type=3)
        self.btn_12 = custom_button(self, x=1040, y=480, w=300, h=60, text='완화-02\n'
                                                                          '"원자로냉각재계통 감압" 수행', type=1)

        self.btn_13 = custom_button(self, x=710, y=570, w=300, h=60, text='노심출구온도 < 371.1℃', type=3)
        self.btn_14 = custom_button(self, x=1040, y=570, w=300, h=60, text='완화-03\n'
                                                                          '"원자로냉각재계통 냉각수 주입"\n'
                                                                          '수행', type=1)

        self.btn_15 = custom_button(self, x=380, y=690, w=300, h=60, text='원자로건물 수위 > 12.5%', type=3)
        self.btn_16 = custom_button(self, x=710, y=690, w=300, h=60, text='완화-04\n'
                                                                          '"원자로건물 냉각수 주입" 수행', type=1)
        # ========
        self.btn_17 = custom_button(self, x=380, y=780, w=300, h=130, text='발전소부지경계선량\n'
                                                                          '<전신: 30분동안 0.5msv/hr\n'
                                                                          '또는 2분동안 5mSv/hr\n'
                                                                          '갑산선선량은 전신선량의 5배'
                                                                          , type=3)
        self.btn_18 = custom_button(self, x=710, y=780, w=300, h=130, text='완화-05\n"핵분열생성물 방출 제어" 수행', type=1)

        self.btn_19 = custom_button(self, x=380, y=940, w=300, h=60, text='원자로건물 압력 < 133.6cmH2Og', type=3)
        self.btn_20 = custom_button(self, x=710, y=940, w=300, h=60, text='완화-06\n'
                                                                          '"원자로건물 상태 제어" 수행', type=1)

        self.btn_21 = custom_button(self, x=380, y=1030, w=300, h=60, text='원자로건물 수소농도 < 5%', type=3)
        self.btn_22 = custom_button(self, x=710, y=1030, w=300, h=60, text='완화-07\n'
                                                                          '"원자로건물내 수소 제어" 수행', type=1)

        self.btn_23 = custom_button(self, x=380, y=1120, w=300, h=60, text='사용후연료저장소수위 > 1%', type=3)
        self.btn_24 = custom_button(self, x=710, y=1120, w=300, h=60, text='완화-08\n'
                                                                           '"사용후연료저장소 지침서" 수행', type=1)

        self.btn_25 = custom_button(self, x=380, y=1210, w=300, h=60, text='감시-01\n'
                                                                           '"장기 관심사항 감시" 수행', type=1)

        self.btn_26 = custom_button(self, x=380, y=1300, w=800, h=180, text='다음 모든 조건을 만족\n'
                                                                            '노심출구온도<371.1℃, 그리고 안정 또는 감소\n'
                                                                            '(단, 노심출구온도 측정 불가시 원자로건물 내 방사선준위 그림3의"노심손상 미발생"영역\n'
                                                                            '발전소부지경계선량<전신: 30분 동안 0.5mSv/hr 또는 2분 동안 5mSv/hr (갑상선량은 전신선량의 5배)\n'
                                                                            '그리고 안정 또는 감소\n'
                                                                            '원자로건물 압력<133.6 cmH2Og, 그리고 안정 또는 감소\n'
                                                                            '원자로건물 수소농도<5%, 그리고 안정 또는 감소\n'
                                                                            '사용후연료저장소 수위>1%, 그리고 안정 또는 증가', type=1)

        self.btn_27 = custom_button(self, x=380, y=1510, w=300, h=60, text='종료-01\n'
                                                                           '"중대사고관리 종료" 수행', type=1)

        self.btn_28 = custom_button(self, x=1240, y=750, w=300, h=60, text='발전소부지경계선량\n'
                                                                          '<전신: 10mSv/hr, 갑상선: 50mSv/hr', type=3)
        self.btn_29 = custom_button(self, x=1570, y=750, w=300, h=60, text='완화-05\n'
                                                                           '"핵분열생성물 방출 제어" 수행', type=1)

        self.btn_30 = custom_button(self, x=1240, y=840, w=300, h=60, text='원자로건물 압력 < 8577.5cmH2Og', type=3)
        self.btn_31 = custom_button(self, x=1570, y=840, w=300, h=60, text='완화-06\n'
                                                                           '"원자로건물 상태 제어" 수행', type=1)

        self.btn_32 = custom_button(self, x=1240, y=930, w=300, h=60, text='원자로건물 수소 농도\n'
                                                                          '그림1의 "수소위협" 영역이외', type=3)
        self.btn_33 = custom_button(self, x=1570, y=930, w=300, h=60, text='완화-07\n'
                                                                           '"원자로건물내 수소 제어" 수행', type=1)

        self.btn_34 = custom_button(self, x=1570, y=1020, w=300, h=60, text='이전 수행 지침서로 되돌아 감', type=1)
        # ==============================================================================================================

        # self.btn_1.clicked.connect(self.btn_1_clicked)

# ======================================================================================================================
    # def btn_1_clicked(self):
    #     print('PPPP')

    # def mouseButtonKind(self, buttons):
    #     if buttons & Qt.LeftButton:
    #         print('LEFT')
    #     if buttons & Qt.MidButton:
    #         print('MIDDLE')
    #     if buttons & Qt.RightButton:
    #         print('RIGHT')
    #
    # def mousePressEvent(self, e):
    #     print('BUTTON PRESS')
    #     self.mouseButtonKind(e.buttons())
# ======================================================================================================================


    def paintEvent(self, event):
        p = QPainter(self)
        p.setPen(QPen(Qt.black))

        p.drawLine(960, 90, 960, 120)   # 1-2
        p.drawLine(960, 180, 960, 200)  # 2-3

        p.drawLine(1110, 150, 1240, 150)  # 2-3
        p.drawLine(1390, 180, 1390, 190)  # 2-3
        p.drawLine(960, 190, 1390, 190)  # 2-3

        p.drawLine(530, 200, 1390, 200)     # 2-4
        p.drawLine(530, 200, 530, 210)      # 2-4
        p.drawLine(1390, 200, 1390, 210)    # 2-5

        p.drawLine(530, 270, 530, 300)    # 4-6

        p.drawLine(560, 350, 860, 350)    # 6-7
        p.drawLine(860, 350, 860, 390)    # 6-7

        p.drawLine(180, 350, 380, 350)    # 6-9
        p.drawLine(180, 350, 180, 480)    # 6-9

        p.drawLine(330, 520, 380, 520)    # 9-10
        p.drawLine(180, 560, 180, 660)    # 9-15
        p.drawLine(180, 660, 860, 660)    # 9-13
        p.drawLine(530, 660, 530, 690)    # -15

        p.drawLine(530, 535, 530, 570)    # 10
        p.drawLine(180, 570, 530, 570)    # 10

        p.drawLine(1010, 420, 1040, 420)  # 7-8
        p.drawLine(1195, 450, 1195, 465)  # 8
        p.drawLine(860, 465, 1195, 465)   # 8

        p.drawLine(860, 450, 860, 480)    # 7-11

        p.drawLine(1010, 510, 1040, 510)  # 11-12
        p.drawLine(1195, 540, 1195, 555)  # 12
        p.drawLine(860, 555, 1195, 555)   # 12

        p.drawLine(860, 540, 860, 570)    # 11-13

        p.drawLine(1010, 600, 1040, 600)    # 13-14
        p.drawLine(860, 630, 860, 660)      # 13
        p.drawLine(1195, 630, 1195, 645)    # 14
        p.drawLine(860, 645, 1195, 645)     # 14

        p.drawLine(680, 720, 710, 720)     # 15-16
        p.drawLine(860, 750, 860, 765)     # 16-17
        p.drawLine(530, 765, 860, 765)     # 16-17
        p.drawLine(530, 750, 530, 780)     # 15-17

        p.drawLine(680, 845, 710, 845)     # 17-18
        p.drawLine(860, 875, 860, 925)     # 18-19
        p.drawLine(530, 925, 860, 925)     # 18-19
        p.drawLine(530, 910, 530, 940)     # 17-19

        p.drawLine(680, 970, 710, 970)       # 19-20
        p.drawLine(860, 1000, 860, 1015)     # 20-21
        p.drawLine(530, 1015, 860, 1015)     # 20-21
        p.drawLine(530, 1000, 530, 1030)     # 19-21

        p.drawLine(680, 1060, 710, 1060)     # 21-22
        p.drawLine(860, 1090, 860, 1105)     # 22-23
        p.drawLine(530, 1105, 860, 1105)     # 22-23
        p.drawLine(530, 1090, 530, 1120)     # 21-23

        p.drawLine(680, 1150, 710, 1150)     # 23-24
        p.drawLine(860, 1180, 860, 1195)     # 24-25
        p.drawLine(530, 1195, 860, 1195)     # 24-25
        p.drawLine(530, 1180, 530, 1210)     # 23-25

        p.drawLine(530, 1270, 530, 1300)     # 25-26

        p.drawLine(530, 1480, 530, 1510)     # 26-27
        p.drawLine(15, 1390, 380, 1390)      # 26-6
        p.drawLine(15, 285, 15, 1390)        # 26-6
        p.drawLine(15, 285, 530, 285)        # 26-6

        p.drawLine(1390, 270, 1390, 750)        # 5-28

        p.drawLine(1540, 780, 1590, 780)        # 28-29
        p.drawLine(1390, 810, 1390, 840)        # 28-30

        p.drawLine(1540, 870, 1590, 870)        # 30-31
        p.drawLine(1390, 900, 1390, 930)        # 30-32

        p.drawLine(1540, 960, 1590, 960)         # 32-33
        p.drawLine(1390, 990, 1390, 1020)        # 32-28
        p.drawLine(1195, 1020, 1390, 1020)       # 32-28
        p.drawLine(1195, 720, 1195, 1020)        # 32-28
        p.drawLine(1195, 720, 1390, 720)         # 32-28

        p.drawLine(1870, 780, 1920, 780)
        p.drawLine(1870, 870, 1920, 870)
        p.drawLine(1870, 960, 1920, 960)
        p.drawLine(1870, 1035, 1920, 1035)
        p.drawLine(1920, 780, 1920, 1035)

    def contextMenuEvent(self, event) -> None:
        """ FlowChart 에 기능 올리기  """
        menu = QMenu(self)  # 메뉴 생성
        add_btn_dia = menu.addAction("Add Diamond Button")
        add_btn_cir = menu.addAction("Add Circle Button")
        add_btn_rec = menu.addAction("Add Rectangle Button")

        add_btn_dia.triggered.connect(lambda a, pos=event.pos(), ele='dia': self.make_diagram(pos, ele))
        add_btn_cir.triggered.connect(lambda a, pos=event.pos(), ele='cir': self.make_diagram(pos, ele))
        add_btn_rec.triggered.connect(lambda a, pos=event.pos(), ele='rec': self.make_diagram(pos, ele))

        menu.exec_(event.globalPos())  # 실행

    def make_diagram(self, pos, ele):
        """ 클릭한 위치에 요소 위치 시키기 """
        if ele == 'dia':
            dig = custom_button(self, x=pos.x(), y=pos.y(), w=200, h=60, text='Start', type=3)
        if ele == 'cir':
            dig = custom_button(self, x=pos.x(), y=pos.y(), w=200, h=60, text='Start', type=2)
        if ele == 'rec':
            dig = custom_button(self, x=pos.x(), y=pos.y(), w=200, h=60, text='Start', type=1)

        dig.show()



if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MainLeftArea()
    window.show()
    app.exec_()
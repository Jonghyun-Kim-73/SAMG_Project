import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from CustomButton import CustomButton
from Flag import Flag

from arrow import Arrow
from Mitigation_01 import MitigationWindow


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


source1 = resource_path("x_button.png")


class MainLeft(QWidget):
    qss = """
            QWidget#main {
                background: rgb(128, 128, 128);
                border: 2px solid rgb(0, 0, 0); 
            }
            QWidget {
                background: rgb(128, 128, 128);
                border: 0px solid rgb(0, 0, 0); 
            }
        """

    def __init__(self, parent=None):
        super(MainLeft, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)  # 상위 스타일 상속
        self.parent = parent
        self.shmem = parent.shmem
        self.setStyleSheet(self.qss)

        # 크기 조정
        self.setMinimumHeight(900 - 40)
        self.setMinimumWidth(int(1920 * (2 / 3)))

        # 레이어 셋업
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 0, 5, 0)
        label2 = FlowChartArea(self)
        label2.setObjectName("main")
        layout.addWidget(label2)
        self.setLayout(layout)


class FlowChartArea(QWidget,QThread):
    qss = """
        QWidget#scroll {
            background: rgb(128, 128, 128);
            border: 2px solid rgb(0, 0, 0); 
        }
        QWidget {
            background: rgb(128, 128, 128);
            border: 0px solid rgb(0, 0, 0); 
        }
    """

    def __init__(self, parent=None):
        super(FlowChartArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.shmem = parent.shmem

        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        flowchart = FlowChart(self)
        self.scroll.setWidget(flowchart)
        layout = QVBoxLayout()
        layout.addWidget(self.scroll)
        self.setLayout(layout)

    # 자동 스크롤
    def paintEvent(self, e):
        if Flag.PAGE1:
            vbar = self.scroll.verticalScrollBar()
            vbar.setValue((vbar.maximum())*8/20)
            Flag.PAGE1 = False

        if Flag.PAGE2:
            vbar = self.scroll.verticalScrollBar()
            vbar.setValue((vbar.maximum()))
            Flag.PAGE2 = False

        if Flag.PAGE3:
            vbar = self.scroll.verticalScrollBar()
            vbar.setValue((vbar.minimum()))
            Flag.PAGE3 = False


class FlowChart(QWidget):
    def __init__(self, parent=None):
        super(FlowChart, self).__init__()
        self.parent = parent
        self.shmem = parent.shmem
        self.setGeometry(0, 0, 1210, 2070)  # 1900*(3/4) = 1425

        # Arrow
        self.line1 = Arrow(self, x=270, y=100, x2=270, y2=123, type=1)
        self.line1 = Arrow(self, x=270, y=210, x2=270, y2=243, type=1)
        self.line1 = Arrow(self, x=270, y=370, x2=270, y2=403, type=1)
        self.line1 = Arrow(self, x=270, y=530, x2=270, y2=563, type=1)
        self.line1 = Arrow(self, x=270, y=690, x2=270, y2=723, type=1)
        self.line1 = Arrow(self, x=270, y=850, x2=270, y2=883, type=1)
        self.line1 = Arrow(self, x=270, y=1010, x2=270, y2=1043, type=1)
        self.line1 = Arrow(self, x=270, y=1170, x2=270, y2=1203, type=1)
        self.line1 = Arrow(self, x=270, y=130, x2=270, y2=1363, type=1)
        self.line1 = Arrow(self, x=270, y=1750, x2=270, y2=1893, type=1)

        #아니오
        self.line1 = Arrow(self, x=270, y=315, x2=663, y2=315, type=3)
        self.line1 = Arrow(self, x=270, y=475, x2=663, y2=475, type=3)
        self.line1 = Arrow(self, x=270, y=635, x2=663, y2=635, type=3)
        self.line1 = Arrow(self, x=270, y=795, x2=663, y2=795, type=3)
        self.line1 = Arrow(self, x=270, y=955, x2=663, y2=955, type=3)
        self.line1 = Arrow(self, x=270, y=1115, x2=663, y2=1115, type=3)
        self.line1 = Arrow(self, x=270, y=1275, x2=663, y2=1275, type=3)

        #돌아오기
        self.line1 = Arrow(self, x=895, y=396, x2=280, y2=396, type=2)
        self.line1 = Arrow(self, x=895, y=556, x2=280, y2=556, type=2)
        self.line1 = Arrow(self, x=895, y=716, x2=280, y2=716, type=2)
        self.line1 = Arrow(self, x=895, y=876, x2=280, y2=876, type=2)
        self.line1 = Arrow(self, x=895, y=1036, x2=280, y2=1036, type=2)
        self.line1 = Arrow(self, x=895, y=1196, x2=280, y2=1196, type=2)
        self.line1 = Arrow(self, x=895, y=1356, x2=280, y2=1356, type=2)
        self.line1 = Arrow(self, x=1200, y=233, x2=280, y2=233, type=2)

        # CustomButton
        self.btn_1 = CustomButton(self, page=1, num=1, x=70, y=30, w=400, h=70, text='TSC “완화” 절차서 사용시작',type=0)
        self.btn_2 = CustomButton(self, page=1, num=2, x=70, y=130, w=400, h=90, text='안전 변수<br/>R02, P09, H04 감시 시작', type=0)
        self.btn_3 = CustomButton(self, page=1, num=3, x=70, y=250, w=400, h=130, text='발전소 부지 경계 선량<br/>&lt; 5분동안 0.5mSv/h', type=2)
        self.btn_4 = CustomButton(self, page=1, num=4, x=70, y=410, w=400, h=130, text='격납건물 압력<br/>&lt; 4.97 psig', type=2)
        self.btn_5 = CustomButton(self, page=1, num=5, x=70, y=570, w=400, h=130, text='격납건물 수소농도<br/>&lt; [H02]%', type=2)
        self.btn_6 = CustomButton(self, page=1, num=6, x=70, y=730, w=400, h=130, text='노심출구온도<br/>&lt; 371.1°C', type=2)
        self.btn_7 = CustomButton(self, page=1, num=7, x=70, y=890, w=400, h=130, text='RCS 압력<br/>&lt;28.12kg/cm2', type=2)
        self.btn_8 = CustomButton(self, page=1, num=8, x=70, y=1050, w=400, h=130, text='모든 증기발생기 수위<br/>> 74% NR', type=2)
        self.btn_9 = CustomButton(self, page=1, num=9, x=70, y=1210, w=400, h=130, text='격납건물 수위<br/>> 27.1%', type=2)
        self.btn_10 = CustomButton(self, page=1, num=10, x=20, y=1370, w=500, h=500, text='● 노심출구온도 &lt; 371.1°C<br/><br/>그리고 안정 또는 감소<br/>●발전소부지 경계 선량 &lt;[R01]<br/><br/>그리고 안정 또는 감소<br/>● 격납건물 압력 &lt; [P11]<br/><br/>그리고 안정 또는 감소<br/>●격납건물 수소농도 &lt; [H02]<br/><br/>그리고 안정 또는 감소', type=2)
        self.btn_11 = CustomButton(self, page=1, num=11, x=70, y=1900, w=400, h=90, text='종료-01<br/>“중대사고관리 종료“ 수행', type=1)

        self.btn_3_1 = CustomButton(self, page=1, num=31, x=670, y=270, w=450, h=90, text='완화-01<br/>“핵분열생성물 방출 제어“ 수행')
        self.btn_4_1 = CustomButton(self, page=1, num=41, x=670, y=430, w=450, h=90, text='완화-02<br/>“격납건물 상태제어“ 수행', type=1)
        self.btn_5_1 = CustomButton(self, page=1, num=51, x=670, y=590, w=450, h=90, text='완화-03<br/>“격납건물내 수소 제어“ 수행', type=1)
        self.btn_6_1 = CustomButton(self, page=1, num=61, x=670, y=750, w=450, h=90, text='완화-04<br/>“원자로 냉각재 계통 냉각수 주입“ 수행', type=1)
        self.btn_7_1 = CustomButton(self, page=1, num=71, x=670, y=910, w=450, h=90, text='완화-05<br/>“원자로 냉각재 계통 감압“ 수행', type=1)
        self.btn_8_1 = CustomButton(self, page=1, num=81, x=670, y=1070, w=450, h=90, text='완화-06<br/>“증기발생기 급수 주입“ 수행', type=1)
        self.btn_9_1 = CustomButton(self, page=1, num=91, x=670, y=1230, w=450, h=90, text='완화-07<br/>“격납건물 냉각수 주입“ 수행', type=1)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setPen(QPen(Qt.black))
        p.setFont(QFont('맑은 고딕', 14))
        p.drawLine(895, 350, 895, 396)
        p.drawText(470, 305, "아니오")
        p.drawText(240, 403, "예")

        p.drawLine(895, 500, 895, 556)
        p.drawText(470, 465, "아니오")
        p.drawText(240, 563, "예")

        p.drawLine(895, 666, 895, 716)
        p.drawText(470, 625, "아니오")
        p.drawText(240, 723, "예")

        p.drawLine(895, 820, 895, 876)
        p.drawText(470, 785, "아니오")
        p.drawText(240, 883, "예")

        p.drawLine(895, 990, 895, 1036)
        p.drawText(470, 945, "아니오")
        p.drawText(240, 1043, "예")

        p.drawLine(895, 1140, 895, 1196)
        p.drawText(470, 1105, "아니오")
        p.drawText(240, 1203, "예")

        p.drawLine(895, 1300, 895, 1356)
        p.drawText(470, 1265, "아니오")
        p.drawText(240, 1363, "예")

        p.drawLine(270, 1620, 1200, 1620)
        p.drawLine(1200, 233, 1200, 1620)

        current = 0
        # Popup open
        if Flag.btn_clicked[1]:
            self.popup = CustomPopup(p_number=1, p_title="TSC “완화” 절차서 사용시작", p_content='\nTSC “완화” 절차서를 시작합니다.')
            Flag.btn_clicked[1] = False
            self.btn_1.color()
            Flag.color[1] = 2
            Flag.close[1] = 0

            # 현재 실행중인 버튼 병행처리
            current = self.together(1)
            self.change(current)

            show = self.popup.showModal()
            if Flag.btn_yes[1] == 0 and Flag.close[1] == 0: #yes # 완료된 버튼 팝업 생성 방지
                self.btn_1.complete()
                Flag.color[1] = 3

                Flag.btn_clicked[2] = True
                self.btn_2.color()
                Flag.color[2] = 2

        if Flag.btn_clicked[2]:
            self.popup = CustomPopup(p_number=2, p_title="안전 변수 R02, P09, H04 감시 시작", p_content='\n안전 변수 R02, P09, H04 감시를 시작합니다.')
            Flag.btn_clicked[2] = False
            self.btn_2.color()
            Flag.color[2] = 2
            Flag.close[2] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(2)
            self.change(current)

            show = self.popup.showModal()
            if Flag.btn_yes[2] == 0 and Flag.close[2] == 0: # 완료된 버튼 팝업 생성 방지
                self.btn_2.complete()
                Flag.color[2] = 3

                Flag.btn_clicked[3] = True
                self.btn_3.color()
                Flag.color[3] = 2

        if Flag.btn_clicked[3]:
            self.popup = CustomPopup(p_number=3, p_title="발전소 부지 경계 선량 확인",  p_content="\n발전소 부지 경계 선량 5분동안 < 0.5mSv/h", p_label1="현재 발전소 부지 경계 선량", p_value1=Flag.value1_1) #단위 추가 필요 "%d"%~
            Flag.btn_clicked[3] = False
            self.btn_3.color()
            Flag.color[3] = 2
            Flag.close[3] = 0  # 팝업 닫기
            # 현재 실행중인 버튼 병행처리
            current = self.together(3)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[3] == 0 and Flag.close[3] == 0:  #yes
                self.btn_3.complete()
                Flag.color[3] = 3
                Flag.btn_clicked[4] = True
                self.btn_3_1.complete()
                self.btn_4.color()
                Flag.color[31] = 3
                Flag.color[4] = 2

            elif Flag.btn_yes[3] == 1 and Flag.close[3] == 0:  #no
                self.btn_3.complete()
                Flag.color[3] = 3
                Flag.btn_clicked_1[31] = True
                self.btn_3_1.color()
                Flag.color[31] = 2

        if Flag.btn_clicked[4]:
            self.popup = CustomPopup(p_number=4, p_title="격납건물 압력 확인", p_content="\n격납건물 압력 < 4.97 psig", p_label1="현재 격납건물 압력", p_value1=Flag.value1_2)
            Flag.btn_clicked[4] = False
            self.btn_4.color()
            Flag.color[4] = 2
            Flag.close[4] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(4)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[4] == 0 and Flag.close[4] == 0:  # yes
                self.btn_4.complete()
                Flag.color[4] = 3
                Flag.btn_clicked[5] = True
                self.btn_4_1.complete()
                self.btn_5.color()
                Flag.color[41] = 3
                Flag.color[5] = 2

            elif Flag.btn_yes[4] == 1 and Flag.close[4] == 0:  # no
                self.btn_4.complete()
                Flag.color[4] = 3
                Flag.btn_clicked_1[41] = True
                self.btn_4_1.color()
                Flag.color[41] = 2

        if Flag.btn_clicked[5]:
            self.popup = CustomPopup(p_number=5, p_title="격납건물 수소농도 확인", p_content="\n격납건물 수소농도 < [H02]%", p_label1="현재 격납건물 수소농도", p_value1=Flag.value2_4)
            Flag.PAGE1 = True
            Flag.btn_clicked[5] = False
            self.btn_5.color()
            Flag.color[5] = 2
            Flag.close[5] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(5)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[5] == 0 and Flag.close[5] == 0:  # yes
                self.btn_5.complete()
                Flag.color[5] = 3
                Flag.btn_clicked[6] = True
                self.btn_5_1.complete()
                self.btn_6.color()
                Flag.color[51] = 3
                Flag.color[6] = 2

            elif Flag.btn_yes[5] == 1 and Flag.close[5] == 0:  # no
                self.btn_5.complete()
                Flag.color[5] = 3
                Flag.btn_clicked_1[51] = True
                self.btn_5_1.color()
                Flag.color[51] = 2

        if Flag.btn_clicked[6]:
            self.popup = CustomPopup(p_number=6, p_title="노심출구온도 확인", p_content="\n노심출구온도 < 371.1°C", p_label1="현재 노심출구온도", p_value1=Flag.value1_3)
            Flag.btn_clicked[6] = False
            Flag.PAGE1 = True
            self.btn_6.color()
            Flag.color[6] = 2
            Flag.close[6] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(6)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[6] == 0 and Flag.close[6] == 0:  # yes
                self.btn_6.complete()
                Flag.color[6] = 3
                Flag.btn_clicked[7] = True
                self.btn_6_1.complete()
                self.btn_7.color()
                Flag.color[61] = 3
                Flag.color[7] = 2

            elif Flag.btn_yes[6] == 1 and Flag.close[6] == 0:  # no
                self.btn_6.complete()
                Flag.color[6] = 3
                Flag.btn_clicked_1[61] = True
                self.btn_6_1.color()
                Flag.color[61] = 2

        if Flag.btn_clicked[7]:
            self.popup = CustomPopup(p_number=7, p_title="RCS 압력 확인", p_content="\nRCS 압력 < 28.12kg/cm^2", p_label1="현재 RCS 압력", p_value1=Flag.value1_4)
            Flag.btn_clicked[7] = False
            self.btn_7.color()
            Flag.color[7] = 2
            Flag.close[7] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(7)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[7] == 0 and Flag.close[7] == 0:  # yes
                self.btn_7.complete()
                Flag.color[7] = 3
                Flag.btn_clicked[8] = True
                self.btn_7_1.complete()
                self.btn_8.color()
                Flag.color[71] = 3
                Flag.color[8] = 2

            elif Flag.btn_yes[7] == 1 and Flag.close[7] == 0:  # no
                self.btn_7.complete()
                Flag.color[7] = 3
                Flag.btn_clicked_1[71] = True
                self.btn_7_1.color()
                Flag.color[71] = 2

        if Flag.btn_clicked[8]:
            self.popup = CustomPopup(p_number=8, p_title="모든 증기발생기 수위 확인", p_content="\n모든 증기발생기 수위 < 74% NR", p_label1="SG 1 Level", p_value1=Flag.value1_5, p_label2="SG 2 Level", p_value2=Flag.value1_6)
            Flag.btn_clicked[8] = False
            self.btn_8.color()
            Flag.color[8] = 2
            Flag.close[8] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(8)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[8] == 0 and Flag.close[8] == 0:  # yes
                self.btn_8.complete()
                Flag.color[8] = 3
                Flag.btn_clicked[9] = True
                self.btn_8_1.complete()
                self.btn_9.color()
                Flag.color[81] = 3
                Flag.color[9] = 2

            elif Flag.btn_yes[8] == 1 and Flag.close[8] == 0:  # no
                self.btn_8.complete()
                Flag.color[8] = 3
                Flag.btn_clicked_1[81] = True
                self.btn_8_1.color()
                Flag.color[81] = 2

        if Flag.btn_clicked[9]:
            self.popup = CustomPopup(p_number=9, p_title="격납건물 수위 확인", p_content="\n격납건물 수위 > 27.1%", p_label1="현재 격납건물 수위", p_value1=Flag.value1_7)
            Flag.btn_clicked[9] = False
            Flag.PAGE2 = True
            self.btn_9.color()
            Flag.color[9] = 2
            Flag.close[9] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(9)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[9] == 0 and Flag.close[9] == 0:  # yes
                self.btn_9.complete()
                Flag.color[9] = 3
                Flag.btn_clicked[10] = True
                self.btn_9_1.complete()
                self.btn_10.color()
                Flag.color[101] = 3
                Flag.color[10] = 2

            elif Flag.btn_yes[9] == 1 and Flag.close[9] == 0:  # no
                self.btn_9.complete()
                Flag.color[9] = 3
                Flag.btn_clicked_1[91] = True
                self.btn_9_1.color()
                Flag.color[91] = 2

        if Flag.btn_clicked[10]:
            self.popup = CustomPopup(p_number=10, p_title="TOTAL", p_content="\nTOTAL",
                                     p_label1="노심출구온도 < 371.1°C", p_value1=Flag.value2_1,
                                     p_label2="발전소부지 경계 선량 30분동안 < 0.5mSv/h", p_value2=Flag.value2_2,
                                     p_label3="격납건물 압력 < 4.97 psig", p_value3=Flag.value2_3,
                                     p_label4="격납건물 수소농도 < [H02]", p_value4=Flag.value2_4)
            Flag.btn_clicked[10] = False
            self.btn_10.color()
            Flag.color[10] = 2
            Flag.close[10] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(10)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[10] == 0 and Flag.close[10] == 0:  # yes
                self.btn_10.complete()
                Flag.color[10] = 3
                Flag.btn_clicked[11] = True
                self.btn_11.color()
                Flag.color[11] = 2

            elif Flag.btn_yes[10] == 1 and Flag.close[10] == 0:  # no #안전변수로 이동(버튼 초기화)
                Flag.PAGE3 = True
                self.btn_1.complete()
                self.btn_2.color()
                self.btn_3.color_init()
                self.btn_4.color_init()
                self.btn_5.color_init()
                self.btn_6.color_init()
                self.btn_7.color_init()
                self.btn_8.color_init()
                self.btn_9.color_init()
                self.btn_10.color_init()
                self.btn_11.color_init()
                self.btn_3_1.color_init()
                self.btn_4_1.color_init()
                self.btn_5_1.color_init()
                self.btn_6_1.color_init()
                self.btn_7_1.color_init()
                self.btn_8_1.color_init()
                self.btn_9_1.color_init()
                for i in range(3, 12):
                    Flag.btn_yes[i] = -1
                    Flag.color[i] = 0
                    Flag.color[i*10+1] = 0
                Flag.color[1] = 3
                Flag.color[2] = 2

        if Flag.btn_clicked[11]:
            Flag.btn_clicked[11] = False
            self.btn_11.color()
            Flag.color[11] = 2
            Flag.close[11] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(11)
            self.change(current)

        if Flag.btn_clicked_1[31]:
            self.popup = CustomPopup(p_number=31, p_title="완화-01 “핵분열생성물 방출 제어“ 수행", p_content="\n완화-01 “핵분열생성물 방출 제어“를 수행합니다.")
            Flag.btn_clicked_1[31] = False
            self.btn_3_1.color()
            Flag.color[31] = 2
            Flag.close[31] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(31)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[31] == 0 and Flag.close[31] == 0:  # yes
                self.btn_3_1.complete()
                Flag.color[31] = 3
                Flag.btn_clicked[4] = True
                self.btn_4.color()
                Flag.color[4] = 2

        if Flag.btn_clicked_1[41]:
            self.popup = CustomPopup(p_number=41, p_title="완화-02 “격납건물 상태제어“ 수행", p_content="\n완화-02 “격납건물 상태제어“를 수행합니다.")
            Flag.btn_clicked_1[41] = False
            self.btn_4_1.color()
            Flag.color[41] = 2
            Flag.close[41] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(41)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[41] == 0 and Flag.close[41] == 0:  # yes
                self.btn_4_1.complete()
                Flag.color[41] = 3
                Flag.btn_clicked[5] = True
                self.btn_5.color()
                Flag.color[5] = 2

        if Flag.btn_clicked_1[51]:
            self.popup = CustomPopup(p_number=51, p_title="완화-03 “격납건물내 수소 제어“ 수행", p_content="\n완화-03 “격납건물내 수소 제어“를 수행합니다.")
            Flag.btn_clicked_1[51] = False
            self.btn_5_1.color()
            Flag.color[51] = 2
            Flag.close[51] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(51)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[51] == 0 and Flag.close[51] == 0:  # yes
                self.btn_5_1.complete()
                Flag.color[51] = 3
                Flag.btn_clicked[6] = True
                self.btn_6.color()
                Flag.color[6] = 2

        if Flag.btn_clicked_1[61]:
            self.popup = CustomPopup(p_number=61, p_title="완화-04 “원자로 냉각재 계통 냉각수 주입“ 수행", p_content="\n완화-04 “원자로 냉각재 계통 냉각수 주입“을 수행합니다.")
            Flag.btn_clicked_1[61] = False
            self.btn_6_1.color()
            Flag.color[61] = 2
            Flag.close[61] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(61)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[61] == 0 and Flag.close[61] == 0:  # yes
                self.btn_6_1.complete()
                Flag.color[61] = 3
                Flag.btn_clicked[7] = True
                self.btn_7.color()
                Flag.color[7] = 2

        if Flag.btn_clicked_1[71]:
            self.popup = CustomPopup(p_number=71, p_title="완화-05 “원자로 냉각재 계통 감압“ 수행", p_content="\n완화-05 “원자로 냉각재 계통 감압“을 수행합니다.")
            Flag.btn_clicked_1[71] = False
            self.btn_7_1.color()
            Flag.color[71] = 2
            Flag.close[71] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(71)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[71] == 0 and Flag.close[71] == 0:  # yes
                self.btn_7_1.complete()
                Flag.color[71] = 3
                Flag.btn_clicked[8] = True
                self.btn_8.color()
                Flag.color[8] = 2

        if Flag.btn_clicked_1[81]:
            self.popup = CustomPopup(p_number=81, p_title="완화-06 “증기발생기 급수 주입“ 수행", p_content="\n완화-06 “증기발생기 급수 주입“을 수행합니다.")
            Flag.btn_clicked_1[81] = False
            self.btn_8_1.color()
            Flag.color[81] = 2
            Flag.close[81] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(81)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[81] == 0 and Flag.close[81] == 0:  # yes
                self.btn_8_1.complete()
                Flag.color[81] = 3
                self.miti_win = MitigationWindow(self)  # self 필수
                self.miti_win.show()

        if Flag.btn_clicked_1[91]:
            self.popup = CustomPopup(p_number=91, p_title="완화-07 “격납건물 냉각수 주입“ 수행", p_content="\n완화-07 “격납건물 냉각수 주입“을 수행합니다.")
            Flag.PAGE2 = True
            Flag.btn_clicked_1[91] = False
            self.btn_9_1.color()
            Flag.color[91] = 2
            Flag.close[91] = 0
            # 현재 실행중인 버튼 병행처리
            current = self.together(91)
            self.change(current)

            show = self.popup.showModal()

            if Flag.btn_yes[91] == 0 and Flag.close[91] == 0:  # yes
                self.btn_9_1.complete()
                Flag.color[91] = 3
                Flag.btn_clicked[10] = True
                self.btn_10.color()
                Flag.color[10] = 2

    def together(self, me):
        for i in range(1, 12):
            if Flag.color[i] == 2:  # 자기 자신 제외, 현재 진행중인 버튼 찾기
                if i == me:
                    pass
                else:
                    Flag.color[i] = 1  # 병행처리
                    return i
            if Flag.color[i*10+1] == 2:
                if me == (i*10+1):
                    pass
                else:
                    Flag.color[i*10+1] = 1  # 병행처리
                    return i*10+1

    def change(self, find):
        if find == 1: self.btn_1.color2()
        elif find == 2: self.btn_2.color2()
        elif find == 3: self.btn_3.color2()
        elif find == 4: self.btn_4.color2()
        elif find == 5: self.btn_5.color2()
        elif find == 6: self.btn_6.color2()
        elif find == 7: self.btn_7.color2()
        elif find == 8: self.btn_8.color2()
        elif find == 9: self.btn_9.color2()
        elif find == 10: self.btn_10.color2()
        elif find == 11: self.btn_11.color2()
        elif find == 31: self.btn_3_1.color2()
        elif find == 41: self.btn_4_1.color2()
        elif find == 51: self.btn_5_1.color2()
        elif find == 61: self.btn_6_1.color2()
        elif find == 71: self.btn_7_1.color2()
        elif find == 81: self.btn_8_1.color2()
        elif find == 91: self.btn_9_1.color2()


class CustomPopup(QDialog):
    qss = """
            QWidget{
                background : rgb(180, 180, 180)
            }
            QLabel#title {
                font-size: 14pt; 
            }
            QLabel#data {
                font-size:12pt;
                border: 2px inset rgb(0, 0, 0);
                background: rgb(255, 255, 255);
            }
            QDialog{
                border: 2px solid rgb(0, 0, 0);       
            }
            QPushButton {
                color: rgb(0, 0, 0);
	            background-color: white;
	            border: 2px solid rgb(0, 0, 0);       
            }
            """

    def __init__(self, p_number=None, p_title=None, p_content=None, p_label1=None, p_value1=None, p_label2=None, p_value2=None, p_label3=None, p_value3=None, p_label4=None, p_value4=None):
        super().__init__()
        self.layout = QVBoxLayout()

        # 팝업 정보(메시지)
        self.p_number = p_number
        self.p_title = p_title
        self.p_content = p_content
        self.p_label1 = p_label1
        self.p_value1 = p_value1
        self.p_label2 = p_label2
        self.p_value2 = p_value2
        self.p_label3 = p_label3
        self.p_value3 = p_value3
        self.p_label4 = p_label4
        self.p_value4 = p_value4

        self.layout.addWidget(CustomPopupContent(self, p_number=self.p_number, p_title=self.p_title, p_content=self.p_content, p_label1=self.p_label1, p_value1=self.p_value1, p_label2=self.p_label2, p_value2=self.p_value2, p_label3=self.p_label3, p_value3=self.p_value3, p_label4=self.p_label4, p_value4=self.p_value4))
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(self.qss)
        self.layout.addStretch(-1)
        self.setGeometry(100, 300, 550, 100)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pressing = False

    def showModal(self):
        return super().exec_()

class CustomPopupContent(QWidget):
    qss = """
        QWidget{
            background : rgb(180, 180, 180)
        }
        QPushButton{
            background : rgb(218,218,218);
            border: 1px solid rgb(0, 0, 0);       
        }
        QTableWidget {
            gridline-color: rgb(0,0,0);
            font-size: 12pt;
        }
        QPushButton#xbutton {
            background-color: none;
            border: 2px solid rgb(0, 0, 0);       
        }
    """
    def __init__(self, parent, p_number = None, p_title = None, p_content = None, p_label1=None, p_value1=None,
                 p_label2=None, p_value2=None, p_label3=None, p_value3=None, p_label4=None, p_value4=None):
        super(CustomPopupContent, self).__init__()
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setMinimumWidth(400)

        self.p_number = p_number
        self.p_label1 = p_label1
        self.p_value1 = p_value1
        self.p_label2 = p_label2
        self.p_value2 = p_value2
        self.p_label3 = p_label3
        self.p_value3 = p_value3
        self.p_label4 = p_label4
        self.p_value4 = p_value4

        self.layout_t = QHBoxLayout()
        self.layout_t.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(p_title)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFixedSize(50, 40)
        self.title.setStyleSheet(""" background-color: rgb(91,155,213); border: 2px solid rgb(0,0,0); color: white;font-size: 14pt; """)
        btn_close = QPushButton()
        btn_close.setIcon(QIcon(source1))
        btn_close.setStyleSheet("border:0px")
        btn_close.clicked.connect(self.close)
        btn_close.setIconSize(QSize(25, 25))
        btn_close.setFixedSize(40, 30)
        btn_close.setObjectName('xbutton')

        self.layout_t.addWidget(self.title)
        self.layout_t.addWidget(btn_close)

        self.layout.addLayout(self.layout_t)

        self.label = QLabel(p_content)
        self.label.setObjectName("title")

        #테두리 제거용
        self.label.setStyleSheet("margin : 3px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.subsub = QHBoxLayout()
        self.subLayout = QHBoxLayout()
        self.layout.addWidget(self.label)

        if self.p_number != 1 and self.p_number != 2\
                and self.p_number != 31 and self.p_number != 41 and self.p_number != 51\
                and self.p_number != 61 and self.p_number != 71 and self.p_number != 81\
                and self.p_number != 91:
            self.tableWidget = QTableWidget()
            self.tableWidget.setStyleSheet("background: rgb(221, 221, 221);"
                                           "border: 0px solid rgb(0, 0, 0);")
            self.tableWidget.horizontalHeader().setVisible(False)  #table 헤더 숨기기
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.setContentsMargins(0, 0, 0, 0)

            if self.p_number == 8:
                self.tableWidget.setRowCount(2)
                self.tableWidget.setFixedSize(350, 60)
            elif self.p_number == 10:
                self.tableWidget.setRowCount(4)
                self.tableWidget.setFixedSize(350, 120)
            else:
                self.tableWidget.setRowCount(1)
                self.tableWidget.setFixedSize(350, 30)

            self.tableWidget.setColumnCount(2)
            self.tableWidget.setColumnWidth(0,250)
            self.tableWidget.horizontalHeader().setStretchLastSection(True)

            # 편집 불가
            self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
            self.tableWidget.setFocusPolicy(Qt.NoFocus)
            self.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)

            if self.p_number == 8:
                item1_ = QTableWidgetItem(p_label1)
                item2_ = QTableWidgetItem(p_value1)

                if float(p_value1) <= 45:
                    item1_.setBackground(QColor(252, 227, 112))
                    item2_.setBackground(QColor(252, 227, 112))

                item3_ = QTableWidgetItem(p_label2)
                item4_ = QTableWidgetItem(p_value2)

                if float(p_value2) <= 45:
                    item3_.setBackground(QColor(252, 227, 112))
                    item4_.setBackground(QColor(252, 227, 112))

                self.tableWidget.setItem(0, 0, item1_)
                self.tableWidget.setItem(0, 1, item2_)
                self.tableWidget.setItem(1, 0, item3_)
                self.tableWidget.setItem(1, 1, item4_)
            else:
                self.tableWidget.setItem(0, 0, QTableWidgetItem(p_label1))
                self.tableWidget.setItem(0, 1, QTableWidgetItem(p_value1))
                self.tableWidget.setItem(1, 0, QTableWidgetItem(p_label2))
                self.tableWidget.setItem(1, 1, QTableWidgetItem(p_value2))
            self.tableWidget.setItem(2, 0, QTableWidgetItem(p_label3))
            self.tableWidget.setItem(2, 1, QTableWidgetItem(p_value3))
            self.tableWidget.setItem(3, 0, QTableWidgetItem(p_label4))
            self.tableWidget.setItem(3, 1, QTableWidgetItem(p_value4))
            self.tableWidget.setGeometry(30, 30, 30, 30)

            # 테이블 정렬
            delegate = AlignDelegate()
            self.tableWidget.setItemDelegate(delegate)

            fnt = self.font()
            fnt.setPointSize(12)
            self.tableWidget.setFont(fnt)

            self.subsub.addWidget(self.tableWidget)
            self.layout.addLayout(self.subsub)

        self.btnOK = QPushButton("예")
        self.btnOK.setFixedSize(100, 35)
        self.btnOK.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnOK.clicked.connect(self.onOKButtonClicked)

        self.btnCancel = QPushButton("아니오")
        self.btnCancel.setFixedSize(100, 35)
        self.btnCancel.setCursor(QCursor(Qt.PointingHandCursor))
        self.btnCancel.clicked.connect(self.onCancelButtonClicked)

        self.subLayout.setContentsMargins(50, 30, 50, 30)
        self.subLayout.addWidget(self.btnOK)
        self.subLayout.addWidget(self.btnCancel)

        if self.p_number == 1 or self.p_number == 2 or self.p_number == 31 or self.p_number == 41 or self.p_number == 51\
                or self.p_number == 71 or self.p_number == 61 or self.p_number == 71\
                or self.p_number == 81 or self.p_number == 91:
            self.btnCancel.hide()
        else:
            self.btnCancel.show()

        self.layout.addLayout(self.subLayout)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

        #Popup move
        self.start = QPoint(0, 0)
        self.pressing = False

    # 그냥 닫으면 병행 컬러로 바뀐다.
    def close(self):
        Flag.close[self.p_number] = 1
        self.setDisabled(True)
        self.parent.close()

    def onOKButtonClicked(self):
        Flag.btn_yes[self.p_number] = 0
        self.setDisabled(True)
        self.parent.close()

    def onCancelButtonClicked(self):
        Flag.btn_yes[self.p_number] = 1
        self.parent.close()

    def showModal(self):
        return super().exec_()

    def resizeEvent(self, QResizeEvent):
        super(CustomPopupContent, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                    self.mapToGlobal(self.movement).y(),
                                    self.parent.width(),
                                    self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainLeft()
    window.show()
    flow = FlowChart()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
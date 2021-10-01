import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Flag import Flag

from button import Custom
from arrow import Arrow
from Mitigation_01 import MitigationWindow


class MainLeft(QWidget):

    def __init__(self, parent=None):
        super(MainLeft, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)  # 상위 스타일 상속
        self.parent = parent
        self.shmem = parent.shmem

        # self.setMouseTracking(True)
        #카운트
        # 크기 조정
        self.setMinimumHeight(900 - 40)
        self.setMinimumWidth(int(1920 * (2 / 3)))
        # self.setStyleSheet(self.qss)
        # self.setMaximumWidth(int(1920*(3/4)))
        # self.setMinimumHeight(self.parent.height() - 40)
        # self.setMinimumWidth(int(self.parent.width() * (2/3))

        # 레이어 셋업 ====================================================================================================
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        self.x = QCursor.pos().x()
        self.y = QCursor.pos().y()

        print("position", self.x, " , ", self.y)

        # label1 = QLabel('전략 수행 제어도')
        # label1.setFixedHeight(30)
        # label1.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)  # 텍스트 정렬
        # label1.setStyleSheet("Color : white; font-size: 14pt; font-weight: bold")

        label2 = FlowChartArea(self)

        layout.addWidget(label2)
        self.setLayout(layout)
        # self.update()

class FlowChartArea(QWidget,QThread):
    qss = """
        QWidget {
            background: rgb(128, 128, 128);
        border: 2px solid rgb(0, 0, 0); 
            
        }
    """

    def __init__(self, parent=None):
        super(FlowChartArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.shmem = parent.shmem
        self.setStyleSheet(self.qss)
        self.setMouseTracking(True)
        # self.filter = Custom(x=0, y=0, w=300, h=300, text='bibi', type=0)
        # self.installEventFilter(self.filter)
        self.scroll = QScrollArea()
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        # scroll.setWidgetResizable(True)


        flowchart = FlowChart(self)
        #
        self.scroll.setWidget(flowchart)
        # self.down()

        #자동스크롤
        #     vbar = aa.scroll.verticalScrollBar()
        #     vbar.setValue(vbar.maximum())

        layout = QVBoxLayout()
        layout.addWidget(self.scroll)

        self.setLayout(layout)

    def paintEvent(self, e):
        if Flag.PAGE1:
            vbar = self.scroll.verticalScrollBar()
            vbar.setValue((vbar.maximum())*9/20)
            Flag.PAGE1 = False

        if Flag.PAGE2:
            vbar = self.scroll.verticalScrollBar()
            vbar.setValue((vbar.maximum()) * 29 / 30)
            Flag.PAGE2 = False

class FlowChart(QWidget):
    qss = """
            QWidget {
                background: rgb(128, 128, 128);
                border: 0px solid rgb(0, 0, 0); 

            }
        """

    def __init__(self, parent=None):
        super(FlowChart, self).__init__()
        self.parent = parent
        self.shmem = parent.shmem

        self.setGeometry(0, 0, 1150, 2300)  # 1900*(3/4) = 1425
        self.setStyleSheet(self.qss)
        self.setMouseTracking(True)

        self.msg_box = QMessageBox()
        # 버튼 색상
        self.color_clicked = QColor(128, 128, 128)
        self.color_click = QColor(0, 176, 218)

        # 커스텀버튼추가===================================================================================================
        # 예 line
        self.line1 = Arrow(self, x=270, y=100, x2=270, y2=130, type=1)
        self.line1 = Arrow(self, x=270, y=200, x2=270, y2=260, type=1)
        self.line1 = Arrow(self, x=270, y=420, x2=270, y2=450, type=1)
        self.line1 = Arrow(self, x=270, y=610, x2=270, y2=640, type=1)
        self.line1 = Arrow(self, x=270, y=790, x2=270, y2=830, type=1)
        self.line1 = Arrow(self, x=270, y=900, x2=270, y2=1020, type=1)
        self.line1 = Arrow(self, x=270, y=1180, x2=270, y2=1210, type=1)
        self.line1 = Arrow(self, x=270, y=1370, x2=270, y2=1400, type=1)
        self.line1 = Arrow(self, x=270, y=1560, x2=270, y2=1590, type=1)
        self.line1 = Arrow(self, x=270, y=1750, x2=270, y2=1780, type=1)
        self.line1 = Arrow(self, x=270, y=1990, x2=270, y2=2140, type=1)

        #아니오
        self.line1 = Arrow(self, x=270, y=345, x2=730, y2=345, type=3)
        self.line1 = Arrow(self, x=270, y=535, x2=730, y2=535, type=3)
        self.line1 = Arrow(self, x=270, y=725, x2=730, y2=725, type=3)
        self.line1 = Arrow(self, x=270, y=915, x2=730, y2=915, type=3)
        self.line1 = Arrow(self, x=270, y=1105, x2=730, y2=1105, type=3)
        self.line1 = Arrow(self, x=270, y=1295, x2=730, y2=1295, type=3)
        self.line1 = Arrow(self, x=270, y=1485, x2=730, y2=1485, type=3)


        #돌아오기
        self.line1 = Arrow(self, x=920, y=440, x2=280, y2=440, type=2)
        self.line1 = Arrow(self, x=920, y=630, x2=280, y2=630, type=2)
        self.line1 = Arrow(self, x=920, y=820, x2=280, y2=820, type=2)
        self.line1 = Arrow(self, x=920, y=1010, x2=280, y2=1010, type=2)
        self.line1 = Arrow(self, x=920, y=1200, x2=280, y2=1200, type=2)
        self.line1 = Arrow(self, x=920, y=1390, x2=280, y2=1390, type=2)
        self.line1 = Arrow(self, x=920, y=1580, x2=280, y2=1580, type=2)
        self.line1 = Arrow(self, x=270, y=1850, x2=760, y2=1850, type=3)

        # 커스텀버튼 type : 3 dia 2 cir 1 rec 0 round_rec

        self.btn_11 = Custom(self, x=70, y=2140, w=400, h=100, text='종료-01\n“중대사고관리 종료“ 수행', type=1
                                    , msg_text='종료-01 “중대사고관리 종료“ 수행'
                                    , msg_text2="종료-01 “중대사고관리 종료“를 수행합니다."
                                    )
        self.btn_11.setObjectName("b18")
        self.btn_10_1 = Custom(self, x=700, y=1815, w=400, h=70, text='안전변수 바로 아래로 이동', type=1
                                      , msg_text='안전변수 바로 아래로 이동'
                                      , msg_text2="안전변수 바로 아래로 이동합니다."
                                      )
        self.btn_10_1.setObjectName("b17")
        self.btn_10 = Custom(self, x=20, y=1600, w=500, h=500,
                                    text='● 노심출구온도 < [T01]\n그리고 안정 또는 감소\n\n●발전소부지 경계 선량 <[R01]\n그리고 안정 또는 감소\n\n● 격납건물 압력 < [P11]\n그리고 안정 또는 감소\n\n●격납건물 수소농도 < [H02]\n그리고 안정 또는 감소',
                                    type=3, msg_text="",
                                    msg_text2="",
                                    msg_text3="",
                                    connected_btn=self.btn_11)
        self.btn_10.setObjectName("b16")
        self.btn_9_1 = Custom(self, x=670, y=1435, w=500, h=100, text='완화-07\n“격납건물 냉각수 주입“ 수행', type=1
                                     , msg_text='완화-07 “격납건물 냉각수 주입“ 수행'
                                     , msg_text2="완화-07 “격납건물 냉각수 주입“을 수행합니다."
                                     , connected_btn=self.btn_10)
        self.btn_9_1.setObjectName("b15")
        self.btn_9 = Custom(self, x=90, y=1410, w=360, h=150, text='격납건물 수위\n> [L06] m', type=3
                                   , msg_text="격납건물 수위 확인"
                                   , msg_text2='격납건물 수위 > [L06] m'
                                   , msg_text3='격납건물 수위'
                                   , connected_btn=self.btn_10, connected_btn_2=self.btn_9_1)
        self.btn_9.setObjectName("b14")
        self.btn_8_1 = Custom(self, x=670, y=1245, w=500, h=100, text='완화-06\n“증기발생기 급수 주입“ 수행', type=1
                                     , msg_text='완화-06 “증기발생기 급수 주입“ 수행'
                                     , msg_text2="완화-06 “증기발생기 급수 주입“을 수행합니다."
                                     , connected_btn=self.btn_9)
        self.btn_8_1.setObjectName("b13")

        self.btn_8 = Custom(self, x=90, y=1220, w=360, h=150, text='모든 증기발생기 수위\n> [L01%] NR', type=3
                                   , msg_text="모든 증기발생기 수위 확인"
                                   , msg_text2='모든 증기발생기 수위 > [L01%] NR'
                                   , msg_text3='SG1 수위 NR'
                                   , msg_text4='SG2 수위 NR'
                                   , connected_btn=self.btn_9, connected_btn_2=self.btn_8_1)

        self.btn_8.setObjectName("b12")
        self.btn_7_1 = Custom(self, x=670, y=1055, w=500, h=100, text='완화-05\n“원자로 냉각재 계통 감압“ 수행', type=1
                                     , msg_text='완화-05 “원자로 냉각재 계통 감압“ 수행'
                                     , msg_text2="완화-05 “원자로 냉각재 계통 감압“을 수행합니다."
                                     , connected_btn=self.btn_8)
        self.btn_7_1.setObjectName("b11")
        self.btn_7 = Custom(self, x=90, y=1030, w=360, h=150, text='RCS 압력\n<[P04] psig', type=3
                                   , msg_text="RCS 압력 확인"
                                   , msg_text2='RCS 압력 <[P04] psig'
                                   , msg_text3='RCS 압력'
                                   , connected_btn=self.btn_8, connected_btn_2=self.btn_7_1)
        self.btn_7.setObjectName("b10")
        self.btn_6_1 = Custom(self, x=670, y=865, w=500, h=100, text='완화-04\n“원자로 냉각재 계통 냉각수 주입“ 수행', type=1
                                     , msg_text='완화-04 “원자로 냉각재 계통 냉각수 주입“ 수행'
                                     , msg_text2="완화-04 “원자로 냉각재 계통 냉각수 주입“을 수행합니다."
                                     , connected_btn=self.btn_7)
        self.btn_6_1.setObjectName("b9")

        self.btn_6 = Custom(self, x=90, y=840, w=360, h=150, text='노심출구온도\n< [T01] °C', type=3
                                   , msg_text="노심출구온도 확인"
                                   , msg_text2='노심출구온도 < [T01] °C'
                                   , msg_text3='노심출구온도'
                                   , connected_btn=self.btn_7, connected_btn_2=self.btn_6_1)
        self.btn_6.setObjectName("b8")
        self.btn_5_1 = Custom(self, x=670, y=675, w=500, h=100, text='완화-03\n“격납건물내 수소 제어“ 수행', type=1
                                     , msg_text='완화-03 “격납건물내 수소 제어“ 수행'
                                     , msg_text2="완화-03 “격납건물내 수소 제어“를 수행합니다."
                                     , connected_btn=self.btn_6)
        self.btn_5_1.setObjectName("b8")
        self.btn_5 = Custom(self, x=90, y=650, w=360, h=150, text='격납건물 수소농도\n< [H02]%', type=3
                                   , msg_text="격납건물 수소농도 확인"
                                   , msg_text2='격납건물 수소농도 < [H02]%'
                                   , msg_text3='격납건물 수소농도'
                                   , connected_btn=self.btn_6, connected_btn_2=self.btn_5_1)
        self.btn_5.setObjectName("b7")
        self.btn_4_1 = Custom(self, x=670, y=485, w=500, h=100, text='완화-02\n“격납건물 상태제어“ 수행', type=1
                                     , msg_text='완화-02 “격납건물 상태제어“ 수행'
                                     , msg_text2="완화-02 “격납건물 상태제어“를 수행합니다."
                                     , connected_btn=self.btn_5)
        self.btn_4_1.setObjectName("b6")
        self.btn_4 = Custom(self, x=90, y=460, w=360, h=150, text='격납건물 압력\n< [P11] psig', type=3
                                   , msg_text="격납건물 압력 확인"
                                   , msg_text2='격납건물 압력 < [P11] psig'
                                   , msg_text3="격납건물 압력"
                                   , connected_btn=self.btn_5, connected_btn_2=self.btn_4_1)
        self.btn_4.setObjectName("b5")
        self.btn_3_1 = Custom(self, x=670, y=295, w=500, h=100, text='완화-01\n“핵분열생성물 방출 제어“ 수행', type=1
                                     , msg_text="완화-01 “핵분열생성물 방출 제어“ 수행"
                                     , msg_text2="완화-01 “핵분열생성물 방출 제어“를 수행합니다."
                                     , connected_btn=self.btn_4)
        self.btn_3_1.setObjectName("b4")

        self.btn_3 = Custom(self, x=90, y=270, w=360, h=150, text='발전소 부지 경계 선량\n< [R01]', type=3
                                   , msg_text="발전소 부지 경계 선량 확인"
                                   , msg_text2="발전소 부지 경계 선량 < [R01]"
                                   , msg_text3="발전소 부지 경계 선량"
                                   , connected_btn=self.btn_4, connected_btn_2=self.btn_3_1,b=3)
        self.btn_3.setObjectName("b3")

        self.btn_2 = Custom(self, x=70, y=130, w=400, h=90, text='안전 변수\nR02, P09, H04 감시 시작', type=0,
                                   msg_text='안전 변수 R02, P09, H04 감시 시작',
                                   msg_text2="안전 변수 R02, P09, H04 감시를 시작합니다", connected_btn=self.btn_3,b=2)

        self.btn_2.setObjectName("b2")

        self.btn_1 = Custom(self, x=70, y=30, w=400, h=80, text='TSC “완화” 절차서 사용시작',
                                   msg_text='TSC “완화” 절차서 사용시작', type=0,
                                   msg_text2='TSC “완화” 절차서를 시작합니다.',connected_btn=self.btn_2, b=1)

        # self.aa = MainLeft()
        # self.btn_1.installEventFilter(self.btn_1)
        self.btn_1.setObjectName("b1")
        # self.btn_1.setEnabled(True)
        # if self.btn_1
        # self.btn_1.shapePath
        # rect = QRect(0,0,100,100)
        # app.removeEventFilter()
        # self.setMouseTracking(True)

        # if((x>100 and x<400) and (y<60 and y>30)):
        #     print("ddd")
        #     app.installEventFilter(self.btn_1)
        # self.btn_2.setEnabled(False)


        # app.installEventFilter(self.btn_1)
        self.installEventFilter(self.btn_2)
        self.installEventFilter(self.btn_3)
        self.installEventFilter(self.btn_3_1)
        self.installEventFilter(self.btn_4)
        self.installEventFilter(self.btn_4_1)
        self.installEventFilter(self.btn_5)
        self.installEventFilter(self.btn_5_1)
        self.installEventFilter(self.btn_6)
        self.installEventFilter(self.btn_6_1)
        self.installEventFilter(self.btn_7)
        self.installEventFilter(self.btn_7_1)
        self.installEventFilter(self.btn_8)
        self.installEventFilter(self.btn_8_1)
        self.installEventFilter(self.btn_9)
        self.installEventFilter(self.btn_9_1)
        self.installEventFilter(self.btn_10)
        self.installEventFilter(self.btn_10_1)
        self.installEventFilter(self.btn_11)


        self.btn_1.clicked.connect(self.clicked1)
        self.btn_2.clicked.connect(self.clicked2)
        self.btn_3.clicked.connect(self.clicked3)
        self.btn_3_1.clicked.connect(self.clicked3_1)
        self.btn_4.clicked.connect(self.clicked4)
        self.btn_4_1.clicked.connect(self.clicked4_1)
        self.btn_5.clicked.connect(self.clicked5)
        self.btn_5_1.clicked.connect(self.clicked5_1)
        self.btn_6.clicked.connect(self.clicked6)
        self.btn_6_1.clicked.connect(self.clicked6_1)
        self.btn_7.clicked.connect(self.clicked7)
        self.btn_7_1.clicked.connect(self.clicked7_1)
        self.btn_8.clicked.connect(self.clicked8)
        self.btn_8_1.clicked.connect(self.clicked8_1) #완화 06 페이지
        self.btn_9.clicked.connect(self.clicked9)
        self.btn_9_1.clicked.connect(self.clicked9_1)
        self.btn_10.clicked.connect(self.clicked10)
        self.btn_10_1.clicked.connect(self.clicked10_1)
        self.btn_11.clicked.connect(self.clicked11)

        # ==============================================================================================================

    def clicked1(self):
        self.btn_1.shapes.setColor(QColor(0, 176, 218))
        self.btn_1.setObjectName("clicked")

        # popup
        self.popup = SubWindow(p_number=1,
                               p_title="TSC “완화” 절차서 사용시작",
                               p_content='\nTSC “완화” 절차서를 시작합니다.')
        show = self.popup.showModal()

        # 예
        if Flag.btn_clicked[1]:
            self.btn_1.shapes.setColor(self.color_clicked)
            self.btn_2.btn_clicked()  # 클릭한것처럼
            self.clicked2()

    def clicked2(self):
        self.btn_2.shapes.setColor(self.color_click)
        self.btn_2.setObjectName("clicked")

        # popup
        self.popup = SubWindow(p_number=2,
                               p_title="안전 변수 R02, P09, H04 감시 시작",
                               p_content='\n안전 변수 R02, P09, H04 감시를 시작합니다')
        show = self.popup.showModal()

        # 예
        if Flag.btn_clicked[2]:
            self.btn_2.shapes.setColor(self.color_clicked)
            self.btn_3.btn_clicked()  # 클릭한것처럼
            self.clicked3()

    def clicked3(self):
        self.btn_3.shapes.setColor(self.color_click)
        self.btn_3.setObjectName("clicked")

        self.shmem.get_shmem_val('')

        # popup
        self.popup = SubWindow(p_number=3,
                               p_title="발전소 부지 경계 선량 확인",
                               p_content="\n발전소 부지 경계 선량 < R[01]",
                               p_label1="현재 발전소 부지 경계 선량",
                               p_value1="현재 값")
        show = self.popup.showModal()

        #예
        if Flag.btn_clicked[3]:
            self.btn_3.shapes.setColor(self.color_clicked)
            self.btn_4.btn_clicked() #클릭한것처럼
            self.clicked4()
        #아니오
        else:
            self.btn_3.shapes.setColor(self.color_clicked)
            self.btn_3_1.btn_clicked() #클릭한것처럼
            self.clicked3_1()

    def clicked3_1(self):
        self.btn_3_1.shapes.setColor(QColor(0, 176, 218))
        self.btn_3_1.setObjectName("clicked")

        # popup
        self.popup = SubWindow(p_number=31,
                               p_title="완화-01 “핵분열생성물 방출 제어“ 수행",
                               p_content="\n완화-01 “핵분열생성물 방출 제어“를 수행합니다.")
        show = self.popup.showModal()

        # 예 - 새로운 page
        if Flag.btn_clicked_1[3]:
            self.btn_3_1.shapes.setColor(self.color_clicked)
            self.btn_4.btn_clicked()  # 클릭한것처럼
            self.clicked4()
            print("완화 01 페이지 open")
        # 아니오 - 새로운 페이지 없으면 일단 넘어가기
        else:
            self.btn_3_1.shapes.setColor(self.color_clicked)
            self.btn_4.btn_clicked()  # 클릭한것처럼
            self.clicked4()

    def clicked4(self):
        self.btn_4.shapes.setColor(QColor(0, 176, 218))
        self.btn_4.setObjectName("clicked")

        # popup
        self.popup = SubWindow(p_number=4,
                               p_title="격납건물 압력 확인",
                               p_content="\n격납건물 압력 < [P11] psig",
                               p_label1="현재 격납건물 압력",
                               p_value1="현재 값")#표에서 얻어오기
        show = self.popup.showModal()

        # 예
        if Flag.btn_clicked[4]:
            self.btn_4.shapes.setColor(self.color_clicked)
            self.btn_5.btn_clicked()  # 클릭한것처럼
            self.clicked5()
        # 아니오
        else:
            self.btn_4.shapes.setColor(self.color_clicked)
            self.btn_4_1.btn_clicked()  # 클릭한것처럼
            self.clicked4_1()

    def clicked4_1(self):
        self.btn_4_1.shapes.setColor(QColor(0, 176, 218))
        self.btn_4_1.setObjectName("clicked")

        # popup
        self.popup = SubWindow(p_number=41,
                               p_title="완화-02 “격납건물 상태제어“ 수행",
                               p_content="\n완화-02 “격납건물 상태제어“를 수행합니다.")
        show = self.popup.showModal()

        # 예 - 새로운 page
        if Flag.btn_clicked_1[4]:
            self.btn_4_1.shapes.setColor(self.color_clicked)
            self.btn_5.btn_clicked()  # 클릭한것처럼
            self.clicked5()
            print("완화 02 페이지 open")
        # 아니오 - 새로운 페이지 없으면 일단 넘어가기
        else:
            self.btn_4_1.shapes.setColor(self.color_clicked)
            self.btn_5.btn_clicked()  # 클릭한것처럼
            self.clicked5()

    def clicked5(self):
        self.btn_5.shapes.setColor(QColor(0, 176, 218))
        self.btn_5.setObjectName("clicked")
        Flag.PAGE1 = True
        # popup
        self.popup = SubWindow(p_number=5,
                               p_title="격납건물 수소농도 확인",
                               p_content="\n격납건물 수소농도 < [H02]%",
                               p_label1="현재 격납건물 수소농도",
                               p_value1="현재 값")  # 표에서 얻어오기
        show = self.popup.showModal()

        # 예
        if Flag.btn_clicked[5]:
            self.btn_5.shapes.setColor(self.color_clicked)
            self.btn_6.btn_clicked()  # 클릭한것처럼
            self.clicked6()
        # 아니오
        else:
            self.btn_5.shapes.setColor(self.color_clicked)
            self.btn_5_1.btn_clicked()  # 클릭한것처럼
            self.clicked5_1()

    def clicked5_1(self):
        self.btn_5_1.shapes.setColor(QColor(0, 176, 218))
        self.btn_5_1.setObjectName("clicked")
        Flag.PAGE1 = True
        # popup
        self.popup = SubWindow(p_number=51,
                               p_title="완화-03 “격납건물내 수소 제어“ 수행",
                               p_content="\n완화-03 “격납건물내 수소 제어“를 수행합니다.")
        show = self.popup.showModal()

        # 예 - 새로운 page
        if Flag.btn_clicked_1[5]:
            self.btn_5_1.shapes.setColor(self.color_clicked)
            self.btn_6.btn_clicked()  # 클릭한것처럼
            self.clicked6()
            print("완화 03 페이지 open")
        # 아니오 - 새로운 페이지 없으면 일단 넘어가기
        else:
            self.btn_5_1.shapes.setColor(self.color_clicked)
            self.btn_6.btn_clicked()  # 클릭한것처럼
            self.clicked6()

    def clicked6(self):
        self.btn_6.shapes.setColor(QColor(0, 176, 218))
        self.btn_6.setObjectName("clicked")

        # popup
        self.popup = SubWindow(p_number=6,
                               p_title="노심출구온도 확인",
                               p_content="\n노심출구온도 < [T01]°C",
                               p_label1="현재 노심출구온도",
                               p_value1="현재 값")  # 표에서 얻어오기
        show = self.popup.showModal()

        # 예
        if Flag.btn_clicked[6]:
            self.btn_6.shapes.setColor(self.color_clicked)
            self.btn_7.btn_clicked()  # 클릭한것처럼
            self.clicked7()
        # 아니오
        else:
            self.btn_6.shapes.setColor(self.color_clicked)
            self.btn_6_1.btn_clicked()  # 클릭한것처럼
            self.clicked6_1()

    def clicked6_1(self):
        self.btn_6_1.shapes.setColor(QColor(0, 176, 218))
        self.btn_6_1.setObjectName("clicked")

        # popup
        self.popup = SubWindow(p_number=61,
                               p_title="완화-04 “원자로 냉각재 계통 냉각수 주입“ 수행",
                               p_content="\n완화-04 “원자로 냉각재 계통 냉각수 주입“을 수행합니다.")
        show = self.popup.showModal()

        # 예 - 새로운 page
        if Flag.btn_clicked_1[6]:
            self.btn_6_1.shapes.setColor(self.color_clicked)
            self.btn_7.btn_clicked()  # 클릭한것처럼
            self.clicked7()
            print("완화 04 페이지 open")
        # 아니오 - 새로운 페이지 없으면 일단 넘어가기
        else:
            self.btn_6_1.shapes.setColor(self.color_clicked)
            self.btn_7.btn_clicked()  # 클릭한것처럼
            self.clicked7()

    def clicked7(self):
        self.btn_7.shapes.setColor(QColor(0, 176, 218))
        self.btn_7.setObjectName("clicked")

        # popup
        self.popup = SubWindow(p_number=7,
                               p_title="RCS 압력 확인",
                               p_content="\nRCS 압력 < [P04]psig",
                               p_label1="현재 RCS 압력",
                               p_value1="현재 값")  # 표에서 얻어오기
        show = self.popup.showModal()

        # 예
        if Flag.btn_clicked[7]:
            self.btn_7.shapes.setColor(self.color_clicked)
            self.btn_8.btn_clicked()  # 클릭한것처럼
            self.clicked8()
        # 아니오
        else:
            self.btn_7.shapes.setColor(self.color_clicked)
            self.btn_7_1.btn_clicked()  # 클릭한것처럼
            self.clicked7_1()

    def clicked7_1(self):
        self.btn_7_1.shapes.setColor(QColor(0, 176, 218))
        self.btn_7_1.setObjectName("clicked")

        # popup
        self.popup = SubWindow(p_number=71,
                               p_title="완화-05 “원자로 냉각재 계통 감압“ 수행",
                               p_content="\n완화-05 “원자로 냉각재 계통 감압“을 수행합니다.")
        show = self.popup.showModal()

        # 예 - 새로운 page
        if Flag.btn_clicked_1[7]:
            self.btn_7_1.shapes.setColor(self.color_clicked)
            self.btn_8.btn_clicked()  # 클릭한것처럼
            self.clicked8()
            print("완화 05 페이지 open")
        # 아니오 - 새로운 페이지 없으면 일단 넘어가기
        else:
            self.btn_7_1.shapes.setColor(self.color_clicked)
            self.btn_8.btn_clicked()  # 클릭한것처럼
            self.clicked8()

    def clicked8(self):
        self.btn_8.shapes.setColor(QColor(0, 176, 218))
        self.btn_8.setObjectName("clicked")
        # popup
        self.popup = SubWindow(p_number=8,
                               p_title="모든 증기발생기 수위 확인",
                               p_content="\n모든 증기발생기 수위 < [L01%] NR",
                               p_label1="SG 1 Level",
                               p_value1="현재 값",
                               p_label2="SG 2 Level",
                               p_value2="현재 값")  # 표에서 얻어오기
        show = self.popup.showModal()

        # 예
        if Flag.btn_clicked[8]:
            self.btn_8.shapes.setColor(self.color_clicked)
            self.btn_9.btn_clicked()  # 클릭한것처럼
            self.clicked9()
        # 아니오
        else:
            self.btn_8.shapes.setColor(self.color_clicked)
            self.btn_8_1.btn_clicked()  # 클릭한것처럼
            self.clicked8_1()

    def clicked8_1(self):
        self.btn_8_1.shapes.setColor(QColor(0, 176, 218))
        self.btn_8_1.setObjectName("clicked")

        # popup
        self.popup = SubWindow(p_number=81,
                               p_title="완화-06 “증기발생기 급수 주입“ 수행",
                               p_content="\n완화-06 “증기발생기 급수 주입“을 수행합니다.")
        show = self.popup.showModal()

        # 예 - 새로운 page
        if Flag.btn_clicked_1[8]:
            self.btn_8_1.shapes.setColor(self.color_clicked)
            # 완화 06 page open
            self.mitigation06 = MitigationWindow()
            self.mitigation06.show()
            # self.btn_9.btn_clicked()  # 클릭한것처럼

        # 아니오 - 새로운 페이지 없으면 일단 넘어가기
        else:
            self.btn_8_1.shapes.setColor(self.color_clicked)
            self.btn_9.btn_clicked()  # 클릭한것처럼
            self.clicked9()

    def clicked9(self):
        self.btn_9.shapes.setColor(QColor(0, 176, 218))
        self.btn_9.setObjectName("clicked")
        Flag.PAGE2 = True
        # popup
        self.popup = SubWindow(p_number=9,
                               p_title="격납건물 수위 확인",
                               p_content="\n격납건물 수위 > [L06] m",
                               p_label1="현재 격납건물 수위",
                               p_value1="현재 값")  # 표에서 얻어오기
        show = self.popup.showModal()

        # 예
        if Flag.btn_clicked[9]:
            self.btn_9.shapes.setColor(self.color_clicked)
            self.btn_10.btn_clicked()  # 클릭한것처럼
            self.clicked10()
        # 아니오
        else:
            self.btn_9.shapes.setColor(self.color_clicked)
            self.btn_9_1.btn_clicked()  # 클릭한것처럼
            self.clicked9_1()

    def clicked9_1(self):
        self.btn_9_1.shapes.setColor(QColor(0, 176, 218))
        self.btn_9_1.setObjectName("clicked")
        Flag.PAGE2 = True

        # popup
        self.popup = SubWindow(p_number=91,
                               p_title="완화-07 “격납건물 냉각수 주입“ 수행",
                               p_content="\n완화-07 “격납건물 냉각수 주입“을 수행합니다.")
        show = self.popup.showModal()

        # 예 - 새로운 page
        if Flag.btn_clicked_1[9]:
            self.btn_9_1.shapes.setColor(self.color_clicked)
            self.btn_10.btn_clicked()  # 클릭한것처럼
            self.clicked10()
            print("완화 07 페이지 open")
        # 아니오 - 새로운 페이지 없으면 일단 넘어가기
        else:
            self.btn_9_1.shapes.setColor(self.color_clicked)
            self.btn_10.btn_clicked()  # 클릭한것처럼
            self.clicked10()

    # 추가 설명 필요
    def clicked10(self):
        self.btn_10.shapes.setColor(QColor(0, 176, 218))
        self.btn_10.setObjectName("clicked")

    def clicked10_1(self):
        self.btn_10_1.shapes.setColor(QColor(0, 176, 218))
        self.btn_10_1.setObjectName("clicked")

    def clicked11(self):
        self.btn_11.shapes.setColor(QColor(0, 176, 218))
        self.btn_11.setObjectName("clicked")

    def btn_count(self):
        self.count = self.count+1

    def btn8_controller(self):
        if self.btn_8.isChecked():
            self.App.show()

    def paintEvent(self, event):
        p = QPainter(self)

        p.setPen(QPen(Qt.black))
        p.setFont(QFont('맑은 고딕', 14))
        p.drawLine(920, 370, 920, 440)
        p.drawText(470, 335, "아니오")
        p.drawText(240, 445, "예")

        p.drawLine(920, 530, 920, 630)

        p.drawText(470, 525, "아니오")
        p.drawText(240, 635, "예")

        p.drawLine(920, 720, 920, 820)

        p.drawText(470, 715, "아니오")
        p.drawText(240, 825, "예")

        p.drawLine(920, 910, 920, 1010)

        p.drawText(470, 905, "아니오")
        p.drawText(240, 1015, "예")

        p.drawLine(920, 1100, 920, 1200)

        p.drawText(470, 1095, "아니오")
        p.drawText(240, 1205, "예")

        p.drawLine(920, 1290, 920, 1390)

        p.drawText(470, 1285, "아니오")
        p.drawText(240, 1395, "예")

        p.drawLine(920, 1480, 920, 1580)

        p.drawText(470, 1475, "아니오")
        p.drawText(240, 1585, "예")

# 마름모 popup
class SubWindow(QDialog):
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

    def __init__(self, p_number=None, p_title = None, p_content = None, p_label1 = None, p_value1 = None, p_label2 = None, p_value2 = None):
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
        print(self.p_title)
        self.layout.addWidget(MyBar(self, p_number=self.p_number, p_title=self.p_title, p_content=self.p_content, p_label1=self.p_label1,
                                    p_value1=self.p_value1, p_label2=self.p_label2, p_value2=self.p_value2))
        # self.layout.addWidget(
        #     MyBar(self))

        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(self.qss)
        self.layout.addStretch(-1)
        self.setGeometry(100, 300, 550, 100)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pressing = False



    def onOKButtonClicked(self):
        print("오키")
        self.close()

    def onCancelButtonClicked(self):
        print("새로운창")

    def showModal(self):
        return super().exec_()


class MyBar(QWidget):
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
    """
    def __init__(self, parent, p_number=None, p_title = None, p_content = None, p_label1 = None, p_value1 = None, p_label2 = None, p_value2 = None):
    # def __init__(self,parent):
        super(MyBar, self).__init__()
        # self. cc = Custom.
        self.parent = parent
        self.setStyleSheet(self.qss)
        print(self.parent.width())
        self.p_number = p_number
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.title = QLabel(p_title)

        #
        self.title.setFixedHeight(40)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)

        self.title.setStyleSheet("""
            font-size: 14pt; 
            background-color: rgb(91,155,213);
            border: 2px solid rgb(0, 0, 0);       
            color: white;
        """)
        #

        self.label = QLabel(p_content)
        self.label.setObjectName("title")

        #테두리 제거용
        self.label.setStyleSheet("""
                margin : 3px;    
            """)
        self.label.setAlignment(Qt.AlignCenter)
        self.subsub = QHBoxLayout()
        self.subLayout = QHBoxLayout()
        self.layout.addWidget(self.label)

        if self.p_number != 1 and self.p_number!=2 and self.p_number!=10\
                and self.p_number != 31 and self.p_number!=41 and self.p_number!=51\
                and self.p_number != 61 and self.p_number!=71 and self.p_number!=81\
                and self.p_number != 91:
            self.tableWidget = QTableWidget()
            self.tableWidget.setStyleSheet("background: rgb(221, 221, 221);"
                                           "border: 0px solid rgb(0, 0, 0);")
            self.tableWidget.horizontalHeader().setVisible(False) #table 헤더 숨기기
            self.tableWidget.verticalHeader().setVisible(False)
            self.tableWidget.setContentsMargins(0, 0, 0, 0)
            if self.p_number == 8:
                self.tableWidget.setRowCount(2)
                self.tableWidget.setFixedSize(350, 60)

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

            self.tableWidget.setItem(0, 0, QTableWidgetItem(p_label1))
            self.tableWidget.setItem(0, 1, QTableWidgetItem(p_value1))
            self.tableWidget.setItem(1, 0, QTableWidgetItem(p_label2))
            self.tableWidget.setItem(1, 1, QTableWidgetItem(p_value2))
            self.tableWidget.setGeometry(30,30,30,30)

            # 테이블 정렬
            delegate = AlignDelegate()
            self.tableWidget.setItemDelegate(delegate)

            fnt = self.font()
            fnt.setPointSize(12)
            self.tableWidget.setFont(fnt)


            self.subsub.addWidget(self.tableWidget)
            self.layout.addLayout(self.subsub)


        self.btnOK = QPushButton("예")
        self.btnCancel = QPushButton("아니오")

        self.btnOK.setFixedSize(100, 35)
        self.btnCancel.setFixedSize(100, 35)

        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.btnCancel.clicked.connect(self.onCancelButtonClicked)
        self.subLayout.setContentsMargins(50, 30, 50, 30)

        self.subLayout.addWidget(self.btnOK)

        if self.p_number!=1 and self.p_number!=2 and self.p_number!=10:
            self.subLayout.addWidget(self.btnCancel)


        self.layout.addLayout(self.subLayout)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False

    def onOKButtonClicked(self):
        #flag
        for i in range(1,12):
            if self.p_number == i:
                Flag.btn_clicked[i] = True
            if self.p_number == i*10+1:
                Flag.btn_clicked_1[i] = True
            if self.p_number == i*100+1:
                Flag.btn_clicked[i] = True #SCROLL
                Flag.btn_clicked_1[i] = True

        self.setDisabled(True)
        self.parent.close()

    def onCancelButtonClicked(self):
        for i in range(1,12):
            if self.p_number == i * 100 + 1:
                Flag.btn_clicked[i] = True  # SCROLL
                Flag.btn_clicked_1[i] = True
        self.parent.close()
        print("새로운창")

    def showModal(self):
        return super().exec_()

    def resizeEvent(self, QResizeEvent):
        super(MyBar, self).resizeEvent(QResizeEvent)
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

    def btn_close_clicked(self):
        self.parent.close()

    def btn_max_clicked(self):
        self.parent.showMaximized()

    def btn_min_clicked(self):
        self.parent.showMinimized()

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter
if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MainLeft()
    window.show()
    flow = FlowChart()
    # if(flow.btn_1):
    # win = Custom(x=10, y=10, w=10,h=200)
    app.installEventFilter(flow.btn_1)
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
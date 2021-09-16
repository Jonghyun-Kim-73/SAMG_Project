import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Flag import Flag
from Mitigation_button import Custom
from Table_5 import table5
from Table_7 import table7
from Table_Na_1 import tableNa_1
from Table_Na_2 import tableNa_2
from Table_ga import tableGa
from arrow import Arrow

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

class MitigationMiddleArea_2L(QWidget):
    qss = """
        QWidget {
            background: rgb(128, 128, 128);   

        }

        QPushButton{
            background-color: rgb(221,221,221);
            border: 1px solid rgb(0,0,0);       
            font-size: 14pt;
            font-weight: bold
        }

    """

    def __init__(self, parent=None):
        super(MitigationMiddleArea_2L, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.setMouseTracking(True)
        # 카운트
        # 크기 조정
        self.setMinimumHeight(900 - 40)
        self.setMinimumWidth(1920)

        # 레이어 셋업 ====================================================================================================
        layout = QHBoxLayout(self)

        label1 = FlowChartArea(self)
        label1.setFixedWidth(1020)

        right = QVBoxLayout(self)
        # right.setContentsMargins(5,5,5,5)
        label2 = MitigationMiddleArea_2R()
        label2.setFixedWidth(860)
        right.addWidget(label2)

        right_bottom = QHBoxLayout()

        back = background()
        back.setFixedWidth(860)
        back.setFixedHeight(60)
        right_bottom.addWidget(back)

        right.addLayout(right_bottom)
        layout.addWidget(label1)
        layout.addLayout(right)
        self.setLayout(layout)

class FlowChartArea(QWidget):
    qss = """
        QWidget {
            background: rgb(221, 221, 221);
            border:0px;
        }
    """

    def __init__(self, parent=None):
        super(FlowChartArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.setMouseTracking(True)
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        flowchart = FlowChart()

        scroll.setWidget(flowchart)

        layout = QVBoxLayout()
        layout.addWidget(scroll)
        self.setLayout(layout)


class FlowChart(QWidget):
    qss = """
            QWidget {
                background: rgb(128, 128, 128);
                border: 0px solid rgb(0, 0, 0); 

            }
        """
    def __init__(self, parent=None):
        super(FlowChart, self).__init__()
        self.setGeometry(0, 0, 1300, 1100)  # 1900*(3/4) = 1425
        self.setStyleSheet(self.qss)
        self.color_clicked = QColor(128, 128, 128)
        self.color_click = QColor(0, 176, 218)
        self.posx = 0
        self.posy = 0
        # 커스텀버튼추가===================================================================================================
        # 하1
        self.line1 = Arrow(self, x=180, y=80, x2=180, y2=110, type=1)
        self.line1 = Arrow(self, x=180, y=190, x2=180, y2=220, type=1)
        self.line1 = Arrow(self, x=180, y=320, x2=180, y2=700, type=1)
        self.line1 = Arrow(self, x=180, y=820, x2=180, y2=850, type=1)

        # 오
        self.line1 = Arrow(self, x=930, y=495, x2=940, y2=495, type=3)

        # 하
        self.line1 = Arrow(self, x=480, y=275, x2=480, y2=330, type=1)
        self.line1 = Arrow(self, x=480, y=430, x2=480, y2=570, type=1)
        self.line1 = Arrow(self, x=780, y=385, x2=780, y2=440, type=1)

        # 커스텀버튼 type : 3 dia 2 cir 1 rec 0 round_rec

        self.btn_9 = Custom(self, x=30, y=860, w=300, h=70, text='Ⅲ 전략수행여부결정', type=0
                            , msg_text="격납건물 수위 확인"
                            , msg_text2='격납건물 수위 > [L06] m'
                            , msg_text3='격납건물 수위'
                            )
        self.btn_9.setObjectName("b9")
        self.btn_8 = Custom(self, x=950, y=470, w=200, h=50, text='제어-01로 이동', type=0
                            , msg_text="모든 증기발생기 수위 확인"
                            , msg_text2='모든 증기발생기 수위 > [L01%] NR'
                            , msg_text3='SG1 수위 NR'
                            , msg_text4='SG2 수위 NR'
                            , connected_btn=self.btn_9)
        self.btn_8.setObjectName("b8")
        self.btn_7 = Custom(self, x=30, y=710, w=300, h=110, text='3. 이용가능한 증기발생기\n급수 주입량이 붕괴열을\n제거하기에 적당한 가를\n결정한다',
                            type=4
                            , msg_text="RCS 압력 확인"
                            , msg_text2='RCS 압력 <[P04] psig'
                            , msg_text3='RCS 압력'
                            , connected_btn=self.btn_8)
        self.btn_7.setObjectName("b7")
        self.btn_6 = Custom(self, x=330, y=580, w=300, h=90, text='2. 증기발생기를 감압하기\n위한 유용한 수단을\n파악한다.', type=4
                            , msg_text="노심출구온도 확인"
                            , msg_text2='노심출구온도 < [T01] °C'
                            , msg_text3='노심출구온도'
                            , connected_btn=self.btn_7)
        self.btn_6.setObjectName("b6")
        self.btn_5 = Custom(self, x=630, y=450, w=300, h=90, text='1. 다. 증기발생기에 급수를\n주입할 수단이 전혀 없으면\n다음을 수행한다.', type=4
                            , msg_text="격납건물 수소농도 확인"
                            , msg_text2='격납건물 수소농도 < [H02]%'
                            , msg_text3='격납건물 수소농도'
                            , connected_btn=self.btn_6)
        self.btn_5.setObjectName("b5")
        self.btn_4 = Custom(self, x=330, y=340, w=300, h=90, text='1. 나. 증기발생기 저압 급수\n주입 경로의 이용가능성을\n확인한다.', type=4
                            , msg_text="격납건물 압력 확인"
                            , msg_text2='격납건물 압력 < [P11] psig'
                            , msg_text3="격납건물 압력"
                            , connected_btn=self.btn_5)
        self.btn_4.setObjectName("b4")
        self.btn_3 = Custom(self, x=30, y=230, w=300, h=90, text='1. 가. 증기발생기 고압 급수\n주입 경로의 이용가능성을\n확인한다.', type=4
                            , msg_text="발전소 부지 경계 선량 확인"
                            , msg_text2="발전소 부지 경계 선량 < [R01]"
                            , msg_text3="발전소 부지 경계 선량"
                            , connected_btn=self.btn_4)
        self.btn_3.setObjectName("b3")
        self.btn_2 = Custom(self, x=30, y=120, w=300, h=70, text='1. 증기발생기에 급수를 주입하기\n위한 유용한 수단을 파악한다.', type=0,
                            msg_text='안전 변수 R02, P09, H04 감시 시작',
                            msg_text2="안전 변수 R02, P09, H04 감시를 시작합니다", connected_btn=self.btn_3)
        self.btn_2.setObjectName("b2")
        self.btn_1 = Custom(self, x=30, y=10, w=300, h=70, text='Ⅰ 목적, 수행 조건 등',
                            msg_text='TSC “완화” 절차서 사용시작', type=0,
                            msg_text2='TSC “완화” 절차서를 시작합니다.', connected_btn=self.btn_2)
        self.btn_1.setObjectName("b1")

        self.installEventFilter(self.btn_2)
        self.installEventFilter(self.btn_3)
        self.installEventFilter(self.btn_4)
        self.installEventFilter(self.btn_5)
        self.installEventFilter(self.btn_6)
        self.installEventFilter(self.btn_7)
        self.installEventFilter(self.btn_8)
        self.installEventFilter(self.btn_9)

        self.btn_1.clicked.connect(self.clicked1)
        self.btn_2.clicked.connect(self.clicked2)
        self.btn_3.clicked.connect(self.clicked3)
        # self.btn_4.clicked.connect(self.clicked4)
        # self.btn_5.clicked.connect(self.clicked5)
        # self.btn_6.clicked.connect(self.clicked6)
        # self.btn_7.clicked.connect(self.clicked7)
        # self.btn_8.clicked.connect(self.clicked8)
        # self.btn_9.clicked.connect(self.clicked9)

        # ==============================================================================================================

        self.changetable = MitigationMiddleArea_2R()

        self.setMouseTracking(True)

    def clicked1(self):
        self.btn_1.shapes.setColor(QColor(0, 176, 218))
        self.btn_1.setObjectName("clicked")

        # popup
        self.popup = SubWindow(p_number=1,
                               p_title="Ⅰ 목적, 수행 조건 등",
                               p_content='\nⅠ 목적, 수행 조건 등을 시작합니다.')
        show = self.popup.showModal()
        # 예
        if Flag.m2_btn_clicked[1]:
            self.btn_1.shapes.setColor(self.color_clicked)
            self.btn_2.btn_clicked()  # 클릭한것처럼
            self.btn_2.setObjectName("clicked")
            self.btn_2.shapes.setColor(self.color_click)

    def clicked2(self):
        # popup
        self.popup = SubWindow(p_number=2,
                               p_title="안전 변수 R02, P09, H04 감시 시작",
                               p_content='\n안전 변수 R02, P09, H04 감시를 시작합니다')
        show = self.popup.showModal()

        # 예
        if Flag.m2_btn_clicked[2]:
            self.btn_2.shapes.setColor(self.color_clicked)
            self.btn_3.btn_clicked()  # 클릭한것처럼
            self.btn_3.setObjectName("clicked")
            self.btn_3.shapes.setColor(self.color_click)
            self.clicked3()

    #오른쪽 화면 리셋
    def clicked3(self):
        Flag.m2_btn_clicked[3] = True



    def paintEvent(self, event):
        p = QPainter(self)
        p.setPen(QPen(Qt.black))
        p.setFont(QFont('맑은 고딕', 14))
        p.drawLine(330, 275, 480, 275)
        p.drawLine(630, 385, 780, 385)
        p.drawLine(780, 540, 780, 560)
        p.drawLine(480, 560, 780, 560)
        p.drawLine(480, 670, 480, 690)
        p.drawLine(180, 690, 480, 690)

        if Flag.pg2_sat[3] and Flag.m2_page_num == 3:
            self.btn_3.shapes.setColor(self.color_clicked)
            self.btn_7.btn_clicked()  # 클릭한것처럼
            self.btn_7.setObjectName("clicked")
            self.btn_7.shapes.setColor(self.color_click)
        if Flag.pg2_dsat[3] and Flag.m2_page_num == 3:
            self.btn_3.shapes.setColor(self.color_clicked)
            self.btn_4.btn_clicked()  # 클릭한것처럼
            self.btn_4.setObjectName("clicked")
            self.btn_4.shapes.setColor(self.color_click)

        if Flag.pg2_sat[4] and Flag.m2_page_num == 4:
            self.btn_4.shapes.setColor(self.color_clicked)
            self.btn_6.btn_clicked()  # 클릭한것처럼
            self.btn_6.setObjectName("clicked")
            self.btn_6.shapes.setColor(self.color_click)
        if Flag.pg2_dsat[4] and Flag.m2_page_num == 4:
            self.btn_4.shapes.setColor(self.color_clicked)
            self.btn_5.btn_clicked()  # 클릭한것처럼
            self.btn_5.setObjectName("clicked")
            self.btn_5.shapes.setColor(self.color_click)

        if Flag.pg2_sat[5] and Flag.m2_page_num == 5:
            self.btn_5.shapes.setColor(self.color_clicked)
            self.btn_6.btn_clicked()  # 클릭한것처럼
            self.btn_6.setObjectName("clicked")
            self.btn_6.shapes.setColor(self.color_click)
        if Flag.pg2_dsat[5] and Flag.m2_page_num == 5:
            self.btn_5.shapes.setColor(self.color_clicked)
            self.btn_8.btn_clicked()  # 클릭한것처럼
            self.btn_8.setObjectName("clicked")
            self.btn_8.shapes.setColor(self.color_click)

        if Flag.pg2_sat[6] and Flag.m2_page_num == 6:
            self.btn_6.shapes.setColor(self.color_clicked)
            self.btn_7.btn_clicked()  # 클릭한것처럼
            self.btn_7.setObjectName("clicked")
            self.btn_7.shapes.setColor(self.color_click)
        if Flag.pg2_dsat[6] and Flag.m2_page_num == 6:
            self.btn_6.shapes.setColor(self.color_clicked)
            self.btn_7.btn_clicked()  # 클릭한것처럼
            self.btn_7.setObjectName("clicked")
            self.btn_7.shapes.setColor(self.color_click)

        if Flag.pg2_sat[7] and Flag.m2_page_num == 7:
            self.btn_7.shapes.setColor(self.color_clicked)
            self.btn_9.btn_clicked()  # 클릭한것처럼
            self.btn_9.setObjectName("clicked")
            self.btn_9.shapes.setColor(self.color_click)
        if Flag.pg2_dsat[7] and Flag.m2_page_num == 7:#병행추가
            self.btn_7.shapes.setColor(QColor(224, 255, 255))
            self.btn_9.btn_clicked()  # 클릭한것처럼
            self.btn_9.setObjectName("clicked")
            self.btn_9.shapes.setColor(self.color_click)



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

        self.layout.addWidget(MyBar(self, p_number=self.p_number, p_title=self.p_title, p_content=self.p_content, p_label1=self.p_label1,
                                    p_value1=self.p_value1, p_label2=self.p_label2, p_value2=self.p_value2))

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


        self.btnOK = QPushButton("예")
        self.btnCancel = QPushButton("아니오")

        self.btnOK.setFixedSize(100, 35)
        self.btnCancel.setFixedSize(100, 35)

        self.btnOK.clicked.connect(self.onOKButtonClicked)
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
        for i in range(1, 3):
            if self.p_number == i:
                Flag.m2_btn_clicked[i] = True

        self.setDisabled(True)
        self.parent.close()


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

#오른쪽 화면
class MitigationMiddleArea_2R(QWidget, QObject):
    qss = """
        QWidget {
            background: rgb(221, 221, 221);
        }
        QTableWidget {
            background: rgb(221, 221, 221);

        }
        QPushButton{
            background: rgb(221, 221, 221)
        }

    """

    def __init__(self, parent=None):
        super(MitigationMiddleArea_2R, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.central_widget = QStackedWidget()


        self.screen1 = tableNone()
        self.screen2 = tableGa()
        self.screen3 = tableNa_1()
        self.screen4 = tableNa_2()
        self.screen5 = table5()
        self.screen7 = table7()

        self.central_widget.addWidget(self.screen1)
        self.central_widget.addWidget(self.screen2)
        self.central_widget.addWidget(self.screen3)
        self.central_widget.addWidget(self.screen4)
        self.central_widget.addWidget(self.screen5)
        self.central_widget.addWidget(self.screen7)

        self.central_widget.setCurrentIndex(0)
        self.window_vbox = QVBoxLayout()

        self.window_vbox.setContentsMargins(0, 0, 0, 0)
        self.window_vbox.addWidget(self.central_widget)
        self.central_widget.update()
        self.setLayout(self.window_vbox)

    def paintEvent(self, e):
        if Flag.m2_btn_clicked[3]:
            self.central_widget.setCurrentIndex(1)
            Flag.m2_btn_clicked[3] = False
            Flag.m2_page_num = 3
        if Flag.m2_btn_clicked[4]:
            self.central_widget.setCurrentIndex(2)
            Flag.m2_btn_clicked[4] = False
            Flag.m2_page_num = 4
        if Flag.m2_btn_clicked[5]:
            self.central_widget.setCurrentIndex(3)
            Flag.m2_btn_clicked[5] = False
            Flag.m2_page_num = 5
        if Flag.m2_btn_clicked[6]:
            self.central_widget.setCurrentIndex(4)
            Flag.m2_btn_clicked[6] = False
            Flag.m2_page_num = 6
        if Flag.m2_btn_clicked[7]:
            self.central_widget.setCurrentIndex(5)
            Flag.m2_btn_clicked[7] = False
            Flag.m2_page_num = 7
        if Flag.m2_btn_clicked[8]:
            self.central_widget.setCurrentIndex(0)
            Flag.m2_btn_clicked[8] = False
            Flag.m2_page_num = 8
        if Flag.m2_btn_clicked[9]:
            self.central_widget.setCurrentIndex(0)
            Flag.m2_btn_clicked[9] = False
            Flag.m2_page_num = 9

        self.central_widget.update()

class tableNone(QWidget):
    def __init__(self, parent=None):
        super(tableNone, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent

class background(QWidget):
    qss = """
        QWidget {
            background: rgb(221, 221, 221);
        }
        QLabel {
            background: rgb(131, 131, 131);
            border-radius: 6px;
            color: rgb(255, 255, 255);
        }
        QTableWidget {
            background: rgb(221, 221, 221)
        }
        QPushButton{
            background: rgb(221, 221, 221)
        }
    """

    def __init__(self, parent=None):
        super(background, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        label3 = QPushButton("만족")
        label4 = QPushButton("불만족")
        self.label5 = QPushButton("병행")
        label3.setFixedSize(200, 40)
        label4.setFixedSize(200, 40)
        self.label5.setFixedSize(200, 40)
        label3.setCursor(QCursor(Qt.PointingHandCursor))
        label4.setCursor(QCursor(Qt.PointingHandCursor))
        self.label5.setCursor(QCursor(Qt.PointingHandCursor))
        label3.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")
        label4.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")
        self.label5.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")

        label3.clicked.connect(self.click_sat)
        label4.clicked.connect(self.click_dsat)
        self.label5.clicked.connect(self.click_dsat)

        self.right_bottom = QHBoxLayout()
        self.right_bottom.addWidget(label3)
        self.right_bottom.addWidget(label4)

        self.setLayout(self.right_bottom)


    def paintEvent(self, QPaintEvent):
        if Flag.m3_page_num == 7:
            self.right_bottom.addWidget(self.label5)
        self.update()

    def click_sat(self):
        if Flag.m2_page_num == 3:
            Flag.m2_btn_clicked[7] = True
            Flag.pg2_sat[3] = True
        if Flag.m2_page_num == 4:
            Flag.m2_btn_clicked[6] = True
            Flag.pg2_sat[4] = True
        if Flag.m2_page_num == 5:
            Flag.m2_btn_clicked[6] = True
            Flag.pg2_sat[5] = True
        if Flag.m2_page_num == 6:
            Flag.m2_btn_clicked[7] = True
            Flag.pg2_sat[6] = True
        if Flag.m2_page_num == 7:
            Flag.m2_btn_clicked[8] = True
            Flag.pg2_sat[7] = True
        print("만족")

    def click_dsat(self):
        if Flag.m2_page_num == 3:
            Flag.m2_btn_clicked[4] = True
            Flag.pg2_dsat[3] = True
        if Flag.m2_page_num == 4:
            Flag.m2_btn_clicked[5] = True
            Flag.pg2_dsat[4] = True
        if Flag.m2_page_num == 5:
            Flag.m2_btn_clicked[8] = True
            Flag.pg2_dsat[5] = True
        if Flag.m2_page_num == 6:
            Flag.m2_btn_clicked[7] = True
            Flag.pg2_dsat[6] = True
        if Flag.m2_page_num == 7:
            Flag.m2_btn_clicked[9] = True
            Flag.pg2_dsat[7] = True
        print("불만족")

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    app.setStyle("fusion")  # +++
    app.setStyleSheet(StyleSheet)
    window = MitigationMiddleArea_2L()
    window.show()
    flow = FlowChart()

    app.installEventFilter(flow.btn_1)
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
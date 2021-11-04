import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from CustomButton import CustomButton
from CustomPopup import CustomPopup
from Flag import Flag

from Table_5 import table5
from Table_7 import table7
from Table_Na_1 import tableNa_1
from Table_Na_2 import tableNa_2
from Table_ga import tableGa
from arrow import Arrow

class MitigationMiddleArea_2(QWidget):
        # QPushButton style - 만족 / 불만족
    qss = """
        QWidget {
            background: rgb(128, 128, 128);   
            border: 0px inset rgb(0, 0, 0);
        }
        QPushButton{
            background-color: rgb(221,221,221);
            border: 1px solid rgb(0,0,0);       
            font-size: 14pt;
            font-weight: bold
        }
    """

    def __init__(self, parent=None):
        super(MitigationMiddleArea_2, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.shmem = parent.shmem
        self.setStyleSheet(self.qss)

        # 크기 조정
        # self.setMinimumHeight(900 - 40)
        # self.setMinimumWidth(1920)

        # 레이어 셋업
        layout = QHBoxLayout(self)
        label1 = FlowChartArea(self)

        label2 = MitigationMiddleArea_2R(self)
        self.split_1 = QSplitter()
        self.split_1.addWidget(label1)
        self.split_1.addWidget(label2)
        self.split_1.setSizes([1045, 860])  # 슬라이드 초기 사이즈 지정
        layout.addWidget(self.split_1)
        layout.setContentsMargins(0,0,0,0)

        self.setLayout(layout)

class FlowChartArea(QWidget):
    qss = """
        QWidget {
            background: rgb(221, 221, 221);
        }
        QWidget#main {
            background: rgb(221, 221, 221);
            border:2px solid;
        }
    """

    def __init__(self, parent=None):
        super(FlowChartArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.setObjectName("main")
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        flowchart = FlowChart()
        scroll.setWidget(flowchart)
        layout = QVBoxLayout()
        layout.addWidget(scroll)
        self.setLayout(layout)

class FlowChart(QWidget):
    def __init__(self, parent=None):
        super(FlowChart, self).__init__()
        self.setGeometry(0, 0, 1300, 1100)  # 1900*(3/4) = 1425

        # Arrow
        self.line1 = Arrow(self, x=180, y=80, x2=180, y2=110, type=1)
        self.line1 = Arrow(self, x=180, y=210, x2=180, y2=240, type=1)
        self.line1 = Arrow(self, x=180, y=350, x2=180, y2=800, type=1)
        self.line1 = Arrow(self, x=180, y=920, x2=180, y2=960, type=1)
        self.line1 = Arrow(self, x=1010, y=585, x2=1040, y2=585, type=3)
        self.line1 = Arrow(self, x=520, y=305, x2=520, y2=380, type=1)
        self.line1 = Arrow(self, x=860, y=445, x2=860, y2=520, type=1)
        self.line1 = Arrow(self, x=520, y=500, x2=520, y2=660, type=1)

        # CustomButton
        self.btn_1 = CustomButton(self, page=2, num=1, x=30, y=10, w=300, h=70, text='Ⅰ 목적, 수행 조건 등', type=0)
        self.btn_2 = CustomButton(self, page=2, num=2, x=30, y=120, w=300, h=90, text='1. 증기발생기에 급수를 주입하기<br/>위한 유용한 수단을 파악한다.', type=0)
        self.btn_3 = CustomButton(self, page=2, num=3, x=30, y=250, w=300, h=110, text='1. 가. 증기발생기 고압 급수<br/>주입 경로의 이용가능성을<br/>확인한다.', type=3)
        self.btn_4 = CustomButton(self, page=2, num=4, x=370, y=390, w=300, h=110, text='1. 나. 증기발생기 저압 급수<br/>주입 경로의 이용가능성을<br/>확인한다.', type=3)
        self.btn_5 = CustomButton(self, page=2, num=5, x=710, y=530, w=300, h=110, text='1. 다. 증기발생기에 급수를<br/>주입할 수단이 전혀 없으면<br/>다음을 수행한다.', type=3)
        self.btn_6 = CustomButton(self, page=2, num=6, x=370, y=670, w=300, h=110, text='2. 증기발생기를 감압하기<br/>위한 유용한 수단을<br/>파악한다.', type=0)
        self.btn_7 = CustomButton(self, page=2, num=7, x=30, y=810, w=300, h=130, text='3. 이용가능한 증기발생기<br/>급수 주입량이 붕괴열을<br/>제거하기에 적당한 가를<br/>결정한다', type=0)
        self.btn_8 = CustomButton(self, page=2, num=8, x=1050, y=545, w=200, h=70, text='제어-01로 이동', type=0)
        self.btn_9 = CustomButton(self, page=2, num=9, x=30, y=970, w=300, h=70, text='Ⅲ 전략수행여부결정', type=0)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setPen(QPen(Qt.black))
        p.setFont(QFont('맑은 고딕', 14))
        p.drawLine(330, 305, 520, 305)
        p.drawLine(670, 445, 860, 445)
        p.drawLine(1010, 585, 1050, 585)
        p.drawLine(520, 655, 860, 655)
        p.drawLine(860, 640, 860, 655)
        p.drawLine(180, 795, 520, 795)
        p.drawLine(520, 780, 520, 795)

        self.update()

        # 버튼 클릭 이벤트
        if Flag.m2_btn_clicked[1]:
            Flag.m2_btn_clicked[1] = False
            self.btn_1.complete()
            Flag.color2[1] = 3
            Flag.m2_screen[1] = True
            # 현재 실행중인 버튼 병행처리
            current = self.together(1)
            self.change(current)

            # 다음 버튼 표시
            self.btn_2.color()
            Flag.color2[2] = 2

        if Flag.m2_btn_clicked[2]:
            Flag.m2_btn_clicked[2] = False
            self.btn_2.complete()
            Flag.color2[2] = 3
            Flag.m2_screen[2] = True
            # 현재 실행중인 버튼 병행처리
            current = self.together(2)
            self.change(current)

            # 다음 버튼 표시
            self.btn_3.color()
            Flag.color2[3] = 2

        if Flag.m2_btn_clicked[3]:
            Flag.m2_btn_clicked[3] = False
            self.btn_3.color()
            Flag.color2[3] = 2
            Flag.m2_screen[3] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(3)
            self.change(current)

        if Flag.m2_btn_clicked[4]:
            Flag.m2_btn_clicked[4] = False
            self.btn_4.color()
            Flag.color2[4] = 2
            Flag.m2_screen[4] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(4)
            self.change(current)

        if Flag.m2_btn_clicked[5]:
            Flag.m2_btn_clicked[5] = False
            self.btn_5.color()
            Flag.color2[5] = 2
            Flag.m2_screen[5] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(5)
            self.change(current)

        if Flag.m2_btn_clicked[6]:
            Flag.m2_btn_clicked[6] = False
            self.btn_6.color()
            Flag.color2[6] = 2
            Flag.m2_screen[6] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(6)
            self.change(current)

        if Flag.m2_btn_clicked[7]:
            Flag.m2_btn_clicked[7] = False
            self.btn_7.color()
            Flag.color2[7] = 2
            Flag.m2_screen[7] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(7)
            self.change(current)

        # 제어 01로 이동 -> 화면 닫힘
        if Flag.m2_btn_clicked[8]:
            Flag.m2_btn_clicked[8] = False
            self.btn_8.color()
            Flag.color2[8] = 2
            Flag.m2_screen[8] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(8)
            self.change(current)

            self.popup = CustomPopup(p_title="제어-01로 이동",
                                     p_content='\n제어-01로 이동하시겠습니까?')
            show = self.popup.showModal()
            if Flag.btn_popup_2_1:
                Flag.btn_popup_2_1 = False
                Flag.miti06_close = True

        # 3. 전략수행여부결정 -> Tab3으로 전환
        if Flag.m2_btn_clicked[9]:
            Flag.m2_btn_clicked[9] = False

            self.btn_9.color()
            Flag.color2[9] = 2
            Flag.m2_screen[9] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(9)
            self.change(current)

            self.popup = CustomPopup(p_title="Ⅲ.전략수행여부결정",
                                     p_content='\nⅢ.전략수행여부결정을 수행하시겠습니까?')
            show = self.popup.showModal()
            if Flag.btn_popup_2_2:
                Flag.btn_popup_2_2 = False
                self.btn_9.complete()
                Flag.color2[9] = 3
                Flag.miti06_btn[3] = True  # Tab3 전환

        # 만족 / 불만족 / 병행 처리
        if Flag.pg2_sat[3]:
            self.btn_3.complete()
            Flag.color2[3] = 3
            self.btn_7.color()
            Flag.color2[7] = 2
            Flag.pg2_sat[3] = False
        if Flag.pg2_dsat[3]:
            self.btn_3.complete()
            Flag.color2[3] = 3
            self.btn_4.color()
            Flag.color2[4] = 2
            Flag.pg2_dsat[3] = False
        if Flag.pg2_p[3]:
            self.btn_3.color2()
            Flag.color2[3] = 1
            self.btn_7.color()
            Flag.color2[7] = 2
            Flag.pg2_p[3] = False

        if Flag.pg2_sat[4]:
            self.btn_4.complete()
            Flag.color2[4] = 3
            self.btn_6.color()
            Flag.color2[6] = 2
            Flag.pg2_sat[4] = False
        if Flag.pg2_dsat[4]:
            self.btn_4.complete()
            Flag.color2[4] = 3
            self.btn_5.color()
            Flag.color2[5] = 2
            Flag.pg2_dsat[4] = False
        if Flag.pg2_p[4]:
            self.btn_4.color2()
            Flag.color2[4] = 1
            self.btn_6.color()
            Flag.color2[6] = 2
            Flag.pg2_p[4] = False

        if Flag.pg2_sat[5]:
            self.btn_5.complete()
            Flag.color2[5] = 3
            self.btn_6.color()
            Flag.color2[6] = 2
            Flag.pg2_sat[5] = False
        if Flag.pg2_dsat[5]:
            self.btn_5.complete()
            Flag.color2[5] = 3
            self.btn_8.color()
            Flag.color2[8] = 2
            Flag.pg2_dsat[8] = False
        if Flag.pg2_p[5]:
            self.btn_5.color2()
            Flag.color2[5] = 1
            self.btn_6.color()
            Flag.color2[6] = 2
            Flag.pg2_p[5] = False

        if Flag.pg2_sat[6]:
            self.btn_6.complete()
            Flag.color2[6] = 3
            self.btn_7.color()
            Flag.color2[7] = 2
            Flag.pg2_sat[6] = False
        if Flag.pg2_p[6]:
            self.btn_6.color2()
            Flag.color2[6] = 1
            self.btn_7.color()
            Flag.color2[7] = 2
            Flag.pg2_p[6] = False

        if Flag.pg2_sat[7]:
            self.btn_7.complete()
            Flag.color2[7] = 3
            self.btn_9.color()
            Flag.color2[9] = 2
            Flag.pg2_sat[7] = False
        if Flag.pg2_p[7]:
            self.btn_7.color2()
            Flag.color2[7] = 1
            self.btn_9.color()
            Flag.color2[9] = 2
            Flag.pg2_p[7] = False

    def together(self, me):
        for i in range(1, 10):
            if Flag.color2[i] == 2:  # 자기 자신 제외, 현재 진행중인 버튼 찾기
                if i == me:
                    pass
                else:
                    Flag.color2[i] = 1  # 병행처리
                    return i

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

# Right Page
class MitigationMiddleArea_2R(QWidget, QObject):
    qss = """
        QWidget#right1 {
            background: rgb(221, 221, 221);
            border : 2px solid
        }
        QWidget#right2 {
            background: rgb(221, 221, 221);
            border : 2px solid
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
        self.shmem = parent.shmem

        self.setStyleSheet(self.qss)
        self.central_widget = QStackedWidget()

        # screen 추가
        self.screen1 = tableNone()
        self.screen2 = tableGa()
        self.screen3 = tableNa_1()
        self.screen4 = table5()
        self.screen5 = tableNa_2()
        self.screen7 = table7(self)

        self.central_widget.addWidget(self.screen1)
        self.central_widget.addWidget(self.screen2)
        self.central_widget.addWidget(self.screen3)
        self.central_widget.addWidget(self.screen4)
        self.central_widget.addWidget(self.screen5)
        self.central_widget.addWidget(self.screen7)

        self.central_widget.setCurrentIndex(0)
        self.window_vbox = QVBoxLayout()
        back = background()

        self.central_widget.setObjectName("right1")
        back.setObjectName("right2")
        self.window_vbox.addWidget(self.central_widget)
        self.window_vbox.addWidget(back)
        self.central_widget.update()
        self.window_vbox.setContentsMargins(0,0,0,0)

        self.setLayout(self.window_vbox)

    def paintEvent(self, e):
        # 버튼 클릭 -> screen 전환
        if Flag.m2_screen[1]:
            self.central_widget.setCurrentIndex(0)
            Flag.m2_page_num = 1
            Flag.m2_screen[1] = False

        if Flag.m2_screen[2]:
            self.central_widget.setCurrentIndex(0)
            Flag.m2_page_num = 2
            Flag.m2_screen[2] = False

        if Flag.m2_screen[3]:
            self.central_widget.setCurrentIndex(1)
            Flag.m2_page_num = 3
            Flag.m2_screen[3] = False

        if Flag.m2_screen[4]:
            self.central_widget.setCurrentIndex(2)
            Flag.m2_screen[4] = False
            Flag.m2_page_num = 4

        if Flag.m2_screen[5]:
            self.central_widget.setCurrentIndex(3)
            Flag.m2_screen[5] = False
            Flag.m2_page_num = 5

        if Flag.m2_screen[6]:
            self.central_widget.setCurrentIndex(4)
            Flag.m2_screen[6] = False
            Flag.m2_page_num = 6

        if Flag.m2_screen[7]:
            self.central_widget.setCurrentIndex(5)
            Flag.m2_screen[7] = False
            Flag.m2_page_num = 7

        if Flag.m2_screen[8]:
            self.central_widget.setCurrentIndex(0)
            Flag.m2_screen[8] = False
            Flag.m2_page_num = 8

        if Flag.m2_screen[9]:
            self.central_widget.setCurrentIndex(0)
            Flag.m2_screen[9] = False
            Flag.m2_page_num = 9

        self.central_widget.update()

# 빈 page
class tableNone(QWidget):
    qss = """
               QWidget {
                   background: rgb(221, 221, 221);   
               }
           """
    def __init__(self, parent=None):
        super(tableNone, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(self.qss)
        self.parent = parent

# 만족 / 불만족 button page
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
        self.setStyleSheet(self.qss)
        self.btn_sat = QPushButton("만족")
        self.btn_dsat = QPushButton("불만족")
        self.btn_parallelism = QPushButton("병행")
        self.setFixedHeight(70)
        self.btn_sat.setFixedSize(200, 50)
        self.btn_dsat.setFixedSize(200, 50)
        self.btn_parallelism.setFixedSize(200, 50)

        self.btn_sat.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dsat.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_parallelism.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_sat.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")
        self.btn_dsat.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")
        self.btn_parallelism.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")

        self.btn_sat.clicked.connect(self.click_sat)
        self.btn_dsat.clicked.connect(self.click_dsat)
        self.btn_parallelism.clicked.connect(self.click_p)

        self.right_bottom = QHBoxLayout()
        self.right_bottom.addWidget(self.btn_sat)
        self.right_bottom.addWidget(self.btn_dsat)
        self.right_bottom.addWidget(self.btn_parallelism)

        self.setLayout(self.right_bottom)

    def paintEvent(self, QPaintEvent):
        # button show
        # print(Flag.m2_page_num)
        if Flag.m2_page_num == 3 or Flag.m2_page_num == 4 or Flag.m2_page_num == 5:
            self.btn_dsat.show()
        else:
            self.btn_dsat.hide()

        if Flag.m2_page_num == 3 or Flag.m2_page_num == 4 or Flag.m2_page_num == 5 or Flag.m2_page_num == 6 or Flag.m2_page_num == 7:
            self.btn_sat.show()
            if Flag.m2_page_num == 3 or Flag.m2_page_num == 4 or Flag.m2_page_num == 5:
                self.btn_dsat.show()
            self.btn_parallelism.show()
        else:
            self.btn_sat.hide()
            self.btn_dsat.hide()
            self.btn_parallelism.hide()
        self.update()

    def click_sat(self):
        # 만족 button click
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
            Flag.m2_btn_clicked[9] = True
            Flag.pg2_sat[7] = True

    def click_dsat(self):
        # 불만족 button click
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
            Flag.m2_btn_clicked[8] = True
            Flag.pg2_dsat[7] = True

    def click_p(self):
        # 병행 button click
        if Flag.m2_page_num == 3:
            Flag.m2_btn_clicked[7] = True
            Flag.pg2_p[3] = True
        if Flag.m2_page_num == 4:
            Flag.m2_btn_clicked[6] = True
            Flag.pg2_p[4] = True
        if Flag.m2_page_num == 5:
            Flag.m2_btn_clicked[6] = True
            Flag.pg2_p[5] = True
        if Flag.m2_page_num == 6:
            Flag.m2_btn_clicked[7] = True
            Flag.pg2_p[6] = True
        if Flag.m2_page_num == 7:
            Flag.m2_btn_clicked[9] = True
            Flag.pg2_p[7] = True

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = MitigationMiddleArea_2()
    window.show()
    flow = FlowChart()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
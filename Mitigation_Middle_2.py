import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from CustomButton import CustomButton
from Flag import Flag

from Table_5 import table5
from Table_7 import table7
from Table_Na_1 import tableNa_1
from Table_Na_2 import tableNa_2
from Table_ga import tableGa
from arrow import Arrow

StyleSheet = '''
QCheckBox {
    margin-left:24px;
    spacing: 5px;
    font-size:25px;
}

QCheckBox::indicator {
    width:  33px;
    height: 33px;
}

'''

class MitigationMiddleArea_2(QWidget):
        # QPushButton style - 만족 / 불만족
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
        super(MitigationMiddleArea_2, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 크기 조정
        self.setMinimumHeight(900 - 40)
        self.setMinimumWidth(1920)

        # 레이어 셋업 ====================================================================================================
        layout = QHBoxLayout(self)
        label1 = FlowChartArea(self)
        label1.setFixedWidth(1020)

        right = QVBoxLayout(self)
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
        # self.color_clicked = QColor(128, 128, 128)
        # self.color_click = QColor(0, 176, 218)

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
        self.btn_1 = CustomButton(self, page=2, num=1, x=30, y=10, w=300, h=70, text='Ⅰ 목적, 수행 조건 등', type=0,
                                  p_title="Ⅰ 목적, 수행 조건 등", p_content='\nⅠ 목적, 수행 조건 등을 시작합니다.')
        self.btn_2 = CustomButton(self, page=2, num=2, x=30, y=120, w=300, h=90, text='1. 증기발생기에 급수를 주입하기<br/>위한 유용한 수단을 파악한다.', type=0,
                                  p_title="안전 변수 R02, P09, H04 감시 시작", p_content='\n안전 변수 R02, P09, H04 감시를 시작합니다')
        self.btn_3 = CustomButton(self, page=2, num=3, x=30, y=250, w=300, h=110, text='1. 가. 증기발생기 고압 급수<br/>주입 경로의 이용가능성을<br/>확인한다.', type=3)
        self.btn_4 = CustomButton(self, page=2, num=4, x=370, y=390, w=300, h=110, text='1. 나. 증기발생기 저압 급수<br/>주입 경로의 이용가능성을<br/>확인한다.', type=3)
        self.btn_5 = CustomButton(self, page=2, num=5, x=710, y=530, w=300, h=110, text='1. 다. 증기발생기에 급수를<br/>주입할 수단이 전혀 없으면<br/>다음을 수행한다.', type=3)
        self.btn_6 = CustomButton(self, page=2, num=6, x=370, y=670, w=300, h=110, text='2. 증기발생기를 감압하기<br/>위한 유용한 수단을<br/>파악한다.', type=3)
        self.btn_7 = CustomButton(self, page=2, num=7, x=30, y=810, w=300, h=130, text='3. 이용가능한 증기발생기<br/>급수 주입량이 붕괴열을<br/>제거하기에 적당한 가를<br/>결정한다', type=3)
        self.btn_8 = CustomButton(self, page=2, num=8, x=1050, y=545, w=200, h=70, text='제어-01로 이동', type=0)
        self.btn_9 = CustomButton(self, page=2, num=9, x=30, y=970, w=300, h=70, text='Ⅲ 전략수행여부결정', type=0)

        #self.btn_1.color()




    # def clicked2(self):
    #     # popup
    #     # self.popup = SubWindow(p_number=2,
    #     #                        p_title="안전 변수 R02, P09, H04 감시 시작", p_content='\n안전 변수 R02, P09, H04 감시를 시작합니다')
    #     # show = self.popup.showModal()
    #
    #     # 예
    #     if Flag.m2_btn_clicked[2]:
    #         self.btn_2.shapes.setColor(self.color_clicked)
    #         self.btn_3.btn_clicked()  # 클릭한것처럼
    #         self.btn_3.setObjectName("clicked")
    #         self.btn_3.shapes.setColor(self.color_click)
    #         self.clicked3()

    # #오른쪽 화면 리셋
    # def clicked3(self):
    #     Flag.m2_btn_clicked[3] = True



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


        # 팝업 나오는 버튼
        if Flag.m2_btn_clicked[1]:
            self.btn_1.complete()
            self.btn_2.color()

        if Flag.m2_btn_clicked[2]:
            self.btn_2.complete()
            self.btn_3.color()
            Flag.m2_btn_clicked[3] = True

        # 만족 병행 페이지
        if Flag.pg2_sat[3] and Flag.m2_page_num == 3:
            Flag.m2_btn_clicked[1] = False
            Flag.m2_btn_clicked[2] = False
            Flag.m2_btn_clicked[3] = False
            self.btn_3.complete()
            self.btn_7.color()
        if Flag.pg2_dsat[3] and Flag.m2_page_num == 3:
            Flag.m2_btn_clicked[1] = False
            Flag.m2_btn_clicked[2] = False
            Flag.m2_btn_clicked[3] = False
            self.btn_3.complete()
            self.btn_4.color()

        if Flag.pg2_sat[4] and Flag.m2_page_num == 4:
            Flag.m2_btn_clicked[4] = False
            self.btn_4.complete()
            self.btn_6.color()
        if Flag.pg2_dsat[4] and Flag.m2_page_num == 4:
            Flag.m2_btn_clicked[4] = False
            self.btn_4.complete()
            self.btn_5.color()

        if Flag.pg2_sat[5] and Flag.m2_page_num == 5:
            Flag.m2_btn_clicked[5] = False
            self.btn_5.complete()
            self.btn_6.color()
        if Flag.pg2_dsat[5] and Flag.m2_page_num == 5:
            Flag.m2_btn_clicked[5] = False
            self.btn_5.complete()
            self.btn_8.color()

        if Flag.pg2_sat[6] and Flag.m2_page_num == 6:
            Flag.m2_btn_clicked[6] = False
            self.btn_6.complete()
            self.btn_7.color()
        if Flag.pg2_dsat[6] and Flag.m2_page_num == 6:
            Flag.m2_btn_clicked[6] = False
            self.btn_7.complete()
            self.btn_7.color()

        if Flag.pg2_sat[7] and Flag.m2_page_num == 7:
            Flag.m2_btn_clicked[7] = False
            self.btn_9.complete()
            self.btn_9.color()
        if Flag.pg2_dsat[7] and Flag.m2_page_num == 7:
            Flag.m2_btn_clicked[7] = False
            self.btn_9.complete()
            self.btn_9.color()
        if Flag.pg2_p[7]  and Flag.m2_page_num == 7:
            Flag.m2_btn_clicked[7] = False
            self.btn_7.color2()
            self.btn_9.color()

        # 화면 update


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
            Flag.m2_page_num = 3
            Flag.m2_btn_clicked[3] = False

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
        self.setStyleSheet(self.qss)
        btn_sat = QPushButton("만족")
        btn_dsat = QPushButton("불만족")
        self.btn_parallelism = QPushButton("병행")

        btn_sat.setFixedSize(200, 40)
        btn_dsat.setFixedSize(200, 40)
        self.btn_parallelism.setFixedSize(200, 40)

        btn_sat.setCursor(QCursor(Qt.PointingHandCursor))
        btn_dsat.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_parallelism.setCursor(QCursor(Qt.PointingHandCursor))

        btn_sat.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")
        btn_dsat.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")
        self.btn_parallelism.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")

        btn_sat.clicked.connect(self.click_sat)
        btn_dsat.clicked.connect(self.click_dsat)
        self.btn_parallelism.clicked.connect(self.click_p)

        self.right_bottom = QHBoxLayout()
        self.right_bottom.addWidget(btn_sat)
        self.right_bottom.addWidget(btn_dsat)

        self.setLayout(self.right_bottom)

    def paintEvent(self, QPaintEvent):
        if Flag.m2_page_num == 7:
            self.right_bottom.addWidget(self.btn_parallelism)
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

    def click_p(self):
        if Flag.m2_page_num == 7:
            Flag.m2_btn_clicked[9] = True
            Flag.pg2_p[7] = True
class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    app.setStyle("fusion")  # +++
    app.setStyleSheet(StyleSheet)
    window = MitigationMiddleArea_2()
    window.show()
    flow = FlowChart()

    # app.installEventFilter(flow.btn_1)
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
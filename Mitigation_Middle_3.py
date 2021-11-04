import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from CustomPopup import CustomPopup
from Flag import Flag
from CustomButton import CustomButton

from Table_3_2 import table_3_2
from Table_3_3 import table_3_3
from Table_3_4 import table_3_4
from Table_3_5 import table_3_5
from Table_3_6 import table_3_6
from arrow import Arrow

class MitigationMiddleArea_3(QWidget):
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
        super(MitigationMiddleArea_3, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.shmem = parent.shmem
        self.setStyleSheet(self.qss)

        # 레이어 셋업
        layout = QHBoxLayout(self)
        label1 = FlowChartArea(self)
        label2 = MitigationMiddleArea_3R()

        self.split_1 = QSplitter()
        self.split_1.addWidget(label1)
        self.split_1.addWidget(label2)
        self.split_1.setSizes([1045, 860])  # 슬라이드 초기 사이즈 지정
        layout.addWidget(self.split_1)
        layout.setContentsMargins(0, 0, 0, 0)

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
        self.setGeometry(0, 0, 1000, 800)  # 1900*(3/4) = 1425

        # Arrow
        self.line1 = Arrow(self, x=180, y=80, x2=180, y2=110, type=1)
        self.line1 = Arrow(self, x=180, y=190, x2=180, y2=250, type=1)
        self.line1 = Arrow(self, x=180, y=320, x2=180, y2=370, type=1)
        self.line1 = Arrow(self, x=180, y=480, x2=180, y2=670, type=1)
        self.line1 = Arrow(self, x=540, y=475, x2=540, y2=510, type=1)
        self.line1 = Arrow(self, x=300, y=435, x2=380, y2=435, type=3)
        self.line1 = Arrow(self, x=670, y=575, x2=740, y2=575, type=3)

        # CustomButton
        self.btn_1 = CustomButton(self, page=3, num=1, x=30, y=20, w=300, h=70, text='Ⅱ.이용가능수단확인', type=0)
        self.btn_2 = CustomButton(self, page=3, num=2, x=30, y=120, w=300, h=110, text='4. 증기발생기 급수 주입에<br/>의한 부정적인 영향을<br/>파악하고 평가한다.', type=0)
        self.btn_3 = CustomButton(self, page=3, num=3, x=30, y=260, w=300, h=90, text='4.가. 발생가능한 부정적<br/>영향을 파악하고 평가한다.', type=0)
        self.btn_4 = CustomButton(self, page=3, num=4, x=30, y=380, w=300, h=110, text='4.나. 부정적 영향이<br/>문제되지 않는다고 판단되면<br/>단계 6으로 간다.', type=3)
        self.btn_5 = CustomButton(self, page=3, num=5, x=390, y=385, w=300, h=110, text='4.다. 부정적 영향을<br/>완화하기 위한 조치들을<br/>평가한다.', type=0)
        self.btn_6 = CustomButton(self, page=3, num=6, x=390, y=520, w=300, h=110, text='5. 증기발생기 급수<br/>주입 실시 여부를<br/>결정한다.', type=3)
        self.btn_7 = CustomButton(self, page=3, num=7, x=750, y=540, w=200, h=70, text='제어-01로 이동', type=0)
        self.btn_8 = CustomButton(self, page=3, num=8, x=30, y=680, w=300, h=70, text='Ⅳ.전략수행방법결정', type=0)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setPen(QPen(Qt.black))
        p.setFont(QFont('맑은 고딕', 14))
        p.drawLine(540, 610, 540, 655)
        p.drawLine(180, 655, 540, 655)

        self.update()

        # 버튼 클릭 이벤트
        if Flag.m3_btn_clicked[1]:
            Flag.m3_btn_clicked[1] = False
            self.btn_1.complete()
            Flag.color3[1] = 3
            Flag.m3_screen[1] = True
            # 현재 실행중인 버튼 병행처리
            current = self.together(1)
            self.change(current)

            # 다음 버튼 표시
            self.btn_2.color()
            Flag.color3[2] = 2

        if Flag.m3_btn_clicked[2]:
            Flag.m3_btn_clicked[2] = False
            self.btn_2.color()
            Flag.color3[2] = 2
            Flag.m3_screen[2] = True
            # 현재 실행중인 버튼 병행처리
            current = self.together(2)
            self.change(current)

        if Flag.m3_btn_clicked[3]:
            Flag.m3_btn_clicked[3] = False
            self.btn_3.color()
            Flag.color3[3] = 2
            Flag.m3_screen[3] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(3)
            self.change(current)

        if Flag.m3_btn_clicked[4]:
            Flag.m3_btn_clicked[4] = False
            self.btn_4.color()
            Flag.color3[4] = 2
            Flag.m3_screen[4] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(4)
            self.change(current)

        if Flag.m3_btn_clicked[5]:
            Flag.m3_btn_clicked[5] = False
            self.btn_5.color()
            Flag.color3[5] = 2
            Flag.m3_screen[5] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(5)
            self.change(current)

        if Flag.m3_btn_clicked[6]:
            Flag.m3_btn_clicked[6] = False
            self.btn_6.color()
            Flag.color3[6] = 2
            Flag.m3_screen[6] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(6)
            self.change(current)

        if Flag.m3_btn_clicked[7]:
            Flag.m3_btn_clicked[7] = False
            self.btn_7.color()
            Flag.color3[7] = 2
            Flag.m3_screen[7] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(7)
            self.change(current)

            self.popup = CustomPopup(p_title="제어-01로 이동",
                                     p_content='\n제어-01로 이동하시겠습니까?')
            show = self.popup.showModal()
            if Flag.btn_popup_3_1:
                Flag.btn_popup_3_1 = False
                Flag.miti06_close = True

        # 4. 전략수행방법결정 -> Tab4으로 전환
        if Flag.m3_btn_clicked[8]:
            Flag.m3_btn_clicked[8] = False

            self.btn_8.color()
            Flag.color3[8] = 2
            Flag.m3_screen[8] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(8)
            self.change(current)

            self.popup = CustomPopup(p_title="Ⅳ.전략수행방법결정",
                                     p_content='\nⅣ.전략수행방법결정을 수행하시겠습니까?')
            show = self.popup.showModal()
            if Flag.btn_popup_3_2:
                Flag.btn_popup_3_2 = False
                self.btn_8.complete()
                Flag.color3[8] = 3
                Flag.miti06_btn[4] = True  # Tab4 전환


        # 만족 / 불만족 / 병행 처리
        if Flag.pg3_sat[2]:
            self.btn_2.complete()
            Flag.color3[3] = 3
            self.btn_3.color()
            Flag.color3[3] = 2
            Flag.pg3_sat[2] = False
        if Flag.pg3_p[2]:
            self.btn_2.color2()
            Flag.color3[2] = 1
            self.btn_3.color()
            Flag.color3[3] = 2
            Flag.pg3_p[2] = False

        if Flag.pg3_sat[3]:
            self.btn_3.complete()
            Flag.color3[3] = 3
            self.btn_4.color()
            Flag.color3[4] = 2
            Flag.pg3_sat[3] = False
        if Flag.pg3_p[3]:
            self.btn_3.color2()
            Flag.color3[3] = 1
            self.btn_4.color()
            Flag.color3[4] = 2
            Flag.pg3_p[3] = False

        if Flag.pg3_sat[4]:
            self.btn_4.complete()
            Flag.color3[4] = 3
            self.btn_8.color()
            Flag.color3[8] = 2
            Flag.pg3_sat[4] = False
        if Flag.pg3_dsat[4]:
            self.btn_4.complete()
            Flag.color3[4] = 3
            self.btn_5.color()
            Flag.color3[5] = 2
            Flag.pg3_dsat[4] = False
        if Flag.pg3_p[4]:
            self.btn_4.color2()
            Flag.color3[4] = 1
            self.btn_8.color()
            Flag.color3[8] = 2
            Flag.pg3_p[4] = False

        if Flag.pg3_sat[5]:
            self.btn_5.complete()
            Flag.color3[5] = 3
            self.btn_6.color()
            Flag.color3[6] = 2
            Flag.pg3_sat[5] = False
        if Flag.pg3_p[5]:
            self.btn_5.color2()
            Flag.color3[5] = 1
            self.btn_6.color()
            Flag.color3[6] = 2
            Flag.pg3_p[5] = False

        if Flag.pg3_sat[6]:
            self.btn_6.complete()
            Flag.color3[6] = 3
            self.btn_8.color()
            Flag.color3[8] = 2
            Flag.pg3_sat[6] = False
        if Flag.pg3_dsat[6]:
            self.btn_6.complete()
            Flag.color3[6] = 3
            self.btn_7.color()
            Flag.color3[7] = 2
            Flag.pg3_dsat[6] = False
        if Flag.pg3_p[6]:
            self.btn_6.color2()
            Flag.color3[6] = 1
            self.btn_8.color()
            Flag.color3[8] = 2
            Flag.pg3_p[6] = False

    def together(self, me):
        for i in range(1, 9):
            if Flag.color3[i] == 2:  # 자기 자신 제외, 현재 진행중인 버튼 찾기
                if i == me:
                    pass
                else:
                    Flag.color3[i] = 1  # 병행처리
                    return i

    def change(self, find):
        if find == 1:
            self.btn_1.color2()
        elif find == 2:
            self.btn_2.color2()
        elif find == 3:
            self.btn_3.color2()
        elif find == 4:
            self.btn_4.color2()
        elif find == 5:
            self.btn_5.color2()
        elif find == 6:
            self.btn_6.color2()
        elif find == 7:
            self.btn_7.color2()
        elif find == 8:
            self.btn_8.color2()

# Right Page
class MitigationMiddleArea_3R(QWidget, QObject):
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
        super(MitigationMiddleArea_3R, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.central_widget = QStackedWidget()

        # screen 추가
        self.screen1 = tableNone()
        self.screen2 = table_3_2()
        self.screen3 = table_3_3()
        self.screen4 = table_3_4()
        self.screen5 = table_3_5()
        self.screen6 = table_3_6()

        self.central_widget.addWidget(self.screen1)
        self.central_widget.addWidget(self.screen2)
        self.central_widget.addWidget(self.screen3)
        self.central_widget.addWidget(self.screen4)
        self.central_widget.addWidget(self.screen5)
        self.central_widget.addWidget(self.screen6)

        self.central_widget.setCurrentIndex(0)
        self.window_vbox = QVBoxLayout()
        back = background()

        self.central_widget.setObjectName("right1")
        back.setObjectName("right2")
        self.window_vbox.addWidget(self.central_widget)
        self.window_vbox.addWidget(back)
        self.central_widget.update()
        self.window_vbox.setContentsMargins(0, 0, 0, 0)

        self.setLayout(self.window_vbox)

    def paintEvent(self, e):
        # 버튼 클릭 -> screen 전환
        if Flag.m3_btn_clicked[1]:
            self.central_widget.setCurrentIndex(0)
            Flag.m3_page_num = 1
            Flag.m3_screen[1] = False

        if Flag.m3_btn_clicked[2]:
            self.central_widget.setCurrentIndex(1)
            Flag.m3_page_num = 2
            Flag.m3_screen[2] = False

        if Flag.m3_btn_clicked[3]:
            self.central_widget.setCurrentIndex(2)
            Flag.m3_page_num = 3
            Flag.m3_screen[3] = False

        if Flag.m3_btn_clicked[4]:
            self.central_widget.setCurrentIndex(3)
            Flag.m3_screen[4] = False
            Flag.m3_page_num = 4

        if Flag.m3_btn_clicked[5]:
            self.central_widget.setCurrentIndex(4)
            Flag.m3_screen[5] = False
            Flag.m3_page_num = 5

        if Flag.m3_btn_clicked[6]:
            self.central_widget.setCurrentIndex(5)
            Flag.m3_screen[6] = False
            Flag.m3_page_num = 6

        if Flag.m3_btn_clicked[7]:
            self.central_widget.setCurrentIndex(0)
            Flag.m3_screen[7] = False
            Flag.m3_page_num = 7

        if Flag.m3_btn_clicked[8]:
            self.central_widget.setCurrentIndex(0)
            Flag.m3_screen[8] = False
            Flag.m3_page_num = 8

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
        # 만족 button 추가
        if Flag.m3_page_num in [2,3,4,5,6]:
            self.btn_sat.show()
            self.btn_parallelism.show()

        else:
            self.btn_sat.hide()
            self.btn_parallelism.hide()

        # 불만족 button 추가
        if Flag.m3_page_num == 4 or Flag.m3_page_num == 6:
            self.btn_dsat.show()
        else:
            self.btn_dsat.hide()
        self.update()

    def click_sat(self):
        # 만족 button click
        if Flag.m3_page_num == 2:
            Flag.m3_btn_clicked[3] = True
            Flag.pg3_sat[2] = True
        if Flag.m3_page_num == 3:
            Flag.m3_btn_clicked[4] = True
            Flag.pg3_sat[3] = True
        if Flag.m3_page_num == 4:
            Flag.m3_btn_clicked[8] = True
            Flag.pg3_sat[4] = True
        if Flag.m3_page_num == 5:
            Flag.m3_btn_clicked[6] = True
            Flag.pg3_sat[5] = True
        if Flag.m3_page_num == 6:
            Flag.m3_btn_clicked[8] = True
            Flag.pg3_sat[6] = True

    def click_dsat(self):
        # 불만족 button click
        if Flag.m3_page_num == 4:
            Flag.m3_btn_clicked[5] = True
            Flag.pg3_dsat[4] = True
        if Flag.m3_page_num == 6:
            Flag.m3_btn_clicked[7] = True
            Flag.pg3_dsat[6] = True

    def click_p(self):
        # 병행 button click
        if Flag.m3_page_num == 2:
            Flag.m3_btn_clicked[3] = True
            Flag.pg3_p[2] = True
        if Flag.m3_page_num == 3:
            Flag.m3_btn_clicked[4] = True
            Flag.pg3_p[3] = True
        if Flag.m3_page_num == 4:
            Flag.m3_btn_clicked[8] = True
            Flag.pg3_p[4] = True
        if Flag.m3_page_num == 5:
            Flag.m3_btn_clicked[6] = True
            Flag.pg3_p[5] = True
        if Flag.m3_page_num == 6:
            Flag.m3_btn_clicked[8] = True
            Flag.pg3_p[6] = True

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = MitigationMiddleArea_3()
    window.show()
    flow = FlowChart()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from CustomPopup import CustomPopup
from Flag import Flag
from CustomButton import CustomButton

from Table_6_2 import table_6_2
from Table_6_3 import table_6_3
from Table_6_4 import table_6_4
from Table_6_5 import table_6_5
from Table_6_6 import table_6_6
from Table_6_7 import table_6_7
from Table_6_8 import table_6_8
from arrow import Arrow

class MitigationMiddleArea_6(QWidget):
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
        super(MitigationMiddleArea_6, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.shmem = parent.shmem
        self.setStyleSheet(self.qss)

        # 레이어 셋업
        layout = QHBoxLayout(self)
        label1 = FlowChartArea(self)

        label2 = MitigationMiddleArea_6R()

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
        self.setGeometry(0, 0, 1000, 1300)  # 1900*(3/4) = 1425

        # Arrow
        self.line1 = Arrow(self, x=180, y=80, x2=180, y2=100, type=1)
        self.line1 = Arrow(self, x=180, y=210, x2=180, y2=240, type=1)
        self.line1 = Arrow(self, x=180, y=330, x2=180, y2=360, type=1)
        self.line1 = Arrow(self, x=180, y=490, x2=180, y2=520, type=1)
        self.line1 = Arrow(self, x=180, y=610, x2=180, y2=640, type=1)
        self.line1 = Arrow(self, x=180, y=730, x2=180, y2=760, type=1)
        self.line1 = Arrow(self, x=180, y=870, x2=180, y2=900, type=1)
        self.line1 = Arrow(self, x=180, y=1010, x2=180, y2=1040, type=1)
        self.line1 = Arrow(self, x=180, y=1170, x2=180, y2=1200, type=1)

        # CustomButton
        self.btn_1 = CustomButton(self, page=6, num=1, x=30, y=10, w=300, h=70, text='Ⅵ.전략종결', type=0)
        self.btn_2 = CustomButton(self, page=6, num=2, x=30, y=110, w=300, h=110, text='12. 증기발생기 급수\n주입으로 인한\n장기관심사항을 확인한다.', type=0)
        self.btn_3 = CustomButton(self, page=6, num=3, x=30, y=250, w=300, h=90, text=' 가. 장기 관심사항들은\n첨부 E를 참조한다.', type=0)
        self.btn_4 = CustomButton(self, page=6, num=4, x=30, y=370, w=300, h=130, text=' 나. 장기 관심사항을\n감시하기 위한 다른\n변수들이 있는지\n파악한다.', type=0)
        self.btn_5 = CustomButton(self, page=6, num=5, x=30, y=530, w=300, h=90, text=' 다. 추가적인 장기\n관심사항들을 파악한다.', type=0)
        self.btn_6 = CustomButton(self, page=6, num=6, x=30, y=650, w=300, h=90, text=' 라. 가능한 회복 조치를\n평가한다.', type=0)
        self.btn_7 = CustomButton(self, page=6, num=7, x=30, y=770, w=300, h=110, text='마. 복구된 기기들을\n사용할 필요가 있는가\n평가한다.', type=0)
        self.btn_8 = CustomButton(self, page=6, num=8, x=30, y=910, w=300, h=110, text='바. 회복조치를\n수행하도록 주제어실에\n지시한다.', type=0)
        self.btn_9 = CustomButton(self, page=6, num=9, x=30, y=1050, w=300, h=130, text='13. 전략수행 제어도 또는\n이전략 수행 직전에\n수행중이든 전략으로\n되돌아간다.', type=0)
        self.btn_10 = CustomButton(self, page=6, num=10, x=30, y=1210, w=300, h=70, text='제어-01', type=0)


    def paintEvent(self, event):
        p = QPainter(self)
        p.setPen(QPen(Qt.black))
        p.setFont(QFont('맑은 고딕', 14))

        self.update()

        # 버튼 클릭 이벤트
        if Flag.m6_btn_clicked[1]:
            Flag.m6_btn_clicked[1] = False
            self.btn_1.complete()
            Flag.color6[1] = 3
            Flag.m6_screen[1] = True
            # 현재 실행중인 버튼 병행처리
            current = self.together(1)
            self.change(current)

            # 다음 버튼 표시
            self.btn_2.color()
            Flag.color6[2] = 2

        if Flag.m6_btn_clicked[2]:
            Flag.m6_btn_clicked[2] = False
            self.btn_2.color()
            Flag.color6[2] = 2
            Flag.m6_screen[2] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(2)
            self.change(current)

        if Flag.m6_btn_clicked[3]:
            Flag.m6_btn_clicked[3] = False
            self.btn_3.color()
            Flag.color6[3] = 2
            Flag.m6_screen[3] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(3)
            self.change(current)

        if Flag.m6_btn_clicked[4]:
            Flag.m6_btn_clicked[4] = False
            self.btn_4.color()
            Flag.color6[4] = 2
            Flag.m6_screen[4] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(4)
            self.change(current)

        if Flag.m6_btn_clicked[5]:
            Flag.m6_btn_clicked[5] = False
            self.btn_5.color()
            Flag.color6[5] = 2
            Flag.m6_screen[5] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(5)
            self.change(current)

        if Flag.m6_btn_clicked[6]:
            Flag.m6_btn_clicked[6] = False
            self.btn_6.color()
            Flag.color6[6] = 2
            Flag.m6_screen[6] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(6)
            self.change(current)

        if Flag.m6_btn_clicked[7]:
            Flag.m6_btn_clicked[7] = False
            self.btn_7.color()
            Flag.color6[7] = 2
            Flag.m6_screen[7] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(7)
            self.change(current)


        if Flag.m6_btn_clicked[8]:
            Flag.m6_btn_clicked[8] = False
            self.btn_8.color()
            Flag.color6[8] = 2
            Flag.m6_screen[8] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(8)
            self.change(current)

        if Flag.m6_btn_clicked[9]:
            Flag.m6_btn_clicked[9] = False
            self.btn_9.color()
            Flag.color6[9] = 2
            Flag.m6_screen[9] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(9)
            self.change(current)

        # 제어 01로 이동
        if Flag.m6_btn_clicked[10]:
            Flag.m6_btn_clicked[10] = False
            self.btn_10.color()
            Flag.color6[10] = 2
            Flag.m6_screen[10] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(10)
            self.change(current)

            self.popup = CustomPopup(p_title="제어-01로 이동",
                                     p_content='\n제어-01로 이동하시겠습니까?')
            show = self.popup.showModal()
            if Flag.btn_popup_6_1:
                Flag.btn_popup_6_1 = False
                Flag.miti06_close = True

        # 만족 / 불만족 / 병행 처리
        if Flag.pg6_sat[2]:
            self.btn_2.complete()
            Flag.color6[2] = 3
            self.btn_3.color()
            Flag.color6[3] = 2
            Flag.pg6_sat[2] = False
        if Flag.pg6_p[2]:
            self.btn_2.color2()
            Flag.color6[2] = 1
            self.btn_3.color()
            Flag.color6[3] = 2
            Flag.pg6_p[2] = False

        if Flag.pg6_sat[3]:
            self.btn_3.complete()
            Flag.color6[3] = 3
            self.btn_4.color()
            Flag.color6[4] = 2
            Flag.pg6_sat[3] = False
        if Flag.pg6_p[3]:
            self.btn_3.color2()
            Flag.color6[3] = 1
            self.btn_4.color()
            Flag.color6[4] = 2
            Flag.pg6_p[3] = False

        if Flag.pg6_sat[4]:
            self.btn_4.complete()
            Flag.color6[4] = 3
            self.btn_5.color()
            Flag.color6[5] = 2
            Flag.pg6_sat[4] = False
        if Flag.pg6_p[4]:
            self.btn_4.color2()
            Flag.color6[4] = 1
            self.btn_5.color()
            Flag.color6[5] = 2
            Flag.pg6_p[4] = False

        if Flag.pg6_sat[5]:
            self.btn_5.complete()
            Flag.color6[5] = 3
            self.btn_6.color()
            Flag.color6[6] = 2
            Flag.pg6_sat[5] = False
        if Flag.pg6_p[5]:
            self.btn_5.color2()
            Flag.color6[5] = 1
            self.btn_6.color()
            Flag.color6[6] = 2
            Flag.pg6_p[5] = False

        if Flag.pg6_sat[6]:
            self.btn_6.complete()
            Flag.color6[6] = 3
            self.btn_7.color()
            Flag.color6[7] = 2
            Flag.pg6_sat[6] = False
        if Flag.pg6_p[6]:
            self.btn_6.color2()
            Flag.color6[6] = 1
            self.btn_7.color()
            Flag.color6[7] = 2
            Flag.pg6_p[6] = False

        if Flag.pg6_sat[7]:
            self.btn_7.complete()
            Flag.color6[7] = 3
            self.btn_8.color()
            Flag.color6[8] = 2
            Flag.pg6_sat[7] = False
        if Flag.pg6_p[7]:
            self.btn_7.color2()
            Flag.color6[7] = 1
            self.btn_8.color()
            Flag.color6[8] = 2
            Flag.pg6_p[7] = False

        if Flag.pg6_sat[8]:
            self.btn_8.complete()
            Flag.color6[8] = 3
            self.btn_9.color()
            Flag.color6[9] = 2
            Flag.pg6_sat[8] = False
        if Flag.pg6_p[8]:
            self.btn_8.color2()
            Flag.color6[8] = 1
            self.btn_9.color()
            Flag.color6[9] = 2
            Flag.pg6_p[8] = False


        if Flag.pg6_sat[9]:
            self.btn_9.complete()
            Flag.color6[9] = 3
            self.btn_10.color()
            Flag.color6[10] = 2
            Flag.pg6_sat[9] = False
        if Flag.pg6_p[9]:
            self.btn_9.color2()
            Flag.color6[9] = 1
            self.btn_10.color()
            Flag.color6[10] = 2
            Flag.pg6_p[9] = False

    def together(self, me):
        for i in range(1, 11):
            if Flag.color6[i] == 2:  # 자기 자신 제외, 현재 진행중인 버튼 찾기
                if i == me:
                    pass
                else:
                    Flag.color6[i] = 1  # 병행처리
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
        elif find == 9: self.btn_10.color2()

#오른쪽 화면
class MitigationMiddleArea_6R(QWidget, QObject):
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
        super(MitigationMiddleArea_6R, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.central_widget = QStackedWidget()

        # screen 추가
        self.screen1 = tableNone()
        self.screen2 = table_6_2()
        self.screen3 = table_6_3()
        self.screen4 = table_6_4()
        self.screen5 = table_6_5()
        self.screen6 = table_6_6()
        self.screen7 = table_6_7()
        self.screen8 = table_6_8()

        self.central_widget.addWidget(self.screen1)
        self.central_widget.addWidget(self.screen2)
        self.central_widget.addWidget(self.screen3)
        self.central_widget.addWidget(self.screen4)
        self.central_widget.addWidget(self.screen5)
        self.central_widget.addWidget(self.screen6)
        self.central_widget.addWidget(self.screen7)
        self.central_widget.addWidget(self.screen8)

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
        if Flag.m6_btn_clicked[1]:
            self.central_widget.setCurrentIndex(0)
            Flag.m6_page_num = 1
            Flag.m6_screen[1] = False

        if Flag.m6_btn_clicked[2]:
            self.central_widget.setCurrentIndex(1)
            Flag.m6_page_num = 2
            Flag.m6_screen[2] = False

        if Flag.m6_btn_clicked[3]:
            self.central_widget.setCurrentIndex(2)
            Flag.m6_page_num = 3
            Flag.m6_screen[3] = False

        if Flag.m6_btn_clicked[4]:
            self.central_widget.setCurrentIndex(3)
            Flag.m6_page_num = 4
            Flag.m6_screen[4] = False

        if Flag.m6_btn_clicked[5]:
            self.central_widget.setCurrentIndex(4)
            Flag.m6_page_num = 5
            Flag.m6_screen[5] = False

        if Flag.m6_btn_clicked[6]:
            self.central_widget.setCurrentIndex(5)
            Flag.m6_page_num = 6
            Flag.m6_screen[6] = False

        if Flag.m6_btn_clicked[7]:
            self.central_widget.setCurrentIndex(6)
            Flag.m6_page_num = 7
            Flag.m6_screen[7] = False

        if Flag.m6_btn_clicked[8]:
            self.central_widget.setCurrentIndex(7)
            Flag.m6_page_num = 8
            Flag.m6_screen[8] = False

        if Flag.m6_btn_clicked[9]:
            self.central_widget.setCurrentIndex(0)
            Flag.m6_page_num = 9
            Flag.m6_screen[9] = False

        if Flag.m6_btn_clicked[10]:
            self.central_widget.setCurrentIndex(0)
            Flag.m6_page_num = 10
            Flag.m6_screen[10] = False
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
        self.btn_sat.setFixedSize(200, 40)
        self.btn_dsat.setFixedSize(200, 40)
        self.btn_parallelism.setFixedSize(200, 40)

        self.btn_sat.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dsat.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_parallelism.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_sat.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")
        self.btn_dsat.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")
        self.btn_parallelism.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")

        self.btn_sat.clicked.connect(self.click_sat)
        self.btn_parallelism.clicked.connect(self.click_p)

        self.right_bottom = QHBoxLayout()
        self.right_bottom.addWidget(self.btn_sat)
        self.right_bottom.addWidget(self.btn_parallelism)

        self.setLayout(self.right_bottom)


    def paintEvent(self, QPaintEvent):
        # 만족 button 추가
        if Flag.m6_page_num in [0, 1, 10]:
            self.btn_sat.hide()
            self.btn_parallelism.hide()
        else:
            self.btn_sat.show()
            self.btn_parallelism.show()
        self.update()

    def click_sat(self):
        if Flag.m6_page_num == 2:
            Flag.m6_btn_clicked[3] = True
            Flag.pg6_sat[2] = True
        if Flag.m6_page_num == 3:
            Flag.m6_btn_clicked[4] = True
            Flag.pg6_sat[3] = True
        if Flag.m6_page_num == 4:
            Flag.m6_btn_clicked[5] = True
            Flag.pg6_sat[4] = True
        if Flag.m6_page_num == 5:
            Flag.m6_btn_clicked[6] = True
            Flag.pg6_sat[5] = True
        if Flag.m6_page_num == 6:
            Flag.m6_btn_clicked[7] = True
            Flag.pg6_sat[6] = True
        if Flag.m6_page_num == 7:
            Flag.m6_btn_clicked[8] = True
            Flag.pg6_sat[7] = True
        if Flag.m6_page_num == 8:
            Flag.m6_btn_clicked[9] = True
            Flag.pg6_sat[8] = True
        if Flag.m6_page_num == 9:
            Flag.m6_btn_clicked[10] = True
            Flag.pg6_sat[9] = True
    def click_p(self):
        if Flag.m6_page_num == 2:
            Flag.m6_btn_clicked[3] = True
            Flag.pg6_p[2] = True
        if Flag.m6_page_num == 3:
            Flag.m6_btn_clicked[4] = True
            Flag.pg6_p[3] = True
        if Flag.m6_page_num == 4:
            Flag.m6_btn_clicked[5] = True
            Flag.pg6_p[4] = True
        if Flag.m6_page_num == 5:
            Flag.m6_btn_clicked[6] = True
            Flag.pg6_p[5] = True
        if Flag.m6_page_num == 6:
            Flag.m6_btn_clicked[7] = True
            Flag.pg6_p[6] = True
        if Flag.m6_page_num == 7:
            Flag.m6_btn_clicked[8] = True
            Flag.pg6_p[7] = True
        if Flag.m6_page_num == 8:
            Flag.m6_btn_clicked[9] = True
            Flag.pg6_p[8] = True
        if Flag.m6_page_num == 9:
            Flag.m6_btn_clicked[10] = True
            Flag.pg6_p[9] = True

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MitigationMiddleArea_6()
    window.show()
    flow = FlowChart()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
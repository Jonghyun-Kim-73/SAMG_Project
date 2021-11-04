import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from CustomPopup import CustomPopup
from Flag import Flag
from CustomButton import CustomButton

from Table_4_2 import table_4_2
from Table_4_3 import table_4_3
from arrow import Arrow

class MitigationMiddleArea_4(QWidget):
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
        super(MitigationMiddleArea_4, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.shmem = parent.shmem
        self.setStyleSheet(self.qss)

        # 레이어 셋업
        layout = QHBoxLayout(self)
        label1 = FlowChartArea(self)
        label2 = MitigationMiddleArea_4R()
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
        self.line1 = Arrow(self, x=180, y=80, x2=180, y2=100, type=1)
        self.line1 = Arrow(self, x=180, y=190, x2=180, y2=220, type=1)
        self.line1 = Arrow(self, x=180, y=320, x2=180, y2=360, type=1)

        # CustomButton
        self.btn_1 = CustomButton(self, page=4, num=1, x=30, y=10, w=300, h=70, text='Ⅳ.전략수행방법결정', type=0)
        self.btn_2 = CustomButton(self, page=4, num=2, x=30, y=110, w=300, h=90, text='6. 증기발생기 급수 주입\n경로를 선정한다.', type=0)
        self.btn_3 = CustomButton(self, page=4, num=3, x=30, y=230, w=300, h=110, text='7. 증기발생기에 급수를\n실시할 때의\n제한사항들을 파악한다.', type=0)
        self.btn_4 = CustomButton(self, page=4, num=4, x=30, y=370, w=300, h=70, text='Ⅴ.전략수행', type=0)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setPen(QPen(Qt.black))
        p.setFont(QFont('맑은 고딕', 14))

        self.update()

        # 버튼 클릭 이벤트
        if Flag.m4_btn_clicked[1]:
            Flag.m4_btn_clicked[1] = False
            self.btn_1.complete()
            Flag.color4[1] = 3
            Flag.m4_screen[1] = True
            # 현재 실행중인 버튼 병행처리
            current = self.together(1)
            self.change(current)

            # 다음 버튼 표시
            self.btn_2.color()
            Flag.color4[2] = 2

        if Flag.m4_btn_clicked[2]:
            Flag.m4_btn_clicked[2] = False
            self.btn_2.color()
            Flag.color4[2] = 2
            Flag.m4_screen[2] = True
            # 현재 실행중인 버튼 병행처리
            current = self.together(2)
            self.change(current)

        if Flag.m4_btn_clicked[3]:
            Flag.m4_btn_clicked[3] = False
            self.btn_3.color()
            Flag.color4[3] = 2
            Flag.m4_screen[3] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(3)
            self.change(current)

        # 5. 전략수행 -> Tab5으로 전환
        if Flag.m4_btn_clicked[4]:
            Flag.m4_btn_clicked[4] = False

            self.btn_4.color()
            Flag.color4[4] = 2
            Flag.m4_screen[4] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(4)
            self.change(current)

            self.popup = CustomPopup(p_title="Ⅴ.전략수행",
                                     p_content='\nⅤ.전략수행을 수행하시겠습니까?')
            show = self.popup.showModal()
            if Flag.btn_popup_4_1:
                Flag.btn_popup_4_1 = False
                self.btn_4.complete()
                Flag.color4[4] = 3
                Flag.miti06_btn[5] = True  # Tab5 전환

        # 만족 / 불만족 / 병행 처리
        if Flag.pg4_sat[2]:
            self.btn_2.complete()
            Flag.color4[3] = 3
            self.btn_3.color()
            Flag.color4[3] = 2
            Flag.pg4_sat[2] = False
        if Flag.pg4_p[2]:
            self.btn_2.color2()
            Flag.color4[2] = 1
            self.btn_3.color()
            Flag.color4[3] = 2
            Flag.pg4_p[2] = False

        if Flag.pg4_sat[3]:
            self.btn_3.complete()
            Flag.color4[3] = 3
            self.btn_4.color()
            Flag.color4[4] = 2
            Flag.pg4_sat[3] = False
        if Flag.pg4_p[3]:
            self.btn_3.color2()
            Flag.color4[3] = 1
            self.btn_4.color()
            Flag.color4[4] = 2
            Flag.pg4_p[3] = False

    def together(self, me):
        for i in range(1, 5):
            if Flag.color4[i] == 2:  # 자기 자신 제외, 현재 진행중인 버튼 찾기
                if i == me:
                    pass
                else:
                    Flag.color4[i] = 1  # 병행처리
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

# Right Page
class MitigationMiddleArea_4R(QWidget, QObject):
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
        super(MitigationMiddleArea_4R, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.central_widget = QStackedWidget()

        # screen 추가
        self.screen1 = tableNone()
        self.screen2 = table_4_2()
        self.screen3 = table_4_3()

        self.central_widget.addWidget(self.screen1)
        self.central_widget.addWidget(self.screen2)
        self.central_widget.addWidget(self.screen3)

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
        if Flag.m4_btn_clicked[1]:
            self.central_widget.setCurrentIndex(0)
            Flag.m4_page_num = 1
            Flag.m4_screen[1] = False

        if Flag.m4_btn_clicked[2]:
            self.central_widget.setCurrentIndex(1)
            Flag.m4_page_num = 2
            Flag.m4_screen[2] = False

        if Flag.m4_btn_clicked[3]:
            self.central_widget.setCurrentIndex(2)
            Flag.m4_page_num = 3
            Flag.m4_screen[3] = False

        if Flag.m4_btn_clicked[4]:
            self.central_widget.setCurrentIndex(3)
            Flag.m4_screen[4] = False
            Flag.m4_page_num = 4

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
        if Flag.m4_page_num == 2 or Flag.m4_page_num == 3:
            self.btn_sat.show()
        else:
            self.btn_sat.hide()

        # 병행 button 추가
        if Flag.m4_page_num == 2 or Flag.m4_page_num == 3:
            self.btn_parallelism.show()
        else:
            self.btn_parallelism.hide()
        self.update()

    def click_sat(self):
        # 만족 button click
        if Flag.m4_page_num == 2:
            Flag.m4_btn_clicked[3] = True
            Flag.pg4_sat[2] = True
        if Flag.m4_page_num == 3:
            Flag.m4_btn_clicked[4] = True
            Flag.pg4_sat[3] = True

    def click_p(self):
        # 확인 button click
        if Flag.m4_page_num == 2:
            Flag.m4_btn_clicked[3] = True
            Flag.pg4_p[2] = True
        if Flag.m4_page_num == 3:
            Flag.m4_btn_clicked[4] = True
            Flag.pg4_p[3] = True

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MitigationMiddleArea_4()
    window.show()
    flow = FlowChart()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
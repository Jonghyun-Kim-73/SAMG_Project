import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Flag import Flag
from CustomPopup import CustomPopup
from CustomButton import CustomButton
from Mitigation_popup1 import Mitigation_popup
from Mitigation_popup2 import Mitigation_popup2

from Table_5_2 import table_5_2
from Table_5_3 import table_5_3
from Table_5_4 import table_5_4
from Table_5_5 import table_5_5

from arrow import Arrow

class MitigationMiddleArea_5(QWidget):
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
        super(MitigationMiddleArea_5, self).__init__()
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
        self.split_1.setSizes([1265, 860])  # 슬라이드 초기 사이즈 지정
        layout.addWidget(self.split_1)
        layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(layout)

class FlowChartArea(QWidget):
    qss = """
        QWidget {
            background: rgb(221, 221, 221);
            border:0px;
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
        self.setGeometry(0, 0, 800, 800)  # 1900*(3/4) = 1425

        # Arrow
        self.line1 = Arrow(self, x=180, y=80, x2=180, y2=100, type=1)
        self.line1 = Arrow(self, x=180, y=190, x2=180, y2=240, type=1)
        self.line1 = Arrow(self, x=180, y=380, x2=180, y2=400, type=1)
        self.line1 = Arrow(self, x=180, y=510, x2=180, y2=540, type=1)
        self.line1 = Arrow(self, x=180, y=660, x2=180, y2=680, type=1)
        self.line1 = Arrow(self, x=320, y=605, x2=370, y2=605, type=3)

        # CustomButton
        self.btn_1 = CustomButton(self, page=5, num=1, x=30, y=10, w=300, h=70, text='Ⅴ.전략수행', type=0)
        self.btn_2 = CustomButton(self, page=5, num=2, x=30, y=110, w=300, h=110, text='8. 증기발생기 급수\n주입을 실시하도록\n주제어실에 지시한다.', type=0)
        self.btn_3 = CustomButton(self, page=5, num=3, x=30, y=250, w=300, h=130, text='9. 주제어실에서\n증기발생기 급수 주입을\n성공적으로\n실시하였는가를 확인한다.', type=0)
        self.btn_4 = CustomButton(self, page=5, num=4, x=30, y=410, w=300, h=110, text='10. 추가적인 완화\n조치들이 필요한 지를\n결정한다.', type=0)
        self.btn_5 = CustomButton(self, page=5, num=5, x=30, y=550, w=300, h=110, text='11. 추가적인 증기발생기\n급수 주입이 필요한지를\n결정한다.', type=0)
        self.btn_6 = CustomButton(self, page=5, num=6, x=380, y=570, w=200, h=70, text='단계 3', type=0)
        self.btn_7 = CustomButton(self, page=5, num=7, x=30, y=690, w=300, h=70, text='Ⅵ.전략종결', type=0)

    def paintEvent(self, event):
        p = QPainter(self)
        p.setPen(QPen(Qt.black))
        p.setFont(QFont('맑은 고딕', 14))

        self.update()

        # 버튼 클릭 이벤트
        if Flag.m5_btn_clicked[1]:
            Flag.m5_btn_clicked[1] = False
            self.btn_1.complete()
            Flag.color5[1] = 3
            Flag.m5_screen[1] = True
            # 현재 실행중인 버튼 병행처리
            current = self.together(1)
            self.change(current)

            # 다음 버튼 표시
            self.btn_2.color()
            Flag.color5[2] = 2

        if Flag.m5_btn_clicked[2]:
            Flag.m5_btn_clicked[2] = False
            self.btn_2.color()
            Flag.color5[2] = 2
            Flag.m5_screen[2] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(2)
            self.change(current)

        if Flag.m5_btn_clicked[3]:
            Flag.m5_btn_clicked[3] = False
            self.btn_3.color()
            Flag.color5[3] = 2
            Flag.m5_screen[3] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(3)
            self.change(current)

        if Flag.m5_btn_clicked[4]:
            Flag.m5_btn_clicked[4] = False
            self.btn_4.color()
            Flag.color5[4] = 2
            Flag.m5_screen[4] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(4)
            self.change(current)

        if Flag.m5_btn_clicked[5]:
            Flag.m5_btn_clicked[5] = False
            self.btn_5.color()
            Flag.color5[5] = 2
            Flag.m5_screen[5] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(5)
            self.change(current)

        # 단계 3
        if Flag.m5_btn_clicked[6]:
            Flag.m5_btn_clicked[6] = False
            self.btn_6.color()
            Flag.color5[6] = 2
            Flag.m5_screen[6] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(6)
            self.change(current)

            self.popup = CustomPopup(p_title="단계 3",
                                     p_content='\n단계 3을 수행하시겠습니까?')
            show = self.popup.showModal()
            if Flag.btn_popup_5_1:
                Flag.btn_popup_5_1 = False
                self.btn_5.complete()
                Flag.color2[5] = 3
                Flag.miti06_btn[2] = True  # 단계 3으로 이동

        # 전략종결 -> Tab6으로 전환
        if Flag.m5_btn_clicked[7]:
            Flag.m5_btn_clicked[7] = False
            self.btn_7.color()
            Flag.color5[7] = 2
            Flag.m5_screen[7] = True

            # 현재 실행중인 버튼 병행처리
            current = self.together(7)
            self.change(current)

            self.popup = CustomPopup(p_title="Ⅵ.전략종결",
                                     p_content='\nⅥ.전략종결을 수행하시겠습니까?')
            show = self.popup.showModal()
            if Flag.btn_popup_5_2:
                Flag.btn_popup_5_2 = False
                self.btn_7.complete()
                Flag.color2[7] = 3
                Flag.miti06_btn[6] = True  # Tab6 전환

        # 만족 / 불만족 / 병행 처리
        if Flag.pg5_sat[2]:
            self.btn_2.complete()
            Flag.color5[2] = 3
            self.btn_3.color()
            Flag.color5[3] = 2
            Flag.pg5_sat[2] = False
        if Flag.pg5_p[2]:
            self.btn_2.color2()
            Flag.color5[2] = 1
            self.btn_3.color()
            Flag.color5[3] = 2
            Flag.pg5_p[2] = False

        if Flag.pg5_sat[3]:
            self.btn_3.complete()
            Flag.color5[3] = 3
            self.btn_4.color()
            Flag.color5[4] = 2
            Flag.pg5_sat[3] = False
        if Flag.pg5_p[3]:
            self.btn_3.color2()
            Flag.color5[3] = 1
            self.btn_4.color()
            Flag.color5[4] = 2
            Flag.pg5_p[3] = False

        if Flag.pg5_sat[4]:
            self.btn_4.complete()
            Flag.color5[4] = 3
            self.btn_5.color()
            Flag.color5[5] = 2
            Flag.pg5_sat[4] = False
        if Flag.pg5_p[4]:
            self.btn_4.color2()
            Flag.color5[4] = 1
            self.btn_5.color()
            Flag.color5[5] = 2
            Flag.pg5_p[4] = False

        if Flag.pg5_sat[5]:
            self.btn_5.complete()
            Flag.color5[5] = 3
            self.btn_7.color()
            Flag.color5[7] = 2
            Flag.pg5_sat[5] = False
        if Flag.pg5_dsat[5]:
            self.btn_5.complete()
            Flag.color5[5] = 3
            self.btn_6.color()
            Flag.color5[6] = 2
            Flag.pg5_dsat[5] = False
        if Flag.pg5_p[5]:
            self.btn_5.color2()
            Flag.color5[5] = 1
            self.btn_7.color()
            Flag.color5[7] = 2
            Flag.pg5_p[5] = False

    def together(self, me):
        for i in range(1, 8):
            if Flag.color5[i] == 2:  # 자기 자신 제외, 현재 진행중인 버튼 찾기
                if i == me:
                    pass
                else:
                    Flag.color5[i] = 1  # 병행처리
                    return i


    def change(self, find):
        if find == 1: self.btn_1.color2()
        elif find == 2: self.btn_2.color2()
        elif find == 3: self.btn_3.color2()
        elif find == 4: self.btn_4.color2()
        elif find == 5: self.btn_5.color2()
        elif find == 6: self.btn_6.color2()
        elif find == 7: self.btn_7.color2()

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
        self.screen2 = table_5_2()
        self.screen3 = table_5_3()
        self.screen4 = table_5_4()
        self.screen5 = table_5_5()

        self.central_widget.addWidget(self.screen1)
        self.central_widget.addWidget(self.screen2)
        self.central_widget.addWidget(self.screen3)
        self.central_widget.addWidget(self.screen4)
        self.central_widget.addWidget(self.screen5)

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
        if Flag.m5_btn_clicked[1]:
            self.central_widget.setCurrentIndex(0)
            Flag.m5_page_num = 1
            Flag.m5_screen[1] = False

        if Flag.m5_btn_clicked[2]:
            self.central_widget.setCurrentIndex(1)
            Flag.m5_page_num = 2
            Flag.m5_screen[2] = False

        if Flag.m5_btn_clicked[3]:
            self.central_widget.setCurrentIndex(2)
            Flag.m5_page_num = 3
            Flag.m5_screen[3] = False

        if Flag.m5_btn_clicked[4]:
            self.central_widget.setCurrentIndex(3)
            Flag.m5_page_num = 4
            Flag.m5_screen[4] = False

        if Flag.m5_btn_clicked[5]:
            self.central_widget.setCurrentIndex(4)
            Flag.m5_page_num = 5
            Flag.m5_screen[5] = False

        if Flag.m5_btn_clicked[6]:
            self.central_widget.setCurrentIndex(0)
            Flag.m5_page_num = 6
            Flag.m5_screen[6] = False

        if Flag.m5_btn_clicked[7]:
            self.central_widget.setCurrentIndex(0)
            Flag.m5_page_num = 7
            Flag.m5_screen[7] = False

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
        self.btn1 = QPushButton("첨부-D")
        self.btn2 = QPushButton("계산표-05")
        self.setFixedHeight(70)
        self.btn_sat.setFixedSize(200, 40)
        self.btn_dsat.setFixedSize(200, 40)
        self.btn_parallelism.setFixedSize(200, 40)
        self.btn1.setFixedSize(200, 40)
        self.btn2.setFixedSize(200, 40)

        self.btn_sat.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_dsat.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_parallelism.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn2.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_sat.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")
        self.btn_dsat.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")
        self.btn_parallelism.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")
        self.btn1.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")
        self.btn2.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")

        self.btn_sat.clicked.connect(self.click_sat)
        self.btn_dsat.clicked.connect(self.click_dsat)
        self.btn_parallelism.clicked.connect(self.click_p)
        self.btn1.clicked.connect(self.click_1)
        self.btn2.clicked.connect(self.click_2)

        self.right_bottom = QHBoxLayout()

        self.right_bottom.addWidget(self.btn_sat)
        self.right_bottom.addWidget(self.btn_dsat)
        self.right_bottom.addWidget(self.btn_parallelism)
        self.right_bottom.addWidget(self.btn1)
        self.right_bottom.addWidget(self.btn2)

        self.setLayout(self.right_bottom)

    def paintEvent(self, QPaintEvent):
        # 만족 button 추가
        if Flag.m5_page_num == 2 or Flag.m5_page_num == 3 or Flag.m5_page_num == 4 or Flag.m5_page_num == 5:
            self.btn_sat.show()
        else:
            self.btn_sat.hide()

        # 불만족 button 추가
        if Flag.m5_page_num == 5:
            self.btn_dsat.show()
        else:
            self.btn_dsat.hide()

        # 병행 button 추가
        if Flag.m5_page_num == 2 or Flag.m5_page_num == 3 or Flag.m5_page_num == 4:
            self.btn_parallelism.show()
        else:
            self.btn_parallelism.hide()

        # 기타 button 추가
        if Flag.m5_page_num == 4:
            self.btn1.show()
        else:
            self.btn1.hide()
        if Flag.m5_page_num == 5:
            self.btn2.show()
        else:
            self.btn2.hide()

        self.update()

    def click_sat(self):
        # 만족 button click
        if Flag.m5_page_num == 2:
            Flag.m5_btn_clicked[3] = True
            Flag.pg5_sat[2] = True
        if Flag.m5_page_num == 3:
            Flag.m5_btn_clicked[4] = True
            Flag.pg5_sat[3] = True
        if Flag.m5_page_num == 4:
            Flag.m5_btn_clicked[5] = True
            Flag.pg5_sat[4] = True
        if Flag.m5_page_num == 5:
            Flag.m5_btn_clicked[7] = True
            Flag.pg5_sat[5] = True

    def click_dsat(self):
        # 불만족 button click
        if Flag.m5_page_num == 5:
            Flag.m5_btn_clicked[6] = True
            Flag.pg5_dsat[5] = True

    def click_p(self):
        # 병행 button click
        if Flag.m5_page_num == 2:
            Flag.m5_btn_clicked[3] = True
            Flag.pg5_p[2] = True
        if Flag.m5_page_num == 3:
            Flag.m5_btn_clicked[4] = True
            Flag.pg5_p[3] = True
        if Flag.m5_page_num == 4:
            Flag.m5_btn_clicked[5] = True
            Flag.pg5_p[4] = True
        if Flag.m5_page_num == 5:
            Flag.m5_btn_clicked[7] = True
            Flag.pg5_p[5] = True

    def click_1(self):
        self.popup = Mitigation_popup()
        self.popup.show()
        pass
    def click_2(self):
        self.popup2 = Mitigation_popup2()
        self.popup2.show()
        pass

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = MitigationMiddleArea_5()
    window.show()
    flow = FlowChart()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
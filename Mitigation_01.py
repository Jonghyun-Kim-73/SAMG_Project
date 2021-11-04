import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from CustomPopup import CustomPopup
from Flag import Flag

from Mitigation_titlebar import MitigationTiltle
from Mitigation_Middle_1 import MitigationMiddleArea_1
from Mitigation_Middle_2 import MitigationMiddleArea_2
from Mitigation_Middle_3 import MitigationMiddleArea_3
from Mitigation_Middle_4 import MitigationMiddleArea_4
from Mitigation_Middle_5 import MitigationMiddleArea_5
from Mitigation_Middle_6 import MitigationMiddleArea_6

#팝업
from Mitigation_popup import Mitigation_popup


class MitigationWindow(QWidget,QObject):
    """메인 윈도우"""
    qss = """
        QWidget {
            background: rgb(128, 128, 128); 
            border: 2px solid rgb(0, 0, 0);
            color:rgb(0,0,0);
        }
        QPushButton{
            color : black; font-size: 16pt; font-weight: bold; background : rgb(221,221,221);
            border:1px solid rgb(0,0,0);
            padding:0px
        }
        QPushButton::pressed { background-color: red }
        QPushButton::hover{ background-color: rgb(0, 176, 218)}
        QWidget#main {
            background: rgb(128, 128, 128); 
            border: 0px solid rgb(0, 0, 0);
            color:rgb(0,0,0);
        }
        QWidget#menu {
            background: rgb(128, 128, 128); 
            border: 2px solid rgb(0, 0, 0);
            color:rgb(0,0,0);
            padding:0px;
        }
        QWidget#middle {
            background: rgb(128, 128, 128); 
            border: 0px solid rgb(0, 0, 0);
            color:rgb(0,0,0);
        }
        QGroupBox {
            padding:0px;
            margin-top: 0px;
        }
    """

    def __init__(self, parent=None):
        super(MitigationWindow, self).__init__()
        self.parent = parent
        self.shmem = parent.shmem

        self.setAttribute(Qt.WA_StyledBackground, True)
        self.central_widget = QStackedWidget()
        self.central_widget.setObjectName("middle")
        screen1 = MitigationMiddleArea_1(self)
        screen2 = MitigationMiddleArea_2(self)
        screen3 = MitigationMiddleArea_3(self)
        screen4 = MitigationMiddleArea_4(self)
        screen5 = MitigationMiddleArea_5(self)
        screen6 = MitigationMiddleArea_6(self)

        self.central_widget.addWidget(screen1)
        self.central_widget.addWidget(screen2)
        self.central_widget.addWidget(screen3)
        self.central_widget.addWidget(screen4)
        self.central_widget.addWidget(screen5)
        self.central_widget.addWidget(screen6)
        self.central_widget.setCurrentIndex(0)

        # Main 기본 속성
        self.setGeometry(0, 30, 1920, 1000)
        self.setStyleSheet(self.qss)
        # self.setWindowOpacity(0.95)  # 프레임 투명도

        # 레이아웃 설정
        self.window_vbox = QVBoxLayout(self)  # 세로 방향 레이아웃
        self.window_vbox.setContentsMargins(5, 5, 5, 5)  # 여백
        # self.window_vbox.setSpacing(5)  # 각 객체 사이의 여백 ?

        title = MitigationTiltle(self)
        self.window_vbox.addWidget(title)
        self.setStyleSheet(self.qss)
        # 크기 조정

        # 레이어 셋업
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.change_color = False
        self.setAttribute(Qt.WA_StyledBackground, True)

        self.btn_top_1 = QPushButton('Ⅰ.목적, 수행 조건 등')
        self.btn_top_1.setFixedHeight(60)
        self.btn_top_1.clicked.connect(self.click1)
        self.btn_top_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_top_2 = QPushButton('Ⅱ.이용가능수단확인')
        self.btn_top_2.setFixedHeight(60)
        self.btn_top_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_top_2.clicked.connect(self.click2)

        self.btn_top_3 = QPushButton('Ⅲ.전략수행여부결정')
        self.btn_top_3.setFixedHeight(60)
        self.btn_top_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_top_3.clicked.connect(self.click3)

        self.btn_top_4 = QPushButton('Ⅳ.전략수행방법결정')
        self.btn_top_4.setFixedHeight(60)
        self.btn_top_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_top_4.clicked.connect(self.click4)

        self.btn_top_5 = QPushButton('Ⅴ.전략수행')
        self.btn_top_5.setFixedHeight(60)
        self.btn_top_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_top_5.clicked.connect(self.click5)

        self.btn_top_6 = QPushButton('Ⅵ.전략종결')
        self.btn_top_6.setFixedHeight(60)
        self.btn_top_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_top_6.clicked.connect(self.click6)

        self.btn_top_7 = QPushButton('제어-01로 이동')
        self.btn_top_7.setFixedHeight(60)
        self.btn_top_7.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_top_7.clicked.connect(self.click7)

        self.btn_top_8 = QPushButton('기능-기반 디스플레이')
        self.btn_top_8.setFixedHeight(60)
        self.btn_top_8.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_top_8.clicked.connect(self.click8)

        self.layout.addWidget(self.btn_top_1)
        self.layout.addWidget(self.btn_top_2)
        self.layout.addWidget(self.btn_top_3)
        self.layout.addWidget(self.btn_top_4)
        self.layout.addWidget(self.btn_top_5)
        self.layout.addWidget(self.btn_top_6)
        self.layout.addWidget(self.btn_top_7)
        self.layout.addWidget(self.btn_top_8)
        self.layout.setContentsMargins(5,5,5,5)
        self.widget = QGroupBox()

        self.widget.setObjectName("menu")

        self.widget.setLayout(self.layout)
        self.widget.setContentsMargins(0,0,0,0)

        self.window_vbox.addWidget(self.widget)
        self.window_vbox.addStretch(1)
        self.window_vbox.addWidget(self.central_widget)
        self.setObjectName("main")
        self.showMaximized()
        self.setLayout(self.window_vbox)

    def paintEvent(self, e):
        if self.central_widget.currentIndex() == 0 : self.btn_top_1.setStyleSheet("background-color: rgb(0, 176, 218)")
        else: self.btn_top_1.setStyleSheet("background-color: rgb(221, 221, 221)")
        if self.central_widget.currentIndex() == 1 : self.btn_top_2.setStyleSheet("background-color: rgb(0, 176, 218)")
        else: self.btn_top_2.setStyleSheet("background-color: rgb(221, 221, 221)")
        if self.central_widget.currentIndex() == 2 : self.btn_top_3.setStyleSheet("background-color: rgb(0, 176, 218)")
        else: self.btn_top_3.setStyleSheet("background-color: rgb(221, 221, 221)")
        if self.central_widget.currentIndex() == 3 : self.btn_top_4.setStyleSheet("background-color: rgb(0, 176, 218)")
        else: self.btn_top_4.setStyleSheet("background-color: rgb(221, 221, 221)")
        if self.central_widget.currentIndex() == 4 : self.btn_top_5.setStyleSheet("background-color: rgb(0, 176, 218)")
        else: self.btn_top_5.setStyleSheet("background-color: rgb(221, 221, 221)")
        if self.central_widget.currentIndex() == 5 : self.btn_top_6.setStyleSheet("background-color: rgb(0, 176, 218)")
        else: self.btn_top_6.setStyleSheet("background-color: rgb(221, 221, 221)")

        if Flag.miti06_close:
            Flag.miti06_close = False
            self.close()
        if Flag.miti06_btn[2]:
            self.click2()
            Flag.miti06_btn_first[2] = True # 다음 단계 버튼 활성화
            Flag.m2_btn_clicked[7] = True
            Flag.miti06_btn[2] = False
        if Flag.miti06_btn[3]:
            self.click3()
            Flag.miti06_btn_first[3] = True # 다음 단계 버튼 활성화
            Flag.m3_btn_clicked[1] = True
            Flag.miti06_btn[3] = False
        if Flag.miti06_btn[4]:
            self.click4()
            Flag.miti06_btn_first[4] = True # 다음 단계 버튼 활성화
            Flag.m4_btn_clicked[1] = True
            Flag.miti06_btn[4] = False
        if Flag.miti06_btn[5]:
            self.click5()
            Flag.miti06_btn_first[5] = True # 다음 단계 버튼 활성화
            Flag.m5_btn_clicked[1] = True
            Flag.miti06_btn[5] = False
        if Flag.miti06_btn[6]:
            self.click6()
            Flag.miti06_btn_first[6] = True # 다음 단계 버튼 활성화
            Flag.m6_btn_clicked[1] = True
            Flag.miti06_btn[6] = False

    def click1(self):
        self.central_widget.setCurrentIndex(0)

    def click2(self):
        self.central_widget.setCurrentIndex(1)

    def click3(self):
        self.central_widget.setCurrentIndex(2)

    def click4(self):
        self.central_widget.setCurrentIndex(3)

    def click5(self):
        self.central_widget.setCurrentIndex(4)

    def click6(self):
        self.central_widget.setCurrentIndex(5)

    def click7(self):
        Flag.m1 = True
        self.popup = CustomPopup(p_title="제어-01로 이동",
                                 p_content='\n제어-01로 이동하시겠습니까?')
        show = self.popup.showModal()
        if Flag.move:   # 창 최소화(창 전환)
            Flag.move = False
            self.showMinimized()

    def click8(self):
        self.popup = Mitigation_popup(self)
        self.popup.show()

    def closeEvent(self, QCloseEvent):
        Flag.btn_clicked[9] = True # 제어 01 popup 다시 시작
        Flag.color[9] = 2

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = MitigationWindow()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
import os
import sys
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Flag import Flag
from Mitigation_Middle_3 import MitigationMiddleArea_3
from Mitigation_Middle_4 import MitigationMiddleArea_4
from Mitigation_Middle_5 import MitigationMiddleArea_5
from Mitigation_Middle_6 import MitigationMiddleArea_6
from Mitigation_titlebar import MitigationTiltle
from Mitigation_top import MitigationTopArea

#팝업
from Mitigation_popup import Mitigation_popup

#하단
from Mitigation_Middle_1 import MitigationMiddleArea_1
from Mitigation_Middle_2 import MitigationMiddleArea_2
from Mitigation_Middle_2R import MitigationMiddleArea_2R
from Mitigation_Right import MitigationRightArea

# from bar import MainTitleBar


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

class MitigationWindow(QWidget,QObject):
    """메인 윈도우"""
    qss = """
        QWidget {
             background: rgb(128, 128, 128);  
              
                color:rgb(0,0,0);
              
        }
         QPushButton {
                color : black; font-size: 16pt; font-weight: bold; background : rgb(221,221,221)
            }
            QPushButton::pressed { background-color: red }
        QPushButton::hover{ background-color: rgb(0, 176, 218)}
    """

    def __init__(self, parent):
    # def __init__(self):
        super(MitigationWindow, self).__init__()
        # self.top_window = parent
        self.parent = parent
        self.shmem = parent.shmem
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.central_widget = QStackedWidget()

        screen1 = MitigationMiddleArea_1()
        screen2 = MitigationMiddleArea_2()
        screen3 = MitigationMiddleArea_3(self)
        screen4 = MitigationMiddleArea_4(self)
        screen5 = MitigationMiddleArea_5()
        screen6 = MitigationMiddleArea_6()

        # screen8 = Mitigation_popup()
        # self.screen.signal.connect(self.func)
        self.central_widget.addWidget(screen1)
        self.central_widget.addWidget(screen2)
        self.central_widget.addWidget(screen3)
        self.central_widget.addWidget(screen4)
        self.central_widget.addWidget(screen5)
        self.central_widget.addWidget(screen6)
        # self.central_widget.addWidget(screen8)
        # self.central_widget.setCurrentWidget(self.screen2)
        self.central_widget.setCurrentIndex(0)
        # self.screen.signal.clicked.connect(lambda: self.central_widget.setCurrentWidget(self.scrren1))

        # screen = MitigationTopArea()
        # screen.btn_top_1.clicked.connect(screen.click1)


        # self.screen.signal.connect(self.func)


        # Main 기본 속성
        # self.setGeometry(300, 300, 1900, 900)
        self.setGeometry(0, 30, 1920, 1000)
        self.setStyleSheet(self.qss)
        self.setObjectName('MitigationWin')

        # self.setWindowOpacity(0.95)  # 프레임 투명도

        # 레이아웃 설정
        self.window_vbox = QVBoxLayout(self)  # 세로 방향 레이아웃
        self.window_vbox.setContentsMargins(5, 5, 5, 5)  # 여백
        self.window_vbox.setSpacing(5)  # 각 객체 사이의 여백 ?

        # 타이틀바 위젯
        title = MitigationTiltle(self)

        # self.BB = MitigationTopArea(self)

        # 하단 섹션
        # self.content_hbox = QHBoxLayout(self)

        self.DD = MitigationRightArea(self)


        self.window_vbox.addWidget(title)
        # self.window_vbox.addWidget(self.BB)
        self.setStyleSheet(self.qss)
        # 크기 조정
        self.setMinimumHeight(70)
        # self.setFixedWidth(400)
        # 레이어 셋업
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.change_color = False
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.btn_top_1 = QPushButton('Ⅰ.목적, 수행 조건 등')
        self.btn_top_1.setMaximumHeight(60)
        self.btn_top_1.clicked.connect(self.click1)
        self.btn_top_1.setCursor(QCursor(Qt.PointingHandCursor))

        self.btn_top_2 = QPushButton('Ⅱ.이용가능수단확인')
        self.btn_top_2.setMaximumHeight(60)
        self.btn_top_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_top_2.clicked.connect(self.click2)

        self.btn_top_3 = QPushButton('Ⅲ.전략수행여부결정')
        self.btn_top_3.setMaximumHeight(60)
        self.btn_top_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_top_3.clicked.connect(self.click3)

        self.btn_top_4 = QPushButton('Ⅳ.전략수행방법결정')
        self.btn_top_4.setMaximumHeight(60)
        self.btn_top_4.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_top_4.clicked.connect(self.click4)

        self.btn_top_5 = QPushButton('Ⅴ.전략수행')
        self.btn_top_5.setMaximumHeight(60)
        self.btn_top_5.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_top_5.clicked.connect(self.click5)

        self.btn_top_6 = QPushButton('Ⅵ.전략종결')
        self.btn_top_6.setMaximumHeight(60)
        self.btn_top_6.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_top_6.clicked.connect(self.click6)

        self.btn_top_7 = QPushButton('제어-01로 이동')
        self.btn_top_7.setMaximumHeight(60)
        self.btn_top_7.setCursor(QCursor(Qt.PointingHandCursor))
        # self.btn_top_7.clicked.connect(self.click7)

        self.btn_top_8 = QPushButton('기능-기반 디스플레이')
        self.btn_top_8.setMaximumHeight(60)
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

        self.window_vbox.addLayout(self.layout)
        self.window_vbox.addWidget(self.central_widget)
        # self.window_vbox.addLayout(self.content_hbox)
        self.setLayout(self.window_vbox)
        # self.setContentsMargins(0, 0, 0, 0)
    #
    # def tab1(self):
    #     self.M1 = MitigationMiddleArea_1(self)
    #     self.content_hbox.addWidget(self.M1)
    #     self.__init__()
    # def tab2(self):
    #     self.M2_L = MitigationMiddleArea_2L(self)
    #     self.M2_R = MitigationMiddleArea_2R(self)
    #     self.content_hbox.addWidget(self.M2_L)
    #     self.content_hbox.addWidget(self.M2_R)
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

    def func(self):
        print("누름")
    # @pyqtSlot(name="s2")
    # def func(self):
    #     print("dddddd")
    #     self.central_widget.setCurrentIndex(1)
    def click1(self):
        print("화면1")
        self.central_widget.setCurrentIndex(0)

    def click2(self):
        print("화면2")
        self.central_widget.setCurrentIndex(1)
    def click3(self):
        print("화면3")
        self.central_widget.setCurrentIndex(2)
    def click4(self):
        print("화면4")
        self.central_widget.setCurrentIndex(3)
    def click5(self):
        print("화면5")
        self.central_widget.setCurrentIndex(4)
    def click6(self):
        print("화면6")
        self.central_widget.setCurrentIndex(5)

    def click8(self):
        print("화면3")
        self.popup = Mitigation_popup()
        self.popup.show()

    def closeEvent(self, QCloseEvent):
        print("완화06 닫음")
        Flag.mitigation06 = True

if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    app.setStyle("fusion")  # +++
    app.setStyleSheet(StyleSheet)
    # window = MitigationWindow(None)
    window = MitigationWindow()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
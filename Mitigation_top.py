import os
import sys
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MitigationTopArea(QWidget,QObject):
    signal = pyqtSignal(name="s2")
    # signal2 = pyqtSignal(int)
    # signal3 = pyqtSignal(int)
    # signal4 = pyqtSignal(int)
    # signal5 = pyqtSignal(int)
    # signal6 = pyqtSignal(int)
    # signal7 = pyqtSignal(int)
    # signal8 = pyqtSignal(int)
    """ 왼쪽 디스플레이 위젯 """
    qss = """
            QWidget {
                background: rgb(128, 128, 128);  
                border: 2px solid rgb(0, 0, 0); 
                color:rgb(0,0,0);
            }

            QPushButton {
                color: rgb(0,0,0);
                background: rgb(221, 221, 221);
                font: bold 14px;
                padding: 4px 4px;      
            }
        
        """

    def __init__(self, parent=None):
        super(MitigationTopArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        # 크기 조정
        self.setMinimumHeight(70)
        # self.setFixedWidth(400)
        # 레이어 셋업
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        self.change_color = False

        self.btn_top_1 = QPushButton('Ⅰ.목적, 수행 조건 등')
        self.btn_top_1.setMaximumHeight(60)
        self.btn_top_1.setStyleSheet("color : black; font-size: 16pt; font-weight: bold")
        # self.btn_top_1.clicked.connect(self.click1)

        self.btn_top_2 = QPushButton('Ⅱ.이용가능수단확인')
        self.btn_top_2.setMaximumHeight(60)
        self.btn_top_2.setStyleSheet("Color : black; font-size: 16pt; font-weight: bold")
        # self.btn_top_2.clicked.connect(self.start)
        # self.btn_top_2.clicked.connect(self.click2)

        self.btn_top_3 = QPushButton('Ⅲ.전략수행여부결정')
        self.btn_top_3.setMaximumHeight(60)
        self.btn_top_3.setStyleSheet("Color : black; font-size: 16pt; font-weight: bold")
        # self.btn_top_3.clicked.connect(self.send(1))

        self.btn_top_4 = QPushButton('Ⅳ.전략수행방법결정')
        self.btn_top_4.setMaximumHeight(60)
        self.btn_top_4.setStyleSheet("Color : black; font-size: 16pt; font-weight: bold")
        # self.btn_top_4.clicked.connect(self.signal.emit)

        self.btn_top_5 = QPushButton('Ⅴ.전략수행')
        self.btn_top_5.setMaximumHeight(60)
        self.btn_top_5.setStyleSheet("Color : black; font-size: 16pt; font-weight: bold")
        # self.btn_top_5.clicked.connect(self.signal.emit)

        self.btn_top_6 = QPushButton('Ⅵ.전략종결')
        self.btn_top_6.setMaximumHeight(60)
        self.btn_top_6.setStyleSheet("Color : black; font-size: 16pt; font-weight: bold")
        # self.btn_top_6.clicked.connect(self.signal.emit)

        self.btn_top_7 = QPushButton('제어-01로 이동')
        self.btn_top_7.setMaximumHeight(60)
        self.btn_top_7.setStyleSheet("Color : black; font-size: 16pt; font-weight: bold")
        # self.btn_top_7.clicked.connect(self.signal.emit)

        self.btn_top_8 = QPushButton('기능-기반 디스플레이')
        self.btn_top_8.setMaximumHeight(60)
        self.btn_top_8.setStyleSheet("Color : black; font-size: 16pt; font-weight: bold")
        # self.btn_top_8.clicked.connect(self.signal.emit)

        layout.addWidget(self.btn_top_1)
        layout.addWidget(self.btn_top_2)
        layout.addWidget(self.btn_top_3)
        layout.addWidget(self.btn_top_4)
        layout.addWidget(self.btn_top_5)
        layout.addWidget(self.btn_top_6)
        layout.addWidget(self.btn_top_7)
        layout.addWidget(self.btn_top_8)

        self.setLayout(layout)

    def click1(self):
        # if self.change_color:
        #     self.change_color = False
        #     self.btn_top_1.setStyleSheet("QPushButton {color: rgb(0,0,0);background: rgb(221, 221, 221);font-size: 16pt; font-weight: bold}")
        # else:
        #     self.change_color = True
        #     self.btn_top_1.setStyleSheet("QPushButton {color: rgb(0,0,0);background: rgb(0, 176, 218);font-size: 16pt; font-weight: bold}")
        print("1클릭")

    def click2(self):
        if self.change_color:
            self.change_color = False
            self.btn_top_2.setStyleSheet(
                "QPushButton {color: rgb(0,0,0);background: rgb(221, 221, 221);font-size: 16pt; font-weight: bold}")
        else:
            self.change_color = True
            self.btn_top_2.setStyleSheet(
                "QPushButton {color: rgb(0,0,0);background: rgb(0, 176, 218);font-size: 16pt; font-weight: bold}")
        print("2클릭")
    #
    # @pyqtSlot()
    # def start(self):






    # def count(self, num):
    #     return num
    #
    # def run(self):
    #     self.signal.emit()

if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MitigationTopArea()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
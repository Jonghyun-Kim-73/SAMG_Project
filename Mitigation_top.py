import os
import sys
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))  # 절대경로>디렉토리명


class MitigationTopArea(QWidget):
    """ 왼쪽 디스플레이 위젯 """
    qss = """
            QWidget {
                background: rgb(0, 0, 0);    
            }

            QLabel {
                background: rgb(131, 131, 131);
                border-radius: 6px;
                color: rgb(255, 255, 255);
            }

            QPushButton {
                background: rgb(62, 74, 84);
                border-radius: 3px;
                border: 2px inset rgb(62, 74, 84);
                font: bold 12px;
                color: rgb(255, 255, 255);          
            }
        """

    def __init__(self, parent=None):
        super(MitigationTopArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 크기 조정
        self.setMinimumHeight(50)
        # self.setFixedWidth(400)

        # 레이어 셋업
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        self.btn_top_1 = QPushButton('목적, 수행 조건 등')
        self.btn_top_1.setMaximumHeight(50)
        self.btn_top_1.setStyleSheet("Color : white; font-size: 14pt; font-weight: bold")
        self.btn_top_2 = QPushButton('이용 가능 수단 확인')
        self.btn_top_2.setMaximumHeight(50)
        self.btn_top_2.setStyleSheet("Color : white; font-size: 14pt; font-weight: bold")
        self.btn_top_3 = QPushButton('전략 수행 여부 결정')
        self.btn_top_3.setMaximumHeight(50)
        self.btn_top_3.setStyleSheet("Color : white; font-size: 14pt; font-weight: bold")
        self.btn_top_4 = QPushButton('전략 수행 방법 결정')
        self.btn_top_4.setMaximumHeight(50)
        self.btn_top_4.setStyleSheet("Color : white; font-size: 14pt; font-weight: bold")
        self.btn_top_5 = QPushButton('전략 수행')
        self.btn_top_5.setMaximumHeight(50)
        self.btn_top_5.setStyleSheet("Color : white; font-size: 14pt; font-weight: bold")
        self.btn_top_6 = QPushButton('전략 종결')
        self.btn_top_6.setMaximumHeight(50)
        self.btn_top_6.setStyleSheet("Color : white; font-size: 14pt; font-weight: bold")

        layout.addWidget(self.btn_top_1)
        layout.addWidget(self.btn_top_2)
        layout.addWidget(self.btn_top_3)
        layout.addWidget(self.btn_top_4)
        layout.addWidget(self.btn_top_5)
        layout.addWidget(self.btn_top_6)

        self.setLayout(layout)

if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MitigationTopArea()
    window.show()
    app.exec_()
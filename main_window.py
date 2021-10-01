import os
import sys
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from main_top import MainTop

from main_right import MainRight
from main_left import *

# QEvent.HoverMove
class MainWindow(QWidget):
    """메인 윈도우"""
    qss = """
        QWidget {
            background: rgb(128, 128, 128);
            
        }
    """

    # def __init__(self, parent):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.parent = parent
        self.shmem = parent.shmem
        # self.top_window = parent

        # Main 기본 속성
        self.setGeometry(0, 30, 1920, 1010)
        self.setStyleSheet(self.qss)

        # self.setWindowOpacity(0.95)  # 프레임 투명도

        # 레이아웃 설정
        window_vbox = QVBoxLayout(self)  # 세로 방향 레이아웃
        window_vbox.setContentsMargins(0, 0, 0, 0)  # 여백
        window_vbox.setSpacing(0)  # 각 객체 사이의 여백

        # 타이틀바 위젯

        self.BB = MainTop(self)

        # 하단 섹션
        content_hbox = QHBoxLayout(self)

        # 왼쪽
        self.GG = MainLeft(self)

        # 오른쪽
        self.DD = MainRight(self.parent)

        # 각 항목을 레이아웃에 배치
        content_hbox.addWidget(self.GG)
        content_hbox.addWidget(self.DD)

        window_vbox.addWidget(self.BB)
        window_vbox.addLayout(content_hbox)

        self.setLayout(window_vbox)
        # self.setContentsMargins(0, 0, 0, 0)


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    # window = MitigationWindow(None)
    window = MainWindow()
    flow = FlowChart()
    app.installEventFilter(flow.btn_1)
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    window.show()
    app.exec_()
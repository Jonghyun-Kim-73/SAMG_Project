from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from main_top import *
from main_left import *
from main_right import *

class MainWindow(QWidget):
    """메인 윈도우"""
    qss = """
        QWidget {
            background: rgb(128, 128, 128);
            padding:0px;
        }
        QLabel#name{
            background: rgb(221, 221, 221);
            font: bold 14px;
            color: rgb(0, 0, 0);
        }
        QWidget#menu {
            background: rgb(128, 128, 128);
            padding:0px;
        }
        QGroupBox {
            padding:0px;
            margin-top: 0px;
        }
    """

    def __init__(self, parent=None):
        super(MainWindow, self).__init__()
        self.shmem = parent.shmem
        self.parent = parent

        # Main 기본 속성
        self.setGeometry(0, 30, 1920, 1010)
        self.setStyleSheet(self.qss)
        # self.setWindowOpacity(0.95)  # 프레임 투명도

        # 레이아웃 설정
        window_vbox = QVBoxLayout(self)  # 세로 방향 레이아웃
        window_vbox.setContentsMargins(0, 0, 5, 5)  # 여백
        window_vbox.setSpacing(0)  # 각 객체 사이의 여백

        # 타이틀바 위젯
        self.BB = MainTop(self)
        # 하단 섹션
        content_hbox = QHBoxLayout(self)
        # 왼쪽
        self.GG = MainLeft(self)
        # 오른쪽
        self.DD = MainRight(self)

        # 각 항목을 레이아웃에 배치
        content_hbox.addWidget(self.GG)
        content_hbox.addWidget(self.DD)
        window_vbox.addWidget(self.BB)
        window_vbox.addLayout(content_hbox)

        self.setLayout(window_vbox)
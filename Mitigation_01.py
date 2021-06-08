import os
import sys
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from Mitigation_titlebar import MitigationTitleBar
from Mitigation_Left import MitigationLeftArea
from Mitigation_Middle import MitigationMiddleArea
from Mitigation_Right import MitigationRightArea

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))  # 절대경로>디렉토리명


class MitigationWindow(QWidget):
    """메인 윈도우"""
    qss = """
        QWidget {
            background: rgb(20, 25, 20);
        }
    """

    def __init__(self, parent):
        super(MitigationWindow, self).__init__()
        self.top_window = parent

        # Main 기본 속성
        self.setGeometry(300, 300, 1900, 900)
        self.setStyleSheet(self.qss)
        self.setObjectName('MitigationWin')

        self.setWindowOpacity(0.95)  # 프레임 투명도

        # 레이아웃 설정
        window_vbox = QVBoxLayout()  # 세로 방향 레이아웃
        window_vbox.setContentsMargins(0, 0, 0, 0)  # 여백
        window_vbox.setSpacing(0)  # 각 객체 사이의 여백 ?

        # 타이틀바 위젯
        title = MitigationTitleBar(self)

        # 하단 섹션
        content_hbox = QHBoxLayout(self)

        # 왼쪽
        self.BB = MitigationLeftArea(self)

        # 중간
        self.GG = MitigationMiddleArea(self)

        # 오른쪽
        self.DD = MitigationRightArea(self)

        # 각 항목을 레이아웃에 배치
        content_hbox.addWidget(self.BB)
        content_hbox.addWidget(self.GG)
        content_hbox.addWidget(self.DD)


        # window_vbox.addWidget(title_bar)
        window_vbox.addLayout(content_hbox)

        self.setLayout(window_vbox)
        self.setContentsMargins(0, 0, 0, 0)


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MitigationWindow(None)
    window.show()
    app.exec_()
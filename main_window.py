import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from bar import MainTitleBar
from main_left import MainLeftArea
from main_right import MainRightArea


ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class MainWindow(QWidget):
    """메인 윈도우"""
    qss = """
        QWidget {
            background: rgb(20, 25, 20);
        }
    """

    def __init__(self, parent):
        super(MainWindow, self).__init__()
        self.top_window = parent            # ?

        self.setGeometry(300, 300, 1900, 1050)
        self.setStyleSheet(self.qss)
        self.setObjectName('MainWin')

        # Main 프레임 모양 정의  # ?
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), 10, 10)
        mask = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)
        # Main 프레임 특징 정의
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)  # 프레임 날리고 | 창은 항상 위 # ?
        self.setWindowOpacity(0.95)  # 프레임 투명도

        # 레이아웃 설정
        window_vbox = QVBoxLayout()  # 세로 방향 레이아웃
        window_vbox.setContentsMargins(0, 0, 0, 0)  # 여백
        window_vbox.setSpacing(0)  # 각 객체 사이의 여백 ?

        # 타이틀바 위젯
        titlebar_widget = MainTitleBar(self)

        # 1] 하단 섹션
        content_hbox = QHBoxLayout()  # 가로 방향 레이아웃
        content_hbox.setContentsMargins(0, 0, 0, 0)
        content_hbox.setSpacing(0)

        # 1.1] 왼쪽
        self.left_area = MainLeftArea(self)


        # 1.2] 오른쪽
        self.right_area = MainRightArea(self)

        # 각 항목을 레이아웃에 배치
        content_hbox.addWidget(self.left_area)
        content_hbox.addWidget(self.right_area)

        window_vbox.addWidget(titlebar_widget)
        window_vbox.addLayout(content_hbox)

        self.setLayout(window_vbox)
        self.setContentsMargins(0, 0, 0, 0)

        # --------------------------------------------------------------------------------------------------------------
        print(self.height())
        print(self.width())


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MainWindow(None)
    window.show()
    app.exec_()

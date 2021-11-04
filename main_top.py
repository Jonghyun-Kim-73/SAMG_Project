import os
import sys
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MainTop(QWidget):
    qss = """
        QWidget {
            background: rgb(128, 128, 128);
            border: 2px solid rgb(0, 0, 0); 
            color:rgb(0,0,0);
        }

        QLabel#name{
            background: rgb(221, 221, 221);
            font: bold;
             font-size: 14pt;
            color: rgb(0, 0, 0);
            padding: 4px 4px;
        }
        """

    def __init__(self, shmem, parent=None):
        super(MainTop, self).__init__()
        self.shmem = shmem
        self.bar_height = 60
        self.setStyleSheet(self.qss)

        # 타이틀 레이어 셋업 ----------------------------------------------------------------------------------------------
        layout = QHBoxLayout(self)  # 수평 방향 레이아웃
        layout.setContentsMargins(5, 5, 5, 5)  # 위젯의 여백 설정

        #DayBarm TimeBar
        widget1 = TimeBar(self, load_realtime=True, load_realtime2=True)
        widget1.setFixedHeight(self.bar_height)
        widget1.setFixedWidth(280)

        #라벨 설정
        label1 = QLabel("한빛 5호기")
        label1.setObjectName('name')

        #AlignVCenter 수직가운데정렬 / AlignHCenter 수평가운데정렬 / AlignCenter 모두 적용
        label1.setAlignment(Qt.AlignCenter)
        label1.setFixedHeight(self.bar_height)
        label1.setFixedWidth(675)

        label2 = QLabel("제어-01, 전략수행제어도")
        label2.setObjectName('name')

        label2.setAlignment(Qt.AlignCenter)
        label2.setFixedHeight(self.bar_height)
        label2.setFixedWidth(943)

        layout.addWidget(widget1)
        layout.addWidget(label1)
        layout.addWidget(label2)

class TimeBar(QWidget):
    qss = """
        QLabel{
            background: rgb(221, 221, 221);
            font: bold 14px;
            color: rgb(0, 0, 0);
            padding: 4px 4px;
             font-size: 14pt;
        }
    """

    def __init__(self, parent, load_realtime: bool = False, load_realtime2: bool = False):
        super(TimeBar, self).__init__()
        self.parent = parent
        self.load_realtime = load_realtime
        self.load_realtime2 = load_realtime2

        self.setObjectName('TimeBar')
        self.setStyleSheet(self.qss)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.timebarlabel = QLabel('time')
        self.timebarlabel.setAlignment(Qt.AlignCenter)  # 텍스트 정렬
        self.timebarlabel.setObjectName('TimeBarLabel')
        self.dis_update()

        layout.addWidget(self.timebarlabel)

        self.setLayout(layout)

        # timer section
        timer = QTimer(self)
        timer.setInterval(1000)
        timer.timeout.connect(self.dis_update)
        timer.start()

    def dis_update(self):
        """ 타이머 디스플레이 업데이트 """
        # if self.load_realtime or self.load_realtime2:
        real_time = datetime.now().strftime('%Y.%m.%d')
        real_time2 = datetime.now().strftime('%H:%M:%S')
        self.timebarlabel.setText(real_time + " / " + real_time2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainTop()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
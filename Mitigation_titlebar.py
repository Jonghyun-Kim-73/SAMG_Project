import sys
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MitigationTiltle(QWidget):
    qss = """
        QWidget {
            background: rgb(128, 128, 128);
        }

        QLabel#name{
            background: rgb(221, 221, 221);
            font: bold 14px;
            color: rgb(0, 0, 0);
            padding: 4px 4px;
        }
        """

    def __init__(self, parent=None):
        super(MitigationTiltle, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.bar_height = 60
        self.setStyleSheet(self.qss)

        # 타이틀 레이어 셋업 ----------------------------------------------------------------------------------------------
        layout = QHBoxLayout(self)  # 수평 방향 레이아웃
        layout.setContentsMargins(5, 5, 5, 5)  # 위젯의 여백 설정
        # layout.setSpacing(3)

        widget1 = TimeBar(self, load_realtime=True, load_realtime2=True)
        widget1.setFixedHeight(self.bar_height)
        widget1.setFixedWidth(280)

        #라벨 설정
        label1 = QLabel("한빛 5호기")
        label1.setObjectName('name')
        label1.setStyleSheet("color : black; font-size: 14pt; font-weight: bold")
        label1.setAlignment(Qt.AlignCenter)
        label1.setFixedHeight(self.bar_height)
        label1.setFixedWidth(665)

        label2 = QLabel("완화-06, 증기발생기 급수주입")
        label2.setObjectName('name')
        label2.setStyleSheet("color : black; font-size: 14pt; font-weight: bold")
        label2.setAlignment(Qt.AlignCenter)
        label2.setFixedHeight(self.bar_height)
        label2.setFixedWidth(942)

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
        layout.setContentsMargins(1, 0, 0, 0)

        self.timebarlabel = QLabel('time')
        self.timebarlabel.setAlignment(Qt.AlignCenter)  # 텍스트 정렬
        self.timebarlabel.setObjectName('TimeBarLabel')
        self.timebarlabel.setStyleSheet("color : black; font-size: 14pt; font-weight: bold")
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
        real_time = datetime.now().strftime('%Y.%m.%d')
        real_time2 = datetime.now().strftime('%H:%M:%S')
        self.timebarlabel.setText(real_time + " / " + real_time2)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MitigationTiltle()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
import os
import sys
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))  # 절대경로>디렉토리명


class MitigationTitleBar(QWidget):
    """제목 표시줄 위젯"""
    qss = """
        QWidget {
            background: rgb(0, 0, 0);
        }

        QLabel#TitleName{
            background: rgb(165, 165, 165);
            border-radius: 6px;
            font: bold 14px;
            color: rgb(0, 0, 0);
            padding: 4px 4px;
        }

        QPushButton {
            background: rgb(248, 108, 107);
            border-radius: 6px;
            border: none;
        }
        QPushButton:hover {
            background: rgb(248, 108, 107);
        }
        QPushButton:pressed {
            background: rgb(220, 152, 162);
        }"""

    # background: rgb(62, 74, 84);

    def __init__(self, parent=None):
        super(MitigationTitleBar, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)  # 상위 스타일 상속

        self.bar_height = 30
        self.parent = parent  # 부모 윈도우 설정
        self.has_clicked = False
        self.setStyleSheet(self.qss)

        # 타이틀 레이어 셋업 ----------------------------------------------------------------------------------------------
        layout = QHBoxLayout(self)  # 수평 방향 레이아웃
        layout.setContentsMargins(5, 5, 5, 5)  # 위젯의 여백 설정

        label = QLabel("SAMG")
        label.setObjectName('TitleName')
        label.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)  # 텍스트 정렬
        label.setFixedHeight(self.bar_height)
        label.setFixedWidth(70)

        widget1 = TimeBar(self, load_realtime=True)
        widget1.setFixedHeight(self.bar_height)
        widget1.setFixedWidth(200)

        label2 = ConditionBar(self)
        label2.setFixedHeight(self.bar_height)
        label2.setFixedWidth(120)

        label3 = QLabel("완화-01")
        label3.setObjectName('TitleName')
        label3.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        label3.setFixedHeight(self.bar_height)
        label3.setFixedWidth(250)

        btn_close = self.create_btn_with_image('close.png')
        btn_close.clicked.connect(self.close)

        # 타이틀에 들어가는 순서 (왼쪽부터 오른쪽 순으로) ---------------------------------------------------------------------
        layout.addWidget(label)
        layout.addWidget(widget1)
        # layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addSpacerItem(QSpacerItem(0, self.bar_height, QSizePolicy.Expanding))
        # layout.addWidget(label3)
        layout.addWidget(btn_close)

    def create_btn_with_image(self, icon_path):
        icon = os.path.join(ROOT_PATH, 'interface_image', icon_path)  # 경로 병합
        btn = QPushButton(self)
        btn.setIcon(QIcon(icon))
        btn.setIconSize(QSize(self.bar_height - 20, self.bar_height - 20))
        btn.setFixedSize(self.bar_height, self.bar_height)
        return btn

    def close(self):
        """버튼 명령: 닫기"""
        self.parent.close()

    def mousePressEvent(self, event):
        """오버로딩: 마우스 클릭 이벤트
        - 제목 표시줄 클릭시 이동 가능 플래그
        """
        if event.button() == Qt.LeftButton:
            self.parent.is_moving = True
            self.parent.offset = event.pos()
        else:
            self.parent.is_moving = False

    def mouseMoveEvent(self, event):
        """오버로딩: 마우스 이동 이벤트
        - 제목 표시줄 드래그시 창 이동
        """
        if self.parent.is_moving:
            self.parent.move(event.globalPos() - self.parent.offset)


class TimeBar(QWidget):
    qss = """
        QWidget#TimeBar {
            background: rgb(31, 39, 42);
        }

        QLabel#TimeBarLabel{
            background: rgb(165, 165, 165);
            border-radius: 6px;
            font: bold 14px;
            color: rgb(0, 0, 0);
            padding: 4px 4px;
        }
    """

    def __init__(self, parent, load_realtime: bool = False):
        super(TimeBar, self).__init__()
        self.parent = parent
        self.load_realtime = load_realtime
        self.setAttribute(Qt.WA_StyledBackground, True)  # 상위 스타일 상속

        self.setObjectName('TimeBar')
        self.setStyleSheet(self.qss)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)

        self.timebarlabel = QLabel('test')
        self.timebarlabel.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)  # 텍스트 정렬
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
        if self.load_realtime:
            real_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.timebarlabel.setText(real_time)
        else:
            # TODO 나중에 CNS 변수 사용시 real_time 부분 수정할 것.
            real_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            self.timebarlabel.setText(real_time)


class ConditionBar(QLabel):
    qss = """
        QLabel#ConditionBar {
            background: rgb(62, 74, 84);
            border-radius: 6px;
            font: bold 14px;
            color: rgb(0, 0, 0);
            padding: 4px 4px;
        }

        QLabel#ConditionBar[Condition="Normal"] {
            background: rgb(96, 186, 70);
        }
        QLabel#ConditionBar[Condition="Emergency"] {
            background: rgb(248, 108, 107);
        }
        QLabel#ConditionBar[Condition="Abnormal"] {
            background: rgb(255, 193, 7);
        }
    """

    def __init__(self, parent, init_condition: str = 'Normal'):
        super(ConditionBar, self).__init__()
        self.parent = parent  # ?
        self.setAttribute(Qt.WA_StyledBackground, True)  # 상위 스타일 상속 # ?
        self.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)  # 텍스트 정렬

        self.setObjectName('ConditionBar')
        self.setStyleSheet(self.qss)

        self.update_condition(init_condition)

    def update_condition(self, condition: str):
        self.setProperty("Condition", condition)
        self.setText(condition)
        self.setStyleSheet(self.qss)

    def contextMenuEvent(self, event) -> None:  # ?
        """ Condition Bar 기능 테스트 """
        menu = QMenu(self)
        test_action1 = menu.addAction("Emergency")
        test_action2 = menu.addAction("Normal")
        test_action3 = menu.addAction("Abnormal")

        test_action1.triggered.connect(lambda a, cond='Emergency': self.update_condition(cond))
        test_action2.triggered.connect(lambda a, cond='Normal': self.update_condition(cond))
        test_action3.triggered.connect(lambda a, cond='Abnormal': self.update_condition(cond))

        menu.exec_(event.globalPos())


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MitigationTitleBar()
    window.show()
    app.exec_()
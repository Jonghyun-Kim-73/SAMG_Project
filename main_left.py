import os
import sys
import pandas as pd
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from button import custom_button

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class MainLeftArea(QWidget):
    """ 왼쪽 디스플레이 위젯 """
    qss = """
        QWidget {
            background: rgb(14, 22, 100);    
        }
        QPushButton {
            background: rgb(62, 74, 84);
            border-radius: 3px;
            border: 2px inset rgb(62, 74, 84);
            font: bold 12px;
            color: rgb(255, 255, 255);          
        }
    """
    # background: rgb(14, 22, 24);

    def __init__(self, parent=None):
        super(MainLeftArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)  # 상위 스타일 상속
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 크기 조정
        self.setMinimumHeight(900-40)
        self.setMinimumWidth(int(1500*(2/3)))

        # self.setMinimumHeight(self.parent.height() - 40)
        # self.setMinimumWidth(int(self.parent.width() * (2/3))

        # 레이어 셋업 ====================================================================================================
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        label1 = FlowChartArea(self)

        layout.addWidget(label1)
        self.setLayout(layout)


class FlowChartArea(QWidget):
    qss = """
            QWidget {
                background: rgb(20, 39, 42);
                border-radius: 6px;
            }
        """

    def __init__(self, parent=None):
        super(FlowChartArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        self.setFixedHeight(self.parent.height())

        # layer = QVBoxLayout()     # 레이어 위에 버튼을 올릴 수는 없을까??
        #
        # text = QLabel('FlowChart Area')
        # text.setFixedHeight(20)
        # text.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)

        # btn = custom_button(self, x=200, y=100, w=100, h=200, text='Start', type=3)

        # layer.addWidget(text)
        # layer.addWidget(btn)

        # self.setLayout(layer)

        # custom_button(self, x=350, y=30, w=300, h=100, text='Start', type=3)

        self.update()

    def contextMenuEvent(self, event) -> None:
        """ FlowChartArea 에 기능 올리기  """
        menu = QMenu(self)  # 메뉴 생성
        add_btn_dia = menu.addAction("Add Diamond Button")
        add_btn_cir = menu.addAction("Add Circle Button")
        add_btn_rec = menu.addAction("Add Rectangle Button")

        add_btn_dia.triggered.connect(lambda a, pos=event.pos(), ele='dia': self.make_diagram(pos, ele))
        add_btn_cir.triggered.connect(lambda a, pos=event.pos(), ele='cir': self.make_diagram(pos, ele))
        add_btn_rec.triggered.connect(lambda a, pos=event.pos(), ele='rec': self.make_diagram(pos, ele))

        menu.exec_(event.globalPos())  # 실행

    def make_diagram(self, pos, ele):
        """ 클릭한 위치에 요소 위치 시키기 """
        if ele == 'dia':
            dig = custom_button(self, x=pos.x(), y=pos.y(), w=200, h=60, text='Start', type=3)
        if ele == 'cir':
            dig = custom_button(self, x=pos.x(), y=pos.y(), w=200, h=60, text='Start', type=2)
        if ele == 'rec':
            dig = custom_button(self, x=pos.x(), y=pos.y(), w=200, h=60, text='Start', type=1)

        dig.show()



if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MainLeftArea()
    window.show()
    app.exec_()
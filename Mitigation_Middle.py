import os
import sys
import pandas as pd
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))

class MitigationMiddleArea(QWidget):
    """ 중간 디스플레이 위젯 """
    qss = """
            QWidget {
                background: rgb(10, 10, 10);
            }
            QLabel {
                background: rgb(131, 131, 131);
                border-radius: 6px;
                color: rgb(255, 255, 255);
            }
            QTableWidget {
                background: rgb(131, 131, 131)
            }
        """

    def __init__(self, parent=None):
        super(MitigationMiddleArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 크기 조정
        self.setMinimumHeight(860)
        self.setMinimumWidth(1900/2)

        # 레이어 셋업
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        label1 = MiddleArea()

        layout.addWidget(label1)

        self.setLayout(layout)


class MiddleArea(QWidget):
    qss = """
            QWidget {
                background: rgb(255, 255, 255);
                border-radius: 6px;
            }
        """

    def __init__(self):
        super(MiddleArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(self.qss)

        self.setGeometry(0, 0, 300, 300)
        self.setStyleSheet(self.qss)


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MitigationMiddleArea()
    window.show()
    app.exec_()


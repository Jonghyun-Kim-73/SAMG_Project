import os
import sys
import pandas as pd
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtChart import *

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))


class MainRightArea(QWidget):
    """ 오른쪽 디스플레이 위젯 """
    qss = """
        QWidget {
            background: rgb(10, 10, 10);
        }
        QLabel {
            background: rgb(31, 39, 42);
            border-radius: 6px;
            color: rgb(255, 255, 255);
        }
    """
    # background: rgb(14, 22, 24);


    def __init__(self, parent = None):
        super(MainRightArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        self.setMinimumHeight(self.parent.height() - 40)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 5, 5, 5)

        self.setLayout(layout)

import os
import sys
from datetime import datetime

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))  # 절대경로>디렉토리명


class MitigationLeftArea(QWidget):
    """ 왼쪽 디스플레이 위젯 """
    qss = """
            QWidget {
                background: rgb(0, 0, 0);    
            }

            QLabel {
                background: rgb(131, 131, 131);
                border-radius: 6px;
                color: rgb(255, 255, 255);
            }

            QPushButton {
                background: rgb(62, 74, 84);
                border-radius: 3px;
                border: 2px inset rgb(62, 74, 84);
                font: bold 12px;
                color: rgb(255, 255, 255);          
            }
        """

    def __init__(self, parent=None):
        super(MitigationLeftArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 크기 조정
        self.setMinimumHeight(50)
        # self.setFixedWidth(400)

        # 레이어 셋업
        layout = QHBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        label1 = QPushButton('1')
        label2 = QPushButton('2')
        label3 = QPushButton('3')
        label4 = QPushButton('3')
        label5 = QPushButton('3')

        layout.addWidget(label1)
        layout.addWidget(label2)
        layout.addWidget(label3)
        layout.addWidget(label4)
        layout.addWidget(label5)

        self.setLayout(layout)

if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MitigationLeftArea()
    window.show()
    app.exec_()
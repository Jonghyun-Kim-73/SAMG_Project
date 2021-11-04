import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from TOOL_MatGP3 import TrendFlow

class table7(QWidget):
    """ 2. 이용가능수단확인 - L7 - 계산표 05 """
    qss = """
        QWidget {
            background: rgb(221, 221, 221);   
        }

        QPushButton {
            background-color: rgb(221, 221, 221);
            border: 1px solid rgb(0, 0, 0);       
            font-size: 14pt;
            font-weight: bold
        }
        """

    def __init__(self, parent=None):
        super(table7, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.shmem = parent.shmem

        self.setStyleSheet(self.qss)

        # 레이어 셋업
        layout = QVBoxLayout(self)
        label1 = QTextEdit("계산표-05, “장기 붕괴열 제거를 위한 냉각제 주입률“")  # splitter 사용 위함
        label1.setStyleSheet("font-size: 18pt;font-weight: bold;color:black")
        label1.setContentsMargins(10,10,10,30)
        label1.setDisabled(True)

        # --- 그래프 파트 수정 21.09.16 ---- #
        # TODO 향후 para_id 바꾸면 시뮬레이터와 자동 연결됨. <-- 인터페이스 디자이너와 상의 요망
        pic = TrendFlow(parent, w=500, h=500, para_name='Flow',
                       xtitle='Time Since Reactor Shutdown (Hours)', ytitle='Minimum Injection Flowrate (gpm)')
        pic.setGeometry(0, 0, 600, 600)
        layout.addWidget(label1)
        layout.addWidget(pic)
        # --- end ------------------------ #

        layout.addStretch(1)
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = table7()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
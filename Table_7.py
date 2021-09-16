import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Temp_All_Module.TOOL.TOOL_MatGP import Trend

StyleSheet = '''
QCheckBox {
    spacing: 5px;
    font-size:25px;
}

QCheckBox::indicator {
    width:  33px;
    height: 33px;
}
'''

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
        self.setStyleSheet(self.qss)

        # 레이어 셋업
        layout = QVBoxLayout(self)

        label1 = QLabel("계산표-05, “장기 붕괴열 제거를 위한 냉각제 주입률“")
        label1.setStyleSheet("font-size: 18pt;font-weight: bold")
        label1.setContentsMargins(10,10,10,30)

        # --- 그래프 파트 수정전 21.09.16 ---- #

        # pic = QPushButton()
        # pic.setIcon(QIcon("table7.png"))
        # pic.setStyleSheet("border:0px")
        # pic.setIconSize(QSize(600, 600))
        # layout.addWidget(label1)
        # layout.addWidget(pic)

        # --- 그래프 파트 수정 21.09.16 ---- #
        # TODO 향후 para_id 바꾸면 시뮬레이터와 자동 연결됨. <-- 인터페이스 디자이너와 상의 요망
        pic = Trend(parent, w=500, h=500, para_name='Flow', para_id='KCNTOMS', para_range=[0, 300],
                       xtitle='Time Since Reactor Shutdown (Hours)', ytitle='Minimum Injection Flowrate (gpm)')
        pic.setGeometry(0, 0, 600, 600)
        layout.addWidget(label1)
        layout.addWidget(pic)
        # --- end ------------------------ #

        layout.addStretch()
        self.setLayout(layout)

if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    app.setStyle("fusion")  # +++
    app.setStyleSheet(StyleSheet)
    window = table7()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
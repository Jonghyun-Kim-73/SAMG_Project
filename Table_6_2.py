import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

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

class table_6_2(QWidget):
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
        super(table_6_2, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 레이어 셋업
        layout = QVBoxLayout(self)

        label1 = QLabel("12. 증기발생기 급수 주입으로 인한 장기관심사항을 확인한다.")
        label1.setStyleSheet("font-size: 18pt;font-weight: bold")
        label1.setContentsMargins(10,10,10,30)

        layout.addWidget(label1)
        layout.addStretch()
        self.setLayout(layout)

if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    app.setStyle("fusion")  # +++
    app.setStyleSheet(StyleSheet)
    window = table_6_2()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
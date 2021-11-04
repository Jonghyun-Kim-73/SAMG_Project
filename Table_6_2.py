import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class table_6_2(QWidget):
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
        QTextEdit{
            font-size: 16pt;
            Color : black;
            border : 0px solid
            }
        """

    def __init__(self, parent=None):
        super(table_6_2, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 레이어 셋업
        layout = QVBoxLayout(self)

        label1 = QTextEdit("12. 증기발생기 급수 주입으로 인한 장기관심사항을 확인한다.")
        label1.setStyleSheet("font-size: 18pt;font-weight: bold")
        label1.setContentsMargins(10,10,10,30)
        label1.setDisabled(True)
        label1.setFixedHeight(40)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)

        layout.addWidget(label1)
        layout.addStretch()
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = table_6_2()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
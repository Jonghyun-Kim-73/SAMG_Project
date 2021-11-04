import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class table_6_7(QWidget):
    """ 중간 디스플레이 위젯 """
    qss = """
            QWidget {
            background: rgb(221, 221, 221);   
            }
            QTextEdit{
                font-size: 18pt;
                Color : black;
                border : 0px solid;
            }
            QPushButton{
                background-color: rgb(221,221,221);
                border: 1px solid rgb(0,0,0);       
                font-size: 14pt;
                font-weight: bold
            }
            QCheckBox {
                margin-top:0px;
                font-size:15px;
            }
            QCheckBox::indicator {
                width:  40px;
                height: 40px;
            }
            QCheckBox::indicator::unchecked {
                width:  40px;
                height: 40px;
                border : 1px solid;
            }
            QCheckBox::indicator::checked {
                image : url(./check.png);
                height:40px;
                width:40px;
            }        
        """

    def __init__(self, parent=None):
        super(table_6_7, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(self.qss)
        self.setContentsMargins(0, 0, 0, 0)

        # 기본 속성
        layout = QVBoxLayout(self)
        label = QTextEdit("12. 증기발생기 급수 주입으로 인한 장기관심사항을 확인한다.")
        label.setStyleSheet("font-size: 18pt;font-weight: bold")
        label.setContentsMargins(10, 10, 10, 20)
        label.setFixedHeight(50)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)
        layout.addWidget(label)
        layout.addWidget(label)

        label1 = QTextEdit("<p style=\"line-height:130%\"<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;<p>"
                        "<p style=\"line-height:130%\">&nbsp;&nbsp;<p>")
        label1.setStyleSheet("font-size: 14pt;font-weight: bold")

        self.s1 = []
        self.checkbox = []
        self.s1.append(QTextEdit('마. 복구된 기기들을 사용할 필요가 있는가 평가한다.'))
        self.s1.append(QTextEdit('&nbsp;&nbsp;1) 현재 전략을 대신하여 복구된 기기들을 (현재 사용하고 있지 않음)'))
        self.s1.append(QTextEdit('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;사용한 대체 전략을 수행할 수 있는가를 결정한다.'))
        self.s1.append(QTextEdit('&nbsp;&nbsp;2) 현재 전략을 대체전략으로 교체하는 데 따른 이점을 평가한다.'))
        self.s1.append(QTextEdit('&nbsp;&nbsp;3) 대체전략을 수행하여야 되는가를 결정한다.'))

        for i in range(5):
            self.s1[i].setDisabled(True)
            self.s1[i].setFixedHeight(40)  # QTextEdit 때문에 설정해줘야함 (addStretch 안먹음)
        self.s1[0].setStyleSheet("font-size: 14pt;font-weight: bold")
        self.layout1 = []
        for i in range(5):
            self.layout1.append(QHBoxLayout())
            self.layout1[i].setContentsMargins(20, 5, 0, 25)
            self.layout1[i].addWidget(self.s1[i])
            if not i == 0:
                self.layout1[i].addWidget(QCheckBox(self))
            layout.addLayout(self.layout1[i])
        self.layout1[1].setContentsMargins(20, 5, 0, 30)
        layout.addStretch(1)
        layout.setSizeConstraint(QLayout.SetMinimumSize)

        self.setLayout(layout)

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("fusion")
    window = table_6_7()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
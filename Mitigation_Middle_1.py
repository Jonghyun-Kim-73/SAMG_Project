import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MitigationMiddleArea_1(QWidget):
    """ 중간 디스플레이 위젯 """
    qss = """
            QWidget {
                background: rgb(128, 128, 128);
                border: 0px inset rgb(0, 0, 0);
            }
            QTableWidget {
                background: rgb(221, 221, 221);
            }
   
            QCheckBox {
                font-size:15px;
            }
            QCheckBox::indicator {
                width:  40px;
                height: 40px;
            
            }
            QCheckBox::indicator::unchecked {
                width:  40px;
                height: 40px;
                border : 1px solid black;
            }
            QCheckBox::indicator::checked {
                image : url(./check.png);
                height:30px;
                width:40px;
            }
        """

    def __init__(self, parent=None):
        super(MitigationMiddleArea_1, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.shmem = parent.shmem
        self.setStyleSheet(self.qss)

        # 레이어 셋업
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        label1 = M_MiddleArea(self)
        none = tableNone(self)

        self.split = QSplitter()
        self.split.addWidget(label1)
        self.split.addWidget(none)
        self.split.setSizes([1440,480])  # 슬라이드 초기 사이즈 지정
        self.split.setSizes([1440, 206])  # 슬라이드 초기 사이즈 지정
        layout.addWidget(self.split)
        self.setLayout(layout)

# 빈 page
class tableNone(QWidget):
    qss = """
           QWidget {
               background: rgb(221, 221, 221);   
               border: 2px inset rgb(0, 0, 0);
           }
       """
    def __init__(self, parent=None):
        super(tableNone, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(self.qss)
        # self.setFixedWidth(860)
        self.parent = parent

class M_MiddleArea(QWidget):
    qss = """
            QWidget {
                background: rgb(221, 221, 221);
                border: 0px solid rgb(0, 0, 0); 
            }
            QWidget#main {
                background: rgb(221, 221, 221);
                border: 2px solid rgb(0, 0, 0); 
            }
        """

    def __init__(self, parent):
        super(M_MiddleArea, self).__init__(parent=parent)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(self.qss)
        self.setObjectName("main")
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        condition = ConditionArea(self)
        scroll.setWidget(condition)

        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)

class ConditionArea(QWidget):
    qss = """
            QWidget {
                background: rgb(221, 221, 221);
            }
            QLabel{
                font-size: 18pt;
                Color : black;
            }
        """

    def __init__(self,parent):
        super(ConditionArea, self).__init__(parent=parent)
        layout = QVBoxLayout(self)
        self.setStyleSheet(self.qss)
        # para 1
        self.label1 = QLabel('<u>목적</u>')
        self.label1.setStyleSheet("font-weight: bold;")
        layout.addWidget(self.label1)

        self.s1 = []
        self.s1.append(QLabel('    증기발생기 급수 주입의 목적은 다음과 같다.'))
        self.s1.append(QLabel('        • RCS 열 제거'))
        self.s1.append(QLabel('        • RCS를 감압하여 RCS 내로 냉각재 공급을 가능하게 함'))
        self.s1.append(QLabel('        • 증기발생기 튜브의 크립 파열 방지'))
        self.s1.append(QLabel('        • 증기발생기로 생성된 핵분열 생성물의 세정'))
        self.s1.append(QLabel('        • 증기발생기 튜브 파손시 파손부를 통하여 RCS 내에 냉각재 공급'))

        self.layout1 = []
        for i in range(5):
            self.layout1.append(QHBoxLayout())
            self.layout1[i].setContentsMargins(0, 5, 0, 5)
            self.layout1[i].addWidget(self.s1[i])
            if i != 0:
                self.layout1[i].addStretch(1)
                self.layout1[i].addWidget(QCheckBox(self))
            layout.addLayout(self.layout1[i])

        # para 2
        self.label2 = QLabel('\n<u>수행 조건</u>')
        self.label2.setStyleSheet("font-weight: bold;")
        self.blank2 = QLabel('')
        layout.addWidget(self.blank2)
        layout.addWidget(self.label2)

        self.s2 = []
        self.s2.append(QLabel('        • 증기발생기 수위가 튜브 최상부 이하일 때'))
        self.s2.append(QLabel('        • 증기발생기 튜브 파손시 RCS 압력이 증기발생기 압력보다 낮을 떄'))

        self.layout2 = []
        for i in range(2):
            self.layout2.append(QHBoxLayout())
            self.layout2[i].setContentsMargins(0, 5, 0, 5)
            self.layout2[i].addWidget(self.s2[i])
            self.layout2[i].addStretch(1)
            self.layout2[i].addWidget(QCheckBox(self))
            layout.addLayout(self.layout2[i])

        # para 3
        self.label3 = QLabel('<u>종결 조건</u>')
        self.label3.setStyleSheet("font-weight: bold;")
        self.blank3 = QLabel('')
        layout.addWidget(self.blank3)
        layout.addWidget(self.label3)

        self.s3 = []
        self.s3.append(QLabel('        • 증기발생기 튜브가 과도하게 가열되어 열충격 발생으로 파손이 예상될 때'))
        self.s3.append(QLabel('        • 증기발생기 튜브 파손시 급수 주입이 증기발생기를 감압하여 RCS 냉각재가 파손부를 통하여 누설이 증가할 때'))
        self.s3.append(QLabel('        • 증기발생기 수위가 복구 되었을 때'))

        self.layout3 = []
        for i in range(3):
            self.layout3.append(QHBoxLayout())
            self.layout3[i].setContentsMargins(0, 5, 0, 5)
            self.layout3[i].addWidget(self.s3[i])
            self.layout3[i].addStretch(1)
            self.layout3[i].addWidget(QCheckBox(self))
            layout.addLayout(self.layout3[i])

        # para 4
        self.label4 = QLabel('<u>예상 발전소 거동</u>')
        self.label4.setStyleSheet("font-weight: bold;")
        self.blank4 = QLabel('')
        layout.addWidget(self.blank4)
        layout.addWidget(self.label4)

        self.s4 = []
        self.s4.append(QLabel('        • 증기발생기 수위 상승'))
        self.s4.append(QLabel('        • 증기발생기 증기 유량 증가'))
        self.s4.append(QLabel('        • 노심 출구와 고온관의 온도 감소'))
        self.s4.append(QLabel('        • U 튜브 상부에 수소 축적'))

        self.layout4 = []
        for i in range(4):
            self.layout4.append(QHBoxLayout())
            self.layout4[i].setContentsMargins(0, 5, 0, 5)
            self.layout4[i].addWidget(self.s4[i])
            self.layout4[i].addStretch(1)

            self.layout4[i].addWidget(QCheckBox(self))
            layout.addLayout(self.layout4[i])


        # para 5
        self.label5 = QLabel('<u>비상운전절차와의 관계</u>')
        self.label5.setStyleSheet("font-weight: bold;")
        self.blank5 = QLabel('')
        layout.addWidget(self.blank5)
        layout.addWidget(self.label5)

        self.s5 = []
        self.s5.append(QLabel('&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;• 상충성<font color=#dcdcdc>marginmarginmarginmarginmarginmarginmarginmarginmarginmarginmarginmarginmarginmarginmarginmarginmarginmargin</font>'))
        self.s5.append(QLabel('          비상운전절차서에는 급수가 있는 증기발생기가 있을 경우에 급수가 없는 증기발생기에는 급수를 주입하지 않고 있으나,\n          사고관리지침서에서는 증기발생기 U 튜브의 크립 파열을 방지하기 위하여 급수가 없는 증기발생기에도\n          급수 주입을 고려한다.'))
        self.s5.append(QLabel('        • 일치성'))
        self.s5.append(QLabel('          이전략은 기능회복지침 회복-06, "노심 및 원자로냉각재계통 열제거"와 일치한다. 증기발생기의 급속한 감압으로\n          발생할 수 있는 증기발생기에서의 불필요한 열응력 증가를 피하기 위하여 세심한 주의가 필요하며 정상적인 증기발생기\n          운전 절차는 이 지침에 적용될 수 있다.'))

        self.layout5 = []
        for i in range(4):
            self.layout5.append(QHBoxLayout())
            self.layout5[i].setContentsMargins(0, 5, 0, 5)
            self.layout5[i].addWidget(self.s5[i])
            if i%2==0:
                self.layout5[i].addStretch(1)
                self.layout5[i].addWidget(QCheckBox(self))
            layout.addLayout(self.layout5[i])

        # para 6
        self.label6 = QLabel('<u>계산 보조 도구</u>')
        self.label6.setStyleSheet("font-weight: bold;")
        self.blank6 = QLabel('')
        layout.addWidget(self.blank6)
        layout.addWidget(self.label6)

        self.s6 = []
        self.s6.append(QLabel('        • 계산표-05, "장기 붕괴열 제거를 위한 냉각재 주입율"'))

        self.layout6 = []
        for i in range(1):
            self.layout6.append(QHBoxLayout())
            self.layout6[i].setContentsMargins(0, 5, 0, 5)
            self.layout6[i].addWidget(self.s6[i])
            self.layout6[i].addStretch(1)
            self.layout6[i].addWidget(QCheckBox(self))
            layout.addLayout(self.layout6[i])

        layout.setSizeConstraint(QLayout.SetMinimumSize)

        self.setLayout(layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MitigationMiddleArea_1()
    app.setStyle("fusion")
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()

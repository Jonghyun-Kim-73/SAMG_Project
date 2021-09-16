import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Flag import Flag
from Mitigation_button import Custom
from Table_3_2 import table_3_2
from Table_3_3 import table_3_3
from Table_3_4 import table_3_4
from Table_3_5 import table_3_5
from Table_3_6 import table_3_6
from Table_4_2 import table_4_2
from Table_4_3 import table_4_3
from Table_5 import table5
from Table_7 import table7
from Table_Na_1 import tableNa_1
from Table_Na_2 import tableNa_2
from Table_ga import tableGa
from arrow import Arrow

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

class MitigationMiddleArea_4(QWidget):
    qss = """
        QWidget {
            background: rgb(128, 128, 128);   

        }
        QPushButton{
            background-color: rgb(221,221,221);
            border: 1px solid rgb(0,0,0);       
            font-size: 14pt;
            font-weight: bold
        }

        """

    def __init__(self, parent=None):
        super(MitigationMiddleArea_4, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.setMouseTracking(True)

        # 크기 조정
        self.setMinimumHeight(900 - 40)
        self.setMinimumWidth(1920)

        # 레이어 셋업 ====================================================================================================
        layout = QHBoxLayout(self)

        label1 = FlowChartArea(self)
        label1.setFixedWidth(1020)

        right = QVBoxLayout(self)
        # right.setContentsMargins(5,5,5,5)
        label2 = MitigationMiddleArea_3R()
        label2.setFixedWidth(860)
        right.addWidget(label2)

        right_bottom = QHBoxLayout()

        back = background()
        back.setFixedWidth(860)
        back.setFixedHeight(60)
        right_bottom.addWidget(back)

        right.addLayout(right_bottom)
        layout.addWidget(label1)
        layout.addLayout(right)
        self.setLayout(layout)

class FlowChartArea(QWidget):
    qss = """
        QWidget {
            background: rgb(221, 221, 221);
            border:0px;
        }
    """

    def __init__(self, parent=None):
        super(FlowChartArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.setMouseTracking(True)
        # self.setGeometry(0, 0, 1100, 1100)  # 1900*(3/4) = 1425
        scroll = QScrollArea()
        scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        flowchart = FlowChart()

        scroll.setWidget(flowchart)

        layout = QVBoxLayout()
        layout.addWidget(scroll)
        self.setLayout(layout)


class FlowChart(QWidget):
    qss = """
            QWidget {
                background: rgb(128, 128, 128);
                border: 0px solid rgb(0, 0, 0); 

            }
        """
    def __init__(self, parent=None):
        super(FlowChart, self).__init__()
        self.setGeometry(0, 0, 1300, 1100)  # 1900*(3/4) = 1425
        self.setStyleSheet(self.qss)
        self.color_clicked = QColor(128, 128, 128)
        self.color_click = QColor(0, 176, 218)

        # 커스텀버튼추가===================================================================================================
        # 하1
        self.line1 = Arrow(self, x=180, y=80, x2=180, y2=120, type=1)
        self.line1 = Arrow(self, x=180, y=190, x2=180, y2=260, type=1)
        self.line1 = Arrow(self, x=180, y=320, x2=180, y2=380, type=1)

        # 커스텀버튼 type : 3 dia 2 cir 1 rec 0 round_rec
        self.btn_4 = Custom(self, x=30, y=380, w=300, h=80,
                            text='Ⅴ.전략수행', type=0)
        self.btn_4.setObjectName("b4")

        self.btn_3 = Custom(self, x=30, y=260, w=300, h=100,
                            text='7. 증기발생기에 급수를\n실시할 때의\n제한사항들을 파악한다.', type=0)
        self.btn_3.setObjectName("b3")

        self.btn_2 = Custom(self, x=30, y=120, w=300, h=100,
                            text='6. 증기발생기 급수 주입\n경로를 선정한다.', type=0)
        self.btn_2.setObjectName("b2")

        self.btn_1 = Custom(self, x=30, y=10, w=300, h=80, text='Ⅳ.전략수행방법결정', type=0)
        self.btn_1.setObjectName("b1")

        self.installEventFilter(self.btn_2)
        self.installEventFilter(self.btn_3)
        self.installEventFilter(self.btn_4)


        self.btn_1.clicked.connect(self.clicked1)
        # self.btn_2.clicked.connect(self.clicked2)
        # self.btn_3.clicked.connect(self.clicked3)
        # self.btn_4.clicked.connect(self.clicked4)
        # self.btn_5.clicked.connect(self.clicked5)
        # self.btn_6.clicked.connect(self.clicked6)
        # self.btn_7.clicked.connect(self.clicked7)
        # self.btn_8.clicked.connect(self.clicked8)

        # ==============================================================================================================

        self.changetable = MitigationMiddleArea_3R()

        self.setMouseTracking(True)

    def clicked1(self):
        self.btn_1.shapes.setColor(QColor(0, 176, 218))
        self.btn_1.setObjectName("clicked")

        # popup
        self.popup = SubWindow(p_number=1,
                               p_title="Ⅳ.전략수행방법결정",
                               p_content='\nⅣ.전략수행방법결정을 시작합니다.')
        show = self.popup.showModal()
        # 예
        if Flag.m4_btn_clicked[1]:
            self.btn_1.shapes.setColor(self.color_clicked)
            self.btn_2.btn_clicked()  # 클릭한것처럼
            self.btn_2.setObjectName("clicked")
            self.btn_2.shapes.setColor(self.color_click)
            Flag.m4_btn_clicked[2] = True


    def paintEvent(self, event):
        p = QPainter(self)
        p.setPen(QPen(Qt.black))
        p.setFont(QFont('맑은 고딕', 14))

        if Flag.pg4_sat[2] and Flag.m4_page_num == 2:
            self.btn_2.shapes.setColor(self.color_clicked)
            self.btn_3.btn_clicked()  # 클릭한것처럼
            self.btn_3.setObjectName("clicked")
            self.btn_3.shapes.setColor(self.color_click)
        if Flag.pg4_dsat[2] and Flag.m4_page_num == 2:
            self.btn_2.shapes.setColor(self.color_clicked)
            self.btn_3.btn_clicked()  # 클릭한것처럼
            self.btn_3.setObjectName("clicked")
            self.btn_3.shapes.setColor(self.color_click)

        if Flag.pg4_sat[3] and Flag.m4_page_num == 3:
            self.btn_3.shapes.setColor(self.color_clicked)
            self.btn_4.btn_clicked()  # 클릭한것처럼
            self.btn_4.setObjectName("clicked")
            self.btn_4.shapes.setColor(self.color_click)
        if Flag.pg4_dsat[3] and Flag.m4_page_num == 3:
            self.btn_3.shapes.setColor(self.color_clicked)
            self.btn_4.btn_clicked()  # 클릭한것처럼
            self.btn_4.setObjectName("clicked")
            self.btn_4.shapes.setColor(self.color_click)



    def contextMenuEvent(self, event) -> None:
        """ FlowChart 에 기능 올리기  """
        menu = QMenu(self)  # 메뉴 생성
        add_btn_dia = menu.addAction("Add Diamond Button")
        add_btn_cir = menu.addAction("Add Circle Button")
        add_btn_rec = menu.addAction("Add Rectangle Button")

        add_btn_dia.triggered.connect(lambda a, pos=event.pos(), ele='dia': self.make_diagram(pos, ele))
        add_btn_cir.triggered.connect(lambda a, pos=event.pos(), ele='cir': self.make_diagram(pos, ele))
        add_btn_rec.triggered.connect(lambda a, pos=event.pos(), ele='rec': self.make_diagram(pos, ele))

        menu.exec_(event.globalPos())  # 실행

class SubWindow(QDialog):
    qss = """
            QWidget{
        background : rgb(180, 180, 180)
        }
            QLabel#title {
                font-size: 14pt; 

            }
            QLabel#data {
                font-size:12pt;
                border: 2px inset rgb(0, 0, 0);
                background: rgb(255, 255, 255);

            }
            QDialog{
            border: 2px solid rgb(0, 0, 0);       
            }
            QPushButton {
                color: rgb(0, 0, 0);
	            background-color: white;
	            border: 2px solid rgb(0, 0, 0);       
            }

        """

    def __init__(self, p_number=None, p_title = None, p_content = None, p_label1 = None, p_value1 = None, p_label2 = None, p_value2 = None):
        super().__init__()
        self.layout = QVBoxLayout()

        # 팝업 정보(메시지)
        self.p_number = p_number
        self.p_title = p_title
        self.p_content = p_content
        self.p_label1 = p_label1
        self.p_value1 = p_value1
        self.p_label2 = p_label2
        self.p_value2 = p_value2
        print(self.p_title)
        self.layout.addWidget(MyBar(self, p_number=self.p_number, p_title=self.p_title, p_content=self.p_content, p_label1=self.p_label1,
                                    p_value1=self.p_value1, p_label2=self.p_label2, p_value2=self.p_value2))

        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(self.qss)
        self.layout.addStretch(-1)
        self.setGeometry(100, 300, 550, 100)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pressing = False



    def onOKButtonClicked(self):
        print("오키")
        self.close()

    def onCancelButtonClicked(self):
        print("새로운창")

    def showModal(self):
        return super().exec_()


class MyBar(QWidget):
    qss = """
        QWidget{
        background : rgb(180, 180, 180)
        }
        QPushButton{
        background : rgb(218,218,218);
        border: 1px solid rgb(0, 0, 0);       
        }
        QTableWidget {
        gridline-color: rgb(0,0,0);
        font-size: 12pt;
        }
    """
    def __init__(self, parent, p_number=None, p_title = None, p_content = None, p_label1 = None, p_value1 = None, p_label2 = None, p_value2 = None):
    # def __init__(self,parent):
        super(MyBar, self).__init__()
        # self. cc = Custom.
        self.parent = parent
        self.setStyleSheet(self.qss)
        print(self.parent.width())
        self.p_number = p_number
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0,0,0,0)
        self.title = QLabel(p_title)

        #
        self.title.setFixedHeight(40)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)

        self.title.setStyleSheet("""
            font-size: 14pt; 
            background-color: rgb(91,155,213);
            border: 2px solid rgb(0, 0, 0);       
            color: white;
        """)
        #

        self.label = QLabel(p_content)
        self.label.setObjectName("title")

        #테두리 제거용
        self.label.setStyleSheet("""
                margin : 3px;    
            """)
        self.label.setAlignment(Qt.AlignCenter)
        self.subsub = QHBoxLayout()
        self.subLayout = QHBoxLayout()
        self.layout.addWidget(self.label)


        self.btnOK = QPushButton("예")
        self.btnCancel = QPushButton("아니오")

        self.btnOK.setFixedSize(100, 35)
        self.btnCancel.setFixedSize(100, 35)

        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.subLayout.setContentsMargins(50, 30, 50, 30)

        self.subLayout.addWidget(self.btnOK)

        if self.p_number!=1 and self.p_number!=2 and self.p_number!=10:
            self.subLayout.addWidget(self.btnCancel)


        self.layout.addLayout(self.subLayout)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

        self.start = QPoint(0, 0)
        self.pressing = False

    def onOKButtonClicked(self):
        #flag
        for i in range(1,2):
            if self.p_number == i:
                Flag.m4_btn_clicked[i] = True

        self.setDisabled(True)
        self.parent.close()


    def showModal(self):
        return super().exec_()

    def resizeEvent(self, QResizeEvent):
        super(MyBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.parent.width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        if self.pressing:
            self.end = self.mapToGlobal(event.pos())
            self.movement = self.end - self.start
            self.parent.setGeometry(self.mapToGlobal(self.movement).x(),
                                    self.mapToGlobal(self.movement).y(),
                                    self.parent.width(),
                                    self.parent.height())
            self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_close_clicked(self):
        self.parent.close()

    def btn_max_clicked(self):
        self.parent.showMaximized()

    def btn_min_clicked(self):
        self.parent.showMinimized()

class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.bb()

    def bb(self):
        # 초기 윈도우 사이즈
        # self.setGeometry(400, 200, 1000, 800)
        self.show()

#오른쪽 화면
class MitigationMiddleArea_3R(QWidget, QObject):
    qss = """
        QWidget {
            background: rgb(221, 221, 221);
        }
        QTableWidget {
            background: rgb(221, 221, 221);

        }
        QPushButton{
            background: rgb(221, 221, 221)
        }

    """

    def __init__(self, parent=None):
        super(MitigationMiddleArea_3R, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.central_widget = QStackedWidget()

        self.screen1 = tableNone()
        self.screen2 = table_4_2()
        self.screen3 = table_4_3()

        self.central_widget.addWidget(self.screen1)
        self.central_widget.addWidget(self.screen2)
        self.central_widget.addWidget(self.screen3)

        self.central_widget.setCurrentIndex(0)
        self.window_vbox = QVBoxLayout()

        self.window_vbox.setContentsMargins(0, 0, 0, 0)
        self.window_vbox.addWidget(self.central_widget)
        self.central_widget.update()
        self.setLayout(self.window_vbox)

    def paintEvent(self, e):
        if Flag.m4_btn_clicked[2]:
            self.central_widget.setCurrentIndex(1)
            Flag.m4_btn_clicked[2] = False
            Flag.m4_page_num = 2
        if Flag.m4_btn_clicked[3]:
            self.central_widget.setCurrentIndex(2)
            Flag.m4_btn_clicked[3] = False
            Flag.m4_page_num = 3
        if Flag.m4_btn_clicked[4]:
            self.central_widget.setCurrentIndex(3)
            Flag.m4_btn_clicked[4] = False
            Flag.m4_page_num = 4

        self.central_widget.update()


class tableNone(QWidget):
    def __init__(self, parent=None):
        super(tableNone, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent

class background(QWidget):
    qss = """
        QWidget {
            background: rgb(221, 221, 221);
        }
        QLabel {
            background: rgb(131, 131, 131);
            border-radius: 6px;
            color: rgb(255, 255, 255);
        }
        QTableWidget {
            background: rgb(221, 221, 221)
        }
        QPushButton{
            background: rgb(221, 221, 221)
        }
    """

    def __init__(self, parent=None):
        super(background, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)
        label3 = QPushButton("만족")
        label4 = QPushButton("병행")
        self.label5 = QPushButton("병행")
        label3.setFixedSize(200, 40)
        label4.setFixedSize(200, 40)
        self.label5.setFixedSize(200, 40)
        label3.setCursor(QCursor(Qt.PointingHandCursor))
        label4.setCursor(QCursor(Qt.PointingHandCursor))
        self.label5.setCursor(QCursor(Qt.PointingHandCursor))
        label3.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")
        label4.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")
        self.label5.setStyleSheet("QPushButton::hover{ background-color: rgb(0, 176, 218)}")

        label3.clicked.connect(self.click_sat)
        label4.clicked.connect(self.click_dsat)
        self.label5.clicked.connect(self.click_dsat)

        self.right_bottom = QHBoxLayout()
        self.right_bottom.addWidget(label3)
        self.right_bottom.addWidget(label4)

        self.setLayout(self.right_bottom)


    def paintEvent(self, QPaintEvent):
        if Flag.m4_page_num == 7:
            self.right_bottom.addWidget(self.label5)
        self.update()

    def click_sat(self):
        if Flag.m4_page_num == 2:
            Flag.m4_btn_clicked[3] = True
            Flag.pg4_sat[2] = True
        if Flag.m4_page_num == 3:
            Flag.m4_btn_clicked[4] = True
            Flag.pg4_sat[3] = True
        print("만족")

    def click_dsat(self):
        if Flag.m4_page_num == 2:
            Flag.m4_btn_clicked[3] = True
            Flag.pg4_dsat[2] = True
        if Flag.m4_page_num == 3:
            Flag.m4_btn_clicked[4] = True
            Flag.pg4_dsat[3] = True
        print("불만족")

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    app.setStyle("fusion")  # +++
    app.setStyleSheet(StyleSheet)
    window = MitigationMiddleArea_4()
    window.show()
    flow = FlowChart()

    app.installEventFilter(flow.btn_1)
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from TOOL_MatGP3 import TrendFlow

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

source1 = resource_path("x_button.png")

class Mitigation_popup2(QDialog):
    qss = """
            QDialog{
            background:rgb(180,180,180);
            border: 1px solid rgb(91,155,213);             
            }
        """

    def __init__(self, parent=None):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.addWidget(MyBar(self))
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(self.qss)
        self.layout.addStretch(-1)
        self.setWindowFlags(Qt.FramelessWindowHint)

        #popup1 이미지
        pic = TrendFlow(parent, w=500, h=500, para_name='Flow',
                    xtitle='Time Since Reactor Shutdown (Hours)', ytitle='Minimum Injection Flowrate (gpm)')
        pic.setGeometry(0, 0, 600, 600)
        self.layout.addWidget(pic)
        self.setLayout(self.layout)

    def showModal(self):
        return super().exec_()

class MyBar(QWidget):
    def __init__(self, parent):
        super(MyBar, self).__init__()
        self.parent = parent
        self.setMinimumHeight(40)
        self.setMinimumWidth(400)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel("첨부 D")

        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFixedSize(50,40)
        self.title.setStyleSheet("""
            background-color: rgb(91,155,213);
            border: 1px solid rgb(91,155,213);       
            color: white;
            font-size: 14pt;
        """)

        btn_close = QPushButton()
        btn_close.setIcon(QIcon(source1))
        btn_close.setStyleSheet("border:0px")
        btn_close.clicked.connect(self.close)
        btn_close.setIconSize(QSize(25,25))
        btn_close.setFixedSize(40,30)

        self.layout.addWidget(self.title)
        self.layout.addWidget(btn_close)
        self.setLayout(self.layout)


    def close(self):
        self.setDisabled(True)
        self.parent.close()

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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mitigation_popup2()
    ex.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    sys.exit(app.exec_())
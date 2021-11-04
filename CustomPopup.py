import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from Flag import Flag


class CustomPopup(QDialog):
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

    def __init__(self, p_title=None, p_content=None, p_label1=None, p_value1=None, p_label2=None, p_value2=None):
        super().__init__()
        self.layout = QVBoxLayout()

        # 팝업 정보(메시지)
        self.p_title = p_title
        self.p_content = p_content
        self.p_label1 = p_label1
        self.p_value1 = p_value1
        self.p_label2 = p_label2
        self.p_value2 = p_value2

        self.layout.addWidget(
            CustomPopupContent(self, p_title=self.p_title, p_content=self.p_content, p_label1=self.p_label1,
                               p_value1=self.p_value1, p_label2=self.p_label2, p_value2=self.p_value2))
        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet(self.qss)
        self.layout.addStretch(-1)
        self.setGeometry(100, 300, 550, 100)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.pressing = False

    def showModal(self):
        return super().exec_()

class CustomPopupContent(QWidget):
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

    def __init__(self, parent, p_title=None, p_content=None, p_label1=None, p_value1=None, p_label2=None,
                 p_value2=None):
        super(CustomPopupContent, self).__init__()
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.p_label1 = p_label1
        self.p_value1 = p_value1
        self.p_label2 = p_label2
        self.p_value2 = p_value2

        self.title = QLabel(p_title)
        self.title.setFixedHeight(40)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)
        self.title.setStyleSheet(
            "font-size: 14pt; background-color: rgb(91,155,213);border: 2px solid rgb(0, 0, 0);color: white;")

        self.label = QLabel(p_content)
        self.label.setObjectName("title")

        # 테두리 제거용
        self.label.setStyleSheet("margin : 3px;")
        self.label.setAlignment(Qt.AlignCenter)
        self.subsub = QHBoxLayout()
        self.subLayout = QHBoxLayout()
        self.layout.addWidget(self.label)

        self.btnOK = QPushButton("예")
        self.btnOK.setFixedSize(100, 35)
        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.btnCancel = QPushButton("아니오")
        self.btnCancel.setFixedSize(100, 35)
        self.btnCancel.clicked.connect(self.onCancelButtonClicked)
        self.subLayout.setContentsMargins(50, 30, 50, 30)
        self.subLayout.addWidget(self.btnOK)
        self.subLayout.addWidget(self.btnCancel)
        self.layout.addLayout(self.subLayout)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

        # Popup move
        self.start = QPoint(0, 0)
        self.pressing = False

    def onOKButtonClicked(self):
        # popup 예 button click
        if Flag.m2_page_num == 8:
            Flag.btn_popup_2_1 = True  # 제어 1로 이동
        if Flag.m2_page_num == 9:
            Flag.btn_popup_2_2 = True
        if Flag.m3_page_num == 7:
            Flag.btn_popup_3_1 = True
        if Flag.m3_page_num == 8:
            Flag.btn_popup_3_2 = True
        if Flag.m4_page_num == 4:
            Flag.btn_popup_4_1 = True
        if Flag.m5_page_num == 6:
            Flag.btn_popup_5_1 = True
        if Flag.m5_page_num == 7:
            Flag.btn_popup_5_2 = True
        if Flag.m6_page_num == 10:
            Flag.btn_popup_6_1 = True
        if Flag.m1:
            Flag.m1 = False
            Flag.move = True
        self.parent.close()

    def onCancelButtonClicked(self):
        self.parent.close()

    def showModal(self):
        return super().exec_()

    def resizeEvent(self, QResizeEvent):
        super(CustomPopupContent, self).resizeEvent(QResizeEvent)
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
    window = CustomPopup()
    window.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()

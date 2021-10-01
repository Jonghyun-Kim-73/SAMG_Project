import sys
import typing

from PyQt5.QtCore import Qt, QPointF, QPoint, QRectF, QEvent
from PyQt5.QtGui import QPolygonF, QBrush, QFont, QFontDatabase, QLinearGradient, QColor, QPen, QPainter
from PyQt5.QtWidgets import (QGraphicsView, QGraphicsScene, QApplication,
                             QGraphicsEllipseItem, QGraphicsSceneHoverEvent,
                             QGraphicsSceneMouseEvent, QGraphicsPolygonItem, QGraphicsItem, QGraphicsTextItem,
                             QGraphicsRectItem, QWidget, QVBoxLayout, QLabel, QHBoxLayout, QPushButton, QDialog)
import math

from Flag import Flag

class CustomButton(QGraphicsView):
    def __init__(self, parent=None, page=None, num=None, x=None, y=None, w=None, h=None, text=None, type=1, p_title=None, p_content=None):
        super(CustomButton, self).__init__(parent)
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.page = page
        self.num = num
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.type = type
        self.p_title = p_title
        self.p_content = p_content

        self.setGeometry(self.x, self.y, self.w+5, self.h+5)
        # background 투명
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        if self.type == 0:  # 둥근 사각형
            points = [
                QPoint(10, 0), QPoint(8, 1), QPoint(5, 2), QPoint(3, 3), QPoint(2, 5), QPoint(1, 8), QPoint(0, 10),
                QPoint(0, self.h - 10), QPoint(1, self.h - 8), QPoint(2, self.h - 5), QPoint(3, self.h - 3), QPoint(5, self.h - 2), QPoint(8, self.h - 1), QPoint(10, self.h),
                QPoint(self.w - 10, self.h), QPoint(self.w - 8, self.h - 1), QPoint(self.w - 5, self.h - 2), QPoint(self.w - 3, self.h - 3), QPoint(self.w - 2, self.h - 5), QPoint(self.w - 1, self.h - 8), QPoint(self.w, self.h - 10),
                QPoint(self.w, 10), QPoint(self.w - 1, 8), QPoint(self.w - 2, 5), QPoint(self.w - 3, 3), QPoint(self.w - 5, 2), QPoint(self.w - 8, 1), QPoint(self.w - 10, 0),
                QPoint(10, 0)]
            poly = QPolygonF(points)

        elif self.type == 1:  # 사각형
            points = [QPoint(0, 0),
                      QPoint(0, self.h),
                      QPoint(self.w, self.h),
                      QPoint(self.w, 0)]
            poly = QPolygonF(points)


        elif self.type == 2:  # 마름모
            points = [QPoint(self.w / 2, 0),
                      QPoint(0, self.h / 2),
                      QPoint(self.w / 2, self.h),
                      QPoint(self.w, self.h / 2)]
            poly = QPolygonF(points)

        elif self.type == 3:  # 육각형
            points = [QPoint(self.w/12, 0),
                      QPoint(0, self.h / 2),
                      QPoint(self.w/12, self.h),
                      QPoint(self.w / 12 * 11, self.h),
                      QPoint(self.w, self.h / 2),
                      QPoint(self.w / 12 * 11, 0),
                      QPoint(self.w / 12, 0)]
            poly = QPolygonF(points)

        self.poly_item = PolyButton(poly, self.page, self.num, self.text, self.p_title, self.p_content)
        self.poly_item.setBrush(QBrush(QColor(221, 221, 221)))
        self.scene.addItem(self.poly_item)

    # current Button paint
    def complete(self):
        self.poly_item.setBrush(QBrush(QColor(120, 120, 120)))
        self.poly_item.setPen(QPen(Qt.black, 3))
        self.setDisabled(True)


    # next Button paint
    def color(self):
        self.poly_item.setBrush(QBrush(QColor(0, 176, 218)))
        self.poly_item.setPen(QPen(Qt.black, 3))
        Flag.color_change[self.num] = True
    # 병행일때
    def color2(self):
        self.poly_item.setBrush(QBrush(QColor(224, 255, 255)))
        self.poly_item.setPen(QPen(Qt.black, 3))
        # Flag.color_change[self.num] = True
        self.setDisabled(True)


class PolyButton(QGraphicsPolygonItem, QPushButton):
    def __init__(self, poly, page=None, num=None, text=None, p_title=None, p_content=None):
        super().__init__(poly)
        self.setBrush(Qt.red)
        self.setAcceptHoverEvents(True)

        self.page = page
        self.num = num
        self.p_title = p_title
        self.p_content = p_content

        #text
        self.textItem = QGraphicsTextItem(self)
        self.textItem.setHtml('<center>%s</center>'%text)
        self.textItem.setTextWidth(self.boundingRect().width())
        self.font = QFont('맑은 고딕', 14)
        # self.font.setBold(True)
        self.textItem.setFont(self.font)

        rect = self.textItem.boundingRect()
        rect.moveCenter(self.boundingRect().center())
        self.textItem.setPos(rect.topLeft())



    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent'):
        if not Flag.color_change[self.num]:
            self.setBrush(QColor(180, 180, 180))
            QApplication.instance().setOverrideCursor(Qt.PointingHandCursor)

    def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent'):
        if not Flag.color_change[self.num]:
            self.setBrush(QColor(221, 221, 221))
        QApplication.instance().restoreOverrideCursor()

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent'):
        if Flag.m2_btn_clicked[self.num-1]:
            Flag.color_change[self.num] = True
            self.setBrush(QColor(0, 176, 218))
            self.setPen(QPen(Qt.black, 3))
            # popup
            ## page2 - button1, button2
            Flag.m2_btn_clicked[self.num] = False

            if self.page == 2 and self.num == 2:
                self.popup = CustomPopup(p_title=self.p_title, p_content=self.p_content)
                show = self.popup.showModal()
                if self.num == 2: Flag.m2_btn_clicked[2] = True

        if self.page == 2 and self.num == 1:
            self.popup = CustomPopup(p_title=self.p_title, p_content=self.p_content)
            show = self.popup.showModal()
            if self.num == 1: Flag.m2_btn_clicked[1] = True

#Custom Popup
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

    def __init__(self, p_title=None, p_content=None):
        super().__init__()
        self.layout = QVBoxLayout()

        # 팝업 정보(메시지)
        self.p_title = p_title
        self.p_content = p_content

        self.layout.addWidget(CustomPopupContent(self, p_title=self.p_title, p_content=self.p_content))
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
    def __init__(self, parent, p_title = None, p_content = None):
        super(CustomPopupContent, self).__init__()
        self.parent = parent
        self.setStyleSheet(self.qss)
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel(p_title)
        self.title.setFixedHeight(40)
        self.title.setAlignment(Qt.AlignCenter)
        self.layout.addWidget(self.title)
        self.title.setStyleSheet("""
            font-size: 14pt; 
            background-color: rgb(91,155,213);
            border: 2px solid rgb(0, 0, 0);       
            color: white;
        """)

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
        self.btnOK.setFixedSize(100, 35)
        self.btnOK.clicked.connect(self.onOKButtonClicked)
        self.subLayout.setContentsMargins(50, 30, 50, 30)
        self.subLayout.addWidget(self.btnOK)
        self.layout.addLayout(self.subLayout)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

        #Popup move
        self.start = QPoint(0, 0)
        self.pressing = False

    def onOKButtonClicked(self):
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
    win_main = CustomButton(x=0, y=0, w=300, h=110, text="Button", type=0)
    win_main.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()
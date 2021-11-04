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
    def __init__(self, parent=None, page=None, num=None, x=None, y=None, w=None, h=None, text=None, type=1):
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
        self.setGeometry(self.x, self.y, self.w + 5, self.h + 5)

        if page == 1:
            self.w = self.w - 3
            self.h = self.h - 3

        # background 투명
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        if self.type == 0:  # 둥근 사각형
            points = [
                QPoint(10, 0), QPoint(8, 1), QPoint(5, 2), QPoint(3, 3), QPoint(2, 5), QPoint(1, 8), QPoint(0, 10),
                QPoint(0, self.h - 10), QPoint(1, self.h - 8), QPoint(2, self.h - 5), QPoint(3, self.h - 3),
                QPoint(5, self.h - 2), QPoint(8, self.h - 1), QPoint(10, self.h),
                QPoint(self.w - 10, self.h), QPoint(self.w - 8, self.h - 1), QPoint(self.w - 5, self.h - 2),
                QPoint(self.w - 3, self.h - 3), QPoint(self.w - 2, self.h - 5), QPoint(self.w - 1, self.h - 8),
                QPoint(self.w, self.h - 10),
                QPoint(self.w, 10), QPoint(self.w - 1, 8), QPoint(self.w - 2, 5), QPoint(self.w - 3, 3),
                QPoint(self.w - 5, 2), QPoint(self.w - 8, 1), QPoint(self.w - 10, 0),
                QPoint(10, 0)]
            poly = QPolygonF(points)

        elif self.type == 1:  # 사각형
            points = [QPoint(0, 0),
                      QPoint(0, self.h),
                      QPoint(self.w, self.h),
                      QPoint(self.w, 0),
                      QPoint(0, 0)]
            poly = QPolygonF(points)

        elif self.type == 2:  # 마름모
            points = [QPoint(self.w / 2 - 1, 0),
                      QPoint(0, self.h / 2 - 1),
                      QPoint(self.w / 2 - 1, self.h - 1),
                      QPoint(self.w - 1, self.h / 2 - 1)]
            poly = QPolygonF(points)

        elif self.type == 3:  # 육각형
            points = [QPoint(self.w / 12, 0),
                      QPoint(0, self.h / 2),
                      QPoint(self.w / 12, self.h),
                      QPoint(self.w / 12 * 11, self.h),
                      QPoint(self.w, self.h / 2),
                      QPoint(self.w / 12 * 11, 0),
                      QPoint(self.w / 12, 0)]
            poly = QPolygonF(points)

        self.poly_item = PolyButton(poly, self.page, self.num, self.text)
        self.poly_item.setBrush(QBrush(QColor(221, 221, 221)))
        self.scene.addItem(self.poly_item)

    # complete Button paint
    def complete(self):
        self.poly_item.setBrush(QBrush(QColor(120, 120, 120)))
        self.poly_item.setPen(QPen(Qt.black, 3))

    # next Button paint
    def color(self):
        if self.page == 1:
            self.poly_item.setBrush(QBrush(QColor(0, 176, 218)))
            self.poly_item.setPen(QPen(Qt.black, 3))
        if self.page == 2:
            self.poly_item.setBrush(QBrush(QColor(0, 176, 218)))
            self.poly_item.setPen(QPen(Qt.black, 3))
        if self.page == 3:
            self.poly_item.setBrush(QBrush(QColor(0, 176, 218)))
            self.poly_item.setPen(QPen(Qt.black, 3))
        if self.page == 4:
            self.poly_item.setBrush(QBrush(QColor(0, 176, 218)))
            self.poly_item.setPen(QPen(Qt.black, 3))
        if self.page == 5:
            self.poly_item.setBrush(QBrush(QColor(0, 176, 218)))
            self.poly_item.setPen(QPen(Qt.black, 3))
        if self.page == 6:
            self.poly_item.setBrush(QBrush(QColor(0, 176, 218)))
            self.poly_item.setPen(QPen(Qt.black, 3))

    # 병행 color
    def color2(self):
        self.poly_item.setBrush(QBrush(QColor(224, 255, 255)))
        self.poly_item.setPen(QPen(Qt.black, 3))
        # self.setDisabled(True)

    # 버튼 초기화
    def color_init(self):
        self.poly_item.setBrush(QBrush(QColor(221, 221, 221)))
        self.poly_item.setPen(QPen(Qt.black, 1))


class PolyButton(QGraphicsPolygonItem, QPushButton):
    def __init__(self, poly, page=None, num=None, text=None):
        super().__init__(poly)
        self.setBrush(Qt.red)
        self.setAcceptHoverEvents(True)

        self.page = page
        self.num = num

        # text
        self.textItem = QGraphicsTextItem(self)
        self.textItem.setHtml('<center>%s</center>' % text)
        self.textItem.setTextWidth(self.boundingRect().width())
        self.font = QFont('맑은 고딕', 14)
        self.textItem.setFont(self.font)

        rect = self.textItem.boundingRect()
        rect.moveCenter(self.boundingRect().center())
        self.textItem.setPos(rect.topLeft())

    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent'):
        if self.page == 1:
            self.setBrush(QColor(180, 180, 180))
        if self.page == 2:
            self.setBrush(QColor(180, 180, 180))
        if self.page == 3:
            self.setBrush(QColor(180, 180, 180))
        if self.page == 4:
            self.setBrush(QColor(180, 180, 180))
        if self.page == 5:
            self.setBrush(QColor(180, 180, 180))
        if self.page == 6:
            self.setBrush(QColor(180, 180, 180))
        QApplication.instance().setOverrideCursor(Qt.PointingHandCursor)

    def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent'):
        if self.page == 1:
            if Flag.color[self.num] == 1:
                self.setBrush(QColor(224, 255, 255))
            elif Flag.color[self.num] == 2:
                self.setBrush((QColor(0, 176, 218)))
            elif Flag.color[self.num] == 3:
                self.setBrush(QColor(120, 120, 120))
            else:
                self.setBrush(QColor(221, 221, 221))
        if self.page == 2:
            if Flag.color2[self.num] == 1:
                self.setBrush(QColor(224, 255, 255))
            elif Flag.color2[self.num] == 2:
                self.setBrush((QColor(0, 176, 218)))
            elif Flag.color2[self.num] == 3:
                self.setBrush(QColor(120, 120, 120))
            else:
                self.setBrush(QColor(221, 221, 221))
        if self.page == 3:
            if Flag.color3[self.num] == 1:
                self.setBrush(QColor(224, 255, 255))
            elif Flag.color3[self.num] == 2:
                self.setBrush((QColor(0, 176, 218)))
            elif Flag.color3[self.num] == 3:
                self.setBrush(QColor(120, 120, 120))
            else:
                self.setBrush(QColor(221, 221, 221))
        if self.page == 4:
            if Flag.color4[self.num] == 1:
                self.setBrush(QColor(224, 255, 255))
            elif Flag.color4[self.num] == 2:
                self.setBrush((QColor(0, 176, 218)))
            elif Flag.color4[self.num] == 3:
                self.setBrush(QColor(120, 120, 120))
            else:
                self.setBrush(QColor(221, 221, 221))
        if self.page == 5:
            if Flag.color5[self.num] == 1:
                self.setBrush(QColor(224, 255, 255))
            elif Flag.color5[self.num] == 2:
                self.setBrush((QColor(0, 176, 218)))
            elif Flag.color5[self.num] == 3:
                self.setBrush(QColor(120, 120, 120))
            else:
                self.setBrush(QColor(221, 221, 221))
        if self.page == 6:
            if Flag.color6[self.num] == 1:
                self.setBrush(QColor(224, 255, 255))
            elif Flag.color6[self.num] == 2:
                self.setBrush((QColor(0, 176, 218)))
            elif Flag.color6[self.num] == 3:
                self.setBrush(QColor(120, 120, 120))
            else:
                self.setBrush(QColor(221, 221, 221))

        QApplication.instance().restoreOverrideCursor()

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent'):
        if self.page == 1:
            Flag.btn_clicked[self.num] = True
            Flag.btn_clicked_1[self.num] = True
        if self.page == 2:
            Flag.m2_btn_clicked[self.num] = True
        elif self.page == 3:
            Flag.m3_btn_clicked[self.num] = True
        elif self.page == 4:
            Flag.m4_btn_clicked[self.num] = True
        elif self.page == 5:
            Flag.m5_btn_clicked[self.num] = True
        elif self.page == 6:
            Flag.m6_btn_clicked[self.num] = True

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_main = CustomButton(x=0, y=0, w=300, h=110, text="Button", type=2)
    win_main.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    app.exec_()

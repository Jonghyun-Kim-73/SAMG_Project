import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QFont, QPolygon
from PyQt5.QtCore import Qt, QPoint


class Arrow(QWidget):
    def __init__(self, parent=None, x=None, y=None, x2=None, y2=None, type=0):
        super(Arrow, self).__init__(parent)
        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.type = type
        self.setGeometry(self.x, self.y, self.x2, self.y2)
        self.setGeometry(0, 0, 3500, 3500)

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_polygon(qp)
        qp.end()

    def draw_polygon(self, qp):
        #type 0123 상하좌우
        points = []
        if self.type == 0:
            points = [
                QPoint(self.x2, self.y2 - 10),
                QPoint(self.x2-5, self.y2),
                QPoint(self.x2+5, self.y2)
            ]
        elif self.type == 1:
            points = [
                QPoint(self.x2, self.y2 + 10),
                QPoint(self.x2 - 5, self.y2),
                QPoint(self.x2 + 5, self.y2)
            ]
        elif self.type == 2:
            points = [
                QPoint(self.x2-10, self.y2),
                QPoint(self.x2, self.y2-5),
                QPoint(self.x2, self.y2+5)
            ]
        elif self.type == 3:
            points = [
                QPoint(self.x2+10, self.y2),
                QPoint(self.x2, self.y2-5),
                QPoint(self.x2, self.y2+5)
            ]
        polygon = QPolygon(points)
        qp.setPen(QPen(Qt.black, 1))
        qp.setBrush(QBrush(Qt.black))
        qp.drawPolygon(polygon)
        qp.drawLine(self.x, self.y, self.x2, self.y2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_main = Arrow(x=100, y=100, x2=100, y2=30, type=1)
    win_main.show()
    app.exec_()
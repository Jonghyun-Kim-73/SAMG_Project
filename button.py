import sys

from PyQt5.QtCore import QEvent, QPoint, QPointF, Qt, QRect, QObject
from PyQt5.QtGui import QColor, QPainter, QPainterPath, QPolygonF, QMouseEvent, QPen, QFont, QCursor
from PyQt5.QtWidgets import QApplication, QToolTip, QWidget, QPushButton, QLabel, QHBoxLayout, QVBoxLayout, QDialog, \
    QMessageBox

class Shape(QPushButton):
    def __init__(self):
        self.mypath = QPainterPath()
        self.col = QColor()

    def path(self):
        return self.mypath

    def color(self):
        return self.col

    def setPath(self, path):
        self.mypath = path

    def setPath2(self,path):
        self.mypath = path

    def setPosition(self, position):
        self.pos = position

    def setPen(self, pen):
        self.pen = pen

    def setColor(self, color):
        self.col = color


class Custom(QPushButton):
    def __init__(self, parent=None, x=None, y=None, w=None, h=None, text=None, type=1, msg_text=None,msg_text2=None,msg_text3=None
                 , msg_text4=None,connected_btn=None, connected_btn_2=None, connected_btn_3=None, b=None):
        super(Custom, self).__init__(parent)
        self.msg_box = QMessageBox()
        self.click = False #버튼 클릭 flag
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.type = type
        self.msg_text = msg_text
        self.msg_text2 = msg_text2
        self.msg_text3 = msg_text3
        self.msg_text4 = msg_text4
        self.setGeometry(self.x, self.y, self.w, self.h)
        self.shapePath = QPainterPath()
        self.shapes = Shape()
        #클릭o 1 / 클릭x 0
        self.color = False
        if self.type == 0:      # 둥근 사각형
            self.shapePath.addRoundedRect(70, 10, self.w-140, self.h-20, 10, 10)
        if self.type == 1:      # 사각형
            self.shapePath.addRect(70, 10, self.w-140, self.h-20)
        elif self.type == 2:    # 타원
            self.shapePath.addEllipse(0, 0, self.w, self.h)
        elif self.type == 3:    # 마름모
            points = [QPoint(self.w / 2, 0),
                      QPoint(0, self.h / 2),
                      QPoint(self.w / 2, self.h),
                      QPoint(self.w, self.h / 2),
                      QPoint(self.w / 2, 0)]
            poly = QPolygonF(points)
            self.shapePath.addPolygon(poly)
        elif self.type == 4:  # 육각형
            points = [QPoint(self.w / 12 * 11, 0),
                      QPoint(self.w/12, 0),
                      QPoint(0, self.h / 2),
                      QPoint(self.w/12, self.h),
                      QPoint(self.w / 12 * 11, self.h),
                      QPoint(self.w, self.h / 2),
                      QPoint(self.w / 12 * 11, 0)
                      ]
            poly = QPolygonF(points)
            self.shapePath.addPolygon(poly)

        self.setMouseTracking(True)
        self.createShape(self.shapePath, QColor(221,221,221),QPen(Qt.black, 1))

        self.clicked.connect(self.btn_clicked)
        self.show()

    def btn_clicked(self):
        self.shapes.setColor(QColor(0, 176, 218))   #클릭시 바로 색 변환
        self.click = True

    def paintEvent(self, e):
        rect = QRect(0, 0, self.w, self.h)
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.black, 1)) # 도형 테두리
        if self.click:
            painter.setPen(QPen(Qt.black, 3))  # 도형 테두리
        painter.setBrush(self.shapes.color())
        painter.setFont(QFont('맑은 고딕', 14))
        painter.drawPath(self.shapes.path())
        painter.drawText(rect, Qt.AlignCenter, self.text)
        # self.update()

    def eventFilter(self, source, e):
        if source.objectName() == "b1" or source.objectName() == "b2" or source.objectName() == "b3" or source.objectName() == "b4" or source.objectName() == "b5" or source.objectName() == "b6" or source.objectName() == "b7" or source.objectName() == "b8"\
                or source.objectName() == "b9" or source.objectName() == "b10"or source.objectName() == "b11"or source.objectName() == "b12"\
                or source.objectName() == "b13"or source.objectName() == "b14"or source.objectName() == "b15"or source.objectName() == "b16"\
                or source.objectName() == "b17"or source.objectName() == "b18":
            if e.type() == QEvent.MouseMove:
                if e.buttons() == Qt.NoButton:
                    if source.shapes.path().contains(e.pos()):
                        index = True
                    else:
                        index = -1
                    if index != -1:
                        source.setCursor(QCursor(Qt.PointingHandCursor))
                        source.shapes.setColor(QColor(180, 180, 180))
                        source.update()
                    else:
                        source.setCursor(QCursor(Qt.CustomCursor))
                        source.shapes.setColor(QColor(221, 221, 221))
                return False
            return False
        return False


    def itemIndexAt(self, pos):#안에들어가면true
        if self.shapes.path().contains(QPointF(pos)):
            return True
        else:
            return -1

    def createShape(self, path, color, pen):
        self.shape = Shape()
        self.shape.setPath(path)
        self.shape.setColor(color)
        # self.shape.setPen(pen)
        self.shape.color()
        self.shapes = self.shape

    def flag(self):
        return self.b




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Custom(x=500, y=500, w=300, h=300, text='bibi', type=4)
    ex.setObjectName("b1")
    ex.show()
    app.installEventFilter(ex)
    sys.exit(app.exec_())
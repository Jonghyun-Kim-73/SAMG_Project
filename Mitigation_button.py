import sys

from PyQt5.QtCore import QEvent, QPoint, QPointF, Qt, QRect, QObject, pyqtSignal, QTimer
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

    def setColor(self, color):
        self.col = color


class Custom(QPushButton):
    cursorMove = pyqtSignal(object)
    def __init__(self, parent=None, x=None, y=None, w=None, h=None, text=None, type=1, msg_text=None,msg_text2=None,msg_text3=None
                 , msg_text4=None,connected_btn=None, connected_btn_2=None, connected_btn_3=None, b=None):
        super(Custom, self).__init__(parent)
        self.msg_box = QMessageBox()
        self.click = False #버튼 클릭 flag
        # self.raise_()
        # self.b = b
        self.posx=0
        self.posy=0
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
        # self.setCheckable(True)
        # self.setMouseTracking(True)
        self.shapePath = QPainterPath()
        # self.shapePath2 = QPainterPath()
        self.shapes = Shape()
        #클릭o 1 / 클릭x 0
        self.color = False
        if self.type == 0:      # 둥근 사각형
            self.shapePath.addRoundedRect(10, 10, self.w-20, self.h-20, 10, 10)
            # self.shapePath2.addRoundedRect(10, 10, self.w+10 , self.h+10,10,10)
        if self.type == 1:      # 사각형
            self.shapePath.addRect(0, 0, self.w, self.h)
            # self.shapePath2.addRect(10, 10, self.w-10, self.h-10)
        elif self.type == 2:    # 타원
            self.shapePath.addEllipse(0, 0, self.w, self.h)
            # self.shapePath2.addRect(2, 2, self.w - 2, self.h - 2)
        elif self.type == 3:    # 마름모
            points = [QPoint(self.w / 2, 0),
                      QPoint(0, self.h / 2),
                      QPoint(self.w / 2, self.h),
                      QPoint(self.w, self.h / 2)]
            poly = QPolygonF(points)
            self.shapePath.addPolygon(poly)
            # self.shapePath2.addPolygon(poly)
        elif self.type == 4:  # 육각형
            points = [QPoint(self.w/12, 10),
                      QPoint(10, self.h / 2),
                      QPoint(self.w/12, self.h-10),
                      QPoint(self.w / 12 * 11, self.h-10),
                      QPoint(self.w-10, self.h / 2),
                      QPoint(self.w / 12 * 11, 10),
                      QPoint(self.w / 12, 10)
                      ]
            poly = QPolygonF(points)
            self.shapePath.addPolygon(poly)
            # self.shapePath2.addPolygon(poly)

        self.setMouseTracking(True)
        self.createShape(self.shapePath, QColor(221,221,221))
        self.cursorMove.connect(self.handleCursorMove)
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.pollCursor)
        self.timer.start()
        self.cursor = None
        # self.resize(400, 400)
        # app.installEventFilter(self)
        self.clicked.connect(self.btn_clicked)
        self.show()


        # self.update()?
    def btn_clicked(self):
        self.shapes.setColor(QColor(0, 176, 218))
        self.click = True

    def pollCursor(self):
        pos = QCursor.pos()
        if pos != self.cursor:
            self.cursor = pos
            self.cursorMove.emit(pos)

    def handleCursorMove(self, pos):
        self.position = pos
        print(pos)

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
        self.update()

    def mouseMoveEvent(self, event):
        self.posx = event.x()
        self.posy = event.y()

        print("%d %d"%(self.position.x(), self.posy))

    def eventFilter(self, source, e):
        if source.objectName() == "b1" or source.objectName() == "b2" or source.objectName() == "b3" or source.objectName() == "b4" or source.objectName() == "b5" or source.objectName() == "b6" or source.objectName() == "b7" or source.objectName() == "b8" \
                or source.objectName() == "b9" or source.objectName() == "b10" or source.objectName() == "b11" or source.objectName() == "b12" \
                or source.objectName() == "b13" or source.objectName() == "b14" or source.objectName() == "b15" or source.objectName() == "b16" \
                or source.objectName() == "b17" or source.objectName() == "b18":
            if e.type() == QEvent.MouseMove:
                if e.buttons() == Qt.NoButton:
                    if source.shapes.path().contains(e.pos()):
                        index = True
                    else:
                        index = -1
                    # if self.color==0 :
                    if index != -1:
                        source.setCursor(QCursor(Qt.PointingHandCursor))
                        # if e.buttons() == Qt.LeftButton and source.color == False:#안누름
                        #     source.color = True
                        #     self.shapes.setColor(QColor(0, 176, 218))
                        # # if self.shapes.color() == QColor(0, 176, 218):
                        # #    print("aaaaaaa")
                        # if source.color==False and self.shapes.color() != QColor(0, 176, 218):

                        # print("ddd", self.shapes.color())
                        source.shapes.setColor(QColor(180, 180, 180))
                        # print("들어옴")
                        source.update()
                    # selectedColor().name()
                    else:
                        source.setCursor(QCursor(Qt.CustomCursor))
                        source.shapes.setColor(QColor(221, 221, 221))

                return False
            return False
        return False


        # if source.shapes.path().contains(e.pos()):
        #     index = True
        # else:
        #     index = -1
        #     # if self.color==0 :
        # if index != -1:
        #     source.setCursor(QCursor(Qt.PointingHandCursor))
        #     source.shapes.setColor(QColor(180, 180, 180))
        #     # print("들어옴")
        #     source.update()
        #     # selectedColor().name()
        # else:
        #     source.setCursor(QCursor(Qt.CustomCursor))
        #     source.shapes.setColor(QColor(221, 221, 221))
    #
    #     return False
    #
    # return False
    # return False
    # def mousePressEvent(self, e):
    #     index = self.itemIndexAt(e.pos())
    #     #
    #     # if index != -1 and e.buttons() == Qt.LeftButton and self.color==1:
    #     #     self.color=0
    #     #     print("Left click")
    #     #     self.shapes.setColor(QColor(0, 176, 218))
    #     #     if self.type == 0:
    #     #         reply = self.msg_box.question(self, self.msg_text, self.msg_text2, self.msg_box.Ok)
    #     #
    #     #         if reply == self.msg_box.Ok:
    #     #             self.setDisabled(True)
    #     #             self.shapes.setColor(QColor(128, 128, 128))
    #     #             self.cnt_btn.btn_clicked_ver2()
    #     #
    #     #     if self.type == 1:
    #     #
    #     #         reply = self.msg_box.question(self, self.msg_text, self.msg_text2, self.msg_box.Ok)
    #     #         if reply == self.msg_box.Ok:
    #     #             self.setDisabled(True)
    #     #             self.shapes.setColor(QColor(128, 128, 128))
    #     #             self.popup()
    #     #             self.cnt_btn.btn_clicked_ver2()
    #     #
    #     #     if self.type == 2:
    #     #         reply = self.msg_box.question(self, self.msg_text, self.msg_text2, self.msg_box.Ok)
    #     #         if reply == self.msg_box.Ok:
    #     #             self.setDisabled(True)
    #     #             self.shapes.setColor(QColor(128, 128, 128))
    #     #             self.cnt_btn.btn_clicked_ver2()
    #     #
    #     #     if self.type == 3:
    #     #         popup = SubWindow()
    #     #         popup.setWindowTitle(self.msg_text)
    #     #         r = popup.showModal()
    #     #         if r:
    #     #             print("확인")
    #     #
    #     #     # self.preMousePosition = e.pos()
    #     if index != -1 and e.buttons() == Qt.LeftButton:
    #         print("Left click")
    #         self.shapes.setColor(QColor(0, 0, 0))
    #         self.shapes.setObjectName("clicked")
            # self.preMousePosition = e.pos()
        # if self.change_color:
        #     self.change_color = False
        #     self.circle_color = QColor(0, 128, 128, 128)
        # else:
        #     self.change_color = True
        #     self.circle_color = QColor(0, 176, 218)



    def itemIndexAt(self, pos):#안에들어가면true
        if self.shapes.path().contains(QPointF(pos)):
            return True
        else:
            return -1

    def createShape(self, path, color):
        self.shape = Shape()
        self.shape.setPath(path)
        self.shape.setColor(color)
        self.shape.color()
        self.shapes = self.shape

    def flag(self):
        return self.b



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Custom(x=100, y=100, w=300, h=300, text='bibi', type=0)
    ex.setObjectName("b1")
    ex.show()
    app.installEventFilter(ex)
    sys.exit(app.exec_())
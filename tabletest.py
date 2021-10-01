from PyQt5 import QtGui
from PyQt5.QtCore import QPoint
from PyQt5.QtWidgets import QApplication, QMainWindow, QGraphicsScene, QGraphicsView, QGraphicsItem
from PyQt5.QtGui import QPen, QBrush, QPolygonF
from PyQt5.Qt import Qt

import sys


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 QGraphicView"
        self.top = 200
        self.left = 500
        self.width = 600
        self.height = 500
        # self.setAcceptHoverEvents(True)
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createGraphicView()

        self.show()

    def createGraphicView(self):
        self.scene = QGraphicsScene()
        self.greenBrush = QBrush(Qt.green)
        self.grayBrush = QBrush(Qt.gray)

        self.pen = QPen(Qt.red)

        graphicView = QGraphicsView(self.scene, self)
        graphicView.setGeometry(0, 0, 600, 500)

        self.shapes()

    def shapes(self):
        points = [QPoint(20, 0),
                  QPoint(0, 20),
                  QPoint(20, 40),
                  QPoint(40, 20)]
        poly = QPolygonF(points)

        ellipse = self.scene.addEllipse(20, 20, 200, 200, self.pen, self.greenBrush)
        rect = self.scene.addRect(-100, -100, 200, 200, self.pen, self.grayBrush)
        aa = self.scene.addPolygon(poly)
        ellipse.setFlag(QGraphicsItem.ItemIsMovable)
        rect.setFlag(QGraphicsItem.ItemIsMovable)
        aa.setFlag(QGraphicsItem.ItemIsMovable)
        ellipse.setFlag(QGraphicsItem.ItemIsSelectable)

    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent'):
        print("DDdd")
        self.setBrush(Qt.black)
        QApplication.instance().setOverrideCursor(Qt.OpenHandCursor)

    def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent'):
        QApplication.instance().restoreOverrideCursor()
        self.setBrush(Qt.yellow)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())

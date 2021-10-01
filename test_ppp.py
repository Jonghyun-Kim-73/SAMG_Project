import sys
from PyQt5.QtCore import Qt, QPointF, QPoint
from PyQt5.QtGui import QPolygonF, QBrush
from PyQt5.QtWidgets import (QGraphicsView, QGraphicsScene, QApplication,
                             QGraphicsEllipseItem, QGraphicsSceneHoverEvent,
                             QGraphicsSceneMouseEvent, QGraphicsPolygonItem, QGraphicsItem)
#
# class MovableDisk(QGraphicsEllipseItem):
#     def __init__(self, top_left_x, top_left_y, radius):
#         super().__init__(0, 0, radius, radius)
#         self.setPos(top_left_x, top_left_y)
#         self.setBrush(Qt.red)
#         self.setAcceptHoverEvents(True)
#
#         self.setToolTip("Test")                                          # < +++++
#
#     def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent'):
#         self.setBrush(Qt.black)
#         QApplication.instance().setOverrideCursor(Qt.OpenHandCursor)
#
#     def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent'):
#         self.setBrush(Qt.red)
#         QApplication.instance().restoreOverrideCursor()
#
#     def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent'):
#         new_cursor_position   = event.scenePos()
#         old_cursor_position   = event.lastScenePos()
#         old_top_left_corner   = self.scenePos()
#         new_top_left_corner_x = new_cursor_position.x() - old_cursor_position.x() + old_top_left_corner.x()
#         new_top_left_corner_y = new_cursor_position.y() - old_cursor_position.y() + old_top_left_corner.y()
#         self.setPos(QPointF(new_top_left_corner_x, new_top_left_corner_y))
#
#     def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent'): pass
#
#     def mouseDoubleClickEvent(self, event: 'QGraphicsSceneMouseEvent'): pass
#
#     def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent'):
#         self.setToolTip("<h3>pos: <hr>x({}), y({})</h3>"                  # < +++++
#                         "".format(self.pos().x(), self.pos().y()))        # < +++++'
#

class MovableDisk2(QGraphicsPolygonItem):
    def __init__(self,poly):
        super().__init__(poly)
        self.setBrush(Qt.red)
        self.setAcceptHoverEvents(True)
        # button click flag
        self.clicked = False

    def hoverEnterEvent(self, event: 'QGraphicsSceneHoverEvent'):
        self.setBrush(Qt.black)
        # QApplication.instance().setOverrideCursor(Qt.OpenHandCursor)

    def hoverLeaveEvent(self, event: 'QGraphicsSceneHoverEvent'):
        if(self.clicked==False):
            self.setBrush(Qt.red)
        # QApplication.instance().restoreOverrideCursor()

    # def mouseMoveEvent(self, event: 'QGraphicsSceneMouseEvent'):
    #     new_cursor_position   = event.scenePos()
    #     old_cursor_position   = event.lastScenePos()
    #     old_top_left_corner   = self.scenePos()
    #     new_top_left_corner_x = new_cursor_position.x() - old_cursor_position.x() + old_top_left_corner.x()
    #     new_top_left_corner_y = new_cursor_position.y() - old_cursor_position.y() + old_top_left_corner.y()
    #     self.setPos(QPointF(new_top_left_corner_x, new_top_left_corner_y))

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent'):
        self.clicked = True
        self.setBrush(Qt.black)

    def mouseDoubleClickEvent(self, event: 'QGraphicsSceneMouseEvent'): pass

    def mouseReleaseEvent(self, event: 'QGraphicsSceneMouseEvent'):
        self.setToolTip("<h3>pos: <hr>x({}), y({})</h3>"                  # < +++++
                        "".format(self.pos().x(), self.pos().y()))        # < +++++

class MyView(QGraphicsView):
    def __init__(self):
        super().__init__()
        self.scene = QGraphicsScene()
        self.setScene(self.scene)
        self.setSceneRect(0, 0, 500, 500)
        # self.disk = MovableDisk(50, 50, 20)
        # self.scene.addItem(self.disk)
        points = [QPoint(200, 0),
                  QPoint(0, 200),
                  QPoint(200, 400),
                  QPoint(400, 200)]
        poly = QPolygonF(points)
        self.poly_item = MovableDisk2(poly)
        self.poly_item.setBrush(QBrush(Qt.red))
        self.scene.addItem(self.poly_item)


if __name__ == '__main__':
    app = QApplication([])
    f = MyView()
    f.show()
    sys.exit(app.exec_())
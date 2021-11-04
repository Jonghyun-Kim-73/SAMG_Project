import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtSvg import QGraphicsSvgItem, QSvgRenderer


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

source1 = resource_path("x_button.png")
source2 = resource_path("기능기반디스플레이.png")

class Mitigation_popup(QDialog):
    qss = """
            QDialog{
            background:rgb(180,180,180);
            border: 1px solid rgb(91,155,213);             
            }
        """

    def __init__(self, parent=None):
        super(Mitigation_popup, self).__init__()
        self.parent = parent
        self.shmem = parent.shmem if self.parent != None else None

        self.layout = QVBoxLayout()
        self.layout.addWidget(MyBar(self))

        self.setLayout(self.layout)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.setGeometry(870, 180, 600, 600)
        self.setWindowFlags(Qt.FramelessWindowHint)

        #기능기반디스플레이 이미지

        self.pic = QPushButton()
        self.pic.setIcon(QIcon(source2))
        self.pic.setStyleSheet("border:0px")
        self.pic.setIconSize(QSize(1000, 770))

        # self.pic = PIC(self)
        self.layout.addWidget(self.pic)

    def showModal(self):
        return super().exec_()


class MyBar(QWidget):
    def __init__(self, parent):
        super(MyBar, self).__init__()
        self.parent = parent

        self.setMinimumHeight(55)
        self.setMinimumWidth(400)
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel("기능-기반 디스플레이")

        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFixedSize(50, 55)
        self.title.setStyleSheet("""
            background-color: rgb(91,155,213);
            border: 1px solid rgb(91,155,213);       
            color: white;
            font-size: 17pt;
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


class PIC(QWidget):
    """메인 윈도우"""
    def __init__(self, parent=None):
        super(PIC, self).__init__()
        self.parent = parent
        self.shmem = parent.shmem if self.parent != None else None
        # --------------------------------------------------------------------------------------------------------------
        self.setGeometry(0, 0, 600, 600)
        # --------------------------------------------------------------------------------------------------------------
        layout = QVBoxLayout()
        self.setLayout(layout)

        self.GraphicsScene = Scene(self)
        self.GraphicsView = Viewer(self.GraphicsScene, self)
        self.GraphicsView.setStyleSheet("border: 0px")
        layout.addWidget(self.GraphicsView)

        # Q Timer ------------------------------------------------------------------------------------------------------
        timer = QTimer(self)
        timer.setInterval(500)  # 500 ms run = 0.5 sec
        timer.timeout.connect(self.local_loop)
        timer.start()

    def resizeEvent(self, a0: QResizeEvent) -> None:
        w, h = self.GraphicsView.size().width(), self.GraphicsView.size().height()
        self.GraphicsScene.setSceneRect(QRectF(0, 0, w, h))

    def local_loop(self):
        self.GraphicsScene.mimic_update()


class Viewer(QGraphicsView):
    def __init__(self, *args):
        super(Viewer, self).__init__(*args)
        self.w = None

    def resizeEvent(self, event: QResizeEvent) -> None:
        pass


class Scene(QGraphicsScene):
    def __init__(self, parent=None):
        super(Scene, self).__init__()
        self.parent = parent
        self.shmem = parent.shmem if self.parent != None else None

        self.setBackgroundBrush(QColor(231, 231, 234))
        # self.svg_render = QSvgRenderer('comp.svg')
        #
        # self.addItem(SVGitem(10, 10, 'valve_v_c', self.svg_render))
        # self.addItem(SVGitem(30, 30, 'valve_v_c', self.svg_render))
        # self.addItem(ArrowItem(100, 100, 100, 130, 1))

        self.p1 = PumpItem(50, 100, 'r', 'AF-PP02', 'KLAMPO134', 1)
        self.tank1 = TankItem(100, 100)

        self.addItem(self.p1)
        self.addItem(self.tank1)

    def mousePressEvent(self, event: 'QGraphicsSceneMouseEvent') -> None:
        super(Scene, self).mousePressEvent(event)

    def mimic_update(self):
        if self.shmem != None:
            self.p1.update_state(self.shmem.get_shmem_val(self.p1.id))

        # Mimic logic


class ArrowItem(QGraphicsPolygonItem):
    def __init__(self, x1, y1, x2, y2, type):
        super(ArrowItem, self).__init__()
        if type == 0:
            points = [
                QPoint(x2, y2 - 8),
                QPoint(x2 - 4, y2),
                QPoint(x2 + 4, y2)
            ]
        if type == 1:
            points = [
                QPoint(x2, y2 + 8),
                QPoint(x2 - 4, y2),
                QPoint(x2 + 4, y2)
            ]
        if type == 2:
            points = [
                QPoint(x2 - 8, y2),
                QPoint(x2, y2 - 4),
                QPoint(x2, y2 + 4)
            ]
        if type == 3:
            points = [
                QPoint(x2 + 8, y2),
                QPoint(x2, y2 - 4),
                QPoint(x2, y2 + 4)
            ]

        self.setScale(2)

        # self.on_brush = QBrush(QColor(91, 155, 213), Qt.SolidPattern)
        self.on_brush = QBrush(QColor(0, 0, 213), Qt.SolidPattern)
        self.off_brush = QBrush(QColor(82, 82, 82), Qt.SolidPattern)
        # self.on_pen = QPen(QColor(91, 155, 213), 2)
        self.on_pen = QPen(QColor(0, 0, 213), 2)
        self.off_pen = QPen(QColor(82, 82, 82), 2)

        if type != 4:
            self.setPolygon(QPolygonF(points))
            self.setPen(QPen(Qt.NoPen))
            self.setBrush(self.on_brush)

        self.line = QGraphicsLineItem(QLineF(x1, y1, x2, y2), self)
        self.line.setPen(self.on_pen)


class PumpItem(QGraphicsSvgItem):
    def __init__(self, x, y, type, name, id, val):
        super(PumpItem, self).__init__()
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setSharedRenderer(QSvgRenderer('comp.svg'))
        self.type = type
        self.name, self.id, self.val = name, id, val
        self.setElementId(f'pump_{self.type}_stop')

        self.setX(x)
        self.setY(y)
        self.setScale(1.2)

    def update_state(self, val):
        self.val = val
        if self.val == 1:
            self.setElementId(f'pump_{self.type}_start')
        else:
            self.setElementId(f'pump_{self.type}_stop')


class TankItem(QGraphicsSvgItem):
    def __init__(self, x, y):
        super(TankItem, self).__init__()
        self.setFlag(QGraphicsItem.ItemIsMovable, True)
        self.setSharedRenderer(QSvgRenderer('comp.svg'))

        self.setElementId(f'Tank')
        self.setScale(1.2)

        self.setX(x)
        self.setY(y)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Mitigation_popup()
    ex.show()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    sys.exit(app.exec_())
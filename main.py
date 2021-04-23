import os
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def drawMarker(self, x, y, qp: QtGui.QPainter, color: QtGui.QColor, number=0):
    if self.markerAtTip:
        y -= self.markerSize
    pen = QtGui.QPen(color)
    qp.setPen(pen)
    qpp = QtGui.QPainterPath()
    qpp.moveTo(x, y + self.markerSize)
    qpp.lineTo(x - self.markerSize, y - self.markerSize)
    qpp.lineTo(x + self.markerSize, y - self.markerSize)
    qpp.lineTo(x, y + self.markerSize)

    if self.filledMarkers:
        qp.fillPath(qpp, color)
    else:
        qp.drawPath(qpp)

    if self.drawMarkerNumbers:
        number_x = x - 3
        number_y = y - self.markerSize - 3
        qp.drawText(number_x, number_y, str(number))


if __name__ == '__main__':
    print_hi('PyCharm')
    drawMarker(3,4)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

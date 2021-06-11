import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


from test_ppp import App

class custom_button(QPushButton):
    def __init__(self, parent=None, x=None, y=None, w=None, h=None, text=None, type=1, msg_text=None,
                 connected_btn=None, connected_btn_2=None, connected_btn_3=None):
        super(custom_button, self).__init__(parent)
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.text = text
        self.type = type
        self.msg_text = msg_text

        self.setCheckable(True)

        self.msg_box = QMessageBox()

        # self.font = QFont()
        # self.font.setFamily("Arial")
        # self.font.setPointSize(15)
        #
        # self.msg_box.setFont(self.font)

        # self.font = QFont()
        # self.font.setBold(True)
        # self.msg_box.setGeometry(300, 300, 800, 300)
        # self.msg_box.setFixedHeight(500)
        # self.msg_box.setStyleSheet("QMessageBox Question {min-width: 50 px;}")
        # self.msg_box.setStyleSheet("font-size: 14pt; font-weight: bold")
        # self.msg_box.setStyleSheet("min-width: 500px; min-height: 200px;")

        self.setGeometry(self.x, self.y, self.w, self.h)
        self.setCheckable(True)

        self.mouseMovePos = None
        self.is_moved = False

        self.change_color = False

        self.circle_color = QColor(91, 91, 91)

        self.cnt_btn = connected_btn
        self.cnt_btn_signal = False

        self.cnt_btn_2 = connected_btn_2
        self.cnt_btn_3 = connected_btn_3

        print(self, '<-', connected_btn)

        self.clicked.connect(self.btn_clicked)

    # def msgbox(self):
    #     msg = QMessageBox()
    #     msg.setStyleSheet("QLabel {min-width: 300px; min-height: 200px;")
    #     msg.exec()

    def btn_clicked(self):
        if self.change_color:
            self.change_color = False
            self.circle_color = QColor(0, 255, 0, 70)
        else:
            self.change_color = True
            self.circle_color = QColor(0, 255, 0, 70)

        if self.type == 1:
            # self.app.show()
            print('pp')

        if self.type == 2:
            reply = self.msg_box.question(self, 'Message', self.msg_text, self.msg_box.Ok)
            if reply == self.msg_box.Ok:
                self.cnt_btn.btn_clicked_ver2()

        if self.type == 3:
            reply = self.msg_box.question(self, 'Message', self.msg_text, self.msg_box.Yes | self.msg_box.No)
            if reply == self.msg_box.Yes:
                self.cnt_btn.btn_clicked_ver2()
                if self.cnt_btn_3:
                    self.cnt_btn_3.btn_clicked_ver2()
            if reply == self.msg_box.No:
                self.cnt_btn_2.btn_clicked_ver2()

    def btn_clicked_ver2(self):
        print('btn_clicked_ver2 진입')
        print(self.cnt_btn_signal)

        if self.cnt_btn_signal:
            self.cnt_btn_signal = False
            self.circle_color = QColor(255, 0, 0, 70)
        else:
            print(self.cnt_btn_signal)
            self.cnt_btn_signal = True
            self.circle_color = QColor(255, 0, 0, 70)


    def paintEvent(self, event):
        rect = QRect(0, 0, self.w, self.h)  # 사각형 정의

        p = QPainter(self)
        p.setPen(QPen(Qt.black, 1))
        p.setBrush(self.circle_color) # 91, 91, 91
        p.setFont(QFont('Arial', 13))

        if self.type == 1:      # 사각형
            p.drawRect(0, 0, self.w, self.h)
            p.drawText(rect, Qt.AlignCenter, self.text)  # rect 텍스트가 표시될 영역 지정
        elif self.type == 2:    # 타원
            p.drawEllipse(0, 0, self.w, self.h)
            p.drawText(rect, Qt.AlignCenter, self.text)
        elif self.type == 3:    # 마름모
            points = [QPoint(self.w / 2, 0),
                      QPoint(0, self.h / 2),
                      QPoint(self.w / 2, self.h),
                      QPoint(self.w, self.h / 2)]
            poly = QPolygon(points)
            p.drawPolygon(poly)
            p.drawText(rect, Qt.AlignCenter, self.text)
        # self.update()         # ?

    def contextMenuEvent(self, event) -> None:
        menu = QMenu(self)
        get_info = menu.addAction("get_info")
        add_text = menu.addAction("add_text")
        get_info.triggered.connect(self.get_info)
        add_text.triggered.connect(self.add_text)
        menu.exec_(event.globalPos())

    def get_info(self):
        """ 위치 출력하기 """
        print(self.geometry())
        print(self.x, self.y, self.type)

    def add_text(self):
        """ 클릭한 위치에 버튼 추가하기 """
        text, cl = QInputDialog.getMultiLineText(self, 'Input Dialog', 'Multi Line Text Input:')
        self.text = text
        # self.update()

    # def mousePressEvent(self, event):
    #     """
    #     - 마우스 왼쪽 클릭 시 위젯이 움직임.
    #     """
    #     if event.button() == Qt.LeftButton:
    #         self.mouseMovePos = event.globalPos()   # ?
    #         self.is_moved = True
    #     else:
    #         self.is_moved = False
    #
    # def mouseMoveEvent(self, event):
    #     if self.is_moved:
    #         curPos = self.mapToGlobal(self.pos())
    #         globalPos = event.globalPos()
    #         diff = globalPos - self.mouseMovePos
    #         newPos = self.mapFromGlobal(curPos + diff)
    #         self.move(newPos)
    #         self.mouseMovePos = globalPos



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win_main = custom_button(x=0, y=0, w=100, h=80, text='bibi', type=2)
    win_main.show()
    app.exec_()
    # sys.exit(app.exec_())

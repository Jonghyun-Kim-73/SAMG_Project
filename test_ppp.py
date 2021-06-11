import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.initUI()
        self.window = None

    def initUI(self):
        # 초기 윈도우 사이즈
        self.setGeometry(200, 200, 200, 200)

        # 초기 윈도우 프레임
        layout = QVBoxLayout()

        label = QLabel('완화-01에 진입하시겠습니까?')
        label.setStyleSheet("Color : black; font-size: 14pt; font-weight: bold")

        layout.addWidget(label)

        self.setLayout(layout)

        # 버튼 추가
        btn = QPushButton('Yes')
        btn.move(20, 20)
        btn.clicked.connect(self.show_window)
        # btn.setText()

        layout.addWidget(btn)

    def show_window(self):
        if self.window is None:
            self.window = Window()
            self.window.show()
        else:
            self.window = None


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        self.bb()

    def bb(self):
        # 초기 윈도우 사이즈
        self.setGeometry(400, 200, 1000, 800)
        self.show()


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()
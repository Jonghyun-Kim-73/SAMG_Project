from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backend_bases import MouseEvent
import matplotlib.pyplot as plt


class TrendFlow(QWidget):
    def __init__(self, parent, w, h, para_name: str,
                 xtitle:str = 'None', ytitle:str = 'None'):
        """
        그래프 위젯
        :param parent: 시뮬레이터에서 공유 메모리에 업데이트된 값을 취득하기위해 부모 위젯 아이디 받기 위해서 사용
        :param w: 위젯 너비
        :param h: 위젯 높이
        :param para_name: 그래프의 타이틀
        :param para_id: 그래프에 그려질 시뮬레이터의 변수 명    ** 공유 메모리의 save_mem 에 변수명이 등록되어야함.
        :param para_range: 변수의 y축의 min / max range
        :param xtitle, ytitle: x, y 축의 라벨
        """

        super(TrendFlow, self).__init__()
        self.parent = parent
        self.shmem = parent.shmem

        x = [1.0070531, 1.3960854, 1.7462845, 2.0962925, 2.915291, 3.92992,   4.671634,
             5.569763,  6.3508835, 8.460163,  9.515089, 10.569888,11.664093, 12.719083,
             13.578697, 14.555574, 15.102613, 15.063526]
        y = [248.03638, 232.65663, 219.3979, 204.54906, 189.15982, 175.35638,
             167.3894, 159.949, 154.63136, 142.39386, 138.6603, 133.86664,
             131.7223, 128.51877,  125.84959, 123.17781, 121.575615, 121.57648]

        # QWidget info
        self.setGeometry(10, 10, w, h)
        self.set_main_frame()
        self.start = QPoint(0, 0)           # 마우스 클릭을 통한 창 이동 관련
        self.pressing = False               # ..

        # para info
        self.para_name = para_name

        # figure
        self.fig = plt.Figure(tight_layout=True, facecolor=[240/255, 232/255, 208/255]) #
        # self.fig.subplots_adjust(left=0.1, right=0.98, top=0.95, bottom=0.05)
        self.canvas = FigureCanvas(self.fig)

        # ax
        self.ax = self.fig.add_subplot(111)

        self.ax.set_title('Injection Flow')
        self.ax.set_xlim(0, 24)
        self.ax.set_ylim(0, 300)
        self.ax.set_xlabel(xtitle)
        self.ax.set_ylabel(ytitle)
        self.ax.set_xticks([_ for _ in range(0, 26, 2)])
        self.ax.set_xticklabels([str(_) for _ in range(0, 26, 2)])
        self.ax.grid()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)
        self.setLayout(layout)

        # Line
        self.line1, = self.ax.plot(x, y, color=[39/255, 39/255, 141/255], linewidth=1.5)    # 현재 값 Trend
        self.line2, = self.ax.plot([0], [0], color=[192/255, 0, 0], linewidth=1.5, marker='o')    # 현재 값 Trend
        # self.makers_ = []    # 예지 값 Trends 저장

        #Q Timer ------------------------------------------------------------------------------------------------------
        timer = QTimer(self)
        timer.setInterval(500)  # 500 ms run = 0.5 sec
        timer.timeout.connect(self.local_loop)
        timer.start()

    def set_main_frame(self):
        """ 라운드 테두리 """
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), 10, 10)
        mask = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        """ 그래프 크기 변경시 """
        self.set_main_frame()

    def local_loop(self):
        """ 그래프 QTimer interval 간격으로 업데이트 """
        Flow = self.shmem.get_shmem_val('WFWLN1') + self.shmem.get_shmem_val('WFWLN2') + self.shmem.get_shmem_val('WFWLN3')
        CurrT = self.shmem.get_shmem_val('KCNTOMS')/(5*60*60)   ## hour

        self.line2.set_data([CurrT], [Flow])
        # 최종 캔버스 드로잉
        try:
            self.canvas.draw()
        except:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TrendFlow(None, w=500, h=500, para_name='Flow',
                       xtitle='Time Since Reactor Shutdown (Hours)', ytitle='Minimum Injection Flowrate (gpm)')
    window.show()
    sys.exit(app.exec_())
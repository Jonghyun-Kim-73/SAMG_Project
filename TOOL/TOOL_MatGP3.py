from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backend_bases import MouseEvent
import matplotlib.pyplot as plt


class Trend(QWidget):
    def __init__(self, parent, w, h, para_name: str, para_id: str,
                 para_range: list = [None, None], xtitle:str = 'None', ytitle:str = 'None'):
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

        super(Trend, self).__init__()
        self.parent = parent
        if parent is not None:
            self.shmem = parent.shmem

        # QWidget info
        self.setGeometry(10, 10, w, h)
        self.set_main_frame()
        self.start = QPoint(0, 0)           # 마우스 클릭을 통한 창 이동 관련
        self.pressing = False               # ..

        # para info
        self.para_name = para_name
        self.para_id = para_id
        self.para_range = para_range

        self.max_time_leg = 24 # hour
        # figure
        self.fig = plt.Figure(tight_layout=True, facecolor=[240/255, 232/255, 208/255]) #
        # self.fig.subplots_adjust(left=0.1, right=0.98, top=0.95, bottom=0.05)
        self.canvas = FigureCanvas(self.fig)
        self.canvas.mpl_connect('motion_notify_event', self.mouse_move_in_trend)
        self.canvas.mpl_connect('button_press_event', self.mouse_press_in_trend)

        # ax
        self.ax = self.fig.add_subplot(111)

        self.ax.set_title(f'{self.para_name}')
        self.ax.set_xlim(0, self.max_time_leg)
        self.ax.set_ylim(0, 5)
        self.ax.set_xlabel(xtitle)
        self.ax.set_ylabel(ytitle)
        self.ax.grid()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.canvas)
        self.setLayout(layout)
        # Line
        self.line1, = self.ax.plot([1.092683,1.7170732,2.7707317,4.097561,5.8146343,7.6878047,9.873171,12.52683,
                                    14.868293],
                                   [249.46808,219.14894,194.68085,173.40425,157.97873,145.74467,138.29787,129.78723,
                                    123.93617], color=[39/255, 39/255, 141/255], linewidth=1, label='Flow line')

        self.SG1, = self.ax.plot([], [], color=[197/255, 224/255, 180/255], linewidth=0, marker='o', label='SG1 Flow')
        self.SG2, = self.ax.plot([], [], color=[255/255, 121/255, 121/255], linewidth=0, marker='o', label='SG2 Flow')

        #Q Timer ------------------------------------------------------------------------------------------------------
        timer = QTimer(self)
        timer.setInterval(500)  # 500 ms run = 0.5 sec
        timer.timeout.connect(self.local_loop)
        timer.start()

        self.vallist = [0]  # For test

    def set_main_frame(self):
        """ 라운드 테두리 """
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), 10, 10)
        mask = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(mask)

    def resizeEvent(self, a0: QResizeEvent) -> None:
        """ 그래프 크기 변경시 """
        self.set_main_frame()

    def mouse_move_in_trend(self, event: MouseEvent):
        """ 그래프 클릭 시 이동 """
        if event.button == 1:
            self.end = self.mapToGlobal(QPoint(event.x, abs(event.y - self.height())))
            self.movement = self.end - self.start
            self.setGeometry(self.mapToGlobal(self.movement).x(),
                                    self.mapToGlobal(self.movement).y(),
                                    self.width(),
                                    self.height())
            self.start = self.end

    def mouse_press_in_trend(self, event: MouseEvent):
        """ 클릭 한 마우스 global pos 저장 """
        if event.button == 3:  # 오른쪽 클릭
            self.close()
        self.start = self.mapToGlobal(QPoint(event.x, abs(event.y - self.height())))

    def local_loop(self):
        """ 그래프 QTimer interval 간격으로 업데이트 """
        if self.parent is not None:
            saved_db = self.shmem.get_shmem_save_db()
            self._update_trend(saved_db)
        else:
            self.vallist.append(self.vallist[-1] + 1)
            self._update_trend(self.vallist)

    def _update_trend(self, val_list):
        """ 그래프 업데이트 """
        # if len(val_list) > 2:   # 2개 이상 포이트가 저장되면 드로잉 시작
        # if self.parent is not None:
        # time
        # x_, ax1_, ax2_ = [], [], []
        # for x, ax1, ax2 in zip(val_list['KCNTOMS'], val_list['WAFWS1'], val_list['WAFWS2']):
        #     if x % 3000 == 0:
        #         x_.append(x)
        #         ax1_.append(ax1)
        #         ax2_.append(ax2)
        #
        # self.SG1.set_data(x_, ax1_)
        # self.SG2.set_data(x_, ax2_)
        #

        # x축 드로잉
        # y축 드로잉
        self.ax.set_ylim(0, 300)
        self.ax.set_xlim(0, 24)

        tick_ = [i for i in range(0, 26, 2)]
        self.ax.set_xticks(tick_)
        self.ax.set_xticklabels([f'{i}' for i in tick_])

        self.canvas.draw()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Trend(None, w=500, h=500, para_name='Flow', para_id='KCNTOMS', para_range=[0, 300],
                   xtitle='Time Since Reactor Shutdown (Hours)', ytitle='Minimum Injection Flowrate (gpm)')
    window.show()
    sys.exit(app.exec_())
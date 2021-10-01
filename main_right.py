import os
import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from TOOL import TOOL_MatGP2


class MainRight(QWidget):

    qss = """
        QWidget {
            background: rgb(128, 128, 128);
        }
        QLabel {
            background: rgb(131, 131, 131);
            border-radius: 6px;
            color: rgb(255, 255, 255);
        }
        QTableWidget {
            background: rgb(221, 221, 221)
        }
        QPushButton{
            background: rgb(221, 221, 221)
        }
    """


    def __init__(self, parent = None):
        super(MainRight, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setStyleSheet(self.qss)

        # 기본 속성
        self.setMinimumHeight(900-40)
        self.setFixedWidth(int(1920 * (1 / 3)))

        # 레이아웃
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)

        label1 = MainParaArea(self.parent)
        label2 = EndCondArea(self.parent)

        layout.addWidget(label1)
        layout.addWidget(label2)
        self.setLayout(layout)
# ======================================================================================================================


class MainParaArea(QWidget):
    def __init__(self, parent=None):
        super(MainParaArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        # 레이아웃
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # 1. 절차서 Table
        # label = QLabel('CTMT 중대사고 위협 변수 감시')
        # label.setFixedHeight(30)
        # label.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)  # 텍스트 정렬
        # label.setStyleSheet("Color : white; font-size: 14pt; font-weight: bold")

        para_table = ParaTable(self.parent)
        #
        # layout.addWidget(label)
        layout.addWidget(para_table)
        #
        self.setLayout(layout)


class ParaTable(QTableWidget):
    def __init__(self, parent=None):
        super(ParaTable, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent                            # <- main_window.py 파일의 MainWindow class 를 바라봄.
                                                        #    main_right.py 를 단독으로 실행히 parent 는 None
        if self.parent is not None:
            self.shmem = parent.shmem                   # <- shmem 인스턴스 가져옴.

        self.setObjectName('ParaTable')

        # 테이블 프레임 모양 정의
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)     # Row 넘버 숨기기

        # 테이블 셋업
        col_info = [('주요 발전소 변수', 360), ('현재 발전소 변수', 268)] # 475
        self.setColumnCount(2)
        self.setRowCount(8)
        self.horizontalHeader().setFixedHeight(60)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)
        # 테이블 행 높이 조절
        for each in range(self.rowCount()):
            self.setRowHeight(each, 60)

        col_names = []
        for i, (l, w) in enumerate(col_info):
            self.setColumnWidth(i, w)
            col_names.append(l)

        cell_height = self.rowHeight(0)
        print(cell_height)

        # 테이블 헤더
        self.setHorizontalHeaderLabels(col_names)
        self.horizontalHeader().setStyleSheet("::section {background: rgb(221, 221, 221);font-size:13pt;}")
        self.horizontalHeader().sectionPressed.disconnect()
        # self.setItem(0, 0, QTableWidgetItem('발전소 부지 경계 선량'))
        # self.setItem(1, 0, QTableWidgetItem('격납건물 압력'))
        # self.setItem(2, 0, QTableWidgetItem('격납건물 압력'))
        # self.setItem(3, 0, QTableWidgetItem('격납건물 압력'))
        # self.setItem(4, 0, QTableWidgetItem('SG 1 수위 NR'))
        # self.setItem(5, 0, QTableWidgetItem('SG 2 수위 NR'))
        # self.setItem(6, 0, QTableWidgetItem('격납건물 수위'))

        item = [0*i for i in range(8)]
        self.item2 = [0*i for i in range(8)]
        item[0] = QTableWidgetItem('주요 발전소 변수')
        item[1] = QTableWidgetItem('발전소 부지 경계 선량')
        item[2] = QTableWidgetItem('격납건물 압력')
        item[3] = QTableWidgetItem('노심출구 온도')
        item[4] = QTableWidgetItem('RCS 압력')
        item[5] = QTableWidgetItem('SG 1 수위 NR')
        item[6] = QTableWidgetItem('SG 2 수위 NR')
        item[7] = QTableWidgetItem('격납건물 수위')

        for i in range(8):
            item[i].setFlags(Qt.NoItemFlags)
            item[i].setForeground(QBrush(QColor(0, 0, 0)))
            self.setItem(i, 0, item[i])
        self.item2[0] = QTableWidgetItem('현재 발전소 변수')
        self.item2[1] = QTableWidgetItem('0 mSv')
        self.item2[2] = QTableWidgetItem('0 psig')
        self.item2[3] = QTableWidgetItem('0 °C')
        self.item2[4] = QTableWidgetItem('0 psig')
        self.item2[5] = QTableWidgetItem('0 %')
        self.item2[6] = QTableWidgetItem('0 %')
        self.item2[7] = QTableWidgetItem('0 %')

        for i in range(8):
            self.setItem(i, 1, self.item2[i])

        self.doubleClicked.connect(self.popup)

        # self.item1 = QPushButton("value1")
        # self.setCellWidget(0, 1, self.item1)

        # self.cellClicked.connect(self.__mycell_clicked)
        # mycom.currentTextChanged.connect(self.__mycom_text_changed)

        # 테이블 셀 내용 가운데 정렬
        delegate = AlignDelegate()
        self.setItemDelegateForColumn(0, delegate)
        self.setItemDelegateForColumn(1, delegate)
        fnt = self.font()
        fnt.setPointSize(12)
        self.setFont(fnt)

        """ QTimer interval 간격으로 item 디스플레이 업데이트 21.09.16 """
        # Q Timer ------------------------------------------------------------------------------------------------------
        timer = QTimer(self)
        timer.setInterval(500)  # 500 ms run = 0.5 sec
        timer.timeout.connect(self.local_loop)
        timer.start()

    def popup(self):
        # TODO 나중에 수정해야해
        # msgBox = QMessageBox()
        # msgBox.setWindowTitle("Pop up")  # 메세지창의 상단 제목
        # msgBox.setText("값")  # 메세지 제목
        # msgBox.setInformativeText("value")  # 메세지 내용
        # msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # 메세지창의 버튼
        # msgBox.setDefaultButton(QMessageBox.Yes)  # 포커스가 지정된 기본 버튼
        # msgBox.exec_()

        r = self.currentItem().row()
        r_db = {
            0: {'Para':'',          'N':'',                 'X':'Time[Min]', 'Y':'', 'Yr': [0, 1]},
            1: {'Para':'',          'N':'',                 'X':'Time[Min]', 'Y':'', 'Yr': [0, 1]},
            2: {'Para':'PCTMT',     'N':'CTMT Pressure',    'X':'Time[Min]', 'Y':'PA', 'Yr': [0, 30000]},
            3: {'Para':'',          'N':'',                 'X':'Time[Min]', 'Y':'', 'Yr': [0, 1]},
            4: {'Para':'ZINST58',   'N':'PZR Pressure',     'X':'Time[Min]', 'Y':'Kg/cm^2', 'Yr': [0, 200]},
            5: {'Para':'ZINST78',   'N':'S/G 1 Level',      'X':'Time[Min]', 'Y':'%', 'Yr': [0, 100]},
            6: {'Para':'ZINST77',   'N':'S/G 2 Level',      'X':'Time[Min]', 'Y':'%', 'Yr': [0, 100]},
            7: {'Para':'ZSUMP',     'N':'CTMP Sump Level',  'X':'Time[Min]', 'Y':'M', 'Yr': [0, 100]}
        }
        get_selected_para = r_db[r]['Para']
        if get_selected_para != '':
            self.popup_W = TOOL_MatGP2.Trend(self, w=500, h=500,
                                             para_name=r_db[r]['N'], para_id=r_db[r]['Para'],
                                             para_range=r_db[r]['Yr'],
                                             xtitle=r_db[r]['X'],
                                             ytitle=r_db[r]['Y'])
            self.popup_W.show()


    def local_loop(self):
        if self.parent is not None:
            get_db = self.shmem.get_shmem_db()
            """
            get_db 의 구조는 딕셔너리로 아래와 같음.
            get_db = {
                'para_id': {'Sig': sig, 'Val': 0, 'Num': idx, 'List': deque(maxlen=max_len)},
                'para_id': {'Sig': sig, 'Val': 0, 'Num': idx, 'List': deque(maxlen=max_len)},
                ...
            }
            """
            self.item2[1].setText(f'{get_db["DCTMT"]["Val"]:.2f} mSv')
            self.item2[2].setText(f'{get_db["PCTMT"]["Val"]:.2f} psig')
            self.item2[3].setText(f'{get_db["UUPPPL"]["Val"]:.2f} °C')
            self.item2[4].setText(f'{get_db["ZINST58"]["Val"]:.2f} psig')
            self.item2[5].setText(f'{get_db["ZINST78"]["Val"]:.2f} %')
            self.item2[6].setText(f'{get_db["ZINST77"]["Val"]:.2f} %')
            self.item2[7].setText(f'{get_db["ZSUMP"]["Val"]:.2f} %')

# ======================================================================================================================

class EndCondArea(QWidget):
    def __init__(self, parent=None):
        super(EndCondArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.setFixedHeight(340)
        # 레이아웃
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # label = QLabel('SAMG 종결 조건 감시')
        # label.setFixedHeight(30)
        # label.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        # label.setStyleSheet("Color : white; font-size: 14pt; font-weight: bold")

        label2 = EndCondTable(self.parent)

        # layout.addWidget(label)
        layout.addWidget(label2)

        self.setLayout(layout)


class EndCondTable(QTableWidget):
    def __init__(self, parent):
        super(EndCondTable, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent                            # <- main_window.py 파일의 MainWindow class 를 바라봄.
                                                        #    main_right.py 를 단독으로 실행히 parent 는 None
        if self.parent is not None:
            self.shmem = parent.shmem                   # <- shmem 인스턴스 가져옴.

        self.setObjectName('EndCondTable')

        # 테이블 프레임 모양 정의
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)     # Row 넘버 숨기기

        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)


        # 테이블 셋업
        col_info = [('종료조건', 360), ('현재 상태', 268)] # 475

        self.setColumnCount(len(col_info))
        self.setRowCount(5)

        col_names = []
        for i, (l, w) in enumerate(col_info):
            self.setColumnWidth(i, w)
            col_names.append(l)

        # 테이블 헤더
        self.setHorizontalHeaderLabels(col_names)
        self.horizontalHeader().setFixedHeight(60)
        self.horizontalHeader().setStyleSheet("::section {background: rgb(221, 221, 221);font-size:13pt;}")
        self.horizontalHeader().sectionPressed.disconnect()
        # 테이블 행 높이 조절
        for each in range(self.rowCount()):
            self.setRowHeight(each, 60)
        # self.setItem(0, 0, QTableWidgetItem('노심출구온도 < [T01]'))
        # self.setItem(1, 0, QTableWidgetItem('발전소부지 경계 선량 < [R01]'))
        # self.setItem(2, 0, QTableWidgetItem('격납건물 압력 < [P11]'))
        # self.setItem(3, 0, QTableWidgetItem('격납건물 수소농도 < [H02]'))


        item = [0 * i for i in range(5)]
        self.item2 = [0 * i for i in range(5)]
        item[0] = QTableWidgetItem('종료조건')
        item[1] = QTableWidgetItem('노심출구온도 < [T01]')
        item[2] = QTableWidgetItem('발전소부지 경계 선량 < [R01]')
        item[3] = QTableWidgetItem('격납건물 압력 < [P11]')
        item[4] = QTableWidgetItem('격납건물 수소농도 < [H02]')

        for i in range(5):
            item[i].setFlags(Qt.NoItemFlags)
            item[i].setForeground(QBrush(QColor(0, 0, 0)))
            self.setItem(i, 0, item[i])
        self.item2[0] = QTableWidgetItem('현재 발전소 변수')
        self.item2[1] = QTableWidgetItem('0 °C')
        self.item2[2] = QTableWidgetItem('0 mSv')
        self.item2[3] = QTableWidgetItem('0 psig')
        self.item2[4] = QTableWidgetItem('0 %')

        for i in range(5):
            self.setItem(i, 1, self.item2[i])

        self.doubleClicked.connect(self.popup)

        # wid = self.cellWidget(0, 1)
        # wid.setCursor(QCursor(Qt.PointingHandCursor))
        # wid.setFocus()
        # 테이블 셀 내용 가운데 정렬
        delegate = AlignDelegate()
        self.setItemDelegateForColumn(0, delegate)
        self.setItemDelegateForColumn(1, delegate)

        fnt = self.font()
        fnt.setPointSize(12)
        self.setFont(fnt)

        """ QTimer interval 간격으로 item 디스플레이 업데이트 21.09.16 """
        # Q Timer ------------------------------------------------------------------------------------------------------
        timer = QTimer(self)
        timer.setInterval(500)  # 500 ms run = 0.5 sec
        timer.timeout.connect(self.local_loop)
        timer.start()

    def popup(self):
        msgBox = QMessageBox()
        msgBox.setWindowTitle("Pop up")  # 메세지창의 상단 제목
        msgBox.setText("값")  # 메세지 제목
        msgBox.setInformativeText("value")  # 메세지 내용
        msgBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No | QMessageBox.Cancel)  # 메세지창의 버튼
        msgBox.setDefaultButton(QMessageBox.Yes)  # 포커스가 지정된 기본 버튼
        msgBox.exec_()

    def local_loop(self):
        if self.parent is not None:
            get_db = self.shmem.get_shmem_db()
            """
            get_db 의 구조는 딕셔너리로 아래와 같음.
            get_db = {
                'para_id': {'Sig': sig, 'Val': 0, 'Num': idx, 'List': deque(maxlen=max_len)},
                'para_id': {'Sig': sig, 'Val': 0, 'Num': idx, 'List': deque(maxlen=max_len)},
                ...
            }
            """
            self.item2[1].setText(f'{get_db["UUPPPL"]["Val"]:.2f} °C')
            self.item2[2].setText(f'{get_db["DCTMT"]["Val"]:.2f} mSv')
            self.item2[3].setText(f'{get_db["PCTMT"]["Val"]:.2f} psig')
            self.item2[4].setText(f'{get_db["H2CONC"]["Val"]:.2f} %')

class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


if __name__ == '__main__':
    print('test')
    app = QApplication(sys.argv)
    window = MainRight()
    window.show()
    app.exec_()

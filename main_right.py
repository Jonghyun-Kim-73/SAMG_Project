import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from Flag import Flag
from TOOL_MatGP2 import Trend

class MainRight(QWidget):

    qss = """
        QWidget {
            background: rgb(128, 128, 128);
            border: 2px solid rgb(0, 0, 0); 
            font-size: 14pt;
        }
        QLabel {
            background: rgb(131, 131, 131);
            border-radius: 6px;
            color: rgb(255, 255, 255);
        }
        QTableWidget {
            background: rgb(221, 221, 221);
            border: 1px solid rgb(0, 0, 0); 
        }
        QPushButton{
            background: rgb(221, 221, 221)
        }
        QWidget#label {
            background: rgb(128, 128, 128);
            border: 0px solid rgb(0, 0, 0); 
        }
    """

    def __init__(self, parent=None):
        super(MainRight, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.shmem = parent.shmem
        self.setStyleSheet(self.qss)

        # # 기본 속성
        self.setMinimumHeight(750)
        #
        # # 레이아웃
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        #
        label1 = MainParaArea(self)
        label2 = EndCondArea(self)
        label1.setObjectName("label")
        label2.setObjectName("label")
        layout.addWidget(label1)
        layout.addWidget(label2)
        self.setLayout(layout)


class MainParaArea(QWidget):
    def __init__(self, parent=None):
        super(MainParaArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.shmem = parent.shmem
        self.setFixedHeight(559)
        # 레이아웃
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 0)

        para_table = ParaTable(self)
        layout.addWidget(para_table)
        self.setLayout(layout)


class ParaTable(QTableWidget):
    def __init__(self, parent=None):
        super(ParaTable, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.shmem = parent.shmem
        self.setObjectName('ParaTable')

        # 테이블 프레임 모양 정의
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)     # Row 넘버 숨기기

        # 테이블 셋업
        col_info = [('주요 발전소 변수', 360), ('현재 발전소 변수', 253)] # 475
        self.setColumnCount(2)
        self.setRowCount(8)
        self.horizontalHeader().setFixedHeight(69)
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 행 높이 조절
        for each in range(self.rowCount()):
            self.setRowHeight(each, 69)

        col_names = []
        for i, (l, w) in enumerate(col_info):
            self.setColumnWidth(i, w)
            col_names.append(l)

        # 테이블 헤더
        self.setHorizontalHeaderLabels(col_names)
        self.horizontalHeader().setStyleSheet("::section {background: rgb(221, 221, 221);font-size:14pt;font-weight: bold;}")
        self.horizontalHeader().sectionPressed.disconnect()

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

        # 테이블 셀 내용 가운데 정렬
        delegate = AlignDelegate()
        self.setItemDelegateForColumn(0, delegate)
        self.setItemDelegateForColumn(1, delegate)
        fnt = self.font()
        fnt.setBold(True)
        fnt.setPointSize(14)
        item[0].setFont(fnt)
        self.item2[0].setFont(fnt)

        """ QTimer interval 간격으로 item 디스플레이 업데이트 21.09.16 """ # Flag 추가 수정 21.10.03 소진
        # Q Timer ------------------------------------------------------------------------------------------------------
        timer = QTimer(self)
        timer.setInterval(500)  # 500 ms run = 0.5 sec
        timer.timeout.connect(self.local_loop)
        timer.start()

    def popup(self):
        r = self.currentItem().row()
        r_db = {
            0: {'Para': '', 'N': '', 'X': 'Time[Min]', 'Y': '', 'Yr': [0, 1]},
            1: {'Para': '', 'N': '', 'X': 'Time[Min]', 'Y': '', 'Yr': [0, 1]},
            2: {'Para': 'PCTMT', 'N': 'CTMT Pressure', 'X': 'Time[Min]', 'Y': 'PA', 'Yr': [0, 30000]},
            3: {'Para': '', 'N': '', 'X': 'Time[Min]', 'Y': '', 'Yr': [0, 1]},
            4: {'Para': 'ZINST58', 'N': 'PZR Pressure', 'X': 'Time[Min]', 'Y': 'Kg/cm^2', 'Yr': [0, 200]},
            5: {'Para': 'ZINST78', 'N': 'S/G 1 Level', 'X': 'Time[Min]', 'Y': '%', 'Yr': [0, 100]},
            6: {'Para': 'ZINST77', 'N': 'S/G 2 Level', 'X': 'Time[Min]', 'Y': '%', 'Yr': [0, 100]},
            7: {'Para': 'ZSUMP', 'N': 'CTMP Sump Level', 'X': 'Time[Min]', 'Y': 'M', 'Yr': [0, 100]}
        }
        get_selected_para = r_db[r]['Para']
        if get_selected_para != '':
            self.popup_W = Trend(self, w=500, h=500,
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
            if get_db['ZINST78']['Val'] <= 45:
                self.item2[5].setBackground(QColor(252, 227, 112))
            else:
                self.item2[5].setBackground(QColor(221, 221, 221))

            self.item2[6].setText(f'{get_db["ZINST77"]["Val"]:.2f} %')
            if get_db['ZINST77']['Val'] <= 45:
                self.item2[6].setBackground(QColor(252, 227, 112))
            else:
                self.item2[6].setBackground(QColor(221, 221, 221))

            self.item2[7].setText(f'{get_db["ZSUMP"]["Val"]:.2f} %')

            Flag.value1_1 = str(get_db["DCTMT"]['Val'])
            Flag.value1_2 = str(get_db["PCTMT"]['Val'])
            Flag.value1_3 = str(get_db["UUPPPL"]['Val'])
            Flag.value1_4 = str(get_db["ZINST58"]['Val'])
            Flag.value1_5 = str(get_db["ZINST78"]['Val'])
            Flag.value1_6 = str(get_db["ZINST77"]['Val'])
            Flag.value1_7 = str(get_db["ZSUMP"]['Val'])

# ======================================================================================================================


class EndCondArea(QWidget):
    def __init__(self, parent=None):
        super(EndCondArea, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.shmem = parent.shmem
        self.setFixedHeight(357)
        # 레이아웃
        layout = QVBoxLayout(self)
        layout.setContentsMargins(5, 5, 5, 5)
        label2 = EndCondTable(self)
        layout.addWidget(label2)

        self.setLayout(layout)


class EndCondTable(QTableWidget):
    def __init__(self, parent):
        super(EndCondTable, self).__init__()
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.parent = parent
        self.shmem = parent.shmem

        self.setObjectName('EndCondTable')

        # 테이블 프레임 모양 정의
        self.horizontalHeader().setVisible(False)
        self.verticalHeader().setVisible(False)     # Row 넘버 숨기기

        # 편집 불가
        self.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.setFocusPolicy(Qt.NoFocus)
        self.setSelectionMode(QAbstractItemView.NoSelection)

        # 테이블 셋업
        col_info = [('종료조건', 360), ('현재 상태', 253)] # 475

        self.setColumnCount(len(col_info))
        self.setRowCount(5)

        col_names = []
        for i, (l, w) in enumerate(col_info):
            self.setColumnWidth(i, w)
            col_names.append(l)

        # 테이블 헤더
        self.setHorizontalHeaderLabels(col_names)
        self.horizontalHeader().setFixedHeight(69)
        self.horizontalHeader().setStyleSheet("::section {background: rgb(221, 221, 221);font-size:14pt;font-weight: bold;}")
        self.horizontalHeader().sectionPressed.disconnect()
        # 테이블 행 높이 조절
        for each in range(self.rowCount()):
            self.setRowHeight(each, 69)

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

        # 테이블 셀 내용 가운데 정렬
        delegate = AlignDelegate()
        self.setItemDelegateForColumn(0, delegate)
        self.setItemDelegateForColumn(1, delegate)

        fnt = self.font()
        fnt.setPointSize(14)
        fnt.setBold(True)
        item[0].setFont(fnt)
        self.item2[0].setFont(fnt)

        """ QTimer interval 간격으로 item 디스플레이 업데이트 21.09.16 """# value 받아옴 - 21.10.03 소진
        # Q Timer ------------------------------------------------------------------------------------------------------
        timer = QTimer(self)
        timer.setInterval(500)  # 500 ms run = 0.5 sec
        timer.timeout.connect(self.local_loop)
        timer.start()

    def popup(self):

        r = self.currentItem().row()
        r_db = {
            0: {'Para':'',          'N':'',                 'X':'Time[Min]', 'Y':'', 'Yr': [0, 1]},
            1: {'Para':'',          'N':'',                 'X':'Time[Min]', 'Y':'', 'Yr': [0, 1]},
            2: {'Para':'PCTMT',     'N':'CTMT Pressure',    'X':'Time[Min]', 'Y':'PA', 'Yr': [0, 30000]},
            3: {'Para':'',          'N':'',                 'X':'Time[Min]', 'Y':'', 'Yr': [0, 1]},
        }
        get_selected_para = r_db[r]['Para']
        if get_selected_para != '':
            self.popup_W = Trend(self, w=500, h=500,
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
            self.item2[1].setText(f'{get_db["UUPPPL"]["Val"]:.2f} °C')
            self.item2[2].setText(f'{get_db["DCTMT"]["Val"]:.2f} mSv')
            self.item2[3].setText(f'{get_db["PCTMT"]["Val"]:.2f} psig')
            self.item2[4].setText(f'{get_db["H2CONC"]["Val"]:.2f} %')

            Flag.value2_1 = str(get_db["UUPPPL"]['Val'])
            Flag.value2_2 = str(get_db["DCTMT"]['Val'])
            Flag.value2_3 = str(get_db["PCTMT"]['Val'])
            Flag.value2_4 = str(get_db["H2CONC"]['Val'])


class AlignDelegate(QStyledItemDelegate):
    def initStyleOption(self, option, index):
        super(AlignDelegate, self).initStyleOption(option, index)
        option.displayAlignment = Qt.AlignCenter


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainRight()
    font = QFontDatabase()
    font.addApplicationFont('./맑은 고딕.ttf')
    app.setFont(QFont('맑은 고딕'))
    window.show()
    app.exec_()

#
import sys
import multiprocessing
from copy import deepcopy
import time
import json

from PyQt5.QtWidgets import *
from PyQt5 import QtCore
from PyQt5.QtCore import *
#
from Temp_All_Module import CNS_Platform_controller_interface as CNS_controller
from main_window import MainWindow
from Temp_All_Module.TOOL.TOOL_etc import p_
# from Temp_All_Module.TOOL.TOOL_MatGP import Trend


class InterfaceFun(multiprocessing.Process):
    def __init__(self, shmem):
        multiprocessing.Process.__init__(self)
        self.shmem = shmem

    def run(self):
        app = QApplication(sys.argv)
        w = MyForm(self.shmem)
        sys.exit(app.exec_())


class MyForm(QWidget):
    def __init__(self, shmem):
        super(MyForm, self).__init__()
        # shmem
        self.shmem = shmem
        # ---- UI 호출
        p_(__file__, f'[SHMem:{self.shmem}][Controller UI 호출]')
        self.ui = CNS_controller.Ui_Form()
        self.ui.setupUi(self)

        # ----------- ADD !!! -------------- (20210419 for 효진)
        self.setGeometry(0, 0, 269, 620)
        self.auto_data_info_list = AutoDataList(parent=self)
        self.auto_data_info_list.setGeometry(20, 380, 225, 100)

        # ----------- Value 값 수정용 ----------------------------
        self.call_val_change_editor = QPushButton('Change Val Editor', self)
        self.call_val_change_editor.setGeometry(20, 540, 225, 30)
        self.call_val_change_editor.clicked.connect(self.go_val_change)

        # ----------- Trend 테스트 용 ----------------------------
        self.call_trend_view = QPushButton('Call Trend View', self)
        self.call_trend_view.setGeometry(20, 580, 225, 30)
        self.call_trend_view.clicked.connect(self.go_trend_view)

        # ---- UI 초기 세팅
        self.ui.Cu_SP.setText(str(self.shmem.get_logic('Speed')))
        self.ui.Se_SP.setText(str(self.shmem.get_logic('Speed')))
        # ---- 초기함수 호출
        # ---- 버튼 명령
        self.ui.Run.clicked.connect(self.run_cns)
        self.ui.Freeze.clicked.connect(self.freeze_cns)
        self.ui.Go_mal.clicked.connect(self.go_mal)
        self.ui.Initial.clicked.connect(self.go_init)
        self.ui.Apply_Sp.clicked.connect(self.go_speed)
        self.ui.Go_db.clicked.connect(self.go_save)

        # self.setWindowFlags(self.windowFlags() ^ QtCore.Qt.WindowStaysOnTopHint)
        self.show()

        # Call
        self.cns_main_win = MainWindow(parent=self)
        self.cns_main_win.show()

    def run_cns(self):
        if self.shmem.get_logic('Initial_condition'):
            p_(__file__, 'CNS 시작')
            self.shmem.change_logic_val('Run', True)
        else:
            p_(__file__, '먼저 초기 조건을 선언')

    def freeze_cns(self):
        if self.shmem.get_logic('Initial_condition'):
            p_(__file__, 'CNS 일시정지')
            self.shmem.change_logic_val('Run', False)
        else:
            p_(__file__, '먼저 초기 조건을 선언')

    def go_mal(self):
        if self.ui.Mal_nub.text() != '' and self.ui.Mal_type.text() != '' and self.ui.Mal_time.text() != '':
            # 1. 입력된 내용 List에 저장
            self.ui.Mal_list.addItem('{}_{}_{}'.format(self.ui.Mal_nub.text(),
                                                       self.ui.Mal_type.text(),
                                                       self.ui.Mal_time.text()))
            # 2. 입력된 내용 Trig mem에 저장
            Mal_index = self.ui.Mal_list.count()
            Mal_dict = {'Mal_nub': int(self.ui.Mal_nub.text()),
                        'Mal_opt': int(self.ui.Mal_type.text()),
                        'Mal_time': int(self.ui.Mal_time.text()) * 5,
                        'Mal_done': False}
            self.shmem.change_mal_val(mal_index=Mal_index, mal_dict=Mal_dict)
            # 3. 입력하는 레이블 Clear
            self.ui.Mal_nub.clear()
            self.ui.Mal_type.clear()
            self.ui.Mal_time.clear()
            p_(__file__, 'Malfunction 입력 완료')
        else:
            p_(__file__, 'Malfunction 입력 실패')

    def go_init(self):
        p_(__file__, 'CNS 초기 조건 선언')
        # 1. Mal list clear
        self.ui.Mal_list.clear()
        # 2. Mal trig_mem clear
        self.shmem.call_init(int(self.ui.Initial_list.currentIndex()) + 1)
        # 3. Controller interface update
        self.ui.Cu_SP.setText(str(self.shmem.get_logic('Speed')))
        self.ui.Se_SP.setText(str(self.shmem.get_logic('Speed')))
        # Main window 초기화

    def go_save(self):
        # 실시간 레코딩 중 ...
        self.shmem.change_logic_val('Run_rc', True)
        p_(__file__, 'Ester_Egg_Run_ROD CONTROL TRICK')

    def go_speed(self):
        p_(__file__, 'CNS 속도 조절')
        self.ui.Cu_SP.setText(self.shmem.get_speed(int(self.ui.Se_SP.text())))

    def go_val_change(self):
        if not self.shmem.get_logic('Run'):
            self.val_editor = ValEditor(self)
            self.val_editor.show()

    def go_trend_view(self):
        pass
        # self.TrendView = Trend(self, 200, 200)
        # self.TrendView.show()

    def show_main_window(self):
        # Controller와 동시 실행
        pass

    def closeEvent(self, QCloseEvent):
        p_(__file__, 'Close')
        self.shmem.send_close()
        sys.exit()


# # 자동 데이터 수집하는 구간 # #
class AutoDataList(QListWidget):
    def __init__(self, parent):
        super(AutoDataList, self).__init__(parent=parent)
        self.run_tirg = False

        # Q Timer ------------------------------------------------------------------------------------------------------
        timer = QTimer(self)
        for _ in [self._check_list]:
            timer.timeout.connect(_)
        timer.start(1000)

    def contextMenuEvent(self, event) -> None:
        """ ChartArea 에 기능 올리기  """
        menu = QMenu(self)
        add_input1 = menu.addAction("Add input")
        add_input2 = menu.addAction("Run")

        add_input1.triggered.connect(self._add_input)
        add_input2.triggered.connect(self._run_cns)

        menu.exec_(event.globalPos())

    def _add_input(self):
        mal, ok = QInputDialog.getText(self, 'Input Man', 'Mal nub')

        #for i in range(10, 21):
        #    self.addItem(f'12_{mal}{i}_10800')
        self.addItem(f'{mal}')

        # self.addItem(mal)

    def _check_list(self):
        if self.__len__() > 0 and self.run_tirg:
            local_logic = self.parent().shmem.get_logic_info()
            if local_logic['Run']:
                pass
            else:
                get_first_row = self.item(0).text().split('_')
                print(get_first_row, 'Start first line mal function')
                self.parent().go_init()
                time.sleep(5)
                self.parent().ui.Mal_nub.setText(get_first_row[0])
                self.parent().ui.Mal_type.setText(get_first_row[1])
                self.parent().ui.Mal_time.setText(get_first_row[2])
                self.parent().go_mal()
                time.sleep(5)
                self.parent().run_cns()
                time.sleep(5)
                self.takeItem(0)
        else:
            self.run_tirg = False

    def _run_cns(self):
        self.run_tirg = True


class ValEditor(QWidget):
    def __init__(self, parent):
        super(ValEditor, self).__init__()
        self.shmem = parent.shmem
        self.setGeometry(0, 0, 300, 50)

        h_layer = QHBoxLayout()
        v_layer = QVBoxLayout()

        name_h_layer = QHBoxLayout()
        self.name_label = QLabel('Name')
        self.name_label.setFixedWidth(50)
        self.name_text = QLineEdit('')
        name_h_layer.addWidget(self.name_label)
        name_h_layer.addWidget(self.name_text)

        val_h_layer = QHBoxLayout()
        self.val_label = QLabel('Val')
        self.val_label.setFixedWidth(50)
        self.val_text = QLineEdit('')
        val_h_layer.addWidget(self.val_label)
        val_h_layer.addWidget(self.val_text)

        v_layer.addLayout(name_h_layer)
        v_layer.addLayout(val_h_layer)

        self.change_btn = QPushButton('Change')
        self.change_btn.clicked.connect(self.change_val)

        h_layer.addLayout(v_layer)
        h_layer.addWidget(self.change_btn)

        self.setLayout(h_layer)

    def change_val(self):
        if self.shmem.check_para(str(self.name_text.text())):
            orgin = self.shmem.get_shmem_val(self.name_text.text())
            try:
                get_val = int(float(self.val_text.text())) if type(orgin) is int else float(self.val_text.text())
                self.shmem.change_shmem_val(self.name_text.text(), get_val)

                self.close()
            except:
                print('잘못된 파라메터 값 입력')
                self.val_text.clear()
        else:
            print('잘못된 파라메터 이름 입력')
            self.name_text.clear()
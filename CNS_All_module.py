import multiprocessing
import sys
#
from ENVCNS import ENVCNS

import pickle
import pandas as pd
from collections import deque
import numpy as np


class All_Function_module(multiprocessing.Process):
    def __init__(self, shmem, Max_len):
        multiprocessing.Process.__init__(self)
        self.daemon = True
        self.shmem = shmem

        # 1 CNS 환경 생성 ----------------------------------------------------
        # CNS 정보 읽기
        self.cns_ip, self.cns_port = self.shmem.get_cns_info()
        self.remote_ip, self.remote_port = self.shmem.get_remote_info()
        self.cns_env = ENVCNS(Name='EnvCNS', IP=self.cns_ip, PORT=int(self.cns_port),
                              RIP=self.remote_ip, RPORT=int(self.remote_port),
                              Max_len=Max_len)
        # 예지 추가 부분 ------------------------------------------------------------------------------ 효진
        self.bi_time_step = 60
        with open('./DB/HK/x_scaler.pkl', 'rb') as f:
            self.x_scaler = pickle.load(f)
        with open('./DB/HK/y_scaler.pkl', 'rb') as f:
            self.y_scaler = pickle.load(f)
        self.bi_para = pd.read_csv('./DB/HK/LOCA_all_para_90.csv')['0'].tolist()
        self.bi_data = deque(maxlen=self.bi_time_step)
        # ------------------------------------ 효진

    def Bi_LSTM(self):
        from keras.layers import TimeDistributed, \
            concatenate, Activation, dot, Bidirectional, Concatenate

        from keras import backend as K
        from keras.models import Model
        from keras.layers import Input, LSTM, RepeatVector
        from keras.layers.core import Dense, Lambda
        from keras.optimizers import RMSprop

        from tensorflow.python.framework.ops import disable_eager_execution
        disable_eager_execution()
        input_train = Input(batch_shape=(None, 60, 439))
        encoder_stack_h, forward_h, forward_c, backward_h, backward_c = Bidirectional(LSTM(
            500, activation='relu', return_state=True, return_sequences=True))(input_train)
        encoder_last_h = Concatenate()([forward_h, backward_h])
        encoder_last_c = Concatenate()([forward_c, backward_c])
        z_mean = Dense(1500)(encoder_last_h)
        z_log_sigma = Dense(1500)(encoder_last_h)

        def samplingz(argz):
            z_mean, z_log_sigma = argz
            epsilongz = K.random_normal(shape=(K.shape(z_mean)[0], K.shape(z_mean)[1]),
                                        mean=0, stddev=1)
            return z_mean + z_log_sigma * epsilongz

        z = Lambda(samplingz, output_shape=(1500,))([z_mean, z_log_sigma])

        decoder_mean = LSTM(1000, activation='relu', return_state=False, return_sequences=True)
        h_decoded = RepeatVector(120)(z)
        h_decoded = decoder_mean(h_decoded, initial_state=[encoder_last_h, encoder_last_c])
        attention = dot([h_decoded, encoder_stack_h], axes=[2, 2])
        attention = Activation('softmax')(attention)
        context = dot([attention, encoder_stack_h], axes=[2, 1])
        decoder_combined_context = concatenate([context, h_decoded])
        out = TimeDistributed(Dense(22, activation='relu'))(decoder_combined_context)
        model = Model(inputs=input_train, outputs=out)

        def vae_loss(y_true, y_pred):
            xent_loss = K.mean(K.square(y_pred - y_true))
            kl_loss = - 0.5 * K.mean(1 + z_log_sigma - K.square(z_mean) - K.exp(z_log_sigma))
            loss = xent_loss + kl_loss
            return loss

        opt = RMSprop(lr=0.000001)
        model.compile(loss=vae_loss, optimizer=opt, experimental_run_tf_function=False,
                      )
        return model

    def pr_(self, s):
        head_ = 'AllFuncM'
        return print(f'[{head_:10}][{s}]')

    def _update_cnsenv_to_sharedmem(self):
        # st = time.time()
        self.shmem.change_shmem_db(self.cns_env.mem)
        # print(time.time()-st)

    def check_init(self):
        if self.shmem.get_logic('Init_Call'):
            self.pr_('Initial Start...')
            self.cns_env.reset(file_name='cns_log', initial_nub=self.shmem.get_logic('Init_nub'))
            self._update_cnsenv_to_sharedmem()
            self.shmem.change_logic_val('Init_Call', False)
            self.pr_('Initial End!')

            # 버그 수정 2번째 초기조건에서 0으로 초기화 되지 않는 현상 수정
            if self.cns_env.CMem.CTIME != 0:
                self.cns_env.CMem.update()

    def check_mal(self):
        sw, info_mal = self.shmem.get_shmem_malinfo()
        if sw:
            self.pr_('Mal Start...')
            self.shmem.change_logic_val('Mal_Call', False)
            for _ in info_mal:
                if not info_mal[_]['Mal_done']:     # mal history 중 입력이 안된 것을 찾아서 수행.
                    self.cns_env._send_malfunction_signal(info_mal[_]['Mal_nub'],
                                                          info_mal[_]['Mal_opt'],
                                                          info_mal[_]['Mal_time']
                                                          )
                    self.shmem.change_mal_list(_)
            self.pr_('Mal End!')
            # -- file name 최초 malcase로 전달받음
            self.cns_env.file_name = f'{info_mal[1]["Mal_nub"]}_{info_mal[1]["Mal_opt"]}_{info_mal[1]["Mal_time"]}'
            self.cns_env.init_line()

    def check_speed(self):
        if self.shmem.get_logic('Speed_Call'):
            self.cns_env.want_tick = self.shmem.get_logic('Speed')
            self.shmem.change_logic_val('Speed_Call', False)

    def run(self):
        # ==============================================================================================================
        # - 공유 메모리에서 logic 부분을 취득 후 사용되는 AI 네트워크 정보 취득
        local_logic = self.shmem.get_logic_info()

        if local_logic['Run_ProDiag']:
            # ------------------------------------ 효진
            self.bi_model = self.Bi_LSTM()  # 효진 사전 정의 모델 구조 입력 (complie 까지 입력)
            self.bi_model.load_weights('./DB/HK/model_60_439_90_variational_ALL_8.h5')  # 모델 가중치 path 입력

        while True:
            local_logic = self.shmem.get_logic_info()
            if local_logic['Close']: sys.exit()
            if local_logic['Run']:
                if local_logic['Run_ai']:
                    """
                    TODO AI 방법론 추가
                    """
                    # Make action from AI ------------------------------------------------------------------------------
                    # - 동작이 허가된 AI 모듈이 cns_env 에서 상태를 취득하여 액션을 계산함.
                    # TODO 향후 cns_env에서 노멀라이제이션까지 모두 처리 할 것.
                    # 예지 모듈 -----------------------------------------------------------------------------------------
                    if local_logic['Run_ProDiag']:

                        bi_db = [self.cns_env.mem[i]['Val'] for i in self.bi_para]
                        self.bi_data.append(bi_db)
                        while True:
                            if np.shape(self.bi_data)[0] == self.bi_time_step:
                                break
                            else:
                                self.bi_data.append(bi_db)

                        if np.shape(self.bi_data)[0] == self.bi_time_step:  # self.lstm_data = 2차원: 추후 []로 3차원 데이터로 성형
                            bi_test_x = self.x_scaler.transform(self.bi_data)
                            bi_result = self.bi_model.predict(np.array([bi_test_x]))
                            bi_result = self.y_scaler.inverse_transform(bi_result[0])

                            bi_prz_level_pred = bi_result[:, 0]  # 가압기 수위
                            bi_prz_pressure_pred = bi_result[:, 1]  # 가압기 압력
                            bi_sg3_pressure_pred = bi_result[:, 2]   # SG3 압력
                            bi_sg2_pressure_pred = bi_result[:, 3]  # SG2 압력
                            bi_sg1_pressure_pred = bi_result[:, 4]  # SG1 압력
                            bi_sg3_level_pred = bi_result[:, 5]  # SG3 수위
                            bi_sg2_level_pred = bi_result[:, 6]  # SG2 수위
                            bi_sg1_level_pred = bi_result[:, 7]  # SG1 수위
                            bi_feedwater3_flow_pred = bi_result[:, 8]  # Feedwater 3 유량
                            bi_feedwater2_flow_pred = bi_result[:, 9]  # Feedwater 2 유량
                            bi_feedwater1_flow_pred = bi_result[:, 10]  # Feedwater 1 유량
                            bi_CTMT_pressure_pred = bi_result[:, 11]  # 컨테이먼트 압력
                            bi_CTMT_radiation_pred = bi_result[:, 12]  # 컨테이먼트 방사능
                            bi_H2_concentration_pred = bi_result[:, 13]  # 컨테이먼트 수소 농도
                            bi_CTMT_temperature_pred = bi_result[:, 14]  # 컨테인먼트 온도
                            bi_CTMT_sump_water_level_pred = bi_result[:, 15]  # 섬프 물 높이
                            bi_coldleg1_temperature_pred = bi_result[:, 16]  # coldleg1 온도
                            bi_coldleg2_temperature_pred = bi_result[:, 17]  # coldleg2 온도
                            bi_coldleg3_temperature_pred = bi_result[:, 18]  # coldleg3 온도
                            bi_hotleg1_temperature_pred = bi_result[:, 19]  # hotleg1 온도
                            bi_hotleg2_temperature_pred = bi_result[:, 20]  # hotleg2 온도
                            bi_hotleg3_temperature_pred = bi_result[:, 21]  # hotleg3 온도

                            make_result = {
                                'PCTMT': bi_CTMT_pressure_pred,
                                'H2CONC': bi_H2_concentration_pred,
                                'ZINST58': bi_prz_pressure_pred,
                                'ZINST78': bi_sg1_level_pred,
                                'ZINST77': bi_sg2_level_pred,
                                'ZSUMP': bi_CTMT_sump_water_level_pred
                            }

                            self.shmem.change_logic_val('Prog_Result', make_result)

                    # end AI
                # One Step CNS -------------------------------------------------------------------------------------
                Action_dict = {}  # 향후 액션 추가
                self.cns_env.step(0) # 1초 돌 때 (5tick)

                # Update All mem -----------------------------------------------------------------------------------
                self._update_cnsenv_to_sharedmem()

                # 자동 멈춤 조건
                # if self.cns_env.mem['KCNTOMS']['Val'] > 7500:
                #     self.shmem.change_logic_val('Run', False)

            else:
                self.check_init()
                self.check_mal()
                self.check_speed()

import numpy as np
from TOOL.TOOL_CNS_UDP_FAST import CNS
from TOOL.TOOL_Cool import CoolingRATE
from TOOL import TOOL_PTCurve

import random


class CMem:
    def __init__(self, mem):
        self.m = mem  # Line CNSmem -> getmem
        self.CoolingRateSW = 0
        self.CoolingRateFixTemp = 0
        self.CoolingRateFixTime = 0

        self.CoolingRATE = CoolingRATE()

        self.StartRL = 0

        self.update()

    def update(self):
        self.CTIME = self.m['KCNTOMS']['Val']       # CNS Time

        # Physical
        self.SG1Nar = self.m['ZINST78']['Val']
        self.SG2Nar = self.m['ZINST77']['Val']
        self.SG3Nar = self.m['ZINST76']['Val']

        self.SG1Wid = self.m['ZINST72']['Val']
        self.SG2Wid = self.m['ZINST71']['Val']
        self.SG3Wid = self.m['ZINST70']['Val']

        self.SG1Pres = self.m['ZINST75']['Val']
        self.SG2Pres = self.m['ZINST74']['Val']
        self.SG3Pres = self.m['ZINST73']['Val']

        self.SG1Feed = self.m['WFWLN1']['Val']
        self.SG2Feed = self.m['WFWLN2']['Val']
        self.SG3Feed = self.m['WFWLN3']['Val']

        self.Aux1Flow = self.m['WAFWS1']['Val']
        self.Aux2Flow = self.m['WAFWS2']['Val']
        self.Aux3Flow = self.m['WAFWS3']['Val']

        self.SteamLine1 = self.m['BHV108']['Val']
        self.SteamLine2 = self.m['BHV208']['Val']
        self.SteamLine3 = self.m['BHV308']['Val']

        self.AVGTemp = self.m['UAVLEG2']['Val']
        self.PZRPres = self.m['ZINST65']['Val']
        self.PZRLevel = self.m['ZINST63']['Val']

        # Signal
        self.Trip = self.m['KLAMPO9']['Val']
        self.SIS = self.m['KLAMPO6']['Val']
        self.MSI = self.m['KLAMPO3']['Val']
        self.NetBRK = self.m['KLAMPO224']['Val']

        # Comp
        self.RCP1 = self.m['KLAMPO124']['Val']
        self.RCP2 = self.m['KLAMPO125']['Val']
        self.RCP3 = self.m['KLAMPO126']['Val']

        self.TurningGear = self.m['KLAMPO165']['Val']
        self.OilSys = self.m['KLAMPO164']['Val']
        self.BHV311 = self.m['BHV311']['Val']

        self.SteamDumpPos = self.m['ZINST98']['Val']
        self.SteamDumpManAuto = self.m['KLAMPO150']['Val']

        self.PMSS = self.m['PMSS']['Val']

        # ??????????????? ?????? ?????? ??????
        self.PZRSprayManAuto = self.m['KLAMPO119']['Val']
        self.PZRSprayPos = self.m['ZINST66']['Val']
        self.PZRSprayPosControl = self.m['BPRZSP']['Val']

        self.PZRBackHeaterOnOff = self.m['KLAMPO118']['Val']
        self.PZRProHeaterManAuto = self.m['KLAMPO117']['Val']
        self.PZRProHeaterPos = self.m['QPRZH']['Val']

        self.SIValve = self.m['BHV22']['Val']

        self.ChargingManAUto = self.m['KLAMPO95']['Val']
        self.ChargingValvePos = self.m['BFV122']['Val']
        self.ChargingPump2State = self.m['KLAMPO70']['Val']

        self.LetdownLV459Pos = self.m['BLV459']['Val']
        self.LetdownHV1Pos = self.m['BHV1']['Val']
        self.LetdownHV2Pos = self.m['BHV2']['Val']
        self.LetdownHV3Pos = self.m['BHV3']['Val']

        # Logic
        if self.CTIME == 0:
            self.CoolingRateSW = 0
            self.CoolingRATE.reset_info()

            self.StartRL = 0

        if self.CoolingRateSW == 1:         # 2.0] Cooling rage ?????? ??????
            self.CoolingRATE.save_info(self.AVGTemp, self.CTIME)
            self.CoolingRateSW += 1     # ??? 2??? ??????????????? ??? ????????? 1?????? ?????????.


class ENVCNS(CNS):
    def __init__(self, Name, IP, PORT, RIP, RPORT, Max_len):
        super(ENVCNS, self).__init__(threrad_name=Name,
                                     CNS_IP=IP, CNS_Port=PORT,
                                     Remote_IP=RIP, Remote_Port=RPORT, Max_len=Max_len)
        self.Name = Name  # = id
        self.ENVStep = 0
        self.LoggerPath = 'DB'
        self.want_tick = 300  # 1sec

        self.Loger_txt = ''

        self.CMem = CMem(self.mem)

        self.input_info_EM = [
            # (para, x_round, x_min, x_max), (x_min=0, x_max=0 is not normalized.)
            ('ZINST98', 1, 0, 100),  # SteamDumpPos
            ('ZINST87', 1, 0, 50),  # Steam Flow 1
            ('ZINST86', 1, 0, 50),  # Steam Flow 2
            ('ZINST85', 1, 0, 50),  # Steam Flow 3
            ('KLAMPO70', 1, 0, 1),  # Charging Pump2 State
            ('BHV22', 1, 0, 1),  # SI Valve State
            ('ZINST66', 1, 0, 25),  # PZRSprayPos
            ('UAVLEG2', 1, 150, 320),  # PTTemp
            ('ZINST65', 1, 0, 160),  # PTPressure
            ('ZINST78', 1, 0, 70),  # SG1Nar
            ('ZINST77', 1, 0, 70),  # SG2Nar
            ('ZINST76', 1, 0, 70),  # SG3Nar
            ('ZINST75', 1, 0, 80),  # SG1Pres
            ('ZINST74', 1, 0, 80),  # SG2Pres
            ('ZINST73', 1, 0, 80),  # SG3Pres
            ('ZINST72', 1, 0, 100),  # SG1Wid
            ('ZINST71', 1, 0, 100),  # SG2Wid
            ('ZINST70', 1, 0, 100),  # SG3Wid
            ('UUPPPL', 1, 100, 350),  # CoreExitTemp
            ('WFWLN1', 1, 0, 25),  # SG1Feed
            ('WFWLN2', 1, 0, 25),  # SG2Feed
            ('WFWLN3', 1, 0, 25),  # SG3Feed
            ('UCOLEG1', 1, 0, 100),  # RCSColdLoop1
            ('UCOLEG2', 1, 0, 100),  # RCSColdLoop2
            ('UCOLEG3', 1, 0, 100),  # RCSColdLoop3
            ('ZINST65', 1, 0, 160),  # RCSPressure
            ('ZINST63', 1, 0, 100),  # PZRLevel
        ]

        # --------------------------------------------------------------------------------------------------------------


    def normalize(self, x, x_round, x_min, x_max):
        if x_max == 0 and x_min == 0:
            # It means X value is not normalized.
            x = x / x_round
        else:
            x = x_max if x >= x_max else x
            x = x_min if x <= x_min else x
            x = (x - x_min) / (x_max - x_min)
        return x

    def get_state(self, input_info):
        state = []
        for para, x_round, x_min, x_max in input_info:
            if para in self.mem.keys():
                _ = self.mem[para]['Val']
            else:
                if para == 'DSetPoint':
                    _ = 0
                else:
                    _ = None
                # ------------------------------------------------------------------------------------------------------
                if _ is None:
                    raise ValueError(f'{para} is not in self.input_info')
                # ------------------------------------------------------------------------------------------------------
            state.append(self.normalize(_, x_round, x_min, x_max))
        return np.array(state), state

    def _send_control_save(self, zipParaVal):
        super(ENVCNS, self)._send_control_save(para=zipParaVal[0], val=zipParaVal[1])

    def _send_act_EM_Module(self, A):
        def a_log_f(s=''):
            pass

        ActOrderBook = {
            'StopAllRCP': (['KSWO132', 'KSWO133', 'KSWO134'], [0, 0, 0]),
            'StopRCP1': (['KSWO132'], [0]),
            'StopRCP2': (['KSWO133'], [0]),
            'StopRCP3': (['KSWO134'], [0]),
            'NetBRKOpen': (['KSWO244'], [0]),
            'OilSysOff': (['KSWO190'], [0]),
            'TurningGearOff': (['KSWO191'], [0]),
            'CutBHV311': (['BHV311', 'FKAFWPI'], [0, 0]),

            'PZRSprayMan': (['KSWO128'], [1]), 'PZRSprayAuto': (['KSWO128'], [0]),

            'PZRSprayClose': (['BPRZSP'], [self.mem['BPRZSP']['Val'] + 0.015 * -1]),
            'PZRSprayOpen': (['BPRZSP'], [self.mem['BPRZSP']['Val'] + 0.015 * 1]),

            'PZRBackHeaterOff': (['KSWO125'], [0]), 'PZRBackHeaterOn': (['KSWO125'], [1]),

            'SteamDumpMan': (['KSWO176'], [1]), 'SteamDumpAuto': (['KSWO176'], [0]),

            'IFLOGIC_SteamDumpUp': (['PMSS'], [self.CMem.PMSS + 2.0E5 * 3 * 0.2]),
            'IFLOGIC_SteamDumpDown': (['PMSS'], [self.CMem.PMSS + 2.0E5 * (-3) * 0.2]),

            'DecreaseAux1Flow': (['KSWO142', 'KSWO143'], [1, 0]),
            'IncreaseAux1Flow': (['KSWO142', 'KSWO143'], [0, 1]),
            'DecreaseAux2Flow': (['KSWO151', 'KSWO152'], [1, 0]),
            'IncreaseAux2Flow': (['KSWO151', 'KSWO152'], [0, 1]),
            'DecreaseAux3Flow': (['KSWO154', 'KSWO155'], [1, 0]),
            'IncreaseAux3Flow': (['KSWO154', 'KSWO155'], [0, 1]),

            'SteamLine1Open': (['KSWO148', 'KSWO149'], [1, 0]),
            'SteamLine2Open': (['KSWO146', 'KSWO147'], [1, 0]),
            'SteamLine3Open': (['KSWO144', 'KSWO145'], [1, 0]),

            'ResetSI': (['KSWO7', 'KSWO5'], [1, 1]),

            'PZRProHeaterMan': (['KSWO120'], [1]), 'PZRProHeaterAuto': (['KSWO120'], [0]),
            'PZRProHeaterDown': (['KSWO121', 'KSWO122'], [1, 0]),
            'PZRProHeaterUp': (['KSWO121', 'KSWO122'], [0, 1]),

            'RL_IncreaseAux1Flow': (['WAFWS1'], [self.mem['WAFWS1']['Val'] + 0.04 * 1]),
            'RL_DecreaseAux1Flow': (['WAFWS1'], [self.mem['WAFWS1']['Val'] + 0.04 * (-1)]),
            'RL_IncreaseAux2Flow': (['WAFWS2'], [self.mem['WAFWS2']['Val'] + 0.04 * 1]),
            'RL_DecreaseAux2Flow': (['WAFWS2'], [self.mem['WAFWS2']['Val'] + 0.04 * (-1)]),
            'RL_IncreaseAux3Flow': (['WAFWS3'], [self.mem['WAFWS3']['Val'] + 0.04 * 1]),
            'RL_DecreaseAux3Flow': (['WAFWS3'], [self.mem['WAFWS3']['Val'] + 0.04 * (-1)]),

            'ChargingValveMan': (['KSWO100'], [1]), 'ChargingValveAUto': (['KSWO100'], [0]),
            'ChargingValveDown': (['KSWO101', 'KSWO102'], [1, 0]),
            'ChargingValveUp': (['KSWO101', 'KSWO102'], [0, 1]),

            'LetdownLV459Open': (['KSWO114', 'KSWO113'], [1, 0]),
            'LetdownLV459Close': (['KSWO114', 'KSWO113'], [0, 1]),

            'LetdownHV1Open': (['KSWO104', 'KSWO103'], [1, 0]),
            'LetdownHV1Close': (['KSWO104', 'KSWO103'], [0, 1]),
            'LetdownHV2Open': (['KSWO106', 'KSWO105'], [1, 0]),
            'LetdownHV2Close': (['KSWO106', 'KSWO105'], [0, 1]),
            'LetdownHV3Open': (['KSWO108', 'KSWO107'], [1, 0]),
            'LetdownHV3Close': (['KSWO108', 'KSWO107'], [0, 1]),

            'RunRCP2': (['KSWO130', 'KSWO133'], [1, 1]),
            'RunCHP2': (['KSWO70'], [1]), 'StopCHP2': (['KSWO70'], [0]),
            'OpenSI': (['KSWO81', 'KSWO82'], [1, 0]), 'CloseSI': (['KSWO81', 'KSWO82'], [0, 1]),
        }

        AMod = A
        print('[EM_Module]', self.CMem.CTIME)
        if self.CMem.Trip == 1:
            # 1.1] ????????? Trip ?????? ?????? ?????? ??????
            # 1.1.1] RCP 97 ?????? ???????????? ?????? ??????
            if self.CMem.RCP1 == 1 and self.CMem.PZRPres < 97 and self.CMem.CTIME < 15 * 60 * 5:
                a_log_f(s=f'Pres [{self.CMem.PZRPres}] < 97 RCP 1 stop')
                self._send_control_save(ActOrderBook['StopRCP1'])
            if self.CMem.RCP2 == 1 and self.CMem.PZRPres < 97 and self.CMem.CTIME < 15 * 60 * 5:
                a_log_f(s=f'Pres [{self.CMem.PZRPres}] < 97 RCP 2 stop')
                self._send_control_save(ActOrderBook['StopRCP2'])
            if self.CMem.RCP3 == 1 and self.CMem.PZRPres < 97 and self.CMem.CTIME < 15 * 60 * 5:
                a_log_f(s=f'Pres [{self.CMem.PZRPres}] < 97 RCP 3 stop')
                self._send_control_save(ActOrderBook['StopRCP3'])
            # 1.1.2] ????????? ?????? ??? Netbrk, turning gear, oil sys, BHV311 ?????? ??? ??????
            if self.CMem.NetBRK == 1:
                a_log_f(s=f'NetBRK [{self.CMem.NetBRK}] Off')
                self._send_control_save(ActOrderBook['NetBRKOpen'])
            if self.CMem.TurningGear == 1:
                a_log_f(s=f'TurningGear [{self.CMem.TurningGear}] Off')
                self._send_control_save(ActOrderBook['TurningGearOff'])
            if self.CMem.OilSys == 1:
                a_log_f(s=f'OilSys [{self.CMem.OilSys}] Off')
                self._send_control_save(ActOrderBook['OilSysOff'])
            if self.CMem.BHV311 > 0:
                a_log_f(s=f'BHV311 [{self.CMem.BHV311}] Cut')
                self._send_control_save(ActOrderBook['CutBHV311'])
            # 1.2] ?????? ???????????? ?????? ?????? ????????? ???????????? ?????? ???????????? ?????? Set-up
            a_log_f(s=f'[Check][{self.CMem.SIS}][{self.CMem.MSI}][Check Main logic 1]')
            if self.CMem.SIS != 0 and self.CMem.MSI != 0:
                if max(self.CMem.SG1Pres, self.CMem.SG2Pres, self.CMem.SG3Pres) < self.CMem.SteamDumpPos:
                    a_log_f(s=f'StemDumpPos [{self.CMem.SteamDumpPos}] change')
                    self._send_control_save(ActOrderBook['IFLOGIC_SteamDumpDown'])
            # 1.2] SI reset ?????? Aux ????????? [?????? ?????? 20200903]
                if self.CMem.SG1Feed == self.CMem.SG2Feed and self.CMem.SG1Feed == self.CMem.SG3Feed and \
                        self.CMem.SG2Feed == self.CMem.SG1Feed and self.CMem.SG2Feed == self.CMem.SG3Feed and \
                        self.CMem.SG3Feed == self.CMem.SG1Feed and self.CMem.SG3Feed == self.CMem.SG2Feed:
                    a_log_f(s=f'[{self.CMem.SG1Feed:10}, {self.CMem.SG2Feed:10}, {self.CMem.SG3Feed:10}] Feed water avg done')
                else:
                    # 1.2.1] ?????? ????????? ??????
                    # 1.2.1.1] ?????? ??? ?????? ??????
                    SGFeedList = [self.CMem.SG1Feed, self.CMem.SG2Feed, self.CMem.SG3Feed]
                    MaxSGFeed = SGFeedList.index(max(SGFeedList))  # 0, 1, 2
                    MinSGFeed = SGFeedList.index(min(SGFeedList))  # 0, 1, 2
                    self._send_control_save(ActOrderBook[f'DecreaseAux{MaxSGFeed + 1}Flow'])
                    self._send_control_save(ActOrderBook[f'IncreaseAux{MinSGFeed + 1}Flow'])
                    a_log_f(s=f'[{self.CMem.SG1Feed:10}, {self.CMem.SG2Feed:10}, {self.CMem.SG3Feed:10}] Feed water avg')
            # 1.3] 3000?????? SI reset
            if self.CMem.CTIME == 3000 + (18000 * 5):
                self._send_control_save(ActOrderBook['ResetSI'])
                a_log_f(s=f'ResetSI [{self.CMem.CTIME}]')
            # 2] SI reset ?????? ??? ?????? ?????? ??????
            if self.CMem.SIS == 0 and self.CMem.MSI == 0 and self.CMem.CTIME > 5 * 60 * 5:
                # 2.0] Cooling rage ?????? ??????
                if self.CMem.CoolingRateSW == 0:
                    self.CMem.CoolingRateSW = 1
                    a_log_f(s=f'CoolingRateSW')
                # 2.1] Press set-point ??? ?????? ?????? ?????? ???????????? ?????? ( not work )
                if self.CMem.SteamDumpManAuto == 0:
                    self._send_control_save(ActOrderBook['SteamDumpMan'])
                    a_log_f(s=f'SteamDumpMan [{self.CMem.SteamDumpManAuto}]')
                # 2.2] Steam Line Open
                if self.CMem.SteamLine1 == 0:
                    self._send_control_save(ActOrderBook['SteamLine1Open'])
                    a_log_f(s=f'SteamLine1 [{self.CMem.SteamLine1}] Open')
                if self.CMem.SteamLine2 == 0:
                    self._send_control_save(ActOrderBook['SteamLine2Open'])
                    a_log_f(s=f'SteamLine2 [{self.CMem.SteamLine2}] Open')
                if self.CMem.SteamLine3 == 0:
                    self._send_control_save(ActOrderBook['SteamLine3Open'])
                    a_log_f(s=f'SteamLine3 [{self.CMem.SteamLine3}] Open')
                # 2.3] Charging flow ?????????
                if self.CMem.ChargingManAUto == 0:
                    self._send_control_save(ActOrderBook['ChargingValveMan'])
                    a_log_f(s=f'ChargingMode [{self.CMem.ChargingManAUto}] Man')
                if self.CMem.ChargingValvePos != 0:
                    self._send_control_save(ActOrderBook['ChargingValveDown'])
                    a_log_f(s=f'ChargingPOS [{self.CMem.ChargingValvePos}] Close')
                # 2.3] PZR spray ?????? ?????? [??????]
                if self.CMem.PZRSprayManAuto == 0:
                    self._send_control_save(ActOrderBook['PZRSprayMan'])
                    a_log_f(s=f'PZRSprayMan [{self.CMem.PZRSprayManAuto}] Man')
                # 2.4] RCP 2 ??????
                if self.CMem.RCP2 == 0:
                    self._send_control_save(ActOrderBook['RunRCP2'])
                    a_log_f(s=f'RCP2 [{self.CMem.RCP2}] Start')
                # 2.5] PZR ????????? ?????? Heater ??????
                if self.CMem.PZRProHeaterManAuto == 0:
                    self._send_control_save(ActOrderBook['PZRProHeaterMan'])
                    a_log_f(s=f'PZR PRO heater [{self.CMem.PZRProHeaterManAuto}] Man')
                if self.CMem.PZRProHeaterPos >= 0:
                    self._send_control_save(ActOrderBook['PZRProHeaterDown'])
                    a_log_f(s=f'PZR PRO Pos [{self.CMem.PZRProHeaterPos}] Down')
                if self.CMem.PZRBackHeaterOnOff == 1:
                    self._send_control_save(ActOrderBook['PZRBackHeaterOff'])
                    a_log_f(s=f'PZRBackHeaterOff [{self.CMem.PZRBackHeaterOnOff}] Off')
                # 3.0] ???????????? ?????? ??????
                if self.CMem.StartRL == 0:
                    self.CMem.StartRL = 1
                    a_log_f(s=f'StartRL [{self.CMem.StartRL}]')
                else:
                    # 3.1] ????????? ??????????????? ???????????? ????????? ?????? Letdown ?????? ??????
                    if self.CMem.PZRLevel > 20:
                        pass
                        # if self.CMem.LetdownLV459Pos == 0:
                        #     self._send_control_save(ActOrderBook['LetdownLV459Open'])
                        # if self.CMem.LetdownHV1Pos == 0:
                        #     self._send_control_save(ActOrderBook['LetdownHV1Open'])
                        # if self.CMem.LetdownHV2Pos == 0:
                        #     self._send_control_save(ActOrderBook['LetdownHV2Open'])

                    # 3.1] Spray control
                    if True:
                        pos = self.CMem.PZRSprayPosControl + 0.015 * np.clip(AMod[0] * 2, -2, 2)
                        zip_spray_pos = (['BPRZSP'], [pos])
                        self._send_control_save(zip_spray_pos)
                        a_log_f(s=f'Change Spray Pos [{self.CMem.PZRSprayPosControl:10}|{pos:10}]')
                    # 3.2] Aux Feed
                    if True:
                        aux123 = 0
                        if AMod[1] < -0.3:
                            # Decrease
                            aux123 = -1
                        elif -0.3 <= AMod[1] < 0.3:
                            # Stay
                            aux123 = 0
                        elif 0.3 <= AMod[1]:
                            # Increase
                            aux123 = 1

                        if self.CMem.SG1Wid > 80:
                            aux123 = -1

                        pos1 = self.CMem.Aux1Flow + 0.04 * aux123
                        pos2 = self.CMem.Aux2Flow + 0.04 * aux123
                        pos3 = self.CMem.Aux3Flow + 0.04 * aux123
                        zip_aux_pos = (['WAFWS1', 'WAFWS2', 'WAFWS3'], [pos1, pos2, pos3])
                        self._send_control_save(zip_aux_pos)
                        a_log_f(s=f'AuxFlow'
                                  f'[{self.CMem.Aux1Flow:10}|{pos1:10}]'
                                  f'[{self.CMem.Aux2Flow:10}|{pos2:10}]'
                                  f'[{self.CMem.Aux3Flow:10}|{pos3:10}]')
                    # 3.3] SI Supply water
                    if True:
                        if AMod[2] < -0.8:
                            # self._send_control_save(ActOrderBook['CloseSI'])
                            a_log_f(s=f'CloseSI')
                        elif -0.8 <= AMod[2] < -0.6:
                            self._send_control_save(ActOrderBook['StopCHP2'])
                            a_log_f(s=f'StopCHP2')
                        elif -0.6 <= AMod[2] < 0.6:
                            #
                            pass
                        elif 0.6 <= AMod[2] < 0.8:
                            self._send_control_save(ActOrderBook['RunCHP2'])
                            a_log_f(s=f'RunCHP2')
                        elif 0.8 <= AMod[2]:
                            # self._send_control_save(ActOrderBook['OpenSI'])
                            a_log_f(s=f'OpenSI')

                        if self.CMem.CTIME > 30000 + (18000 * 5):     # TRICK
                            # SI logic <- ?????? ????????? ?????? ??????.
                            Updis, Botdis = TOOL_PTCurve.PTCureve()._check_distance(self.CMem.AVGTemp, self.CMem.PZRPres)
                            if Botdis > 12:
                                self._send_control_save(ActOrderBook['CloseSI'])
                            elif Botdis < 5:
                                self._send_control_save(ActOrderBook['OpenSI'])

                    # 3.4] Steam Dump
                    if True:
                        SteamDumpRate = 4
                        DumpPos = self.CMem.PMSS + 2.0E5 * np.clip(AMod[3] * SteamDumpRate,
                                                                   - SteamDumpRate, SteamDumpRate) * 0.2
                        zip_Dump_pos = (['PMSS'], [DumpPos])
                        self._send_control_save(zip_Dump_pos)
                        a_log_f(s=f'PMSS [{self.CMem.PMSS:10}|{DumpPos:10}]')

        return 0

    def send_act(self, A):
        """
        A ??? ???????????? ????????? ????????? ???????????? ??????
        E.x)
            self._send_control_save(['KSWO115'], [0])
            ...
            self._send_control_to_cns()
        :param A: A ?????? [0, 0, 0] <- act space??? ?????????
        :return: AMod: ????????? ??????
        """
        AMod = A

        if isinstance(A, int):      # A=0 ?????????
            if A == 1:
                # 16.0
                for _tar, _val in zip(['WAFWS1', 'WAFWS2', 'WAFWS3'], ['KSWO143', 'KSWO152', 'KSWO155']):
                    if self.mem[_tar]['Val'] < 20:
                        if self.CMem.CTIME >= self.FixedRad + 1325: self._send_control_save([_val], [1])
                # 17.2
                if self.CMem.CTIME == self.FixedRad + 1750: self._send_control_save(['KSWO208'], [1])

                # 20.4
                if self.CMem.CTIME == self.FixedRad + 2000: self._send_control_save(['KSWO115'], [1])
                if self.CMem.CTIME == self.FixedRad + 2300: self._send_control_save(['KSWO123'], [1])

                # 21.3
                if self.CMem.CTIME == self.FixedRad + 2600: self._send_control_save(['KSWO132'], [0])
                if self.CMem.CTIME == self.FixedRad + 2650: self._send_control_save(['KSWO133'], [0])
                if self.CMem.CTIME == self.FixedRad + 2700: self._send_control_save(['KSWO134'], [0])
            pass
        elif isinstance(A, dict):   # A = { ... } ??? AI ????????? ????????? ???????????? ??????
            if A['EM'] is not None:
                if self.CMem.CoolingRateSW == 0:
                    if self.CMem.CTIME % 100 == 0:
                        self._send_act_EM_Module(A['EM'])
                else:
                    if self.CMem.CTIME % 100 == 0:
                        self._send_act_EM_Module(A['EM'])
        else:
            print('Error')
        # Done Act
        self._send_control_to_cns()
        return AMod

    def step(self, A):
        """
        A??? ?????? 1 step ??????
        :param A: A -> dict
        :return: ?????? state??? reward done ??????
        """
        # Old Data (time t) ---------------------------------------
        AMod = self.send_act(A)

        # if self.CMem.CoolingRateSW == 0:
        #     if self.CMem.CTIME >= 800:
        #         # ???????????? ?????? ??? 5 tick
        #         self.want_tick = int(5)
        #     else:
        #         self.want_tick = int(5)
        # else:
        #     # Cooling ?????? ?????? ??? ???????????? ?????? ??? 100 tick
        #     self.want_tick = int(5)

        print(self.want_tick, self.CMem.CTIME)

        # New Data (time t+1) -------------------------------------
        super(ENVCNS, self).step() # ?????? CNS mem run-Freeze ?????? mem ????????????
        self.CMem.update()  # ?????? ?????? mem ????????????

        # ????????? ?????? ??????
        self.mem['cCOOLRATE']['Val'] = self.CMem.CoolingRATE.get_temp(self.CMem.CTIME)

        self._append_val_to_list()
        self.ENVStep += 1

        # next_state, next_state_list = self.get_state(self.input_info)  # [s(t+1)] #
        # ----------------------------------------------------------
        return 0

    def reset(self, file_name, initial_nub=1, mal=False, mal_case=1, mal_opt=0, mal_time=5):
        # 1] CNS ?????? ????????? ??? ???????????? ?????? ???????????? ????????????
        super(ENVCNS, self).reset(initial_nub=initial_nub, mal=False, mal_case=1, mal_opt=0, mal_time=5, file_name=file_name)
        # 2] ??????????????? 'Val'??? 'List'??? ?????? ??? ENVLogging ?????????
        self._append_val_to_list()
        # 3] ENVStep ?????????
        self.ENVStep = 0
        # 5 FIX RADVAL
        self.FixedRad = random.randint(0, 20) * 5
        return 0


if __name__ == '__main__':
    # ENVCNS TEST
    env = ENVCNS(Name='Env1', IP='192.168.0.103', PORT=int(f'7101'))
    # Run
    for _ in range(1, 4):
        env.reset(file_name=f'Ep{_}')
        for __ in range(500):
            A = 0
            env.step(A)
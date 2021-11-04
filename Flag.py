class Flag():
    m1 = False # 제어 1로 이동
    move = False

    miti06_close = False
    miti06_btn = [0] * 10
    miti06_btn_first = [0] * 10

    color = [0] * 150  # 0=클릭x(회) / 1=병행(하늘) / 2=클릭(파랑) / 3=완료(어두운회색)
    color2 = [0] * 150
    color3 = [0] * 150
    color4 = [0] * 150
    color5 = [0] * 150
    color6 = [0] * 150

    # 이용가능한 수단 2_1.가
    s2_1_1 = [["터빈 구동 보조급수 펌프 1A", False],
              ["터빈 구동 보조급수 펌프 1B", False],
              ["모터 구동 보조급수 펌프 1A", False],
              ["모터 구동 보조급수 펌프 1B", False],
              ["터빈 구동 주급수 펌프 1A", False],
              ["터빈 구동 주급수 펌프 1B", False],
              ["모터 구동 주급수 펌프", False],
              ["기동용 급수 펌프", False]]

    s2_1_2 = [["복수 저장 탱크", False],
              ["탈염수 저장 탱크", False],
              ["원수 저장 탱크", False],
              ["탈기 저장 탱크", False]]

    s2_1_3 = [["주급수 배관", False],
              ["보조급수 배관", False]]

    s2_1_1_final = ""
    s2_1_2_final = ""
    s2_1_3_final = ""

    s2_1_1_backup = ""
    s2_1_2_backup = ""
    s2_1_3_backup = ""

    # 이용가능한 수단 2_1.나
    s2_2_1 = [["급수 승압 펌프 1", False],
              ["급수 승압 펌프 2", False],
              ["급수 승압 펌프 3", False]]

    s2_2_2 = [["탈기 저장 탱크", False]]

    s2_2_3 = [["주급수 배관", False]]

    s2_2_1_final = ""
    s2_2_2_final = ""
    s2_2_3_final = ""

    s2_2_1_backup = ""
    s2_2_2_backup = ""
    s2_2_3_backup = ""

    # 이용가능한 수단 2_2.
    s2_3_1 = [["주증기 대기 방출 밸브 1", False],
              ["주증기 대기 방출 밸브 2", False],
              ["주증기 대기 방출 밸브 3", False],
              ["주증기 대기 방출 밸브 4", False],
              ["터빈 우회 복수기 밸브 1", False],
              ["터빈 우회 복수기 밸브 2", False],
              ["터빈 우회 복수기 밸브 3", False],
              ["터빈 우회 복수기 밸브 4", False],
              ["터빈 우회 복수기 밸브 5", False],
              ["터빈 우회 복수기 밸브 6", False],
              ["터빈 우회 대기 밸브 1", False],
              ["터빈 우회 대기 밸브 2", False]]
    s2_3_1_final = ""
    s2_3_1_backup = ""

    s3_3 = [False] * 9
    s3_4 = [False] * 9

    # 선정된 증기발생기 4_2
    s4_2_1 = [["SG1", False],
              ["SG2", False]]
    s4_2_1_final = ""
    s4_2_1_backup = ""

    s4_2_2 = [["건전한 증기발생기", False],
              ["고장난 증기발생기", False],
              ["튜브가 파손된 증기발생기", False]]
    s4_2_2_final = ""
    s4_2_2_backup = ""

    # 완화 01 팝업 버튼 체크
    btn_popup_2_1 = False
    btn_popup_2_2 = False
    btn_popup_3_1 = False
    btn_popup_3_2 = False
    btn_popup_4_1 = False
    btn_popup_4_2 = False
    btn_popup_5_1 = False
    btn_popup_5_2 = False
    btn_popup_6_1 = False
    btn_popup_6_2 = False

    # main 버튼 체크
    btn_clicked = [0]*150
    btn_clicked_1 = [0]*150
    btn_yes = [-1]*150  # 0=yes / 1=cancel / 2=parallelism
    btn_parallelism = [0] * 150  # 병행 체크
    blue = 0  # 현재 실행 버튼 체크
    close = [0] * 150

    # main page 자동 scroll
    PAGE1 = False
    PAGE2 = False
    PAGE3 = False

    # mitigation
    m2_btn_clicked = [0] * 100
    m3_btn_clicked = [0] * 100
    m4_btn_clicked = [0] * 100
    m5_btn_clicked = [0] * 100
    m6_btn_clicked = [0] * 100

    m2_screen = [0] * 100
    m3_screen = [0] * 100
    m4_screen = [0] * 100
    m5_screen = [0] * 100
    m6_screen = [0] * 100

    # mitigation - 만족 불만족
    m2_page_num = 0
    m3_page_num = 0
    m4_page_num = 0
    m5_page_num = 0
    m6_page_num = 0

    pg2_sat = [0] * 100  # page2
    pg2_dsat = [0] * 100
    pg2_p = [0] * 100

    pg3_sat = [0] * 100  # page3
    pg3_dsat = [0] * 100
    pg3_p = [0] * 100

    pg4_sat = [0] * 100  # page4
    pg4_dsat = [0] * 100
    pg4_p = [0] * 100

    pg5_sat = [0] * 100  # page
    pg5_dsat = [0] * 100
    pg5_p = [0] * 100

    pg6_sat = [0] * 100  # page6
    pg6_dsat = [0] * 100
    pg6_p = [0] * 100

    # 제어 01 table value
    value1_1 = ""
    value1_2 = ""
    value1_3 = ""
    value1_4 = ""
    value1_5 = ""
    value1_6 = ""
    value1_7 = ""

    value2_1 = ""
    value2_2 = ""
    value2_3 = ""
    value2_4 = ""
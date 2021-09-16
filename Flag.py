class Flag():
    main_left_button_click = False
    #main
    btn_clicked = [0]*10000
    btn_clicked_1 = [0]*10000

    #완화 06 page close flag
    PAGE1 = False
    PAGE2 = False

    # mitigation
    m2_btn_clicked = [0] * 10000
    m3_btn_clicked = [0] * 10000
    m4_btn_clicked = [0] * 10000
    # mitigation - 만족 불만족
    m2_page_num = 0
    m3_page_num = 0
    m4_page_num = 0
    pg2_sat = [0] * 10000 # page2
    pg2_dsat = [0] * 10000
    pg3_sat = [0] * 10000  # page3
    pg3_dsat = [0] * 10000
    pg4_sat = [0] * 10000  # page4
    pg4_dsat = [0] * 10000

    #버튼 클릭 변수 생성
    for i in range(0, 12):
        btn_clicked[i] = False
        btn_clicked_1[i] = False
        m2_btn_clicked[i] = False
        m3_btn_clicked[i] = False
        m4_btn_clicked[i] = False
    for i in range(0, 10):
        pg2_sat[i] = False
        pg2_dsat[i] = False
        pg3_sat[i] = False
        pg3_dsat[i] = False
        pg4_sat[i] = False
        pg4_dsat[i] = False

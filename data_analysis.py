import csv
import systemStatus
import Manager

### 系統提供文字顯示
# 高度有空: 目前會回覆 / 回覆率高
# 中度有空: 有可能會回覆 / 回覆率中等
# 中度沒空: 回覆率中等 / 可能不會回覆
# 高度沒空: 回覆率低 / 目前不會回覆 / 目前不會看訊息
#
### 使用者自己表達狀態
# 高度有空: 回覆率高 / 目前會回覆 / 上線中 / 有空 / 歡迎打擾
# 中度有空: 回覆率中等 / 有可能會回覆 / 可能會看訊息
# 中度沒空: 回覆率中等 / 可能不會回覆 /
# 高度沒空: 回覆率低 / 目前不會回覆 / 目前不會看訊息 / 忙碌中 / 開會中 / 請勿打擾
#
### 情境
# Company: "男/女朋友"/朋友/同學/同事/家人/"老師/教授/上司"/學生/下屬/陌生人/自己
# Location: 家裡/"宿舍/租屋處"/"實驗室/辦公室"/教室/會議室/圖書館/健身房/室外/餐廳/交通工具裡/"商場/百貨"
# Activity: 工作/"讀書/寫作業"/"上課/開會"/吃飯/睡覺/運動/上廁所/洗澡/玩遊戲/"看電視/看影片"/用電腦/聊天/滑手機(消磨時間)/移動中(交通工具)/移動中(開車)/移動中(走路)/逛街/購物
# text_highly_unavailable location = {"家裡": 5}
#                              
location = "selectedLocation"
activity = "selectedActivity"
company = "selectedWhom"

#TODO: 需handle "其他"
def saveData(context, row, myDict):
    if row[context] not in myDict:
        myDict.setdefault(row[context], 1)
    else:
        myDict[row[context]] += 1


with open('analysis data(python).csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    # thu = systemStatus.text_highly_unavailable()
    # text_highly_unavailable_count = 0

    # tha = systemStatus.text_highly_available()
    # tma = systemStatus.text_middle_available()
    Manager manager(rows)

    for row in rows:
        # 系統文字顯示
        if row['idealShowDifferent']=='FALSE' and row['presentWay']=='text':
            # 系統呈現高度有空
            if row['statusText']=='目前會回覆' or row['statusText']=='回覆率高':
                if row['changeStatusOrNot']=='notChange':
                    tha.highly_available_count += 1
                    saveData(location, row, tha.highly_available_location)
                    saveData(activity, row, tha.highly_available_activity)
                    saveData(company, row, tha.highly_available_company)
                else: # change
                    if row['idealStatusWay']=='文字顯示':
                        # 保持文字高度有空
                        if row['idealStatusString']=='回覆率高' or row['idealStatusString']=='目前會回覆' or row['idealStatusString']=='上線中' or row['idealStatusString']=='有空' or row['idealStatusString']=='歡迎打擾':
                            tha.highly_available_count += 1
                            saveData(location, row, tha.highly_available_location)
                            saveData(activity, row, tha.highly_available_activity)
                            saveData(company, row, tha.highly_available_company)
                        # 改為文字中度有空
                        elif row['idealStatusString']=='回覆率中等' or row['idealStatusString']=='有可能會回覆' or row['idealStatusString']=='可能會看訊息':
                            tha.middle_available_count += 1
                            saveData(location, row, tha.middle_available_location)
                            saveData(activity, row, tha.middle_available_activity)
                            saveData(company, row, tha.middle_available_company)
                        # 改為文字沒空
                        elif row['idealStatusString']=='可能不會回覆' or row['idealStatusString']=='回覆率低' or row['idealStatusString']=='目前不會回覆' or row['idealStatusString']=='目前不會看訊息' or row['idealStatusString']=='忙碌中' or row['idealStatusString']=='開會中' or row['idealStatusString']=='請勿打擾':
                            tha.unavailable_count += 1
                            saveData(location, row, tha.unavailable_location)
                            saveData(activity, row, tha.unavailable_activity)
                            saveData(company, row, tha.unavailable_company)
                    elif row['idealStatusWay']=='數字顯示':
                        if row['idealStatusForm']=='回覆率' or row['idealStatusForm']=='讀訊息率':
                            #ideal_minus_system = row['idealStatusRate'] - row['status']
                            #if ideal_minus_system
                            if int(row['idealStatusRate']) >= 70:
                                tha.using_digit_available_count += 1 
                                saveData(location, row, tha.using_digit_high_responseRate)
                            elif int(row['idealStatusRate']) >=50:
                                tha.using_digit_available_count += 1
                                saveData(location, row, tha.using_digit_middleHigh_responseRate)
                            elif int(row['idealStatusRate']) >= 30:
                                tha.using_digit_unavailable_count += 1
                                saveData(location, row, tha.using_digit_middleLow_responseRate)
                            else:
                                tha.using_digit_unavailable_count += 1
                                saveData(location, row, tha.using_digit_low_responseRate)
            # 系統呈現中度有空
            elif row['statusText']=='有可能會回覆' or row['statusText']=='回覆率中等':
                if row['changeStatusOrNot']=='notChange':
                    tma.middle_available_count += 1 
                    saveData(location, row, tma.middle_available_location) 
                    saveData(activity, row, tma.middle_available_activity) 
                    saveData(company, row, tma.middle_available_company)
                else: #change
                    if row['idealStatusWay']=='文字顯示':
                        # 提高為高度有空
                        if row['idealStatusString']=='回覆率高' or row['idealStatusString']=='目前會回覆' or row['idealStatusString']=='上線中' or row['idealStatusString']=='有空' or row['idealStatusString']=='歡迎打擾':
                            tma.highly_available_count += 1
                            saveData(location, row, tma.highly_available_location)
                            saveData(activity, row, tma.highly_available_activity)
                            saveData(company, row, tma.highly_available_company)
                        # 保持中度有空
                        elif row['idealStatusString']=='回覆率中等' or row['idealStatusString']=='有可能會回覆' or row['idealStatusString']=='可能會看訊息':
                            tma.middle_available_count += 1
                            saveData(location, row, tma.middle_available_location)
                            saveData(activity, row, tma.middle_available_activity)
                            saveData(company, row, tma.middle_available_company)
                        # 改為沒空
            # 系統呈現中度沒空
            # 系統呈現高度沒空
            elif (row['statusText']=='回覆率低' or row['statusText']=='目前不會回覆' or row['statusText']=='目前不會看訊息'):
                if row['changeStatusOrNot']=='notChange':
                    text_highly_unavailable_count += 1  # 24
                    saveData(location, row, thu.highly_unavailable_location)
                else: # change
                    if row['idealStatusWay']=='文字顯示' and (row['idealStatusString']=='回覆率低' or row['idealStatusString']=='目前不會回覆' or row['idealStatusString']=='目前不會看訊息' or row['idealStatusString']=='忙碌中' or row['idealStatusString']=='開會中' or row['idealStatusString']=='請勿打擾'):
                        text_highly_unavailable_count += 1 
                        saveData(location, row, thu.highly_unavailable_location)
        elif row['idealShowDifferent']=='FALSE' and row['presentWay']=='digit':
            if row['statusForm']=='回覆率' or row['statusForm']=='讀訊息率':
                if int(row['status']) >= 70:
                    if row['changeStatusOrNot']=='notChange':




    print ("(系統文字呈現) 使用者保持高度有空: ", tha.highly_available_count)
    print ("(系統文字呈現) 使用者保持高度有空_location: ", tha.highly_available_location) 
    print ("(系統文字呈現) 使用者保持高度有空_activity: ", tha.highly_available_activity)
    print ("(系統文字呈現) 使用者保持高度有空_company: ", tha.highly_available_company)
    print ("(系統文字呈現) 使用者降低為中度有空: ", tha.middle_available_count)
    print ("(系統文字呈現) 使用者降低為中度有空_location: ", tha.middle_available_location)
    print ("(系統文字呈現) 使用者降低為中度有空_activity: ", tha.middle_available_activity)
    print ("(系統文字呈現) 使用者降低為中度有空_company: ", tha.middle_available_company)
    print ("(系統文字呈現) 使用者降低為沒空: ", tha.unavailable_count)
    print ("(系統文字呈現) 使用者降低為沒空_location: ", tha.unavailable_location)
    print ("(系統文字呈現) 使用者降低為沒空_activity: ", tha.unavailable_activity)
    print ("(系統文字呈現) 使用者降低為沒空_company: ", tha.unavailable_company)
    print ("使用者改用數字 回覆率>50%: ", tha.using_digit_available_count)
    print ("使用者改用數字 高回覆率_location: ", tha.using_digit_high_responseRate)
    # print ("使用者改用數字 中高回覆率: ", text_digit_middleHigh_responseRate)
    print ("使用者改用數字 中高回覆率_location: ", tha.using_digit_middleHigh_responseRate)
    print ("使用者改用數字 回覆率<50%: ", tha.using_digit_unavailable_count)
    print ("使用者改用數字 中低回覆率_location: ", tha.using_digit_middleLow_responseRate)
    # print ("使用者改用數字 低回覆率: ", text_digit_low_responseRate)
    print ("使用者改用數字 低回覆率_location: ", tha.using_digit_low_responseRate)

    print ("text_highly_unavailable_count: ", text_highly_unavailable_count)
    print ("text_highly_unavailable: ", thu.highly_unavailable_location)
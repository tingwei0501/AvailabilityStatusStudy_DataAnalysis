import csv
import systemStatus
from Manager import Manager

### 系統提供文字顯示
# 高度有空: 目前會回覆 / 回覆率高
# 中度有空: 有可能會回覆 / 回覆率中等
# 中度沒空: 可能不會回覆 / 回覆率低
# 高度沒空: 目前不會回覆 / 目前不會看訊息
#
### 使用者自己表達狀態
# 高度有空: 回覆率高 / 目前會回覆 / 上線中 / 有空 / 歡迎打擾
# 中度有空: 回覆率中等 / 有可能會回覆 / 可能會看訊息
# 中度沒空: 可能不會回覆 / 回覆率低
# 高度沒空: 目前不會回覆 / 目前不會看訊息 / 忙碌中 / 開會中 / 請勿打擾
#
### 情境
# Company: "男/女朋友"/朋友/同學/同事/家人/"老師/教授/上司"/學生/下屬/陌生人/自己
# Location: 家裡/"宿舍/租屋處"/"實驗室/辦公室"/教室/會議室/圖書館/健身房/室外/餐廳/交通工具裡/"商場/百貨"
# Activity: 工作/"讀書/寫作業"/"上課/開會"/吃飯/睡覺/運動/上廁所/洗澡/玩遊戲/"看電視/看影片"/用電腦/聊天/滑手機(消磨時間)/移動中(交通工具)/移動中(開車)/移動中(走路)/逛街/購物
# text_highly_unavailable location = {"家裡": 5}
#                              


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
    manager = Manager(rows)

    system_text_highly_available = []
    system_text_middle_available = []
    system_text_middle_unavailable = []
    system_text_highly_unavailable = []

    system_digit_highly_available = []
    system_digit_middle_available = []
    system_digit_middle_unavailable = []
    system_digit_highly_unavailable = []

    system_graphic_highly_available = []
    system_graphic_middle_available = []
    system_graphic_middle_unavailable = []
    system_graphic_highly_unavailable = []
    
    user_text_highly_available = []
    user_text_middle_available = []
    user_text_middle_unavailable = []
    user_text_highly_unavailable = []

    user_digit_highly_available = []
    user_digit_middle_available = []
    user_digit_middle_unavailable = []
    user_digit_highly_unavailable = []

    user_graphic_highly_available = []
    user_graphic_middle_available = []
    user_graphic_middle_unavailable = []
    user_graphic_highly_unavailable = []

    text_keep_highly_available = 0
    text_highly_available_2_middle_available = 0
    text_highly_available_2_unavailable = 0
    text_highly_available_2_digit_highly_available = 0
    text_highly_available_2_digit_middle_available = 0
    text_highly_available_2_digit_middle_unavailable = 0
    text_highly_available_2_digit_highly_unavailable = 0
    text_highly_available_2_graphic_highly_available = 0
    text_highly_available_2_graphic_middle_available = 0
    text_highly_available_2_graphic_middle_unavailable = 0
    text_highly_available_2_graphic_highly_unavailable = 0

    system = []
    systemType = ["text", "digit", "graphic"]
    systemStatus = ["HighlyAvailable", "MiddleAvailable", "MiddleUnavailable", "HighlyUnavailable"]
    
    
    # print (len(manager.getListSystemStatus("HighlyAvailable")))

    # result = list(set(manager.getListSystemType("text")) & set(manager.getListSystemStatus("HighlyAvailable")))
    # print (len(result))
    for t in systemType:
        for s in systemStatus:
            result = list(set(manager.getListSystemType(t)) & set(manager.getListSystemStatus(s)))
            # print (len(result))
            system.append(result)
    
    selfReport = []
    selfReportType = ["文字顯示", "數字顯示", "圖像顯示"]
    selfReportStatus = ["HighlyAvailable", "MiddleAvailable", "MiddleUnavailable", "HighlyUnavailable"]
    for t in selfReportType:
        for s in selfReportStatus:
            result = list(set(manager.getListSelfReportType(t)) & set(manager.getListSelfReportStatus(s)))
            selfReport.append(result)
    
    for s in system:
        for u in selfReport:
            result = list(set(s) & set(u))
            print (len(result))
    


    # for data in manager.dataTable:
    #     if data.getSystemStatus()=='text_HighlyAvailable':
    #         if data.getSelfReportStatus()=='text_HighlyAvailable':
    #             # 存情境資料??
    #             text_keep_highly_available += 1
    #         elif data.getSelfReportStatus()=='text_MiddleAvailable':
    #             text_highly_available_2_middle_available += 1
    #         elif data.getSelfReportStatus()=='text_MiddleUnavailable' or data.getSelfReportStatus()=='text_HighlyUnavailable':
    #             text_highly_available_2_unavailable += 1
    #         # 改用數字
    #         elif data.getSelfReportStatus()=='digit_HighlyAvailable':
    #             text_highly_available_2_digit_highly_available += 1
    #         elif data.getSelfReportStatus()=='digit_MiddleAvailable':
    #             text_highly_available_2_digit_middle_available += 1
    #         elif data.getSelfReportStatus()=='digit_MiddleUnavailable':
    #             text_highly_available_2_digit_middle_unavailable += 1
    #         elif data.getSelfReportStatus()=='digit_HighlyUnavailable':
    #             text_highly_available_2_digit_highly_unavailable += 1
    #         # 改用圖像
    #         elif data.getSelfReportStatus()=='graphic_HighlyAvailable':
    #             text_highly_available_2_graphic_highly_available += 1
    #         elif data.getSelfReportStatus()=='graphic_MiddleAvailable':
    #             text_highly_available_2_graphic_middle_available += 1
    #         elif data.getSelfReportStatus()=='graphic_MiddleUnavailable':
    #             text_highly_available_2_graphic_middle_unavailable += 1
    #         elif data.getSelfReportStatus()=='graphic_HighlyUnavailable':
    #             text_highly_available_2_graphic_highly_unavailable += 1
        
            # if data.getSystemStatus()=='text_HighlyAvailable':
            #     system_text_highly_available.append(data)
            # elif data.getSystemStatus()=='text_MiddleAvailable':
            #     system_text_middle_available.append(data)
            # elif data.getSystemStatus()=='text_MiddleUnavailable':
            #     system_text_middle_unavailable.append(data)
            # elif data.getSystemStatus()=='text_HighlyUnavailable':
            #     system_text_highly_unavailable.append(data)
            # # digit
            # elif data.getSystemStatus()=='digit_HighlyAvailable':
            #     system_digit_highly_available.append(data)
            # elif data.getSystemStatus()=='digit_MiddleAvailable':
            #     system_digit_middle_available.append(data)
            # elif data.getSystemStatus()=='digit_MiddleUnavailable':
            #     system_digit_middle_unavailable.append(data)
            # elif data.getSystemStatus()=='digit_HighlyUnavailable':
            #     system_digit_highly_unavailable.append(data)
            # # graphic
            # elif data.getSystemStatus()=='graphic_HighlyAvailable':
            #     system_graphic_highly_available.append(data)
            # elif data.getSystemStatus()=='graphic_MiddleAvailable':
            #     system_graphic_middle_available.append(data)
            # elif data.getSystemStatus()=='graphic_MiddleUnavailable':
            #     system_graphic_middle_unavailable.append(data)
            # elif data.getSystemStatus()=='graphic_HighlyUnavailable':
            #     system_graphic_highly_unavailable.append(data)
            # else:
            #     print ("error: SystemStatus")

            # if data.getSelfReportStatus()=='text_HighlyAvailable':
            #     user_text_highly_available.append(data)
            # elif data.getSelfReportStatus()=='text_MiddleAvailable':
            #     user_text_middle_available.append(data)
            # elif data.getSelfReportStatus()=='text_MiddleUnavailable':
            #     user_text_middle_unavailable.append(data)
            # elif data.getSelfReportStatus()=='text_HighlyUnavailable':
            #     user_text_highly_unavailable.append(data)
            # # digit
            # elif data.getSelfReportStatus()=='digit_HighlyAvailable':
            #     user_digit_highly_available.append(data)
            # elif data.getSelfReportStatus()=='digit_MiddleAvailable':
            #     user_digit_middle_available.append(data)
            # elif data.getSelfReportStatus()=='digit_MiddleUnavailable':
            #     user_digit_middle_unavailable.append(data)
            # elif data.getSelfReportStatus()=='digit_HighlyUnavailable':
            #     user_digit_highly_unavailable.append(data)
            # # graphic
            # elif data.getSelfReportStatus()=='graphic_HighlyAvailable':
            #     user_graphic_highly_available.append(data)
            # elif data.getSelfReportStatus()=='graphic_MiddleAvailable':
            #     user_graphic_middle_available.append(data)
            # elif data.getSelfReportStatus()=='graphic_MiddleUnavailable':
            #     user_graphic_middle_unavailable.append(data)
            # elif data.getSelfReportStatus()=='graphic_HighlyUnavailable':
            #     user_graphic_highly_unavailable.append(data)
            # else:
            #     print ("error: SelfReportStatus") 

        
    # s = Manager(system_text_highly_available)
    # u = Manager(user_text_highly_available)
    # text_keep_highly_available_list = s & u
    # print (text_keep_highly_available_list)
    # for i in text_keep_highly_available_list:
    #     print (i)

    # print ("text_keep_highly_available: ", text_keep_highly_available)
    # print ("text_highly_available_2_middle_available: ", text_highly_available_2_middle_available)
    # print ("text_highly_available_2_unavailable: ", text_highly_available_2_unavailable)

    # print ("text_highly_available_2_digit_highly_available: ", text_highly_available_2_digit_highly_available)
    # print ("text_highly_available_2_digit_middle_available: ", text_highly_available_2_digit_middle_available)
    # print ("text_highly_available_2_digit_middle_unavailable: ", text_highly_available_2_digit_middle_unavailable)
    # print ("text_highly_available_2_digit_highly_unavailable: ", text_highly_available_2_digit_highly_unavailable)

    # print ("text_highly_available_2_graphic_highly_available: ", text_highly_available_2_graphic_highly_available)
    # print ("text_highly_available_2_graphic_middle_available: ", text_highly_available_2_graphic_middle_available)
    # print ("text_highly_available_2_graphic_middle_unavailable: ", text_highly_available_2_graphic_middle_unavailable)
    # print ("text_highly_available_2_graphic_highly_unavailable: ", text_highly_available_2_graphic_highly_unavailable)




    # for row in rows:
    #     # 系統文字顯示
    #     if row['idealShowDifferent']=='FALSE' and row['presentWay']=='text':
    #         # 系統呈現高度有空
    #         if row['statusText']=='目前會回覆' or row['statusText']=='回覆率高':
    #             if row['changeStatusOrNot']=='notChange':
    #                 tha.highly_available_count += 1
    #                 saveData(location, row, tha.highly_available_location)
    #                 saveData(activity, row, tha.highly_available_activity)
    #                 saveData(company, row, tha.highly_available_company)
    #             else: # change
    #                 if row['idealStatusWay']=='文字顯示':
    #                     # 保持文字高度有空
    #                     if row['idealStatusString']=='回覆率高' or row['idealStatusString']=='目前會回覆' or row['idealStatusString']=='上線中' or row['idealStatusString']=='有空' or row['idealStatusString']=='歡迎打擾':
    #                         tha.highly_available_count += 1
    #                         saveData(location, row, tha.highly_available_location)
    #                         saveData(activity, row, tha.highly_available_activity)
    #                         saveData(company, row, tha.highly_available_company)
    #                     # 改為文字中度有空
    #                     elif row['idealStatusString']=='回覆率中等' or row['idealStatusString']=='有可能會回覆' or row['idealStatusString']=='可能會看訊息':
    #                         tha.middle_available_count += 1
    #                         saveData(location, row, tha.middle_available_location)
    #                         saveData(activity, row, tha.middle_available_activity)
    #                         saveData(company, row, tha.middle_available_company)
    #                     # 改為文字沒空
    #                     elif row['idealStatusString']=='可能不會回覆' or row['idealStatusString']=='回覆率低' or row['idealStatusString']=='目前不會回覆' or row['idealStatusString']=='目前不會看訊息' or row['idealStatusString']=='忙碌中' or row['idealStatusString']=='開會中' or row['idealStatusString']=='請勿打擾':
    #                         tha.unavailable_count += 1
    #                         saveData(location, row, tha.unavailable_location)
    #                         saveData(activity, row, tha.unavailable_activity)
    #                         saveData(company, row, tha.unavailable_company)
    #                 elif row['idealStatusWay']=='數字顯示':
    #                     if row['idealStatusForm']=='回覆率' or row['idealStatusForm']=='讀訊息率':
    #                         #ideal_minus_system = row['idealStatusRate'] - row['status']
    #                         #if ideal_minus_system
    #                         if int(row['idealStatusRate']) >= 70:
    #                             tha.using_digit_available_count += 1 
    #                             saveData(location, row, tha.using_digit_high_responseRate)
    #                         elif int(row['idealStatusRate']) >=50:
    #                             tha.using_digit_available_count += 1
    #                             saveData(location, row, tha.using_digit_middleHigh_responseRate)
    #                         elif int(row['idealStatusRate']) >= 30:
    #                             tha.using_digit_unavailable_count += 1
    #                             saveData(location, row, tha.using_digit_middleLow_responseRate)
    #                         else:
    #                             tha.using_digit_unavailable_count += 1
    #                             saveData(location, row, tha.using_digit_low_responseRate)
    #         # 系統呈現中度有空
    #         elif row['statusText']=='有可能會回覆' or row['statusText']=='回覆率中等':
    #             if row['changeStatusOrNot']=='notChange':
    #                 tma.middle_available_count += 1 
    #                 saveData(location, row, tma.middle_available_location) 
    #                 saveData(activity, row, tma.middle_available_activity) 
    #                 saveData(company, row, tma.middle_available_company)
    #             else: #change
    #                 if row['idealStatusWay']=='文字顯示':
    #                     # 提高為高度有空
    #                     if row['idealStatusString']=='回覆率高' or row['idealStatusString']=='目前會回覆' or row['idealStatusString']=='上線中' or row['idealStatusString']=='有空' or row['idealStatusString']=='歡迎打擾':
    #                         tma.highly_available_count += 1
    #                         saveData(location, row, tma.highly_available_location)
    #                         saveData(activity, row, tma.highly_available_activity)
    #                         saveData(company, row, tma.highly_available_company)
    #                     # 保持中度有空
    #                     elif row['idealStatusString']=='回覆率中等' or row['idealStatusString']=='有可能會回覆' or row['idealStatusString']=='可能會看訊息':
    #                         tma.middle_available_count += 1
    #                         saveData(location, row, tma.middle_available_location)
    #                         saveData(activity, row, tma.middle_available_activity)
    #                         saveData(company, row, tma.middle_available_company)
    #                     # 改為沒空
    #         # 系統呈現中度沒空
    #         # 系統呈現高度沒空
    #         elif (row['statusText']=='回覆率低' or row['statusText']=='目前不會回覆' or row['statusText']=='目前不會看訊息'):
    #             if row['changeStatusOrNot']=='notChange':
    #                 text_highly_unavailable_count += 1  # 24
    #                 saveData(location, row, thu.highly_unavailable_location)
    #             else: # change
    #                 if row['idealStatusWay']=='文字顯示' and (row['idealStatusString']=='回覆率低' or row['idealStatusString']=='目前不會回覆' or row['idealStatusString']=='目前不會看訊息' or row['idealStatusString']=='忙碌中' or row['idealStatusString']=='開會中' or row['idealStatusString']=='請勿打擾'):
    #                     text_highly_unavailable_count += 1 
    #                     saveData(location, row, thu.highly_unavailable_location)
    #     elif row['idealShowDifferent']=='FALSE' and row['presentWay']=='digit':
    #         if row['statusForm']=='回覆率' or row['statusForm']=='讀訊息率':
    #             if int(row['status']) >= 70:
    #                 if row['changeStatusOrNot']=='notChange':




    # print ("(系統文字呈現) 使用者保持高度有空: ", tha.highly_available_count)
    # print ("(系統文字呈現) 使用者保持高度有空_location: ", tha.highly_available_location) 
    # print ("(系統文字呈現) 使用者保持高度有空_activity: ", tha.highly_available_activity)
    # print ("(系統文字呈現) 使用者保持高度有空_company: ", tha.highly_available_company)
    # print ("(系統文字呈現) 使用者降低為中度有空: ", tha.middle_available_count)
    # print ("(系統文字呈現) 使用者降低為中度有空_location: ", tha.middle_available_location)
    # print ("(系統文字呈現) 使用者降低為中度有空_activity: ", tha.middle_available_activity)
    # print ("(系統文字呈現) 使用者降低為中度有空_company: ", tha.middle_available_company)
    # print ("(系統文字呈現) 使用者降低為沒空: ", tha.unavailable_count)
    # print ("(系統文字呈現) 使用者降低為沒空_location: ", tha.unavailable_location)
    # print ("(系統文字呈現) 使用者降低為沒空_activity: ", tha.unavailable_activity)
    # print ("(系統文字呈現) 使用者降低為沒空_company: ", tha.unavailable_company)
    # print ("使用者改用數字 回覆率>50%: ", tha.using_digit_available_count)
    # print ("使用者改用數字 高回覆率_location: ", tha.using_digit_high_responseRate)
    # print ("使用者改用數字 中高回覆/率: ", text_digit_middleHigh_responseRate)
    # print ("使用者改用數字 中高回覆率_location: ", tha.using_digit_middleHigh_responseRate)
    # print ("使用者改用數字 回覆率<50%: ", tha.using_digit_unavailable_count)
    # print ("使用者改用數字 中低回覆率_location: ", tha.using_digit_middleLow_responseRate)
    # # print ("使用者改用數字 低回覆率: ", text_digit_low_responseRate)
    # print ("使用者改用數字 低回覆率_location: ", tha.using_digit_low_responseRate)

    # print ("text_highly_unavailable_count: ", text_highly_unavailable_count)
    # print ("text_highly_unavailable: ", thu.highly_unavailable_location)
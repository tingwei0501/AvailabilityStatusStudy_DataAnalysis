import csv

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
# text_keep_highly_unavailable location = {"家裡": 5}
#                              activity = {"工作": 4} 

class text_highly_available: #系統給出 文字顯示 高度有空
    def __init__(self):
        self.keep_highly_available_location = {}
        self.keep_highly_available_activity = {}
        self.keep_highly_available_company = {}

        self.middle_available_location = {}
        self.middle_available_activity = {}
        self.middle_available_company = {}

        self.unavailable_location = {}
        self.unavailable_activity = {}
        self.unavailable_company = {}

        self.using_digit_high_responseRate = {} # >=70%
        self.using_digit_middleHigh_responseRate = {} # 50%<= x <70%
        self.using_digit_middleLow_responseRate = {} # 30%<= x <50%
        self.using_digit_low_responseRate = {} # <30%
        self.using_digit_low_interruptibility = {} # 干擾率<=30%
        self.using_digit_middleLow_interruptibility = {} # 干擾率 30%< x <=50%
        self.using_digit_middleHigh_interruptibility = {} # 干擾率 50%< x <=70%
        self.using_digit_high_interruptibility = {} # 干擾率 >70%

        self.using_graphic_high_responseRate = {} # >=70%
        self.using_graphic_middleHigh_responseRate = {} # 50%<= x <70%
        self.using_graphic_middleLow_responseRate = {} # 30%<= x <50%
        self.using_graphic_low_responseRate = {} # <30%
        self.using_graphic_low_interruptibility = {} # 干擾率<=30%
        self.using_graphic_middleLow_interruptibility = {} # 干擾率 30%< x <=50%
        self.using_graphic_middleHigh_interruptibility = {} # 干擾率 50%< x <=70%
        self.using_graphic_high_interruptibility = {} # 干擾率 >70%

class text_middle_available: #系統給出 文字顯示 中度有空
    def __init__(self):
        self.keep_middle_available_location = {}
        self.keep_middle_available_activity = {}
        self.keep_middle_available_company = {}

class text_middle_unavailable: #系統給出 文字顯示 中度沒空
    def __init__(self):
        self.keep_middle_unavailable_location = {}
        self.keep_middle_unavailable_activity = {}
        self.keep_middle_unavailable_company = {}

class text_highly_unavailable: #系統給出 文字顯示 高度沒空
    def __init__(self):
        self.keep_highly_unavailable_location = {}
        self.keep_highly_unavailable_activity = {}
        self.keep_highly_unavailable_company = {}

def saveLocation(row, myDict):
    if row['selectedLocation'] not in myDict:
        myDict.setdefault(row['selectedLocation'], 1)
    else:
        myDict[row['selectedLocation']] += 1

with open('analysis data(python).csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    thu = text_highly_unavailable()
    text_keep_highly_unavailable_count = 0

    tha = text_highly_available()
    text_keep_highly_available_count = 0
    text_middle_available = 0
    text_unavailable = 0
    text_digit_high_responseRate = 0
    text_digit_middleHigh_responseRate = 0

    for row in rows:
        # 系統文字顯示
        if row['idealShowDifferent']=='FALSE' and row['presentWay']=='text':
            # 系統呈現高度沒空
            if (row['statusText']=='回覆率低' or row['statusText']=='目前不會回覆' or row['statusText']=='目前不會看訊息'):
                if row['changeStatusOrNot']=='notChange':
                    text_keep_highly_unavailable_count += 1  # 24
                    saveLocation(row, thu.keep_highly_unavailable_location)
                else: # change
                    if row['idealStatusWay']=='文字顯示' and (row['idealStatusString']=='回覆率低' or row['idealStatusString']=='目前不會回覆' or row['idealStatusString']=='目前不會看訊息' or row['idealStatusString']=='忙碌中' or row['idealStatusString']=='開會中' or row['idealStatusString']=='請勿打擾'):
                        text_keep_highly_unavailable_count += 1 
                        saveLocation(row, thu.keep_highly_unavailable_location)
            # 系統呈現高度有空
            elif row['statusText']=='目前會回覆' or row['statusText']=='回覆率高':
                if row['changeStatusOrNot']=='notChange':
                    text_keep_highly_available_count += 1
                    saveLocation(row, tha.keep_highly_available_location)
                else: # change
                    if row['idealStatusWay']=='文字顯示':
                        # 保持文字高度有空
                        if row['idealStatusString']=='回覆率高' or row['idealStatusString']=='目前會回覆' or row['idealStatusString']=='上線中' or row['idealStatusString']=='有空' or row['idealStatusString']=='歡迎打擾':
                            text_keep_highly_available_count += 1
                            saveLocation(row, tha.keep_highly_available_location)
                        # 改為文字中度有空
                        elif row['idealStatusString']=='回覆率中等' or row['idealStatusString']=='有可能會回覆' or row['idealStatusString']=='可能會看訊息':
                            text_middle_available += 1
                            saveLocation(row, tha.middle_available_location)
                        # 改為文字沒空
                        elif row['idealStatusString']=='可能不會回覆' or row['idealStatusString']=='回覆率低' or row['idealStatusString']=='目前不會回覆' or row['idealStatusString']=='目前不會看訊息' or row['idealStatusString']=='忙碌中' or row['idealStatusString']=='開會中' or row['idealStatusString']=='請勿打擾':
                            text_unavailable += 1
                            saveLocation(row, tha.unavailable_location)
                    elif row['idealStatusWay']=='數字顯示':
                        if row['idealStatusForm']=='回覆率' or row['idealStatusForm']=='讀訊息率':
                            #ideal_minus_system = row['idealStatusRate'] - row['status']
                            #if ideal_minus_system
                            if int(row['idealStatusRate']) >= 70:
                                text_digit_high_responseRate += 1
                                saveLocation(row, tha.using_digit_high_responseRate)
                            elif int(row['idealStatusRate']) >=50:
                                text_digit_middleHigh_responseRate += 1
                                saveLocation(row, tha.using_digit_middleHigh_responseRate)
                                


    print ("text_keep_highly_available_count: ", text_keep_highly_available_count)
    print ("text_keep_highly_available_location: ", tha.keep_highly_available_location) 
    print ("text_middle_available: ", text_middle_available)
    print ("text_middle_available_location: ", tha.middle_available_location)
    print ("text_unavailable: ", text_unavailable)
    print ("text_unavailable_location: ", tha.unavailable_location)
    print ("text_digit_high_responseRate: ", text_digit_high_responseRate)
    print ("text_digit_middleHigh_responseRate: ", text_digit_middleHigh_responseRate)

    print ("text_keep_highly_unavailable_count: ", text_keep_highly_unavailable_count)
    print ("text_keep_highly_unavailable: ", thu.keep_highly_unavailable_location)
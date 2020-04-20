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

class text_keep_highly_unavailable:
    def __init__(self):
        self.location = {}
        self.activity = {}
        self.company = {}

with open('analysis data(python).csv', newline='') as csvfile:
    rows = csv.DictReader(csvfile)
    tkhu = text_keep_highly_unavailable()
    high_unavailable_text_count = 0
    for row in rows:
        # 保持文字顯示
        if row['idealShowDifferent']=='FALSE' and row['presentWay']=='text':
            # 保持高度沒空
            if (row['statusText']=='回覆率低' or row['statusText']=='目前不會回覆' or row['statusText']=='目前不會看訊息'):
                if row['changeStatusOrNot']=='notChange':
                    high_unavailable_text_count+=1  # 24
                    if row['selectedLocation'] not in tkhu.location:
                        tkhu.location.setdefault(row['selectedLocation'], 1)
                    else:
                        tkhu.location[row['selectedLocation']]+=1
                elif row['changeStatusOrNot']=='change' and row['idealStatusWay']=='文字顯示' and (row['idealStatusString']=='回覆率低' or row['idealStatusString']=='目前不會回覆' or row['idealStatusString']=='目前不會看訊息' or row['idealStatusString']=='忙碌中' or row['idealStatusString']=='開會中' or row['idealStatusString']=='請勿打擾'):
                    high_unavailable_text_count+=1 
                    if row['selectedLocation'] not in tkhu.location:
                        tkhu.location.setdefault(row['selectedLocation'], 1)
                    else:
                        tkhu.location[row['selectedLocation']]+=1
            # 保持高度有空
            elif (row['statusText']=='')
            
    print ("high_unavailable_text_count: ", high_unavailable_text_count)
    print ("text_keep_highly_unavailable: ", tkhu.location)
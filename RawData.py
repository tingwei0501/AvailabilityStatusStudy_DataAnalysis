class RawData:
    def __init__(self, id, row, s=""):
        self.id = id
        self.data = row
        self.systemStatus = s
        self.selfReportStatus = s
        self.action = s
    
    def getLocation(self):
        return self.data['selectedLocation']

    def setSystemStatus(self): #文字狀態或數字狀態 highAvailable/ middleAvailable/...
        if self.data['idealShowDifferent']=='FALSE' and self.data['presentWay']=='text':
            # 系統提供文字 高度有空
            if self.data['statusText']=='目前會回覆' or self.data['statusText']=='回覆率高':
                self.systemStatus = "text_HighlyAvailable"
                if self.data['changeStatusOrNot']=='notChange':
                    self.selfReportStatus = "text_HighlyAvailable"
            # 系統提供文字 中度有空
            elif self.data['statusText']=='有可能會回覆' or self.data['statusText']=='回覆率中等':
                self.systemStatus = "text_MiddleAvailable"
                if self.data['changeStatusOrNot']=='notChange':
                    self.selfReportStatus = "text_MiddleAvailable"
            # 系統提供文字 中度沒空
            elif self.data['statusText']=='回覆率中等' or self.data['statusText']=='可能不會回覆':
                self.systemStatus = "text_MiddleUnavailable"
                if self.data['changeStatusOrNot']=='notChange':
                    self.selfReportStatus = "text_MiddleUnavailable"
            # 系統提供文字 高度沒空
            elif self.data['statusText']=='回覆率低' or self.data['statusText']=='目前不會回覆' or self.data['statusText']=='目前不會看訊息':
                self.systemStatus = "text_HighlyUnavailable"
                if self.data['changeStatusOrNot']=='notChange':
                    self.selfReportStatus = "text_HighlyUnavailable"
        elif self.data['idealShowDifferent']=='FALSE' and self.data['presentWay']=='digit':
            # 系統提供數字 回覆率/讀訊息率
            if self.data['statusForm']=='回覆率' or self.data['statusForm']=='讀訊息率':
                # 高度有空
                if int(self.data['status']) >= 70:
                    self.systemStatus = "digit_HighlyAvailable"
                    if self.data['changeStatusOrNot']=='notChange':
                        self.selfReportStatus = "digit_HighlyAvailable"
                # 中度有空
                elif int(self.data['status']) >= 50:
                    self.systemStatus = "digit_MiddleAvailable"
                    if self.data['changeStatusOrNot']=='notChange':
                        self.selfReportStatus = "digit_MiddleAvailable"
                # 中度沒空
                elif int(self.data['status']) >= 30:
                    self.systemStatus = "digit_MiddleUnavailable"
                    if self.data['changeStatusOrNot']=='notChange':
                        self.selfReportStatus = "digit_MiddleUnavailable"
                # 高度沒空
                else:
                    self.systemStatus = "digit_HighlyUnavailable"
                    if self.data['changeStatusOrNot']=='notChange':
                        self.selfReportStatus = "digit_HighlyUnavailable"
            
    
    def setSelfReportStatus(self):
        if self.data['idealShowDifferent']=='FALSE' and self.data['idealStatusWay']=='文字顯示' and self.data['changeStatusOrNot']=='change':
            if self.data['idealStatusString']=='回覆率高' or self.data['idealStatusString']=='目前會回覆' or self.data['idealStatusString']=='上線中' or self.data['idealStatusString']=='有空' or self.data['idealStatusString']=='歡迎打擾':
                self.selfReportStatus = "text_HighlyAvailable"
            elif self.data['idealStatusString']=='回覆率中等' or self.data['idealStatusString']=='有可能會回覆' or self.data['idealStatusString']=='可能會看訊息':
                self.selfReportStatus = "text_MiddleAvailable"
            elif self.data['idealStatusString']=='可能不會回覆' or self.data['idealStatusString']=='回覆率低' or self.data['idealStatusString']=='目前不會回覆' or self.data['idealStatusString']=='目前不會看訊息' or self.data['idealStatusString']=='忙碌中' or self.data['idealStatusString']=='開會中' or self.data['idealStatusString']=='請勿打擾':
                self.selfReportStatus = "text_HighlyUnavailable" #用HighlyUnavailable來表示沒空




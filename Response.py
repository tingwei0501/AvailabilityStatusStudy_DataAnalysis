class Response(object):
    def __init__(self, _id, row, s=""):
        self.id = _id
        self.data = row
        self.systemStatus = s
        self.selfReportStatus = s
        self.action = s
        self.setSystemStatus()
        self.setSelfReportStatus()
    
    def getId(self):
        return self.id

    def getSystemStatus(self):
        return self.systemStatus

    def getSelfReportStatus(self):
        return self.selfReportStatus

    def getAction(self):
        return self.action

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
            elif self.data['statusText']=='可能不會回覆' or self.data['statusText']=='回覆率低':
                self.systemStatus = "text_MiddleUnavailable"
                if self.data['changeStatusOrNot']=='notChange':
                    self.selfReportStatus = "text_MiddleUnavailable"
            # 系統提供文字 高度沒空
            elif self.data['statusText']=='目前不會回覆' or self.data['statusText']=='目前不會看訊息':
                self.systemStatus = "text_HighlyUnavailable"
                if self.data['changeStatusOrNot']=='notChange':
                    self.selfReportStatus = "text_HighlyUnavailable"

        elif self.data['idealShowDifferent']=='FALSE':
            if self.data['presentWay']=='digit':
                prefix = "digit"
            else:
                prefix = "graphic"
            # 從回覆率改成用干擾率 之後判斷
            # 系統提供數字 圖像 回覆率/讀訊息率/干擾率
            # 高度有空
            if int(self.data['status']) >= 70:
                self.systemStatus = prefix + "_HighlyAvailable"
                if self.data['changeStatusOrNot']=='notChange':
                    self.selfReportStatus = prefix + "_HighlyAvailable"
            # 中度有空
            elif int(self.data['status']) >= 50:
                self.systemStatus = prefix + "_MiddleAvailable"
                if self.data['changeStatusOrNot']=='notChange':
                    self.selfReportStatus = prefix + "_MiddleAvailable"
            # 中度沒空
            elif int(self.data['status']) >= 30:
                self.systemStatus = prefix + "_MiddleUnavailable"
                if self.data['changeStatusOrNot']=='notChange':
                    self.selfReportStatus = prefix + "_MiddleUnavailable"
            # 高度沒空
            else:
                self.systemStatus = prefix + "_HighlyUnavailable"
                if self.data['changeStatusOrNot']=='notChange':
                    self.selfReportStatus = prefix + "_HighlyUnavailable"
            
    def setSelfReportStatus(self):
        if self.data['idealShowDifferent']=='FALSE' and self.data['idealStatusWay']=='文字顯示' and self.data['changeStatusOrNot']=='change':
            # 文字 自己覺得高度有空
            if self.data['idealStatusString']=='回覆率高' or self.data['idealStatusString']=='目前會回覆' or self.data['idealStatusString']=='上線中' or self.data['idealStatusString']=='有空' or self.data['idealStatusString']=='歡迎打擾':
                self.selfReportStatus = "text_HighlyAvailable"
            # 文字 自己覺得中度有空
            elif self.data['idealStatusString']=='回覆率中等' or self.data['idealStatusString']=='有可能會回覆' or self.data['idealStatusString']=='可能會看訊息':
                self.selfReportStatus = "text_MiddleAvailable"
            # 文字 自己覺得中度沒空
            elif self.data['idealStatusString']=='可能不會回覆' or self.data['idealStatusString']=='回覆率低':
                self.selfReportStatus = "text_MiddleUnavailable"
            # 文字 自己覺得高度沒空
            elif self.data['idealStatusString']=='目前不會回覆' or self.data['idealStatusString']=='目前不會看訊息' or self.data['idealStatusString']=='忙碌中' or self.data['idealStatusString']=='開會中' or self.data['idealStatusString']=='請勿打擾':
                self.selfReportStatus = "text_HighlyUnavailable"
        # 數字或圖像
        elif self.data['idealShowDifferent']=='FALSE' and self.data['changeStatusOrNot']=='change':
            if self.data['idealStatusWay']=='數字顯示':
                prefix = "digit"
            else:
                prefix = "graphic"

            # 回覆率/讀訊息率/干擾率
            # 判斷 action: increase/ decrease/ keep
            if int(self.data['idealStatusRate']) - int(self.data['status']) > 0:
                self.action = "increase"
            elif int(self.data['idealStatusRate']) - int(self.data['status']) < 0:
                self.action = "decrease"
            else:
                self.action = "keep"

            # 高度有空
            if int(self.data['idealStatusRate']) >= 70:
                self.selfReportStatus = prefix + "_HighlyAvailable"
            # 中度有空
            elif int(self.data['idealStatusRate']) >= 50:
                self.selfReportStatus = prefix + "_MiddleAvailable"
            # 中度沒空
            elif int(self.data['idealStatusRate']) >= 30:
                self.selfReportStatus = prefix + "_MiddleUnavailable"
            # 高度沒空
            else:
                self.selfReportStatus = prefix + "_HighlyUnavailable"
            

class Response:
    def __init__(self, _id, row):
        self.id = _id
        self.data = row
        self.systemStatus = ""
        self.selfReportStatus = ""
        self.action = ""
        self.setSystemStatus()
        self.setSelfReportStatus()
        self.setAction()
    
    def __hash__(self):
        return hash(self.id)
    
    def __eq__(self, other):
        return self.id == other.id

    def getId(self):
        return self.id

    def getSystemStatus(self):
        return self.systemStatus

    def getSelfReportStatus(self):
        return self.selfReportStatus

    def getAction(self):
        return self.action

    def getIdealShowDifferent(self):
        return self.data['idealShowDifferent']

    def getSystemType(self):
        return self.data['presentWay']

    def getSelfReportType(self):
        return self.data['idealStatusWay']

    def getLocation(self):
        return self.data['selectedLocation']

    def setSystemStatus(self): 
        if self.data['idealShowDifferent']=='FALSE':
            if self.data['presentWay']=='text':
                self.systemStatus =  self.textSystemStatus()
            elif self.data['presentWay']=='digit':
                self.systemStatus =  self.digit_graphicSystemStatus()
            else: # graphic 
                self.systemStatus =  self.digit_graphicSystemStatus()  

    def textSystemStatus(self):
        # 系統提供文字 高度有空
        if self.data['statusText']=='目前會回覆' or self.data['statusText']=='回覆率高':
            return "HighlyAvailable"
        # 系統提供文字 中度有空
        elif self.data['statusText']=='有可能會回覆' or self.data['statusText']=='回覆率中等':
            return "MiddleAvailable"
        # 系統提供文字 中度沒空
        elif self.data['statusText']=='可能不會回覆' or self.data['statusText']=='回覆率低':
            return "MiddleUnavailable"
        # 系統提供文字 高度沒空
        elif self.data['statusText']=='目前不會回覆' or self.data['statusText']=='目前不會看訊息':
            return "HighlyUnavailable" 
    
    def digit_graphicSystemStatus(self):
        # 從回覆率改成用干擾率 之後判斷
        # 系統提供數字 圖像 回覆率/讀訊息率/干擾率
        # 高度有空
        if int(self.data['status']) >= 70:
            return "HighlyAvailable"
        # 中度有空
        elif int(self.data['status']) >= 50:
            return "MiddleAvailable"
        # 中度沒空
        elif int(self.data['status']) >= 30:
            return "MiddleUnavailable"
        # 高度沒空
        else:
            return "HighlyUnavailable"

    def setSelfReportStatus(self):
        if self.data['idealShowDifferent']=='FALSE':
            if self.data['idealStatusWay']=='文字顯示':
                self.selfReportStatus =  self.textSelfReportStatus()
            elif self.data['idealStatusWay']=='數字顯示':
                self.selfReportStatus =  self.digit_graphicSelfReportStatus()
            else: # graphic 
                self.selfReportStatus =  self.digit_graphicSelfReportStatus()

    def textSelfReportStatus(self):
        if self.data['changeStatusOrNot']=='notChange':
            # 系統提供文字 高度有空
            if self.data['statusText']=='目前會回覆' or self.data['statusText']=='回覆率高':
                return "HighlyAvailable"
            # 系統提供文字 中度有空
            elif self.data['statusText']=='有可能會回覆' or self.data['statusText']=='回覆率中等':
                return "MiddleAvailable"
            # 系統提供文字 中度沒空
            elif self.data['statusText']=='可能不會回覆' or self.data['statusText']=='回覆率低':
                return "MiddleUnavailable"
            # 系統提供文字 高度沒空
            elif self.data['statusText']=='目前不會回覆' or self.data['statusText']=='目前不會看訊息':
                return "HighlyUnavailable"
        else:
            # 文字 自己覺得高度有空
            if self.data['idealStatusString']=='回覆率高' or self.data['idealStatusString']=='目前會回覆' or self.data['idealStatusString']=='上線中' or self.data['idealStatusString']=='有空' or self.data['idealStatusString']=='歡迎打擾':
                return "HighlyAvailable"
            # 文字 自己覺得中度有空
            elif self.data['idealStatusString']=='回覆率中等' or self.data['idealStatusString']=='有可能會回覆' or self.data['idealStatusString']=='可能會看訊息':
                return "MiddleAvailable"
            # 文字 自己覺得中度沒空
            elif self.data['idealStatusString']=='可能不會回覆' or self.data['idealStatusString']=='回覆率低':
                return "MiddleUnavailable"
            # 文字 自己覺得高度沒空
            elif self.data['idealStatusString']=='目前不會回覆' or self.data['idealStatusString']=='目前不會看訊息' or self.data['idealStatusString']=='忙碌中' or self.data['idealStatusString']=='開會中' or self.data['idealStatusString']=='請勿打擾':
                return "HighlyUnavailable"

    def digit_graphicSelfReportStatus(self):
        # 從回覆率改成用干擾率 之後判斷
        # 系統提供數字 圖像 回覆率/讀訊息率/干擾率
        # 高度有空
        if self.data['changeStatusOrNot']=='notChange':
            if int(self.data['status']) >= 70:
                return "HighlyAvailable"
            # 中度有空
            elif int(self.data['status']) >= 50:
                return "MiddleAvailable"
            # 中度沒空
            elif int(self.data['status']) >= 30:
                return "MiddleUnavailable"
            # 高度沒空
            else:
                return "HighlyUnavailable"
        else:
            # 高度有空
            if int(self.data['idealStatusRate']) >= 70:
                return "HighlyAvailable"
            # 中度有空
            elif int(self.data['idealStatusRate']) >= 50:
                return "MiddleAvailable"
            # 中度沒空
            elif int(self.data['idealStatusRate']) >= 30:
                return "MiddleUnavailable"
            # 高度沒空
            else:
                return "HighlyUnavailable"

    def setAction(self):
        # 數字或圖像
        if self.data['idealShowDifferent']=='FALSE' and self.data['changeStatusOrNot']=='change' and self.data['idealStatusWay']!='文字顯示':
            # 判斷 action: increase/ decrease/ keep
            if int(self.data['idealStatusRate']) - int(self.data['status']) > 0:
                self.action = "increase"
            elif int(self.data['idealStatusRate']) - int(self.data['status']) < 0:
                self.action = "decrease"
            else:
                self.action = "keep"


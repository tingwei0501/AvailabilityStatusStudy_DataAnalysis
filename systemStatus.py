class text_highly_available: #系統給出 文字顯示 高度有空
    def __init__(self, c=0):
        self.highly_available_count = c
        self.highly_available_location = {}
        self.highly_available_activity = {}
        self.highly_available_company = {}

        self.middle_available_count = c
        self.middle_available_location = {}
        self.middle_available_activity = {}
        self.middle_available_company = {}

        self.unavailable_count = c
        self.unavailable_location = {}
        self.unavailable_activity = {}
        self.unavailable_company = {}

        # 只先用location 回覆率/讀訊息率
        # 文字改成數字只先統計改成回覆率>50%  or <50%
        self.using_digit_available_count = c 
        self.using_digit_unavailable_count = c
        self.using_digit_high_responseRate = {} # >=70%
        self.using_digit_middleHigh_responseRate = {} # 50%<= x <70%
        self.using_digit_middleLow_responseRate = {} # 30%<= x <50%
        self.using_digit_low_responseRate = {} # <30%
        self.using_digit_low_interruptibility = {} # 干擾率<=30%
        self.using_digit_middleLow_interruptibility = {} # 干擾率 30%< x <=50%
        self.using_digit_middleHigh_interruptibility = {} # 干擾率 50%< x <=70%
        self.using_digit_high_interruptibility = {} # 干擾率 >70%
        # 圖像以下都還沒寫
        self.using_graphic_high_responseRate = {} # >=70%
        self.using_graphic_middleHigh_responseRate = {} # 50%<= x <70%
        self.using_graphic_middleLow_responseRate = {} # 30%<= x <50%
        self.using_graphic_low_responseRate = {} # <30%
        self.using_graphic_low_interruptibility = {} # 干擾率<=30%
        self.using_graphic_middleLow_interruptibility = {} # 干擾率 30%< x <=50%
        self.using_graphic_middleHigh_interruptibility = {} # 干擾率 50%< x <=70%
        self.using_graphic_high_interruptibility = {} # 干擾率 >70%

class text_middle_available: #系統給出 文字顯示 中度有空
    def __init__(self, c=0):
        self.highly_available_count = c
        self.highly_available_location = {}
        self.highly_available_activity = {}
        self.highly_available_company = {}

        self.middle_available_count = c
        self.middle_available_location = {}
        self.middle_available_activity = {}
        self.middle_available_company = {}

        self.unavailable_count = c
        self.unavailable_location = {}
        self.unavailable_activity = {}
        self.unavailable_company = {}

        # 只先用location 回覆率/讀訊息率
        # 文字改成數字只先統計改成回覆率>50%  or <50%
        self.using_digit_available_count = c
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

class text_middle_unavailable: #系統給出 文字顯示 中度沒空
    def __init__(self):
        self.middle_unavailable_location = {}
        self.middle_unavailable_activity = {}
        self.middle_unavailable_company = {}

class text_highly_unavailable: #系統給出 文字顯示 高度沒空
    def __init__(self):
        self.highly_unavailable_location = {}
        self.highly_unavailable_activity = {}
        self.highly_unavailable_company = {}

# class digit_highly_available:
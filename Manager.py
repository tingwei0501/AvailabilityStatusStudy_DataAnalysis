from Response import Response  # [avoid error]: Response is not callable

class Manager:
    dataTable = []

    def __init__(self, rows):
        for i, data in enumerate(rows):
            self.dataTable.append(Response(i, data))
    
    # @staticmethod
    # def intersection(list1, list2): 
    #     return list(set(mange.getSystemType("text")) & set(magn.getSystemStats("high")))
        # result = []
        # for element1 in list1:
        #     for element2 in list2:
        #         if element1.getId()==element2.getId():
        #             print (element1.getId())
        #             result.append(element1)

        # return result

    def getListSystemType(self, inputType):
        result = []
        for r in self.dataTable:
            if r.getIdealShowDifferent()=="FALSE" and r.getSystemType()==inputType:
                result.append(r)

        return result

    def getListSelfReportType(self, inputType):
        result = []
        for r in self.dataTable:
            if r.getIdealShowDifferent()=="FALSE" and r.getSelfReportType()==inputType:
                result.append(r)

        return result
    
    def getListSystemStatus(self, inputStatus):
        result = []
        for r in self.dataTable:
            if r.getSystemStatus()==inputStatus:
                # print (r.getId())
                result.append(r)

        return result

    def getListSelfReportStatus(self, inputStatus):
        result = []
        for r in self.dataTable:
            if r.getSelfReportStatus()==inputStatus:
                result.append(r)

        return result


    # def isSystemTextHighlyAvailable()

    
from Response import Response  # [avoid error]: Response is not callable

class Manager:
    dataTable = []

    def __init__(self, rows):
        for i, data in enumerate(rows):
            self.dataTable.append(Response(i, data))
    
    def __and__(self, other): # A[Response, Response, ...]  B[Response, Response, ...]
        result = []
        for each_response in self.dataTable:
            for each_response_other in other.dataTable:
                if each_response.getId()==each_response_other.getId():
                    print (each_response.getId())
                    result.append(each_response)

        return result

    

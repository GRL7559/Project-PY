from DB import DB

class DB_Doctor(DB):
    def __init__(self):
        pass

    def insertData(self, data):
        super().insertData("Attending_Doctor", data)
    
    def getData(self):
        result = super().getData("Attending_Doctor")
        print("Результат запроса:", result) 
        return result

from DB import DB

class DB_Doctor(DB):
    def insertData(self, data):
        super().insertData("Attending_doctor", data)
    
    def getData(self):
        super().getData("Attending_doctor")
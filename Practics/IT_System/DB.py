import sqlite3 as sql  

class DB:
    def __init__(self):
        pass

    def executeQuerry(self, query, value=None):
        try:
            with sql.connect("registry.db") as conn:
                cursor = conn.cursor()
                if value:
                    cursor.execute(query, value)
                else:
                    cursor.execute(query)
                return cursor.fetchall()
        except sql.Error as e:
            print(f"Ошибка: {e}")

    def createTable(self, table, column):
        querry = f"CREATE TABLE IF NOT EXISTS {table} ({', '.join(column)})"
        self.executeQuerry(querry)

    def insertData(self, table, data):
        columns = ", ".join(data.keys())  # name, surname, age
        placeholders = ", ".join("?" for _ in data)  # ?, ?, ?
        querry = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
        self.executeQuerry(querry, tuple(data.values()))

    def updateData(self, table, data, condition):
        updateData = ", ".join(f"{column} = ?" for column in data.keys())  # name = ?, surname = ?
        querry = f"UPDATE {table} SET {updateData} WHERE {list(condition.keys())[0]} = ?"
        self.executeQuerry(querry, tuple(list(data.values()) + list(condition.values())))

    def deleteData(self, table, condition):
        querry = f"DELETE FROM {table} WHERE {list(condition.keys())[0]} = ?"
        self.executeQuerry(querry, tuple(list(condition.values())[0]))

    def getData(self, table):
        querry = f"SELECT * FROM {table}"
        self.executeQuerry(querry)

    @staticmethod
    def getCondion(condition):
        if len(condition) > 1:
            conditions = " AND ".join(f"{column} = ?" for column in condition.keys())
        else:
            conditions = condition
        return conditions

    def getId(self, table, condition):
        conditions = self.getCondion(condition)
        querry = f"SELECT id FROM {table} WHERE {conditions}"
        self.executeQuerry(querry)

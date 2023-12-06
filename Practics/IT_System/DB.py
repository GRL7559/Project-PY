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
                conn.commit()
                return cursor.fetchall()
        except sql.Error as e:
            print(f"Ошибка: {e}")

    def insertData(self, table, data):
        columns = ", ".join(data.keys())
        values = ', '.join([f'"{value}"' if isinstance(value, str) else str(value) for value in data.values()])
        querry = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        self.executeQuerry(querry, tuple(data.values()))

    def insertMultiplyData(self, table, data):
        columns = ", ".join(data[0].keys())
        values = ', '.join(["(" + ', '.join([f'"{str(value)}"' if isinstance(value, str) else str(value) for value in data.values()]) + ")" for data in data])
        query = f"INSERT INTO {table} ({columns}) VALUES {values}"
        all_values = [value for data in data for value in data.values()]
        self.executeQuerry(query, tuple(all_values))

    def deleteData(self, table, condition):
        querry = f"DELETE FROM {table} WHERE {list(condition.keys())[0]} = ?"
        self.executeQuerry(querry, tuple(list(condition.values())[0]))


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

    def getData(self, table):
        querry = f"SELECT * FROM {table}"
        self.executeQuerry(querry)

    def createTable(self, table, column):
        querry = f"CREATE TABLE IF NOT EXISTS {table} ({', '.join(column)})"
        self.executeQuerry(querry)

    def updateData(self, table, data, condition):
        updateData = ", ".join(f"{column} = ?" for column in data.keys())  # name = ?, surname = ?
        querry = f"UPDATE {table} SET {updateData} WHERE {list(condition.keys())[0]} = ?"
        self.executeQuerry(querry, tuple(list(data.values()) + list(condition.values())))

    def createDatabase(self):
        
        columns = [
            "ID_Patient INTEGER PRIMARY KEY",
            "Surname_P VARCHAR(100) NOT NULL",
            "Name_P VARCHAR(100) NOT NULL",
            "Secondname_P VARCHAR(100)",
            "Polis_OMC VARCHAR(100) UNIQUE NOT NULL",
            "SNILS VARCHAR(100) UNIQUE NOT NULL"
        ]
        self.createTable("Patient",columns)

        data = [
            {"Surname_P":'Антонова',"Name_P":'Ксения',"Secondname_P":'Львовна',"Polis_OMC":'4441404609486520',"SNILS":'89361151025'},
            {"Surname_P":'Морозов',"Name_P":'Матвей',"Secondname_P":'Ильич',"Polis_OMC":'2040042952844640',"SNILS":'71892411616'},
            {"Surname_P":'Князев',"Name_P":'Егор',"Secondname_P":'Михайлович',"Polis_OMC":'3086023455292780',"SNILS":'68629632658'},
            {"Surname_P":'Белоусов',"Name_P":'Владимир',"Secondname_P":'Никитич',"Polis_OMC":'8268105210075770',"SNILS":'92839271853'},
            {"Surname_P":'Крылов',"Name_P":'Пётр',"Secondname_P":'Алексеевич',"Polis_OMC":'9861074245590960',"SNILS":'48029996939'},
            {"Surname_P":'Дегтярев',"Name_P":'Евгений',"Secondname_P":'Иванович',"Polis_OMC":'4732469975570230',"SNILS":'95405915425'}
        ]
        self.insertMultiplyData("Patient",data)

        #self.executeQuerry("""
        #    INSERT INTO Patient(Surname_P,Name_P,Secondname_P,Polis_OMC,SNILS)
        #   VALUES 
        #    ('Антонова','Ксения','Львовна','4441404609486520','89361151025'),
        #    ('Морозов','Матвей',' Ильич','2040042952844640','71892411616'),
        #    ('Князев','Егор','Михайлович','3086023455292780','68629632658'),
        #    ('Белоусов','Владимир','Никитич','8268105210075770','92839271853'),
        #    ('Крылов','Пётр ','Алексеевич','9861074245590960','48029996939'),
        #    ('Дегтярев','Евгений','Иванович','4732469975570230','95405915425');""")
        
        columns = [
            "ID_Doctor INTEGER PRIMARY KEY",
            "Surname_D VARCHAR(100) NOT NULL",
            "Name_D VARCHAR(100) NOT NULL",
            "Secondname_D VARCHAR(100)",
            "Phone INTEGER UNIQUE",
            "Password INTEGER"
        ]

        self.createTable("Attending_Doctor",columns)

        #self.executeQuerry("""
        #    INSERT INTO Attending_Doctor(Surname_D,Name_D,Secondname_D,Phone,Password)
        #    VALUES
        #    ('Титов','Михаил','Владимирович',78873178684,1234),
        #    ('Тихомиров','Андрей','Антонович',71651330207,5678),
        #    ('Булатова','Светлана','Владленовна',72534834347,8765);""")

        data = [
            {"Surname_D":'Титов',"Name_D":'Михаил',"Secondname_D":'Владимирович',"Phone":'78873178684',"Password":'pBf#1234'},
            {"Surname_D":'Тихомиров',"Name_D":'Андрей',"Secondname_D":'Антонович',"Phone":'71651330207',"Password":'Fvf*5678'},
            {"Surname_D":'Булатова',"Name_D":'Светлана',"Secondname_D":'Владленовна',"Phone":'72534834347',"Password":'SSm$8765'}
        ]
        self.insertMultiplyData("Attending_Doctor",data)

        #self.executeQuerry(""" 
        #    CREATE TABLE IF NOT EXISTS Disease(
        #        ID_Disease INTEGER PRIMARY KEY AUTOINCREMENT,
        #        Disease VARCHAR(100) NOT NULL
        #    );""")
        
        columns = [
            "ID_Disease INTEGER PRIMARY KEY",
            "Disease VARCHAR(100) NOT NULL"
        ]
        self.createTable("Disease",columns)

        #self.executeQuerry("""
        #    INSERT INTO Disease(Disease)
        #    VALUES
        #    ('Стенокардия'),
        #    ('Предсердная экстрасистолия'),
        #    ('Легочная гипертензия'),
        #    ('Фибрилляция'
        #    );""")
        
        data = [
            {"Disease":'Стенокардия'},
            {"Disease":'Предсердная экстрасистолия'},
            {"Disease":'Легочная гипертензия'},
            {"Disease":'Фибрилляция'}
        ]
        self.insertMultiplyData("Disease",data)

        #self.executeQuerry("""
        #    CREATE TABLE IF NOT EXISTS Severity(
        #        ID_Severity INTEGER PRIMARY KEY AUTOINCREMENT,
        #        Severity VARCHAR(100) NOT NULL
        #    );""")
        
        columns = [
            "ID_Severity INTEGER PRIMARY KEY",
            "Severity VARCHAR(100) NOT NULL"
        ]
        self.createTable("Severity",columns)

        #self.executeQuerry("""
        #    INSERT INTO Severity(Severity)
        #    VALUES
        #    ('Легкая'),
        #    ('Средней тяжести'),
        #    ('Тяжелая'
        #    );""")

        data = [
            {"Severity":'Легкая'},
            {"Severity":'Средняя'},
            {"Severity":'Тяжелая'}
        ]
        self.insertMultiplyData("Severity",data)

        #self.executeQuerry("""
        #    CREATE TABLE IF NOT EXISTS Medical_card(
        #        ID_Medical_card INTEGER PRIMARY KEY AUTOINCREMENT,
        #        Patient_ID INTEGER,
        #        Doctor_ID INTEGER,
        #        Disease_ID INTEGER,
        #        Severity_ID INTEGER,
        #        Сost_services INTEGER,
        #        CONSTRAINT FK_Patient FOREIGN KEY(Patient_ID) REFERENCES Patient(ID_Patient),
        #        CONSTRAINT FK_Doctor FOREIGN KEY(Doctor_ID) REFERENCES Attending_Doctor(ID_Doctor),
        #        CONSTRAINT FK_Disease FOREIGN KEY(Disease_ID) REFERENCES Disease(ID_Disease),
        #        CONSTRAINT FK_Severity FOREIGN KEY(Severity_ID) REFERENCES Severity(ID_Severity)
        #    );""")
        #self.executeQuerry("""
        #    INSERT INTO Medical_card(Patient_ID,Doctor_ID,Disease_ID,Severity_ID,Сost_services)
        #    VALUES
        #    (1,1,1,1,7800),
        #    (2,2,2,3,30850),
        #    (3,3,3,2,9030),
        #    (4,1,1,1,2500),
        #    (5,3,4,2,3000),
        #    (6,1,3,2,0);    
        #    """)
        
        columns =[
            "ID_Medical_card INTEGER PRIMARY KEY",
                "Patient_ID INTEGER, FOREIGN KEY(Patient_ID) REFERENCES Patient(ID_Patient)",
                "Doctor_ID INTEGER, FOREIGN KEY(Doctor_ID) REFERENCES Attending_Doctor(ID_Doctor)",
                "Disease_ID INTEGER, FOREIGN KEY(Disease_ID) REFERENCES Disease(ID_Disease)",
                "Severity_ID INTEGER, FK_Disease FOREIGN KEY(Disease_ID) REFERENCES Disease(ID_Disease)",
                "Сost_services INTEGER, FK_Severity FOREIGN KEY(Severity_ID) REFERENCES Severity(ID_Severity)"
        ]
        self.createTable("Medical_card",columns)

        data = [
            {"Patient_ID":1,"Doctor_ID":1,"Disease_ID":1,"Severity_ID":1,"Сost_services":7800},
            {"Patient_ID":2,"Doctor_ID":2,"Disease_ID":2,"Severity_ID":3,"Сost_services":30850},
            {"Patient_ID":3,"Doctor_ID":3,"Disease_ID":3,"Severity_ID":2,"Сost_services":9030},
            {"Patient_ID":4,"Doctor_ID":1,"Disease_ID":1,"Severity_ID":1,"Сost_services":2500},
            {"Patient_ID":5,"Doctor_ID":3,"Disease_ID":4,"Severity_ID":2,"Сost_services":3000},
            {"Patient_ID":6,"Doctor_ID":1,"Disease_ID":3,"Severity_ID":2,"Сost_services":0}
        ]
        self.insertMultiplyData("Medical_card",data)




    

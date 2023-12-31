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
        finally: 
            conn.close()

    def insertData(self, table, data):
        columns = ", ".join(data.keys())
        values = ', '.join(['?' for _ in data.values()])
        query = f"INSERT INTO {table} ({columns}) VALUES ({values})"
        self.executeQuerry(query, tuple(data.values()))

    def getData(self, table):
        querry = f"SELECT * FROM {table}"
        return self.executeQuerry(querry)

    def createDatabase(self):
        self.executeQuerry("""
            CREATE TABLE IF NOT EXISTS Patient( 
                ID_Patient INTEGER PRIMARY KEY AUTOINCREMENT,
                Surname_P VARCHAR(100) NOT NULL,
                Name_P VARCHAR(100) NOT NULL,
                Secondname_P VARCHAR(100),
                Polis_OMC VARCHAR(100) UNIQUE NOT NULL,
                SNILS VARCHAR(100) UNIQUE NOT NULL
            );""")
        self.executeQuerry("""
            INSERT INTO Patient(Surname_P,Name_P,Secondname_P,Polis_OMC,SNILS)
            VALUES 
            ('Антонова','Ксения','Львовна','4441404609486520','89361151025'),
            ('Морозов','Матвей',' Ильич','2040042952844640','71892411616'),
            ('Князев','Егор','Михайлович','3086023455292780','68629632658'),
            ('Белоусов','Владимир','Никитич','8268105210075770','92839271853'),
            ('Крылов','Пётр ','Алексеевич','9861074245590960','48029996939'),
            ('Дегтярев','Евгений','Иванович','4732469975570230','95405915425');""")
        self.executeQuerry("""                              
            CREATE TABLE IF NOT EXISTS Attending_Doctor(
                ID_Doctor INTEGER PRIMARY KEY AUTOINCREMENT,
                Surname_D VARCHAR(100) NOT NULL,
                Name_D VARCHAR(100) NOT NULL,
                Secondname_D VARCHAR(100),
                Phone INTEGER UNIQUE,
                Password VARCHAR(100)           
            );""")
        self.executeQuerry("""
            INSERT INTO Attending_Doctor(Surname_D,Name_D,Secondname_D,Phone,Password)
            VALUES
            ('Титов','Михаил','Владимирович',78873178684,'Gf*1234'),
            ('Тихомиров','Андрей','Антонович',71651330207,'5678'),
            ('Булатова','Светлана','Владленовна',72534834347,'8765');""")
        self.executeQuerry(""" 
            CREATE TABLE IF NOT EXISTS Disease(
                ID_Disease INTEGER PRIMARY KEY AUTOINCREMENT,
                Disease VARCHAR(100) NOT NULL
            );""")
        self.executeQuerry("""
            INSERT INTO Disease(Disease)
            VALUES
            ('Стенокардия'),
            ('Предсердная экстрасистолия'),
            ('Легочная гипертензия'),
            ('Фибрилляция'
            );""")
        self.executeQuerry("""
            CREATE TABLE IF NOT EXISTS Severity(
                ID_Severity INTEGER PRIMARY KEY AUTOINCREMENT,
                Severity VARCHAR(100) NOT NULL
            );""")
        self.executeQuerry("""
            INSERT INTO Severity(Severity)
            VALUES
            ('Легкая'),
            ('Средней тяжести'),
            ('Тяжелая'
            );""")
        self.executeQuerry("""
            CREATE TABLE IF NOT EXISTS Medical_card(
                ID_Medical_card INTEGER PRIMARY KEY AUTOINCREMENT,
                Patient_ID INTEGER,
                Doctor_ID INTEGER,
                Disease_ID INTEGER,
                Severity_ID INTEGER,
                Сost_services INTEGER,
                CONSTRAINT FK_Patient FOREIGN KEY(Patient_ID)REFERENCES Patient(ID_Patient),
                CONSTRAINT FK_Doctor FOREIGN KEY(Doctor_ID)REFERENCES Attending_Doctor(ID_Doctor),
                CONSTRAINT FK_Disease FOREIGN KEY(Disease_ID)REFERENCES Disease(ID_Disease),
                CONSTRAINT FK_Severity FOREIGN KEY(Severity_ID)REFERENCES Severity(ID_Severity)
            );""")
        self.executeQuerry("""
            INSERT INTO Medical_card(Patient_ID,Doctor_ID,Disease_ID,Severity_ID,Сost_services)
            VALUES
            (1,1,1,1,7800),
            (2,2,2,3,30850),
            (3,3,3,2,9030),
            (4,1,1,1,2500),
            (5,3,4,2,3000),
            (6,1,3,2,0);    
            """)
from DB import DB

class DB_Patient(DB):
    def __init__(self,id):
        self.id = id
        #self.createDatabase()
        pass
       
    def show_patient(self):
        select = self.executeQuerry(f"""SELECT Patient_ID FROM Medical_card WHERE Doctor_ID = {self.id}""")
        patients = self.executeQuerry(f"""SELECT * FROM Patient""")
        k=0
        for patient in patients:
            for item in select:
                if patient[0] == item:
                    k+=1
                    print(f"{k} {patient[1]} {patient[2]} {patient[3]}")
        return k-1

    def create_patient(self,insert):
        self.executeQuerry(f"""
            INSERT INTO Patient(Surname_P,Name_P,Secondname_P,Polis_OMC,SNILS)
            VALUES
            ('{insert[0]}','{insert[1]}','{insert[2]}','{insert[3]}','{insert[4]}');
        """)
        self.executeQuerry(f"""
            INSERT INTO Disease(Disease)
            VALUES
            ('{insert[5]}');
        """)
        id_d = self.executeQuerry(f"""SELECT ID_Disease FROM Disease WHERE Disease = {insert[5]}""")
        id_p = self.executeQuerry(f"""SELECT ID_Patient FROM Patient WHERE SNILS = {insert[4]}""")
        self.executeQuerry(f"""
            INSERT INTO Medical_card(Patient_ID,Doctor_ID,Disease_ID,Severity_ID,Сost_services)
            VALUES
            ({id_p},{id_d},{insert[6]},{insert[7]},{insert[8]}),    
        """)


    def delete_patient(self, num_p):
        select = self.executeQuerry(f"""SELECT Patient_ID FROM Medical_card WHERE Doctor_ID = {self.id}""")
        self.executeQuerry(f"""DELETE * FROM Patient WHERE ID_Patient = {select[num_p]};""")
        self.executeQuerry(f"""DELETE * FROM Medical_card WHERE Patient_ID = {select[num_p]};""")

    def medcard_check(self,num_p):
        select = self.executeQuerry(f"""SELECT Patient_ID FROM Medical_card WHERE Doctor_ID = {self.id}""")
        data = self.executeQuerry(f"""SELECT * FROM Medical_card WHERE Patient_ID = {select[num_p]};""")
        patient = self.executeQuerry(f"""SELECT * FROM Patient WHERE ID_Patient = {data[1]}""")
        disease = self.executeQuerry(f"""SELECT * FROM Disease WHERE ID_Disease = {data[3]}""")
        severity = self.executeQuerry(f"""SELECT * FROM Severity WHERE ID_Severity = {data[4]}""")
        medical_card = patient + disease + severity
        medical_card.append(data[5])
        return medical_card


    def update_cost(self,num_p,cost):
        select = self.executeQuerry(f"""SELECT Patient_ID FROM Medical_card WHERE Doctor_ID = {self.id}""")
        self.executeQuerry(f"""UPDATE Medical_card SET Cost_service = '{cost}' WHERE Patient_ID = {select[num_p]};""")

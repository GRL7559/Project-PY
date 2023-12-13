from DB import DB

class DB_Patient(DB):
    def __init__(self,id):
        self.id = id
        self.createDatabase()
        #pass
       
    def show_patient(self):
        select = self.executeQuerry(f"""SELECT Patient_ID FROM Medical_card WHERE Doctor_ID = {self.id}""")
        patients = self.executeQuerry(f"""SELECT * FROM Patient""")
        k=0
        for patient in patients:
            for item in select:
                if patient[0] == item[0]:
                    k+=1
                    print(f"{k}.{patient[1]} {patient[2]} {patient[3]}")
        return k

    def create_patient(self,insert):
        self.executeQuerry(f"""
            INSERT INTO Patient(Surname_P,Name_P,Secondname_P,Polis_OMC,SNILS)
            VALUES
            ('{insert[0]}','{insert[1]}','{insert[2]}','{insert[3]}','{insert[4]}');
        """)
        self.executeQuerry(f"""
            INSERT INTO Disease(Disease)
            VALUES
            ('{insert[6]}');
        """)
        id_d = self.executeQuerry(f"""SELECT ID_Disease FROM Disease WHERE Disease = '{insert[6]}'""")
        id_p = self.executeQuerry(f"""SELECT ID_Patient FROM Patient WHERE SNILS = '{insert[4]}'""")
        self.executeQuerry(f"""
            INSERT INTO Medical_card(Patient_ID,Doctor_ID,Disease_ID,Severity_ID,Сost_services)
            VALUES
            ('{id_p[0][0]}','{insert[5]}','{id_d[0][0]}','{insert[7]}','{insert[8]}');    
        """)


    def delete_patient(self, num_p):
        select = self.executeQuerry(f"""SELECT Patient_ID FROM Medical_card WHERE Doctor_ID = {self.id}""")
        self.executeQuerry(f"""DELETE FROM Patient WHERE ID_Patient = {select[num_p-1][0]};""")
        self.executeQuerry(f"""DELETE FROM Medical_card WHERE Patient_ID = {select[num_p-1][0]};""")

    def medcard_check(self,num_p):
        select = self.executeQuerry(f"""SELECT Patient_ID FROM Medical_card WHERE Doctor_ID = {self.id}""")
        data = self.executeQuerry(f"""SELECT * FROM Medical_card WHERE Patient_ID = {select[num_p-1][0]};""")
        data = data[0]
        patient = self.executeQuerry(f"""SELECT * FROM Patient WHERE ID_Patient = {data[1]}""")
        disease = self.executeQuerry(f"""SELECT * FROM Disease WHERE ID_Disease = {data[3]}""")
        severity = self.executeQuerry(f"""SELECT * FROM Severity WHERE ID_Severity = {data[4]}""")
        medical_card = patient
        medical_card.append(disease[0][1])
        medical_card.append(severity[0][1])
        medical_card.append(data[5])
        medical_card = list(medical_card[0][0:]) + medical_card[1:]
        return medical_card


    def update_cost(self,num_p,cost):
        select = self.executeQuerry(f"""SELECT Patient_ID FROM Medical_card WHERE Doctor_ID = {self.id}""")
        self.executeQuerry(f"""UPDATE Medical_card SET Сost_services = '{cost}' WHERE Patient_ID = {select[num_p-1][0]};""")

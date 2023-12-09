from DB import DB

class DB_Patient(DB):
    def __init__(self):
        self.createDatabase()
        #pass

    def getData(self):
        result = super().getData("Patient")
        print("Результат запроса:", result)  
        return result
       
    def show_patient(self, id_doctor):
        id_p = self.executeQuerry(f"""SELECT Patient_ID FROM Medicial_card WHERE Doctor_ID = {id_doctor}""")
        patients = self.executeQuerry(f"""SELECT * FROM Patient WHERE ID_Patient = {id_p}""")
        k=1
        for patient in patients:
            print(f"{k} {patient.Surname_P} {patient.Name_P} {patient.Secondname_P}")
            k+=1
        return patients
    
    def insertData(self, data):
        super().insertData('Patient', data)

    def delete_patient(self ,patients, num_p):
        id_p=patients[num_p].ID_Patient
        self.executeQuerry(f"""DELETE FROM Patient WHERE ID_Patient={id_p};""")

    def medcard_check(self,patients,num_p):
        id_p=patients[num_p].ID_Patient
        self.executeQuerry(f"""SELECT * FROM Medical_card WHERE Patient_ID={id_p};""")

    def update_cost(self,patients,num_p,cost):
        id_p=patients[num_p].ID_Patient
        self.executeQuerry(f"""UPDATE Medical_card SET Cost_service = '{cost}' WHERE Patient_ID={id_p};""")
        
    
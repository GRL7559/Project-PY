from DB import DB

class DB_Patient(DB):
    def show_patient(self, id_doctor):
        patients = self.executeQuerry(f"""SELECT Patient_ID FROM Medicial_card WHERE Doctor_ID = {id_doctor}""")
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

    def update_diagnos(self,patients,num_p,diagnos):
        id_p=patients[num_p].ID_Patient
        self.executeQuerry(f"""UPDATE Disease SET Disease = {diagnos} WHERE ID_Disease={id_p};""")
        
    
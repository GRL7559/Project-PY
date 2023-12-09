from DB import DB

class DB_Patient(DB):
    def __init__(self):
        #self.createDatabase()
        pass
       
    def show_patient(self):
        patients = self.executeQuerry(f"""SELECT * FROM Patient""")
        for patient in patients:
            print(f"{patient['ID_Patient']} {patient['Surname_P']} {patient['Name_P']} {patient['Secondname_P']}")

    def delete_patient(self, num_p):
        self.executeQuerry(f"""DELETE * FROM Patient WHERE ID_Patient = {num_p};""")
        self.executeQuerry(f"""DELETE * FROM Medical_card WHERE Patient_ID = {num_p};""")

    def medcard_check(self,num_p):
        self.executeQuerry(f"""SELECT * FROM Medical_card WHERE Patient_ID = {num_p};""")

    def update_cost(self,num_p,cost):
        self.executeQuerry(f"""UPDATE Medical_card SET Cost_service = '{cost}' WHERE Patient_ID = {num_p};""")
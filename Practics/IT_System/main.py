from Auth import Auth 
from DB_Patient import DB_Patient 

class main:
    registry = DB_Patient()
    auth = Auth()
    print("Здравствуйте, для Входа нажмите 1 , для регестрации нажмите 2")
    enter = int(input())
    match enter:
        case 1: id=auth.log_in()
        case 2: id=auth.sign_up()
        case _: print("Введено неккоректное значение")
    while(True):
        print("Что вы хотите сделать?\n1.Добавить пациента\n2.Выписать пациента\n3.Изменить диагноз\n4.Посмотреть данные медкарты\n5.Заврешить работу с программой")
        choise=int(input())
        match (choise):
            case 1:
                data = {
                "Surname_P": "",
                "Name_P": "",
                "Secondname_P": "",
                "POLIS_OMS": 0,
                "SNILS": 0}
                print("Введите фамилию",end="")
                data["Surname_P"]=input()
                print("Введите имя",end="")
                data["Name_P"]=input()
                print("Введите отчество",end="")
                data["Secondname_P"]=input()
                print("Введите ПОЛИС ОМС",end="")
                data["POLIS_OMS"]=int(input())
                print("Введите СНИЛС",end="")
                data["SNILS"]=int(input())
                registry.insertData(data)
            case 2:
                patients=registry.show_patient(id)
                print("Введите номер пациента,которого нужно удалить")
                num_p = int(input())
                registry.delete_patient(patients,num_p)
            case 3:
                patients=registry.show_patient(id)
                print("Введите номер пациента,диагноз которого нужно иземенить") 
                num_p = int(input())
                print("Введите новый диагноз пациента") 
                diagnos = input()
                registry.update_diagnos(patients,num_p,diagnos)
            case 4:
                patients=registry.show_patient(id)
                print("Введите номер пациента,медкарту которого вы хотите просмотреть")
                num_p = int(input())  
                registry.medcard_check(patients,num_p)
            case 5:
                exit()
            case _:
                print("Введено неккоректное значение")
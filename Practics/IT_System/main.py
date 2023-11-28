import Auth 
import My_DB

class main:

    id = Auth
    while(True):
        print("Что вы хотите сделать?\n1.Добавить пациента\n2.Выписать пациента\n3.Изменить диагноз\n4.Посмотреть данные медкарты\n5.Заврешить работу с программой")
        choise=int(input())
        match (choise):
            case 1:
                insert = [{"Surname_P":""},{"Name_P":""},{"Secondname_P":""},{"POLIS_OMS":0},{"SNILS":0}]
                print("Введите фамилию",end="")
                insert.Surname_P=input()
                print("Введите имя",end="")
                insert.Name_P=input()
                print("Введите отчество",end="")
                insert.Secondname_P=input()
                print("Введите ПОЛИС ОМС",end="")
                insert.POLIS_OMS=int(input())
                print("Введите СНИЛС",end="")
                insert.SNILS=int(input())
                My_DB.insert_patient(insert)
            case 2:
                patients=My_DB.show_patient(id)
                print("Введите номер пациента,которого нужно удалить")
                num_p = int(input())
                My_DB.delete_patient(patients,num_p)
            case 3:
                patients=My_DB.show_patient(id)
                print("Введите номер пациента,диагноз которого нужно иземенить") 
                num_p = int(input())
                print("Введите новый диагноз пациента") 
                diagnos = input()
                My_DB.update_diagnos(patients,num_p,diagnos)
            case 4:
                patients=My_DB.show_patient(id)
                print("Введите номер пациента,медкарту которого вы хотите просмотреть")
                num_p = int(input())  
                My_DB.medcard_check(patients,num_p)
            case 5:
                exit()
            case _:
                print("Введено неккоректное значение")
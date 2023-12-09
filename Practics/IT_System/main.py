from Auth import Auth 
from DB_Patient import DB_Patient 

class main:
    registry = DB_Patient()
    auth = Auth()
    while(True):
        print("Здравствуйте, для Входа нажмите 1 , для регестрации нажмите 2")
        enter=input()
        match enter:
            case "1": 
                sid=auth.log_in()
                break
            case "2": 
                id=auth.sign_up()
                break
            case _: print("Введено неккоректное значение")
    while(True):
        print("Что вы хотите сделать?\n1.Выписать пациента\n2.Изменить счёт\n3.Посмотреть данные медкарты\n4.Заврешить работу с программой")
        choise=input()
        match (choise):
            case "1":
                registry.show_patient()
                print("Введите номер пациента,которого нужно выписать")
                num_p = int(input())
                registry.delete_patient(num_p)
            case "2":
                registry.show_patient()
                print("Введите номер пациента,счёт которого нужно иземенить") 
                num_p = int(input())
                print("Введите сумму") 
                cost = input()
                registry.update_cost(num_p,cost)
            case "3":
                registry.show_patient(id)
                print("Введите номер пациента,медкарту которого вы хотите просмотреть")
                num_p = int(input())  
                registry.medcard_check(num_p)
            case "4":
                exit(0)
            case _:
                print("Введено неккоректное значение")
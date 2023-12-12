from Auth import Auth 
from DB_Patient import DB_Patient 

class main:
    registry = DB_Patient(-1)
    auth = Auth()
    while(True):
        print("Здравствуйте, для Входа нажмите 1 , для регестрации нажмите 2")
        enter=input()
        match enter:
            case "1": 
                registry.id=auth.log_in()
                break
            case "2": 
                registry.id=auth.sign_up()
                break
            case _: print("Введено неккоректное значение")
    while(True):
        print("Что вы хотите сделать?\n1.Добавить пациента\n2.Выписать пациента\n3.Изменить счёт\n4.Посмотреть данные медкарты\n5.Заврешить работу с программой")
        choise=input()
        match (choise):
            case "1":
                insert = ["","","",0,0,id,"",0,0]
                patients = registry.getData("Patient")
                severities = registry.getData("Severity")
                while(True):
                    print("Введите фамилию: ", end="")
                    insert[0] = input()
                    if insert[0] == "":
                        print("Фамилия не может быть пустой")
                    else:break
                while(True):
                    print("Введите имя: ", end="")
                    insert[1] = input()
                    if insert[1] == "":
                        print("Имя не может быть пустым")
                    else:break
                print("Введите отчество: ", end="")
                insert[2] = input()
                while True:
                    try:
                        print("Введите ПОЛИС ОМС: ", end="")
                        insert[3] = int(input()) 
                        unique = True
                        for patient in patients:
                            if insert[3] == patient[3]:
                                unique = False
                        if unique:
                            break
                    except(Exception):
                        print("Введено некорректное значение")
                while True:
                    try:
                        print("Введите СНИЛС: ", end="")
                        insert[4] = int(input()) 
                        for patient in patients:
                            if insert[4] == patient[4]:
                                unique = False
                        if unique:
                            break
                    except(Exception):
                        print("Введено некорректное значение")
                print("Введите диагноз: ", end="")
                insert[6] = input()
                print(f"Введите номер степени тяжести\n1.{severities[0][1]}\n2.{severities[1][1]}\n3.{severities[2][1]}")
                while True:
                    try:
                        insert[7] = int(input()) 
                        if insert[7] > 0 and insert[7] < 4:
                            break
                        else:
                            print("Введите номер из приведенного списка")
                    except(Exception):
                        print("Введено некорректное значение")
                while True:
                    try:
                        print("Введите текущую задолженность по счёту: ", end="")
                        insert[8] = int(input())
                        if insert[8]<0:
                            print("Счёт не может быть отрицательным")
                        else:
                            break
                    except(Exception):
                        print("Введено некорректное значение")
            case "2":
                k = registry.show_patient()
                print("Введите номер пациента,которого нужно выписать")
                num_p = int(input())
                registry.delete_patient(num_p)
            case "3":
                k = registry.show_patient()
                print("Введите номер пациента,счёт которого нужно иземенить") 
                while True:
                    try:
                        num_p = int(input()) 
                        if num_p>k and 0<num_p:
                            break
                        else:
                            print("Введите номер, присвоенный пациенту")
                    except(Exception):
                        print("Введено некорректное значение")
                print("Введите сумму") 
                while True:
                    try:
                        cost = int(input()) 
                        break
                    except(Exception):
                        print("Введено некорректное значение")
                registry.update_cost(num_p,cost)
            case "4":
                k = registry.show_patient()
                print("Введите номер пациента,медкарту которого вы хотите просмотреть")
                while True:
                    try:
                        num_p = int(input()) 
                        if num_p>k and 0<num_p:
                            break
                        else:
                            print("Введите номер, присвоенный пациенту")
                    except(Exception):
                        print("Введено некорректное значение")
                data = registry.medcard_check(num_p)
                print(f"ID: {data[0]}\nФамилия: {data[1]}\nИмя: {data[2]}\nОтчество: {data[3]}\nПолис ОМС: {data[4]}\nСНИЛС: {data[5]}\nЗаболевание: {data[6]}\nСтепень тяжести: {data[7]}\nСчёт: {data[8]}")
            case "5":
                exit(0)
            case _:
                print("Введено неккоректное значение")
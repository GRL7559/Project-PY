import sqlite3 as sql  

class Authentication:
    @staticmethod
    def log_in():
        while True:
            code = My_DB.getData("Attending_doctor")
            print("Введите логин(телефон)", end="")
            login = int(input)
            if len.login != 11:
                print("Введено некорректное значение")
                continue
            else:
                confirm_login = False
                for i in range(1, len.code-1):
                    if code[i] == login:
                        id_doctor = i
                        confirm_login = True
                if confirm_login:
                    break
                else:
                    print("Пользователь не найден")
        while True:
            print("Введите пароль", end="")
            password = input()
            true_password = code[id_doctor].password
            if password == true_password:
                print("Вход успешно выполнен")
                return id_doctor
            else:
                print("Неверный пароль")

    @staticmethod
    def sign_up():
        insert = {"Surname_D": "", "Name_D": "", "Secondname_D": "", "Phone": 0, "Password": 0}
        print("Введите фамилию", end="")
        insert["Surname_D"] = input()
        print("Введите имя", end="")
        insert["Name_D"] = input()
        print("Введите отчество", end="")
        insert["Secondname_D"] = input()
        print("Введите номер телефона", end="")
        insert["Phone"] = int(input())
        print("Введите пароль", end="")
        insert["Password"] = input()
        My_DB.insertData("Attending_doctor", insert)
        print("Пользователь успешно добавлен")
        id_doctor = My_DB.getId()
        return id_doctor

class Main(Authentication):  # Добавляем наследование от класса Auth, чтобы использовать его методы
    while True:
        print("Что вы хотите сделать?n1.Добавить пациентаn2.Выписать пациентаn3.Изменить диагнозn4.Посмотреть данные медкартыn5.Завершить работу с программой")
        choise = int(input())
        match choise:
            case 1:
                new_patient = []
                print("Введите фамилию:")
                new_patient[0] = input()
                print("Введите имя:")
                new_patient[1] = input()
                print("Введите отчество:")
                new_patient[2] = input()
                print("Введите диагноз:")
                new_patient[3] = input()
                print("Введите :")
                new_patient[4] = input()
                print("Введите :")
                new_patient[5] = input()
                My_DB.insertData("Patient", new_patient)
            case 2:
                My_DB.show_patient()
                print("Введите номер пациента, которого нужно удалить")
                delete = int(input())
                My_DB.deleteData("Patient", delete)
            case 3:
                My_DB.show_patient()
                print("Введите номер пациента, диагноз которого нужно изменить") 
                diag = int(input())
            case 4:
                My_DB.show_patient()
                print("Введите номер пациента, медкарту которого вы хотите просмотреть")
                medcard = int(input())  
            case 5:
                exit()
            case _:
                print("Введено некорректное значение")
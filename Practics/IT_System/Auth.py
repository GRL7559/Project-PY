from DB_Doctor import DB_Doctor 
import re
class Auth:
	def __init__(self):
		pass

	def log_in(self):
		doctor = DB_Doctor()
		code = doctor.getData()
		while(True):
			print("Введите логин(телефон): ",end="")
			try:
				login = int(input())
			except(Exception):
				print("Введено некорректное значение")
				continue
			confirm_login=False
			for i in range(1,len(code)-1):
				if code[i]["Phone"]==login:
					id_doctor = i
					confirm_login = True
			if confirm_login:break
			else:
				print("Пользователь не найден")
		while(True):
			print("Введите пароль: ",end="")
			password=input()
			true_password=code[id_doctor]["Password"]
			if password==true_password:
				print("Вход успешно выполнен")
				return id_doctor
			else:
				print("Неверный пароль"),

	def sign_up(self):
		insert = {"Surname_D":"","Name_D":"","Secondname_D":"","Phone":0,"Password":0}
		print("Введите фамилию: ", end="")
		insert["Surname_D"] = input()
		print("Введите имя: ", end="")
		insert["Name_D"] = input()
		print("Введите отчество: ", end="")
		insert["Secondname_D"] = input()
		print("Введите номер телефона: ", end="")
		insert["Phone"] = int(input())
		while True:
			insert["Password"] = input("Введите пароль: ")
			if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", insert["Password"]):
				break
			else:
				print("Пароль должен содержать строчные и заглавные буквы, цифры и специальные символы, и быть не менее 8 символов длиной.")
		DB_Doctor.insertData("Attending_Doctor",insert)
		print("Пользователь успешно добавлен")
		search = {"Phone":insert["Phone"]}
		id_doctor=DB_Doctor.getId(search)
		return id_doctor

	

			
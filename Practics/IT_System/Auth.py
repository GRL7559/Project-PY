from DB import DB
import re

class Auth:
	def __init__(self):
		pass

	def log_in(self):
		doctor = DB()
		doctors_data = doctor.getData("Attending_Doctor")
		while(True):
			print("Введите логин(телефон): ",end="")
			try:
				login = int(input())
			except(Exception):
				print("Введено некорректное значение")
				continue
			confirm_login=False
			for doctor_data in doctors_data:
				if doctor_data["Phone"] == login:
					true_password = doctor_data["Password"]
					confirm_login = True
			if confirm_login:break
			else:
				print("Пользователь не найден")
		while(True):
			print("Введите пароль: ",end="")
			password=input()
			if password==true_password:
				print("Вход успешно выполнен")
				break
			else:
				print("Неверный пароль"),

	def sign_up(self):
		doctor = DB()
		insert = {"Surname_D":"","Name_D":"","Secondname_D":"","Phone":0,"Password":0}
		print("Введите фамилию: ", end="")
		insert["Surname_D"] = input()
		print("Введите имя: ", end="")
		insert["Name_D"] = input()
		print("Введите отчество: ", end="")
		insert["Secondname_D"] = input()
		print("Введите номер телефона: ", end="")
		while True:
			try:
				insert["Phone"] = int(input()) 
				break
			except(Exception):
				print("Введено некорректное значение")
				continue
		while True:
			insert["Password"] = input("Введите пароль: ")
			if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", insert["Password"]):
				break
			else:
				print("Пароль должен содержать строчные и заглавные буквы, цифры и специальные символы, и быть не менее 8 символов длиной.")
		doctor.insertData("Attending_Doctor",insert)
		print("Пользователь успешно добавлен")

	

			
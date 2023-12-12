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
				if doctor_data[4] == login:
					true_password = doctor_data[5]
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
		insert = ("","","",0,0)
		while(True):
			print("Введите фамилию: ", end="")
			insert[0] = input()
			if insert[0] == "":
				print("Фамилия не может быть пустым")
			else:break
		while(True):
			print("Введите имя: ", end="")
			insert[1] = input()
			if insert[1] == "":
				print("Имя не может быть пустым")
			else:break
		print("Введите отчество: ", end="")
		insert[2] = input()
		print("Введите номер телефона: ", end="")
		while True:
			try:
				insert[3] = int(input()) 
				break
			except(Exception):
				print("Введено некорректное значение")
				continue
		while True:
			insert[4] = input("Введите пароль: ")
			if re.match(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$", insert[4]):
				break
			else:
				print("Пароль должен содержать строчные и заглавные буквы, цифры и специальные символы, и быть не менее 8 символов длиной.")
		doctor.insertData("Attending_Doctor",insert)
		print("Пользователь успешно добавлен")

	

			
import My_DB 

class Auth:
	def log_in():
		while(True):
			code = My_DB.getData("Attending_doctor")
			print("Введите логин(телефон)",end="")
			login = int(input)
			if len.login != 11:
				print("Введено некорректное значение")
				continue
			else:
				confirm_login=False
				for i in range(1,len.code-1):
					if code[i]==login:
						id_doctor = i
						confirm_login = True
				if confirm_login:break
				else:
					print("Пользователь не найден")
		while(True):
			print("Введите пароль",end="")
			password=input()
			true_password=code[id_doctor].password
			if password==true_password:
				print("Вход успешно выполнен")
				return id_doctor
			else:
				print("Неверный пароль")

	def sign_up():
		insert = [{"Surname_D":""},{"Name_D":""},{"Secondname_D":""},{"Phone":0},{"Password":0}]
		print("Введите фамилию",end="")
		insert.Surname_D=input()
		print("Введите имя",end="")
		insert.Name_D=input()
		print("Введите отчество",end="")
		insert.Secondname_D=input()
		print("Введите номер телефона",end="")
		insert.Phone=int(input())
		print("Введите пароль",end="")
		insert.Password=input()
		My_DB.insertData("Attending_doctor",insert)
		print("Пользователь успешно добавлен")
		id_doctor=My_DB.getId()
		return id_doctor

	
	print("Здравствуйте, для Входа нажмите 1 , для регестрации нажмите 2")
	enter = input()
	match enter:
		case 1:log_in
		case 2:sign_up
			
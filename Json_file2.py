from json import dump, load
from time import sleep
from random import random

def json_file(path, data = None, delay = 0.1):
	while True:
		try:
			if data == None: # если дата="нет ничего" загружаем из файла
				with open(path, "r", encoding = "utf-8") as f:
				  return load(f)
			else:
				with open(path, "w", encoding = "utf-8") as f:
				  return dump(data, f)
		except:
			sleep(random()*delay) # concurrency

tr=json_file('no.txt', data = None, delay = 0.1) # функция в действии: загружаем данные
print(tr)

json_file('no2.txt', data = tr, delay = 0.1)  # функция в действии: сохраняем данные

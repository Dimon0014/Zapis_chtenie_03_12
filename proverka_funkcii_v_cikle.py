import json
import random


# ------------- в начале обработка единичных символов

def last_last_seen_steps_of_simv_01(dict, key):  # альтернатива  "last_next_seen_all_steps_1"
	result = dict[key][0]
	
	# print('функия next_seen_steps =',result)
	return result


def dob_next_seen_1(dict, key, steps):  # функция добавления/инициализация шагов с последнего появления
	
	if (key) in dict:  # проверка на наличие значений
		last_seen = last_last_seen_steps_of_simv_01(dict, key)
		# print('steps-last_time seen_in_key =', last_seen)
		# print('печатает dict[key][1][0]', dict[key][1][0])
		dict[key][1].append(last_seen)
		dict[key][2] = len(dict[key][1])  # сколько раз уже выпадала
	
	
	else:  # инициализация
		dict.update({(key): [0, [steps], 1, key, steps]})  # инициализация
	# print('key in function =', key)


def add_step_to_all_1(dict):
	for item in dict:
		dict[item][0] = dict[item][0] + 1
		dict[item][4] = dict[item][4] + 1


def more_of_1(dict):
	spisok = []
	a = 0
	s = 0
	spisok2 = []
	for item in dict:
		if dict[item][2] == 1:
			
			if dict[item][4] > 100:
				
				spisok.append(dict[item])
				if len(spisok) > 0:
					a = dict[item][3]
					s = dict[item][4]
					
					# print('spisok', spisok)
					spisok2.append(a)
					spisok2.append(s)
				# print('spisok2', spisok2)
				break
			
			# print("номер", dict[item][3], "выпал", dict[item][2], "раз(а)--шаг", dict[item][4])
	return spisok2


def podchet_simv(s):  # подсчет сколько раз встречаются символы в строке(списке)
	d = dict()
	for c in s:
		if c not in d:
			d[c] = 1
		else:
			d[c] += 1
	return d


# отсюда функции патернов-------------------------------
#
# сначала из двух цифр



# key1 -- значение выпавшего числа\\
# key1step(key,dictEd) - функция находит значение интервала для выпавшего числа в словаре dictEd  \\
# key1step - значение интервала у выпавшего сейчас числа\\
# key2step - значение интервала с предыдущего шага\\
# key1step, key2step -- паттерн который нужно сравнить \\
# dictEd -- словарь одиночных символов, откуда нужно взять значение step(dict[key][0])\\

# listAll_inter -- список всех интервалов друг за другом -- сплошняком
# dict2Glob -- словарь интервалов двоек глобал\\
# dict2Lok -- словарь интервалов двоек локал\\

#

#
# def intervals_of_02(key1_step,key2step):
def key01step(key, dictEd):
	result = dictEd[(key)][0]
	dictEd[key][0] = 0  # после того как достанет обнуляет
	# print('из функции достающей интервалы result',result )
	# print('из функции достающей интервалы dictEd[(key)][0]', dictEd[(key)][0])
	return result


def key01step1(key, dictEd):
	result = dictEd[(key)][0]
	# dictEd[key][0] = 0  # после того как достанет обнуляет
	# print('из функции достающей интервалы result',result )
	# print('из функции достающей интервалы dictEd[(key)][0]', dictEd[(key)][0])
	return result


# key01step = key01step(key,dictEd) # вычисляем когда последний раз был виден выпавший номер
def intervals_of_2(key2step, key1step, dict2Glob,
				   steps_sesia):  # функция добавления интервалов как для глобал так и для локал
	if (key2step, key1step) in dict2Glob:  # проверка dict2Glob на наличие ключа, если нет то инициализация
		
		last_seen = dict2Glob[(key2step, key1step)][0]  # переменную последний раз видели загоняем в буфер
		dict2Glob[(key2step, key1step)][0] = 0  # переменную последний раз видели обнуляем
		dict2Glob[(key2step, key1step)][1].append(last_seen)  # добавляем значение к списку последний раз видели
		count = len(dict2Glob[(key2step, key1step)][1])  # переменную переменную раз видели загоняем в буфер
		dict2Glob[(key2step, key1step)][2] = count
	# dict2Glob[(key2step,key1step)][3] = steps_sesia # количество шагов в сесии- нужно для предсказанияkey1step # первый символ ключа
	#  dict2Glob[(key2step,key1step)][4] = key2step # первый символ ключа
	#  dict2Glob[(key2step,key1step)][5] = key1step # второй символ ключа
	else:
		dict2Glob.update({(key2step, key1step): [0, [1], 1, key2step, key1step, steps_sesia]})  # инициализация


def intervals_of_3(key3step, key2step, key1step, dict3Glob,
				   steps_sesia):  # функция добавления интервалов как для глобал так и для локал
	if (key3step, key2step, key1step) in dict3Glob:  # проверка dict2Glob на пустоту, если пусто то инициализация
		last_seen = dict3Glob[(key3step, key2step, key1step)][0]  # переменную последний раз видели загоняем в буфер
		dict3Glob[(key3step, key2step, key1step)][0] = 0  # переменную последний раз видели обнуляем
		dict3Glob[(key3step, key2step, key1step)][1].append(
			last_seen)  # добавляем значение к списку последний раз видели
		count = len(
			dict3Glob[(key3step, key2step, key1step)][1])  # переменную переменную раз видели загоняем в буфер
		dict3Glob[(key3step, key2step, key1step)][2] = count
		# dict3Glob[(key3step, key2step,key1step)][3] = steps_sesia   #количество шагов в сесии- нужно для предсказания
		#  dict3Glob[(key3step, key2step,key1step)][4] = key3step  # первый символ ключа
		#  dict3Glob[(key3step, key2step,key1step)][5] = key2step   # второй символ ключа
		#  dict3Glob[(key3step, key2step,key1step)][6] = key1step # третий символ ключа
		print(' обновление словаря')
	else:
		dict3Glob.update({(key3step, key2step, key1step): [0, [1], 1, key3step, key2step, key1step,
														   steps_sesia]})  # инициализация
		print(' создание словаря')


def intervals_of_all(key1step, listAll_inter):  # список всех подряд интервалов
	listAll_inter.append(key1step)


# функция добавляющая шаги к словарям
def add_step_to_all_intervals_of_2(dict_interv2, key2step, key1step):  # а вот функция которая добовляет всем шаги
	# key=(key2step, key1step)
	for item in dict_interv2:
		# if item != key:
		
		dict_interv2[item][0] = dict_interv2[item][0] + 1
		dict_interv2[item][3] = dict_interv2[item][3] + 1
		print('dict_interv2[item][0]', dict_interv2[item][0])
		print('dict_interv2[item][3]', dict_interv2[item][3])
	# for item in dict_interv2:
	#     if item == key:
	#        dict[item][3] = dict[item][0] + 1
	
	
	# def intervals_of_2(key1_step,key2step, dictEd, dict2,dict2lok,listAll_inter):
	#     #  перебор всех значений словаря по ключу в другой функции, эта функция сравнивает и добавляет
	#
	#       if len(dict2[(key1)][0]) != 0:  # проверка на наличие значений, проверяется длинна словаря- умное решение
	#         # times_seen = len(dict[key][1])
	#         listAll_inter.append(0) # добавление 0-левого интервала в общий список
	#                             # в принципе интервал равный нулю может быть только в начале, как и интервал [1,0], [2,1] в
	#                            # общем первые значения интервалов в мусор
	#         listAll_inter.append(dict[key1][0]) # добавление первого значимого интервала в общий список
	#         key2step=key1
	#         dict2[(key1)][0]=1
	#         print('первая запись в списке интервалов', key1)
	#       else:
	#         listAll_inter.append(dict[key1][0])
	#         dict[(key)][0]
	#         for item in dict:
	#             if item == key1:
	#                 dict2[item][0] = dict[item][0] + 1
	
	# собственно тело программы начинается здесь----------------------------------------------------------------


# steps = 225  типа имитатор счетчика ходов
# значение словаря еденичных символо на текущий момент

# проверочный словарь d = {(36):[ 1,[1, 2], 33, 22,2],(35):[ 11,[101, 102], 31, 22,2],(34):[ 13,[103, 106], 71, 22,2]}
# типа число полученное от распознователя символов key = (35)

# востановление всех ходов
def postrocno(spisok, name):  # вывод из списка на консоль не одной строкой, а каждое значение на своей строке
	i = 0
	for item in spisok:
		i = i + 1
		print(steps, name, 'стока', i, item)


# def podchet_interv_odd(slovar): # подсчет интервалов у всех нечетных выпадений
# 	obshie = 0
# 	rezult = 0
# 	for item in slovar:
# 		if (slovar[item][3] % 2) != 0:
# 			if (slovar[item][0]) > 180:
# 				rezult = obshie + slovar[item][0]
#
# 	return rezult


# def podchet_interv_iven(slovar):   # подсчет интервалов у всех четных выпадений
# 	obshie = 0
# 	rezult = 0
# 	for item in slovar:
# 		if (slovar[item][3] % 2) == 0:
# 			if (slovar[item][0]) > 180:
# 				rezult = obshie + slovar[item][0]
# 	return rezult


def podchet_count_odd(slovar):  # подсчет количества едениц(а не интервал, тоесть сколько раз выпадали за игру
	# нечетные значения) у всех нечетных выпадений
	obshie = []
	rezult = 0
	for item in slovar:
		if (slovar[item][3] % 2) != 0:
			if (slovar[item][0]) < 110:
				obshie.append(slovar[item][3])
				rezult = len(obshie)
	return rezult


def podchet_count_iven(slovar):  # подсчет количества едениц(а не интервал, тоесть сколько раз выпадали за
	# игру четные значения) у всех четных выпадений
	obshie = []
	rezult = 0
	for item in slovar:
		if (slovar[item][3] % 2) == 0:
			if (slovar[item][0]) < 110:
				obshie.append(slovar[item][3])
				rezult = len(obshie)
	return rezult


def stepsbig(interval, porog, steps_big):
	steps_big
	if interval < porog:
		steps_big = steps_big + 1
	return steps_big


def nahogd_big_interv(slovar):
	rezult = 0
	big = 0
	for item in slovar:
		
		if (slovar[item][0]) > big:
			rezult = slovar[item][3]
			slovar[item][0] = big
	return rezult


# def chislo_1(razresh_1, key, dict_contr_1):
# 	win = 0
# 	proig = 0
# 	spisok = [0, 0, True]
# 	result = []
# 	if razresh_1:
# 		if key == 1:
# 			# блок обработки выигрыша
# 			win = 36 * dict_contr_1["koef"]
# 			razresh_1 = False
# 			dict_contr_1["step"] = 0
# 			dict_contr_1["koef"] = 0.1  # установка минимальной ставки
# 			spisok[0] = win
# 			spisok[2] = razresh_1
# 		else:
# 			razresh_1 = True
# 			dict_contr_1["step"] = dict_contr_1["step"] + 1
# 			if dict_contr_1["step"] == 36:
# 				dict_contr_1["koef"] = dict_contr_1["koef"] * 2
#
# 			if dict_contr_1["step"] == 54:
# 				dict_contr_1["koef"] = dict_contr_1["koef"] * 2
# 			if dict_contr_1["step"] == 72:
# 				dict_contr_1["koef"] = dict_contr_1["koef"] * 2
# 			if dict_contr_1["step"] == 90:
# 				dict_contr_1["koef"] = dict_contr_1["koef"] * 2
# 			if dict_contr_1["step"] == 108:
# 				razresh_1 = False
# 			proig = proig - dict_contr_1["koef"]
# 			spisok[0] = win
# 			spisok[1] = proig
# 			spisok[2] = razresh_1
# 	return spisok
#
#
# def chislo_2(razresh_2, key, dict_contr_2):
# 	win = 0
# 	proig = 0
# 	spisok = [0, 0, True]
# 	result = []
# 	if razresh_2:
# 		if key == 2:
# 			win = 36 * dict_contr_2["koef"]
# 			razresh_2 = False
# 			dict_contr_2["step"] = 0
# 			dict_contr_2["koef"] = 0.1
# 			spisok[0] = win
# 			spisok[2] = razresh_2
# 		else:
# 			razresh_2 = True
# 			dict_contr_2["step"] = dict_contr_2["step"] + 1
# 			if dict_contr_2["step"] == 36:
# 				dict_contr_2["koef"] = dict_contr_2["koef"] * 2
#
# 			if dict_contr_2["step"] == 54:
# 				dict_contr_2["koef"] = dict_contr_2["koef"] * 2
# 			if dict_contr_2["step"] == 72:
# 				dict_contr_2["koef"] = dict_contr_2["koef"] * 2
# 			if dict_contr_2["step"] == 90:
# 				dict_contr_2["koef"] = dict_contr_2["koef"] * 2
# 			if dict_contr_2["step"] == 108:
# 				razresh_2 = False
# 			proig = proig - dict_contr_2["koef"]
# 			spisok[0] = win
# 			spisok[1] = proig
# 			spisok[2] = razresh_2
# 	return spisok
#
#
# def chislo_3(razresh_3, key, dict_contr_3):
# 	win = 0
# 	proig = 0
# 	spisok = [0, 0, True]
# 	result = []
# 	if razresh_3:
# 		if key == 2:
# 			win = 36 * dict_contr_3["koef"]
# 			razresh_3 = False
# 			dict_contr_3["step"] = 0
# 			dict_contr_3["koef"] = 0.1
# 			spisok[0] = win
# 			spisok[2] = razresh_3
# 		else:
# 			razresh_3 = True
# 			dict_contr_3["step"] = dict_contr_3["step"] + 1
# 			if dict_contr_3["step"] == 36:
# 				dict_contr_3["koef"] = dict_contr_3["koef"] * 2
#
# 			if dict_contr_3["step"] == 54:
# 				dict_contr_3["koef"] = dict_contr_3["koef"] * 2
# 			if dict_contr_3["step"] == 72:
# 				dict_contr_3["koef"] = dict_contr_3["koef"] * 2
# 			if dict_contr_3["step"] == 90:
# 				dict_contr_3["koef"] = dict_contr_3["koef"] * 2
# 			if dict_contr_3["step"] == 108:
# 				razresh_3 = False
# 			proig = proig - dict_contr_3["koef"]
# 			spisok[0] = win
# 			spisok[1] = proig
# 			spisok[2] = razresh_3
# 	return spisok
#
#
# def chislo_4(razresh_4, key, dict_contr_4):
# 	win = 0
# 	proig = 0
# 	spisok = [0, 0, True]
# 	result = []
# 	if razresh_4:
# 		if key == 2:
# 			win = 36 * dict_contr_4["koef"]
# 			razresh_4 = False
# 			dict_contr_4["step"] = 0
# 			dict_contr_4["koef"] = 0.1
# 			spisok[0] = win
# 			spisok[2] = razresh_4
# 		else:
# 			razresh_4 = True
# 			dict_contr_4["step"] = dict_contr_4["step"] + 1
# 			if dict_contr_4["step"] == 36:
# 				dict_contr_4["koef"] = dict_contr_4["koef"] * 2
#
# 			if dict_contr_4["step"] == 54:
# 				dict_contr_4["koef"] = dict_contr_4["koef"] * 2
# 			if dict_contr_4["step"] == 72:
# 				dict_contr_4["koef"] = dict_contr_4["koef"] * 2
# 			if dict_contr_4["step"] == 90:
# 				dict_contr_4["koef"] = dict_contr_4["koef"] * 2
# 			if dict_contr_4["step"] == 108:
# 				razresh_4 = False
# 			proig = proig - dict_contr_4["koef"]
# 			spisok[0] = win
# 			spisok[1] = proig
# 			spisok[2] = razresh_4
# 	return spisok
#
for i in range(2):
	chis = str(i)
	
	
	# print('def chislo_0'+str(i)+'(razresh_0'+str(i)+', key, dict_contr_0'+str(i)+'):\n')
	# print('    win = 0\n ')
	# print('    proig = 0\n ')
	# print('    spisok = [0, 0, True] ')
	
	
	def chislo_chis(razresh_chis, key, dict_contr_chis):
		win = 0
		proig = 0
		spisok = [0, 0, True]
		result = []
		if razresh_chis:
			if key == 2:
				win = 36 * dict_contr_chis["koef"]
				razresh_chis = False
				dict_contr_chis["step"] = 0
				dict_contr_chis["koef"] = 0.1
				spisok[0] = win
				spisok[2] = razresh_chis
			else:
				razresh_chis = True
				dict_contr_chis["step"] = dict_contr_chis["step"] + 1
				if dict_contr_chis["step"] == 36:
					dict_contr_chis["koef"] = dict_contr_chis["koef"] * 2
				
				if dict_contr_chis["step"] == 54:
					dict_contr_chis["koef"] = dict_contr_chis["koef"] * 2
				if dict_contr_chis["step"] == 72:
					dict_contr_chis["koef"] = dict_contr_chis["koef"] * 2
				if dict_contr_chis["step"] == 90:
					dict_contr_chis["koef"] = dict_contr_chis["koef"] * 2
				if dict_contr_chis["step"] == 108:
					razresh_chis = False
				proig = proig - dict_contr_chis["koef"]
				spisok[0] = win
				spisok[1] = proig
				spisok[2] = razresh_chis
		return spisok

rasnica2 = 0
ik = 0
vig = 0
prg = 0
chag = 0
while (ik < 10):
	ik = ik + 1
	file_obj = open('100_xodov.txt', 'w')  ##
	file_obj.close()  ## генератор чисел
	file_obj = open('100_xodov.txt', 'a')  ##
	for i in range(400):  ##
		chislo = random.randint(0, 36)  # генерируем число##
		file_obj.write(str(chislo) + '\n')  ##
	##
	file_obj.close()  ##
	
	viborka = []  ##
	file_obj = open('100_xodov.txt')  ## Создание списка из нагерерированого
	data_list = file_obj.readlines()  ##
	for line in data_list:  ##
		viborka.append(int(line))  ##
	# объявление всех переменных-----------------------------------------------------------------------------------
	dic_ed = {}  # болванка под словарь едениц
	# -----------------------------------------------------------------------------------
	
	key = 0
	steps_sesia = 1
	key1 = key
	steps = 0
	
	log = True
	win = ''
	win1 = True
	win2 = True
	win3 = True
	win4 = True
	Viigral = 0
	Proigral = 0
	
	index_predscazan = 0
	interval_chis
	raznica = 0
	razresh_1 = True
	dict_contr_1 = {"koef": 0.1, "step": 0}
	dict_tansf_1 = [0, 0, 0]
	interval_1 = 0
	razresh_2 = True
	dict_contr_2 = {"koef": 0.1, "step": 0}
	dict_tansf_2 = [0, 0, 0]
	interval_2 = 0
	razresh_3 = True
	dict_contr_3 = {"koef": 0.1, "step": 0}
	dict_tansf_3 = [0, 0, 0]
	interval_3 = 0
	razresh_4 = True
	dict_contr_4 = {"koef": 0.1, "step": 0}
	dict_tansf_4 = [0, 0, 0]
	interval_4 = 0
	while (steps < len(viborka)):
		key = viborka[steps]
		key1 = key
		steps = steps + 1
		if steps == 1:
			dob_next_seen_1(dic_ed, 1, steps)
			dob_next_seen_1(dic_ed, 2, steps)
			dob_next_seen_1(dic_ed, 3, steps)
			dob_next_seen_1(dic_ed, 4, steps)
		dob_next_seen_1(dic_ed, key, steps)  # создание\ обновление словаря едениц
		# добавление шагов всем еденицам
		# проверочный - dictEd = {(36): [23, [1, 2], 33]}
		
		for i in range(2):
			chis = str(i)
			if interval_chis < 120:
				
				if razresh_chis:
					dict_tansf_1 = chislo_chis(razresh_1, key, dict_contr_chis)
					Viigral = Viigral + dict_tansf_chis[0]
					Proigral = Proigral + dict_tansf_chis[1]
					razresh_chis = dict_tansf_chis[2]
		# if interval_1 < 120:
		#
		# 	if razresh_1:
		# 		dict_tansf_1 = chislo_1(razresh_1, key, dict_contr_1)
		# 		Viigral = Viigral + dict_tansf_1[0]
		# 		Proigral = Proigral + dict_tansf_1[1]
		# 		razresh_1 = dict_tansf_1[2]
		# if interval_2 < 120:
		# 	if razresh_2:
		# 		dict_tansf_2 = chislo_2(razresh_2, key, dict_contr_2)
		# 		Viigral = Viigral + dict_tansf_2[0]
		# 		Proigral = Proigral + dict_tansf_2[1]
		# 		razresh_2 = dict_tansf_2[2]
		# if interval_3 < 120:
		# 	if razresh_3:
		# 		dict_tansf_3 = chislo_3(razresh_3, key, dict_contr_3)
		# 		Viigral = Viigral + dict_tansf_3[0]
		# 		Proigral = Proigral + dict_tansf_3[1]
		# 		razresh_3 = dict_tansf_3[2]
		# if interval_4 < 120:
		# 	if razresh_4:
		# 		dict_tansf_4 = chislo_4(razresh_4, key, dict_contr_4)
		# 		Viigral = Viigral + dict_tansf_4[0]
		# 		Proigral = Proigral + dict_tansf_4[1]
		# 		razresh_4 = dict_tansf_4[2]
		if (not razresh_1) and (not razresh_2) and (not razresh_3) and (not razresh_4):
			razresh_1 = True
			razresh_2 = True
			razresh_3 = True
			razresh_4 = True
		rasnica = Viigral + Proigral
		print('Разница:', rasnica)
		
		interval_1 = key01step1(1, dic_ed)
		interval_2 = key01step1(2, dic_ed)
		interval_3 = key01step1(3, dic_ed)
		interval_4 = key01step1(4, dic_ed)
		interval = key01step(key1, dic_ed)  # последний интервал выпавшего числа
		add_step_to_all_1(dic_ed)
		if rasnica > 0.1:
			break
		if rasnica < -0.5:
			break
	
	# print('количество рзных символов',int_count )
	# print('количество шагов биг',steps_big )
	print('Выиграл:', Viigral)
	print('Проиграл:', Proigral)
	vig = vig + Viigral
	prg = prg + Proigral
	rasnica2 = vig + prg
	# if rasnica2> 0.1:
	#     break
	# if rasnica2< - 0.1:
	#     break
	chag = chag + 1
	rasnica = Viigral + Proigral
	
	print(rasnica)
# if rasnica> 100:
#     break
# postrocno(int_count)
# print('словарь едениц',dic_ed)
# print('chag', chag)

# postrocno(bad_pred,'Bad')
# postrocno(good_pred,'Good')
# print('Выиграл:',vig)
# print('Проиграл:',prg)
rasnica = vig - prg
print('---------------------------------')
print('общтй итог:', rasnica2)
# print('chag',ik)

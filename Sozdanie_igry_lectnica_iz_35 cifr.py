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


# начало блока 0
def chislo_1(razresh_1, key, dict_contr_1):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_1:
       if key == 2:
          win = 36 * dict_contr_1["koef"]
          razresh_1 = False
          dict_contr_1["step"] = 0
          dict_contr_1["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_1
       else:
          razresh_1 = True
          dict_contr_1["step"] = dict_contr_1["step"] + 1
          if dict_contr_1["step"] == 36:
             dict_contr_1["koef"] = dict_contr_1["koef"] * 2
          if dict_contr_1["step"] == 54:
             dict_contr_1["koef"] = dict_contr_1["koef"] * 2
          if dict_contr_1["step"] == 72:
             dict_contr_1["koef"] = dict_contr_1["koef"] * 2
          if dict_contr_1["step"] == 90:
             dict_contr_1["koef"] = dict_contr_1["koef"] * 2
          if dict_contr_1["step"] == 108:
             razresh_1 = False
          proig = proig - dict_contr_1["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_1
    return spisok
def chislo_2(razresh_2, key, dict_contr_2):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_2:
       if key == 2:
          win = 36 * dict_contr_2["koef"]
          razresh_2 = False
          dict_contr_2["step"] = 0
          dict_contr_2["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_2
       else:
          razresh_2 = True
          dict_contr_2["step"] = dict_contr_2["step"] + 1
          if dict_contr_2["step"] == 36:
             dict_contr_2["koef"] = dict_contr_2["koef"] * 2
          if dict_contr_2["step"] == 54:
             dict_contr_2["koef"] = dict_contr_2["koef"] * 2
          if dict_contr_2["step"] == 72:
             dict_contr_2["koef"] = dict_contr_2["koef"] * 2
          if dict_contr_2["step"] == 90:
             dict_contr_2["koef"] = dict_contr_2["koef"] * 2
          if dict_contr_2["step"] == 108:
             razresh_2 = False
          proig = proig - dict_contr_2["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_2
    return spisok
def chislo_3(razresh_3, key, dict_contr_3):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_3:
       if key == 2:
          win = 36 * dict_contr_3["koef"]
          razresh_3 = False
          dict_contr_3["step"] = 0
          dict_contr_3["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_3
       else:
          razresh_3 = True
          dict_contr_3["step"] = dict_contr_3["step"] + 1
          if dict_contr_3["step"] == 36:
             dict_contr_3["koef"] = dict_contr_3["koef"] * 2
          if dict_contr_3["step"] == 54:
             dict_contr_3["koef"] = dict_contr_3["koef"] * 2
          if dict_contr_3["step"] == 72:
             dict_contr_3["koef"] = dict_contr_3["koef"] * 2
          if dict_contr_3["step"] == 90:
             dict_contr_3["koef"] = dict_contr_3["koef"] * 2
          if dict_contr_3["step"] == 108:
             razresh_3 = False
          proig = proig - dict_contr_3["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_3
    return spisok
def chislo_4(razresh_4, key, dict_contr_4):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_4:
       if key == 2:
          win = 36 * dict_contr_4["koef"]
          razresh_4 = False
          dict_contr_4["step"] = 0
          dict_contr_4["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_4
       else:
          razresh_4 = True
          dict_contr_4["step"] = dict_contr_4["step"] + 1
          if dict_contr_4["step"] == 36:
             dict_contr_4["koef"] = dict_contr_4["koef"] * 2
          if dict_contr_4["step"] == 54:
             dict_contr_4["koef"] = dict_contr_4["koef"] * 2
          if dict_contr_4["step"] == 72:
             dict_contr_4["koef"] = dict_contr_4["koef"] * 2
          if dict_contr_4["step"] == 90:
             dict_contr_4["koef"] = dict_contr_4["koef"] * 2
          if dict_contr_4["step"] == 108:
             razresh_4 = False
          proig = proig - dict_contr_4["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_4
    return spisok
def chislo_5(razresh_5, key, dict_contr_5):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_5:
       if key == 2:
          win = 36 * dict_contr_5["koef"]
          razresh_5 = False
          dict_contr_5["step"] = 0
          dict_contr_5["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_5
       else:
          razresh_5 = True
          dict_contr_5["step"] = dict_contr_5["step"] + 1
          if dict_contr_5["step"] == 36:
             dict_contr_5["koef"] = dict_contr_5["koef"] * 2
          if dict_contr_5["step"] == 54:
             dict_contr_5["koef"] = dict_contr_5["koef"] * 2
          if dict_contr_5["step"] == 72:
             dict_contr_5["koef"] = dict_contr_5["koef"] * 2
          if dict_contr_5["step"] == 90:
             dict_contr_5["koef"] = dict_contr_5["koef"] * 2
          if dict_contr_5["step"] == 108:
             razresh_5 = False
          proig = proig - dict_contr_5["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_5
    return spisok
def chislo_6(razresh_6, key, dict_contr_6):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_6:
       if key == 2:
          win = 36 * dict_contr_6["koef"]
          razresh_6 = False
          dict_contr_6["step"] = 0
          dict_contr_6["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_6
       else:
          razresh_6 = True
          dict_contr_6["step"] = dict_contr_6["step"] + 1
          if dict_contr_6["step"] == 36:
             dict_contr_6["koef"] = dict_contr_6["koef"] * 2
          if dict_contr_6["step"] == 54:
             dict_contr_6["koef"] = dict_contr_6["koef"] * 2
          if dict_contr_6["step"] == 72:
             dict_contr_6["koef"] = dict_contr_6["koef"] * 2
          if dict_contr_6["step"] == 90:
             dict_contr_6["koef"] = dict_contr_6["koef"] * 2
          if dict_contr_6["step"] == 108:
             razresh_6 = False
          proig = proig - dict_contr_6["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_6
    return spisok
def chislo_7(razresh_7, key, dict_contr_7):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_7:
       if key == 2:
          win = 36 * dict_contr_7["koef"]
          razresh_7 = False
          dict_contr_7["step"] = 0
          dict_contr_7["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_7
       else:
          razresh_7 = True
          dict_contr_7["step"] = dict_contr_7["step"] + 1
          if dict_contr_7["step"] == 36:
             dict_contr_7["koef"] = dict_contr_7["koef"] * 2
          if dict_contr_7["step"] == 54:
             dict_contr_7["koef"] = dict_contr_7["koef"] * 2
          if dict_contr_7["step"] == 72:
             dict_contr_7["koef"] = dict_contr_7["koef"] * 2
          if dict_contr_7["step"] == 90:
             dict_contr_7["koef"] = dict_contr_7["koef"] * 2
          if dict_contr_7["step"] == 108:
             razresh_7 = False
          proig = proig - dict_contr_7["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_7
    return spisok
def chislo_8(razresh_8, key, dict_contr_8):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_8:
       if key == 2:
          win = 36 * dict_contr_8["koef"]
          razresh_8 = False
          dict_contr_8["step"] = 0
          dict_contr_8["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_8
       else:
          razresh_8 = True
          dict_contr_8["step"] = dict_contr_8["step"] + 1
          if dict_contr_8["step"] == 36:
             dict_contr_8["koef"] = dict_contr_8["koef"] * 2
          if dict_contr_8["step"] == 54:
             dict_contr_8["koef"] = dict_contr_8["koef"] * 2
          if dict_contr_8["step"] == 72:
             dict_contr_8["koef"] = dict_contr_8["koef"] * 2
          if dict_contr_8["step"] == 90:
             dict_contr_8["koef"] = dict_contr_8["koef"] * 2
          if dict_contr_8["step"] == 108:
             razresh_8 = False
          proig = proig - dict_contr_8["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_8
    return spisok
def chislo_9(razresh_9, key, dict_contr_9):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_9:
       if key == 2:
          win = 36 * dict_contr_9["koef"]
          razresh_9 = False
          dict_contr_9["step"] = 0
          dict_contr_9["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_9
       else:
          razresh_9 = True
          dict_contr_9["step"] = dict_contr_9["step"] + 1
          if dict_contr_9["step"] == 36:
             dict_contr_9["koef"] = dict_contr_9["koef"] * 2
          if dict_contr_9["step"] == 54:
             dict_contr_9["koef"] = dict_contr_9["koef"] * 2
          if dict_contr_9["step"] == 72:
             dict_contr_9["koef"] = dict_contr_9["koef"] * 2
          if dict_contr_9["step"] == 90:
             dict_contr_9["koef"] = dict_contr_9["koef"] * 2
          if dict_contr_9["step"] == 108:
             razresh_9 = False
          proig = proig - dict_contr_9["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_9
    return spisok
def chislo_10(razresh_10, key, dict_contr_10):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_10:
       if key == 2:
          win = 36 * dict_contr_10["koef"]
          razresh_10 = False
          dict_contr_10["step"] = 0
          dict_contr_10["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_10
       else:
          razresh_10 = True
          dict_contr_10["step"] = dict_contr_10["step"] + 1
          if dict_contr_10["step"] == 36:
             dict_contr_10["koef"] = dict_contr_10["koef"] * 2
          if dict_contr_10["step"] == 54:
             dict_contr_10["koef"] = dict_contr_10["koef"] * 2
          if dict_contr_10["step"] == 72:
             dict_contr_10["koef"] = dict_contr_10["koef"] * 2
          if dict_contr_10["step"] == 90:
             dict_contr_10["koef"] = dict_contr_10["koef"] * 2
          if dict_contr_10["step"] == 108:
             razresh_10 = False
          proig = proig - dict_contr_10["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_10
    return spisok
def chislo_11(razresh_11, key, dict_contr_11):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_11:
       if key == 2:
          win = 36 * dict_contr_11["koef"]
          razresh_11 = False
          dict_contr_11["step"] = 0
          dict_contr_11["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_11
       else:
          razresh_11 = True
          dict_contr_11["step"] = dict_contr_11["step"] + 1
          if dict_contr_11["step"] == 36:
             dict_contr_11["koef"] = dict_contr_11["koef"] * 2
          if dict_contr_11["step"] == 54:
             dict_contr_11["koef"] = dict_contr_11["koef"] * 2
          if dict_contr_11["step"] == 72:
             dict_contr_11["koef"] = dict_contr_11["koef"] * 2
          if dict_contr_11["step"] == 90:
             dict_contr_11["koef"] = dict_contr_11["koef"] * 2
          if dict_contr_11["step"] == 108:
             razresh_11 = False
          proig = proig - dict_contr_11["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_11
    return spisok
def chislo_12(razresh_12, key, dict_contr_12):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_12:
       if key == 2:
          win = 36 * dict_contr_12["koef"]
          razresh_12 = False
          dict_contr_12["step"] = 0
          dict_contr_12["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_12
       else:
          razresh_12 = True
          dict_contr_12["step"] = dict_contr_12["step"] + 1
          if dict_contr_12["step"] == 36:
             dict_contr_12["koef"] = dict_contr_12["koef"] * 2
          if dict_contr_12["step"] == 54:
             dict_contr_12["koef"] = dict_contr_12["koef"] * 2
          if dict_contr_12["step"] == 72:
             dict_contr_12["koef"] = dict_contr_12["koef"] * 2
          if dict_contr_12["step"] == 90:
             dict_contr_12["koef"] = dict_contr_12["koef"] * 2
          if dict_contr_12["step"] == 108:
             razresh_12 = False
          proig = proig - dict_contr_12["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_12
    return spisok
def chislo_13(razresh_13, key, dict_contr_13):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_13:
       if key == 2:
          win = 36 * dict_contr_13["koef"]
          razresh_13 = False
          dict_contr_13["step"] = 0
          dict_contr_13["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_13
       else:
          razresh_13 = True
          dict_contr_13["step"] = dict_contr_13["step"] + 1
          if dict_contr_13["step"] == 36:
             dict_contr_13["koef"] = dict_contr_13["koef"] * 2
          if dict_contr_13["step"] == 54:
             dict_contr_13["koef"] = dict_contr_13["koef"] * 2
          if dict_contr_13["step"] == 72:
             dict_contr_13["koef"] = dict_contr_13["koef"] * 2
          if dict_contr_13["step"] == 90:
             dict_contr_13["koef"] = dict_contr_13["koef"] * 2
          if dict_contr_13["step"] == 108:
             razresh_13 = False
          proig = proig - dict_contr_13["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_13
    return spisok
def chislo_14(razresh_14, key, dict_contr_14):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_14:
       if key == 2:
          win = 36 * dict_contr_14["koef"]
          razresh_14 = False
          dict_contr_14["step"] = 0
          dict_contr_14["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_14
       else:
          razresh_14 = True
          dict_contr_14["step"] = dict_contr_14["step"] + 1
          if dict_contr_14["step"] == 36:
             dict_contr_14["koef"] = dict_contr_14["koef"] * 2
          if dict_contr_14["step"] == 54:
             dict_contr_14["koef"] = dict_contr_14["koef"] * 2
          if dict_contr_14["step"] == 72:
             dict_contr_14["koef"] = dict_contr_14["koef"] * 2
          if dict_contr_14["step"] == 90:
             dict_contr_14["koef"] = dict_contr_14["koef"] * 2
          if dict_contr_14["step"] == 108:
             razresh_14 = False
          proig = proig - dict_contr_14["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_14
    return spisok
def chislo_15(razresh_15, key, dict_contr_15):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_15:
       if key == 2:
          win = 36 * dict_contr_15["koef"]
          razresh_15 = False
          dict_contr_15["step"] = 0
          dict_contr_15["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_15
       else:
          razresh_15 = True
          dict_contr_15["step"] = dict_contr_15["step"] + 1
          if dict_contr_15["step"] == 36:
             dict_contr_15["koef"] = dict_contr_15["koef"] * 2
          if dict_contr_15["step"] == 54:
             dict_contr_15["koef"] = dict_contr_15["koef"] * 2
          if dict_contr_15["step"] == 72:
             dict_contr_15["koef"] = dict_contr_15["koef"] * 2
          if dict_contr_15["step"] == 90:
             dict_contr_15["koef"] = dict_contr_15["koef"] * 2
          if dict_contr_15["step"] == 108:
             razresh_15 = False
          proig = proig - dict_contr_15["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_15
    return spisok
def chislo_16(razresh_16, key, dict_contr_16):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_16:
       if key == 2:
          win = 36 * dict_contr_16["koef"]
          razresh_16 = False
          dict_contr_16["step"] = 0
          dict_contr_16["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_16
       else:
          razresh_16 = True
          dict_contr_16["step"] = dict_contr_16["step"] + 1
          if dict_contr_16["step"] == 36:
             dict_contr_16["koef"] = dict_contr_16["koef"] * 2
          if dict_contr_16["step"] == 54:
             dict_contr_16["koef"] = dict_contr_16["koef"] * 2
          if dict_contr_16["step"] == 72:
             dict_contr_16["koef"] = dict_contr_16["koef"] * 2
          if dict_contr_16["step"] == 90:
             dict_contr_16["koef"] = dict_contr_16["koef"] * 2
          if dict_contr_16["step"] == 108:
             razresh_16 = False
          proig = proig - dict_contr_16["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_16
    return spisok
def chislo_17(razresh_17, key, dict_contr_17):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_17:
       if key == 2:
          win = 36 * dict_contr_17["koef"]
          razresh_17 = False
          dict_contr_17["step"] = 0
          dict_contr_17["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_17
       else:
          razresh_17 = True
          dict_contr_17["step"] = dict_contr_17["step"] + 1
          if dict_contr_17["step"] == 36:
             dict_contr_17["koef"] = dict_contr_17["koef"] * 2
          if dict_contr_17["step"] == 54:
             dict_contr_17["koef"] = dict_contr_17["koef"] * 2
          if dict_contr_17["step"] == 72:
             dict_contr_17["koef"] = dict_contr_17["koef"] * 2
          if dict_contr_17["step"] == 90:
             dict_contr_17["koef"] = dict_contr_17["koef"] * 2
          if dict_contr_17["step"] == 108:
             razresh_17 = False
          proig = proig - dict_contr_17["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_17
    return spisok
def chislo_18(razresh_18, key, dict_contr_18):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_18:
       if key == 2:
          win = 36 * dict_contr_18["koef"]
          razresh_18 = False
          dict_contr_18["step"] = 0
          dict_contr_18["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_18
       else:
          razresh_18 = True
          dict_contr_18["step"] = dict_contr_18["step"] + 1
          if dict_contr_18["step"] == 36:
             dict_contr_18["koef"] = dict_contr_18["koef"] * 2
          if dict_contr_18["step"] == 54:
             dict_contr_18["koef"] = dict_contr_18["koef"] * 2
          if dict_contr_18["step"] == 72:
             dict_contr_18["koef"] = dict_contr_18["koef"] * 2
          if dict_contr_18["step"] == 90:
             dict_contr_18["koef"] = dict_contr_18["koef"] * 2
          if dict_contr_18["step"] == 108:
             razresh_18 = False
          proig = proig - dict_contr_18["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_18
    return spisok
def chislo_19(razresh_19, key, dict_contr_19):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_19:
       if key == 2:
          win = 36 * dict_contr_19["koef"]
          razresh_19 = False
          dict_contr_19["step"] = 0
          dict_contr_19["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_19
       else:
          razresh_19 = True
          dict_contr_19["step"] = dict_contr_19["step"] + 1
          if dict_contr_19["step"] == 36:
             dict_contr_19["koef"] = dict_contr_19["koef"] * 2
          if dict_contr_19["step"] == 54:
             dict_contr_19["koef"] = dict_contr_19["koef"] * 2
          if dict_contr_19["step"] == 72:
             dict_contr_19["koef"] = dict_contr_19["koef"] * 2
          if dict_contr_19["step"] == 90:
             dict_contr_19["koef"] = dict_contr_19["koef"] * 2
          if dict_contr_19["step"] == 108:
             razresh_19 = False
          proig = proig - dict_contr_19["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_19
    return spisok
def chislo_20(razresh_20, key, dict_contr_20):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_20:
       if key == 2:
          win = 36 * dict_contr_20["koef"]
          razresh_20 = False
          dict_contr_20["step"] = 0
          dict_contr_20["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_20
       else:
          razresh_20 = True
          dict_contr_20["step"] = dict_contr_20["step"] + 1
          if dict_contr_20["step"] == 36:
             dict_contr_20["koef"] = dict_contr_20["koef"] * 2
          if dict_contr_20["step"] == 54:
             dict_contr_20["koef"] = dict_contr_20["koef"] * 2
          if dict_contr_20["step"] == 72:
             dict_contr_20["koef"] = dict_contr_20["koef"] * 2
          if dict_contr_20["step"] == 90:
             dict_contr_20["koef"] = dict_contr_20["koef"] * 2
          if dict_contr_20["step"] == 108:
             razresh_20 = False
          proig = proig - dict_contr_20["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_20
    return spisok
def chislo_21(razresh_21, key, dict_contr_21):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_21:
       if key == 2:
          win = 36 * dict_contr_21["koef"]
          razresh_21 = False
          dict_contr_21["step"] = 0
          dict_contr_21["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_21
       else:
          razresh_21 = True
          dict_contr_21["step"] = dict_contr_21["step"] + 1
          if dict_contr_21["step"] == 36:
             dict_contr_21["koef"] = dict_contr_21["koef"] * 2
          if dict_contr_21["step"] == 54:
             dict_contr_21["koef"] = dict_contr_21["koef"] * 2
          if dict_contr_21["step"] == 72:
             dict_contr_21["koef"] = dict_contr_21["koef"] * 2
          if dict_contr_21["step"] == 90:
             dict_contr_21["koef"] = dict_contr_21["koef"] * 2
          if dict_contr_21["step"] == 108:
             razresh_21 = False
          proig = proig - dict_contr_21["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_21
    return spisok
def chislo_22(razresh_22, key, dict_contr_22):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_22:
       if key == 2:
          win = 36 * dict_contr_22["koef"]
          razresh_22 = False
          dict_contr_22["step"] = 0
          dict_contr_22["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_22
       else:
          razresh_22 = True
          dict_contr_22["step"] = dict_contr_22["step"] + 1
          if dict_contr_22["step"] == 36:
             dict_contr_22["koef"] = dict_contr_22["koef"] * 2
          if dict_contr_22["step"] == 54:
             dict_contr_22["koef"] = dict_contr_22["koef"] * 2
          if dict_contr_22["step"] == 72:
             dict_contr_22["koef"] = dict_contr_22["koef"] * 2
          if dict_contr_22["step"] == 90:
             dict_contr_22["koef"] = dict_contr_22["koef"] * 2
          if dict_contr_22["step"] == 108:
             razresh_22 = False
          proig = proig - dict_contr_22["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_22
    return spisok
def chislo_23(razresh_23, key, dict_contr_23):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_23:
       if key == 2:
          win = 36 * dict_contr_23["koef"]
          razresh_23 = False
          dict_contr_23["step"] = 0
          dict_contr_23["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_23
       else:
          razresh_23 = True
          dict_contr_23["step"] = dict_contr_23["step"] + 1
          if dict_contr_23["step"] == 36:
             dict_contr_23["koef"] = dict_contr_23["koef"] * 2
          if dict_contr_23["step"] == 54:
             dict_contr_23["koef"] = dict_contr_23["koef"] * 2
          if dict_contr_23["step"] == 72:
             dict_contr_23["koef"] = dict_contr_23["koef"] * 2
          if dict_contr_23["step"] == 90:
             dict_contr_23["koef"] = dict_contr_23["koef"] * 2
          if dict_contr_23["step"] == 108:
             razresh_23 = False
          proig = proig - dict_contr_23["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_23
    return spisok
def chislo_24(razresh_24, key, dict_contr_24):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_24:
       if key == 2:
          win = 36 * dict_contr_24["koef"]
          razresh_24 = False
          dict_contr_24["step"] = 0
          dict_contr_24["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_24
       else:
          razresh_24 = True
          dict_contr_24["step"] = dict_contr_24["step"] + 1
          if dict_contr_24["step"] == 36:
             dict_contr_24["koef"] = dict_contr_24["koef"] * 2
          if dict_contr_24["step"] == 54:
             dict_contr_24["koef"] = dict_contr_24["koef"] * 2
          if dict_contr_24["step"] == 72:
             dict_contr_24["koef"] = dict_contr_24["koef"] * 2
          if dict_contr_24["step"] == 90:
             dict_contr_24["koef"] = dict_contr_24["koef"] * 2
          if dict_contr_24["step"] == 108:
             razresh_24 = False
          proig = proig - dict_contr_24["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_24
    return spisok
def chislo_25(razresh_25, key, dict_contr_25):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_25:
       if key == 2:
          win = 36 * dict_contr_25["koef"]
          razresh_25 = False
          dict_contr_25["step"] = 0
          dict_contr_25["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_25
       else:
          razresh_25 = True
          dict_contr_25["step"] = dict_contr_25["step"] + 1
          if dict_contr_25["step"] == 36:
             dict_contr_25["koef"] = dict_contr_25["koef"] * 2
          if dict_contr_25["step"] == 54:
             dict_contr_25["koef"] = dict_contr_25["koef"] * 2
          if dict_contr_25["step"] == 72:
             dict_contr_25["koef"] = dict_contr_25["koef"] * 2
          if dict_contr_25["step"] == 90:
             dict_contr_25["koef"] = dict_contr_25["koef"] * 2
          if dict_contr_25["step"] == 108:
             razresh_25 = False
          proig = proig - dict_contr_25["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_25
    return spisok
def chislo_26(razresh_26, key, dict_contr_26):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_26:
       if key == 2:
          win = 36 * dict_contr_26["koef"]
          razresh_26 = False
          dict_contr_26["step"] = 0
          dict_contr_26["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_26
       else:
          razresh_26 = True
          dict_contr_26["step"] = dict_contr_26["step"] + 1
          if dict_contr_26["step"] == 36:
             dict_contr_26["koef"] = dict_contr_26["koef"] * 2
          if dict_contr_26["step"] == 54:
             dict_contr_26["koef"] = dict_contr_26["koef"] * 2
          if dict_contr_26["step"] == 72:
             dict_contr_26["koef"] = dict_contr_26["koef"] * 2
          if dict_contr_26["step"] == 90:
             dict_contr_26["koef"] = dict_contr_26["koef"] * 2
          if dict_contr_26["step"] == 108:
             razresh_26 = False
          proig = proig - dict_contr_26["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_26
    return spisok
def chislo_27(razresh_27, key, dict_contr_27):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_27:
       if key == 2:
          win = 36 * dict_contr_27["koef"]
          razresh_27 = False
          dict_contr_27["step"] = 0
          dict_contr_27["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_27
       else:
          razresh_27 = True
          dict_contr_27["step"] = dict_contr_27["step"] + 1
          if dict_contr_27["step"] == 36:
             dict_contr_27["koef"] = dict_contr_27["koef"] * 2
          if dict_contr_27["step"] == 54:
             dict_contr_27["koef"] = dict_contr_27["koef"] * 2
          if dict_contr_27["step"] == 72:
             dict_contr_27["koef"] = dict_contr_27["koef"] * 2
          if dict_contr_27["step"] == 90:
             dict_contr_27["koef"] = dict_contr_27["koef"] * 2
          if dict_contr_27["step"] == 108:
             razresh_27 = False
          proig = proig - dict_contr_27["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_27
    return spisok
def chislo_28(razresh_28, key, dict_contr_28):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_28:
       if key == 2:
          win = 36 * dict_contr_28["koef"]
          razresh_28 = False
          dict_contr_28["step"] = 0
          dict_contr_28["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_28
       else:
          razresh_28 = True
          dict_contr_28["step"] = dict_contr_28["step"] + 1
          if dict_contr_28["step"] == 36:
             dict_contr_28["koef"] = dict_contr_28["koef"] * 2
          if dict_contr_28["step"] == 54:
             dict_contr_28["koef"] = dict_contr_28["koef"] * 2
          if dict_contr_28["step"] == 72:
             dict_contr_28["koef"] = dict_contr_28["koef"] * 2
          if dict_contr_28["step"] == 90:
             dict_contr_28["koef"] = dict_contr_28["koef"] * 2
          if dict_contr_28["step"] == 108:
             razresh_28 = False
          proig = proig - dict_contr_28["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_28
    return spisok
def chislo_29(razresh_29, key, dict_contr_29):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_29:
       if key == 2:
          win = 36 * dict_contr_29["koef"]
          razresh_29 = False
          dict_contr_29["step"] = 0
          dict_contr_29["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_29
       else:
          razresh_29 = True
          dict_contr_29["step"] = dict_contr_29["step"] + 1
          if dict_contr_29["step"] == 36:
             dict_contr_29["koef"] = dict_contr_29["koef"] * 2
          if dict_contr_29["step"] == 54:
             dict_contr_29["koef"] = dict_contr_29["koef"] * 2
          if dict_contr_29["step"] == 72:
             dict_contr_29["koef"] = dict_contr_29["koef"] * 2
          if dict_contr_29["step"] == 90:
             dict_contr_29["koef"] = dict_contr_29["koef"] * 2
          if dict_contr_29["step"] == 108:
             razresh_29 = False
          proig = proig - dict_contr_29["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_29
    return spisok
def chislo_30(razresh_30, key, dict_contr_30):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_30:
       if key == 2:
          win = 36 * dict_contr_30["koef"]
          razresh_30 = False
          dict_contr_30["step"] = 0
          dict_contr_30["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_30
       else:
          razresh_30 = True
          dict_contr_30["step"] = dict_contr_30["step"] + 1
          if dict_contr_30["step"] == 36:
             dict_contr_30["koef"] = dict_contr_30["koef"] * 2
          if dict_contr_30["step"] == 54:
             dict_contr_30["koef"] = dict_contr_30["koef"] * 2
          if dict_contr_30["step"] == 72:
             dict_contr_30["koef"] = dict_contr_30["koef"] * 2
          if dict_contr_30["step"] == 90:
             dict_contr_30["koef"] = dict_contr_30["koef"] * 2
          if dict_contr_30["step"] == 108:
             razresh_30 = False
          proig = proig - dict_contr_30["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_30
    return spisok
def chislo_31(razresh_31, key, dict_contr_31):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_31:
       if key == 2:
          win = 36 * dict_contr_31["koef"]
          razresh_31 = False
          dict_contr_31["step"] = 0
          dict_contr_31["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_31
       else:
          razresh_31 = True
          dict_contr_31["step"] = dict_contr_31["step"] + 1
          if dict_contr_31["step"] == 36:
             dict_contr_31["koef"] = dict_contr_31["koef"] * 2
          if dict_contr_31["step"] == 54:
             dict_contr_31["koef"] = dict_contr_31["koef"] * 2
          if dict_contr_31["step"] == 72:
             dict_contr_31["koef"] = dict_contr_31["koef"] * 2
          if dict_contr_31["step"] == 90:
             dict_contr_31["koef"] = dict_contr_31["koef"] * 2
          if dict_contr_31["step"] == 108:
             razresh_31 = False
          proig = proig - dict_contr_31["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_31
    return spisok
def chislo_32(razresh_32, key, dict_contr_32):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_32:
       if key == 2:
          win = 36 * dict_contr_32["koef"]
          razresh_32 = False
          dict_contr_32["step"] = 0
          dict_contr_32["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_32
       else:
          razresh_32 = True
          dict_contr_32["step"] = dict_contr_32["step"] + 1
          if dict_contr_32["step"] == 36:
             dict_contr_32["koef"] = dict_contr_32["koef"] * 2
          if dict_contr_32["step"] == 54:
             dict_contr_32["koef"] = dict_contr_32["koef"] * 2
          if dict_contr_32["step"] == 72:
             dict_contr_32["koef"] = dict_contr_32["koef"] * 2
          if dict_contr_32["step"] == 90:
             dict_contr_32["koef"] = dict_contr_32["koef"] * 2
          if dict_contr_32["step"] == 108:
             razresh_32 = False
          proig = proig - dict_contr_32["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_32
    return spisok
def chislo_33(razresh_33, key, dict_contr_33):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_33:
       if key == 2:
          win = 36 * dict_contr_33["koef"]
          razresh_33 = False
          dict_contr_33["step"] = 0
          dict_contr_33["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_33
       else:
          razresh_33 = True
          dict_contr_33["step"] = dict_contr_33["step"] + 1
          if dict_contr_33["step"] == 36:
             dict_contr_33["koef"] = dict_contr_33["koef"] * 2
          if dict_contr_33["step"] == 54:
             dict_contr_33["koef"] = dict_contr_33["koef"] * 2
          if dict_contr_33["step"] == 72:
             dict_contr_33["koef"] = dict_contr_33["koef"] * 2
          if dict_contr_33["step"] == 90:
             dict_contr_33["koef"] = dict_contr_33["koef"] * 2
          if dict_contr_33["step"] == 108:
             razresh_33 = False
          proig = proig - dict_contr_33["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_33
    return spisok
def chislo_34(razresh_34, key, dict_contr_34):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_34:
       if key == 2:
          win = 36 * dict_contr_34["koef"]
          razresh_34 = False
          dict_contr_34["step"] = 0
          dict_contr_34["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_34
       else:
          razresh_34 = True
          dict_contr_34["step"] = dict_contr_34["step"] + 1
          if dict_contr_34["step"] == 36:
             dict_contr_34["koef"] = dict_contr_34["koef"] * 2
          if dict_contr_34["step"] == 54:
             dict_contr_34["koef"] = dict_contr_34["koef"] * 2
          if dict_contr_34["step"] == 72:
             dict_contr_34["koef"] = dict_contr_34["koef"] * 2
          if dict_contr_34["step"] == 90:
             dict_contr_34["koef"] = dict_contr_34["koef"] * 2
          if dict_contr_34["step"] == 108:
             razresh_34 = False
          proig = proig - dict_contr_34["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_34
    return spisok
def chislo_35(razresh_35, key, dict_contr_35):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    if razresh_35:
       if key == 2:
          win = 36 * dict_contr_35["koef"]
          razresh_35 = False
          dict_contr_35["step"] = 0
          dict_contr_35["koef"] = 0.1
          spisok[0] = win
          spisok[2] = razresh_35
       else:
          razresh_35 = True
          dict_contr_35["step"] = dict_contr_35["step"] + 1
          if dict_contr_35["step"] == 36:
             dict_contr_35["koef"] = dict_contr_35["koef"] * 2
          if dict_contr_35["step"] == 54:
             dict_contr_35["koef"] = dict_contr_35["koef"] * 2
          if dict_contr_35["step"] == 72:
             dict_contr_35["koef"] = dict_contr_35["koef"] * 2
          if dict_contr_35["step"] == 90:
             dict_contr_35["koef"] = dict_contr_35["koef"] * 2
          if dict_contr_35["step"] == 108:
             razresh_35 = False
          proig = proig - dict_contr_35["koef"]
          spisok[0] = win
          spisok[1] = proig
          spisok[2] = razresh_35
    return spisok

# конец блока0
rasnica2 = 0
ik = 0
vig = 0
prg = 0
chag = 0
while (ik < 1000):
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
	
	
	
	
	Viigral = 0
	Proigral = 0
	
	index_predscazan = 0
	raznica = 0
# сюда добавить блок инисиализации лестница
	win1 = True
	razresh_1 = True
	dict_contr_1 = {"koef": 0.1, "step": 0}
	dict_tansf_1 = [0, 0, 0]
	interval_1 = 0
	win2 = True
	razresh_2 = True
	dict_contr_2 = {"koef": 0.1, "step": 0}
	dict_tansf_2 = [0, 0, 0]
	interval_2 = 0
	win3 = True
	razresh_3 = True
	dict_contr_3 = {"koef": 0.1, "step": 0}
	dict_tansf_3 = [0, 0, 0]
	interval_3 = 0
	win4 = True
	razresh_4 = True
	dict_contr_4 = {"koef": 0.1, "step": 0}
	dict_tansf_4 = [0, 0, 0]
	interval_4 = 0
	win5 = True
	razresh_5 = True
	dict_contr_5 = {"koef": 0.1, "step": 0}
	dict_tansf_5 = [0, 0, 0]
	interval_5 = 0
	win6 = True
	razresh_6 = True
	dict_contr_6 = {"koef": 0.1, "step": 0}
	dict_tansf_6 = [0, 0, 0]
	interval_6 = 0
	win7 = True
	razresh_7 = True
	dict_contr_7 = {"koef": 0.1, "step": 0}
	dict_tansf_7 = [0, 0, 0]
	interval_7 = 0
	win8 = True
	razresh_8 = True
	dict_contr_8 = {"koef": 0.1, "step": 0}
	dict_tansf_8 = [0, 0, 0]
	interval_8 = 0
	win9 = True
	razresh_9 = True
	dict_contr_9 = {"koef": 0.1, "step": 0}
	dict_tansf_9 = [0, 0, 0]
	interval_9 = 0
	win10 = True
	razresh_10 = True
	dict_contr_10 = {"koef": 0.1, "step": 0}
	dict_tansf_10 = [0, 0, 0]
	interval_10 = 0
	win11 = True
	razresh_11 = True
	dict_contr_11 = {"koef": 0.1, "step": 0}
	dict_tansf_11 = [0, 0, 0]
	interval_11 = 0
	win12 = True
	razresh_12 = True
	dict_contr_12 = {"koef": 0.1, "step": 0}
	dict_tansf_12 = [0, 0, 0]
	interval_12 = 0
	win13 = True
	razresh_13 = True
	dict_contr_13 = {"koef": 0.1, "step": 0}
	dict_tansf_13 = [0, 0, 0]
	interval_13 = 0
	win14 = True
	razresh_14 = True
	dict_contr_14 = {"koef": 0.1, "step": 0}
	dict_tansf_14 = [0, 0, 0]
	interval_14 = 0
	win15 = True
	razresh_15 = True
	dict_contr_15 = {"koef": 0.1, "step": 0}
	dict_tansf_15 = [0, 0, 0]
	interval_15 = 0
	win16 = True
	razresh_16 = True
	dict_contr_16 = {"koef": 0.1, "step": 0}
	dict_tansf_16 = [0, 0, 0]
	interval_16 = 0
	win17 = True
	razresh_17 = True
	dict_contr_17 = {"koef": 0.1, "step": 0}
	dict_tansf_17 = [0, 0, 0]
	interval_17 = 0
	win18 = True
	razresh_18 = True
	dict_contr_18 = {"koef": 0.1, "step": 0}
	dict_tansf_18 = [0, 0, 0]
	interval_18 = 0
	win19 = True
	razresh_19 = True
	dict_contr_19 = {"koef": 0.1, "step": 0}
	dict_tansf_19 = [0, 0, 0]
	interval_19 = 0
	win20 = True
	razresh_20 = True
	dict_contr_20 = {"koef": 0.1, "step": 0}
	dict_tansf_20 = [0, 0, 0]
	interval_20 = 0
	win21 = True
	razresh_21 = True
	dict_contr_21 = {"koef": 0.1, "step": 0}
	dict_tansf_21 = [0, 0, 0]
	interval_21 = 0
	win22 = True
	razresh_22 = True
	dict_contr_22 = {"koef": 0.1, "step": 0}
	dict_tansf_22 = [0, 0, 0]
	interval_22 = 0
	win23 = True
	razresh_23 = True
	dict_contr_23 = {"koef": 0.1, "step": 0}
	dict_tansf_23 = [0, 0, 0]
	interval_23 = 0
	win24 = True
	razresh_24 = True
	dict_contr_24 = {"koef": 0.1, "step": 0}
	dict_tansf_24 = [0, 0, 0]
	interval_24 = 0
	win25 = True
	razresh_25 = True
	dict_contr_25 = {"koef": 0.1, "step": 0}
	dict_tansf_25 = [0, 0, 0]
	interval_25 = 0
	win26 = True
	razresh_26 = True
	dict_contr_26 = {"koef": 0.1, "step": 0}
	dict_tansf_26 = [0, 0, 0]
	interval_26 = 0
	win27 = True
	razresh_27 = True
	dict_contr_27 = {"koef": 0.1, "step": 0}
	dict_tansf_27 = [0, 0, 0]
	interval_27 = 0
	win28 = True
	razresh_28 = True
	dict_contr_28 = {"koef": 0.1, "step": 0}
	dict_tansf_28 = [0, 0, 0]
	interval_28 = 0
	win29 = True
	razresh_29 = True
	dict_contr_29 = {"koef": 0.1, "step": 0}
	dict_tansf_29 = [0, 0, 0]
	interval_29 = 0
	win30 = True
	razresh_30 = True
	dict_contr_30 = {"koef": 0.1, "step": 0}
	dict_tansf_30 = [0, 0, 0]
	interval_30 = 0
	win31 = True
	razresh_31 = True
	dict_contr_31 = {"koef": 0.1, "step": 0}
	dict_tansf_31 = [0, 0, 0]
	interval_31 = 0
	win32 = True
	razresh_32 = True
	dict_contr_32 = {"koef": 0.1, "step": 0}
	dict_tansf_32 = [0, 0, 0]
	interval_32 = 0
	win33 = True
	razresh_33 = True
	dict_contr_33 = {"koef": 0.1, "step": 0}
	dict_tansf_33 = [0, 0, 0]
	interval_33 = 0
	win34 = True
	razresh_34 = True
	dict_contr_34 = {"koef": 0.1, "step": 0}
	dict_tansf_34 = [0, 0, 0]
	interval_34 = 0
	win35 = True
	razresh_35 = True
	dict_contr_35 = {"koef": 0.1, "step": 0}
	dict_tansf_35 = [0, 0, 0]
	interval_35 = 0
# конец блока инисиализации лестница
	while (steps < len(viborka)):
		key = viborka[steps]
		key1 = key
		steps = steps + 1
		if steps == 1:
			# сюда добавить блок тела1 лестница1
			dob_next_seen_1(dic_ed, 1, steps)
			dob_next_seen_1(dic_ed, 2, steps)
			dob_next_seen_1(dic_ed, 3, steps)
			dob_next_seen_1(dic_ed, 4, steps)
			dob_next_seen_1(dic_ed, 5, steps)
			dob_next_seen_1(dic_ed, 6, steps)
			dob_next_seen_1(dic_ed, 7, steps)
			dob_next_seen_1(dic_ed, 8, steps)
			dob_next_seen_1(dic_ed, 9, steps)
			dob_next_seen_1(dic_ed, 10, steps)
			dob_next_seen_1(dic_ed, 11, steps)
			dob_next_seen_1(dic_ed, 12, steps)
			dob_next_seen_1(dic_ed, 13, steps)
			dob_next_seen_1(dic_ed, 14, steps)
			dob_next_seen_1(dic_ed, 15, steps)
			dob_next_seen_1(dic_ed, 16, steps)
			dob_next_seen_1(dic_ed, 17, steps)
			dob_next_seen_1(dic_ed, 18, steps)
			dob_next_seen_1(dic_ed, 19, steps)
			dob_next_seen_1(dic_ed, 20, steps)
			dob_next_seen_1(dic_ed, 21, steps)
			dob_next_seen_1(dic_ed, 22, steps)
			dob_next_seen_1(dic_ed, 23, steps)
			dob_next_seen_1(dic_ed, 24, steps)
			dob_next_seen_1(dic_ed, 25, steps)
			dob_next_seen_1(dic_ed, 26, steps)
			dob_next_seen_1(dic_ed, 27, steps)
			dob_next_seen_1(dic_ed, 28, steps)
			dob_next_seen_1(dic_ed, 29, steps)
			dob_next_seen_1(dic_ed, 30, steps)
			dob_next_seen_1(dic_ed, 31, steps)
			dob_next_seen_1(dic_ed, 32, steps)
			dob_next_seen_1(dic_ed, 33, steps)
			dob_next_seen_1(dic_ed, 34, steps)
			dob_next_seen_1(dic_ed, 35, steps)
		    # конец блок тела1 лестница1
		dob_next_seen_1(dic_ed, key, steps)  # создание\ обновление словаря едениц
		# добавление шагов всем еденицам
		# проверочный - dictEd = {(36): [23, [1, 2], 33]}
		
		# сюда добавить блок тела2 лестница2
		if interval_1 < 120:
			if razresh_1:
				dict_tansf_1 = chislo_1(razresh_1, key, dict_contr_1)
				Viigral = Viigral + dict_tansf_1[0]
				Proigral = Proigral + dict_tansf_1[1]
				razresh_1 = dict_tansf_1[2]
		if interval_2 < 120:
			if razresh_2:
				dict_tansf_2 = chislo_2(razresh_2, key, dict_contr_2)
				Viigral = Viigral + dict_tansf_2[0]
				Proigral = Proigral + dict_tansf_2[1]
				razresh_2 = dict_tansf_2[2]
		if interval_3 < 120:
			if razresh_3:
				dict_tansf_3 = chislo_3(razresh_3, key, dict_contr_3)
				Viigral = Viigral + dict_tansf_3[0]
				Proigral = Proigral + dict_tansf_3[1]
				razresh_3 = dict_tansf_3[2]
		if interval_4 < 120:
			if razresh_4:
				dict_tansf_4 = chislo_4(razresh_4, key, dict_contr_4)
				Viigral = Viigral + dict_tansf_4[0]
				Proigral = Proigral + dict_tansf_4[1]
				razresh_4 = dict_tansf_4[2]
		if interval_5 < 120:
			if razresh_5:
				dict_tansf_5 = chislo_5(razresh_5, key, dict_contr_5)
				Viigral = Viigral + dict_tansf_5[0]
				Proigral = Proigral + dict_tansf_5[1]
				razresh_5 = dict_tansf_5[2]
		if interval_6 < 120:
			if razresh_6:
				dict_tansf_6 = chislo_6(razresh_6, key, dict_contr_6)
				Viigral = Viigral + dict_tansf_6[0]
				Proigral = Proigral + dict_tansf_6[1]
				razresh_6 = dict_tansf_6[2]
		if interval_7 < 120:
			if razresh_7:
				dict_tansf_7 = chislo_7(razresh_7, key, dict_contr_7)
				Viigral = Viigral + dict_tansf_7[0]
				Proigral = Proigral + dict_tansf_7[1]
				razresh_7 = dict_tansf_7[2]
		if interval_8 < 120:
			if razresh_8:
				dict_tansf_8 = chislo_8(razresh_8, key, dict_contr_8)
				Viigral = Viigral + dict_tansf_8[0]
				Proigral = Proigral + dict_tansf_8[1]
				razresh_8 = dict_tansf_8[2]
		if interval_9 < 120:
			if razresh_9:
				dict_tansf_9 = chislo_9(razresh_9, key, dict_contr_9)
				Viigral = Viigral + dict_tansf_9[0]
				Proigral = Proigral + dict_tansf_9[1]
				razresh_9 = dict_tansf_9[2]
		if interval_10 < 120:
			if razresh_10:
				dict_tansf_10 = chislo_10(razresh_10, key, dict_contr_10)
				Viigral = Viigral + dict_tansf_10[0]
				Proigral = Proigral + dict_tansf_10[1]
				razresh_10 = dict_tansf_10[2]
		if interval_11 < 120:
			if razresh_11:
				dict_tansf_11 = chislo_11(razresh_11, key, dict_contr_11)
				Viigral = Viigral + dict_tansf_11[0]
				Proigral = Proigral + dict_tansf_11[1]
				razresh_11 = dict_tansf_11[2]
		if interval_12 < 120:
			if razresh_12:
				dict_tansf_12 = chislo_12(razresh_12, key, dict_contr_12)
				Viigral = Viigral + dict_tansf_12[0]
				Proigral = Proigral + dict_tansf_12[1]
				razresh_12 = dict_tansf_12[2]
		if interval_13 < 120:
			if razresh_13:
				dict_tansf_13 = chislo_13(razresh_13, key, dict_contr_13)
				Viigral = Viigral + dict_tansf_13[0]
				Proigral = Proigral + dict_tansf_13[1]
				razresh_13 = dict_tansf_13[2]
		if interval_14 < 120:
			if razresh_14:
				dict_tansf_14 = chislo_14(razresh_14, key, dict_contr_14)
				Viigral = Viigral + dict_tansf_14[0]
				Proigral = Proigral + dict_tansf_14[1]
				razresh_14 = dict_tansf_14[2]
		if interval_15 < 120:
			if razresh_15:
				dict_tansf_15 = chislo_15(razresh_15, key, dict_contr_15)
				Viigral = Viigral + dict_tansf_15[0]
				Proigral = Proigral + dict_tansf_15[1]
				razresh_15 = dict_tansf_15[2]
		if interval_16 < 120:
			if razresh_16:
				dict_tansf_16 = chislo_16(razresh_16, key, dict_contr_16)
				Viigral = Viigral + dict_tansf_16[0]
				Proigral = Proigral + dict_tansf_16[1]
				razresh_16 = dict_tansf_16[2]
		if interval_17 < 120:
			if razresh_17:
				dict_tansf_17 = chislo_17(razresh_17, key, dict_contr_17)
				Viigral = Viigral + dict_tansf_17[0]
				Proigral = Proigral + dict_tansf_17[1]
				razresh_17 = dict_tansf_17[2]
		if interval_18 < 120:
			if razresh_18:
				dict_tansf_18 = chislo_18(razresh_18, key, dict_contr_18)
				Viigral = Viigral + dict_tansf_18[0]
				Proigral = Proigral + dict_tansf_18[1]
				razresh_18 = dict_tansf_18[2]
		if interval_19 < 120:
			if razresh_19:
				dict_tansf_19 = chislo_19(razresh_19, key, dict_contr_19)
				Viigral = Viigral + dict_tansf_19[0]
				Proigral = Proigral + dict_tansf_19[1]
				razresh_19 = dict_tansf_19[2]
		if interval_20 < 120:
			if razresh_20:
				dict_tansf_20 = chislo_20(razresh_20, key, dict_contr_20)
				Viigral = Viigral + dict_tansf_20[0]
				Proigral = Proigral + dict_tansf_20[1]
				razresh_20 = dict_tansf_20[2]
		if interval_21 < 120:
			if razresh_21:
				dict_tansf_21 = chislo_21(razresh_21, key, dict_contr_21)
				Viigral = Viigral + dict_tansf_21[0]
				Proigral = Proigral + dict_tansf_21[1]
				razresh_21 = dict_tansf_21[2]
		if interval_22 < 120:
			if razresh_22:
				dict_tansf_22 = chislo_22(razresh_22, key, dict_contr_22)
				Viigral = Viigral + dict_tansf_22[0]
				Proigral = Proigral + dict_tansf_22[1]
				razresh_22 = dict_tansf_22[2]
		if interval_23 < 120:
			if razresh_23:
				dict_tansf_23 = chislo_23(razresh_23, key, dict_contr_23)
				Viigral = Viigral + dict_tansf_23[0]
				Proigral = Proigral + dict_tansf_23[1]
				razresh_23 = dict_tansf_23[2]
		if interval_24 < 120:
			if razresh_24:
				dict_tansf_24 = chislo_24(razresh_24, key, dict_contr_24)
				Viigral = Viigral + dict_tansf_24[0]
				Proigral = Proigral + dict_tansf_24[1]
				razresh_24 = dict_tansf_24[2]
		if interval_25 < 120:
			if razresh_25:
				dict_tansf_25 = chislo_25(razresh_25, key, dict_contr_25)
				Viigral = Viigral + dict_tansf_25[0]
				Proigral = Proigral + dict_tansf_25[1]
				razresh_25 = dict_tansf_25[2]
		if interval_26 < 120:
			if razresh_26:
				dict_tansf_26 = chislo_26(razresh_26, key, dict_contr_26)
				Viigral = Viigral + dict_tansf_26[0]
				Proigral = Proigral + dict_tansf_26[1]
				razresh_26 = dict_tansf_26[2]
		if interval_27 < 120:
			if razresh_27:
				dict_tansf_27 = chislo_27(razresh_27, key, dict_contr_27)
				Viigral = Viigral + dict_tansf_27[0]
				Proigral = Proigral + dict_tansf_27[1]
				razresh_27 = dict_tansf_27[2]
		if interval_28 < 120:
			if razresh_28:
				dict_tansf_28 = chislo_28(razresh_28, key, dict_contr_28)
				Viigral = Viigral + dict_tansf_28[0]
				Proigral = Proigral + dict_tansf_28[1]
				razresh_28 = dict_tansf_28[2]
		if interval_29 < 120:
			if razresh_29:
				dict_tansf_29 = chislo_29(razresh_29, key, dict_contr_29)
				Viigral = Viigral + dict_tansf_29[0]
				Proigral = Proigral + dict_tansf_29[1]
				razresh_29 = dict_tansf_29[2]
		if interval_30 < 120:
			if razresh_30:
				dict_tansf_30 = chislo_30(razresh_30, key, dict_contr_30)
				Viigral = Viigral + dict_tansf_30[0]
				Proigral = Proigral + dict_tansf_30[1]
				razresh_30 = dict_tansf_30[2]
		if interval_31 < 120:
			if razresh_31:
				dict_tansf_31 = chislo_31(razresh_31, key, dict_contr_31)
				Viigral = Viigral + dict_tansf_31[0]
				Proigral = Proigral + dict_tansf_31[1]
				razresh_31 = dict_tansf_31[2]
		if interval_32 < 120:
			if razresh_32:
				dict_tansf_32 = chislo_32(razresh_32, key, dict_contr_32)
				Viigral = Viigral + dict_tansf_32[0]
				Proigral = Proigral + dict_tansf_32[1]
				razresh_32 = dict_tansf_32[2]
		if interval_33 < 120:
			if razresh_33:
				dict_tansf_33 = chislo_33(razresh_33, key, dict_contr_33)
				Viigral = Viigral + dict_tansf_33[0]
				Proigral = Proigral + dict_tansf_33[1]
				razresh_33 = dict_tansf_33[2]
		if interval_34 < 120:
			if razresh_34:
				dict_tansf_34 = chislo_34(razresh_34, key, dict_contr_34)
				Viigral = Viigral + dict_tansf_34[0]
				Proigral = Proigral + dict_tansf_34[1]
				razresh_34 = dict_tansf_34[2]
		if interval_35 < 120:
			if razresh_35:
				dict_tansf_35 = chislo_35(razresh_35, key, dict_contr_35)
				Viigral = Viigral + dict_tansf_35[0]
				Proigral = Proigral + dict_tansf_35[1]
				razresh_35 = dict_tansf_35[2]
		# конец блока тела2 лестница2
		# начало блока тела3 лестница3
		if (not razresh_1) and (not razresh_2) and (not razresh_3) and (not razresh_4) and (not razresh_5) and \
		(not razresh_6) and (not razresh_7) and (not razresh_8) and (not razresh_9) and (not razresh_10) and \
		(not razresh_11) and (not razresh_12) and (not razresh_13) and (not razresh_14) and (not razresh_15) and \
		(not razresh_16) and (not razresh_17) and (not razresh_18) and (not razresh_19) and (not razresh_20) and \
		(not razresh_21) and (not razresh_22) and (not razresh_23) and (not razresh_24) and (not razresh_25) and \
		(not razresh_26) and (not razresh_27) and (not razresh_28) and (not razresh_29) and (not razresh_30) and \
		(not razresh_31) and (not razresh_32) and (not razresh_33) and (not razresh_34) and (not razresh_35) :
		# конец блока тела3 лестница3
		# начало блока тела4 лестница4
			razresh_1 = True
			razresh_2 = True
			razresh_3 = True
			razresh_4 = True
			razresh_5 = True
			razresh_6 = True
			razresh_7 = True
			razresh_8 = True
			razresh_9 = True
			razresh_10 = True
			razresh_11 = True
			razresh_12 = True
			razresh_13 = True
			razresh_14 = True
			razresh_15 = True
			razresh_16 = True
			razresh_17 = True
			razresh_18 = True
			razresh_19 = True
			razresh_20 = True
			razresh_21 = True
			razresh_22 = True
			razresh_23 = True
			razresh_24 = True
			razresh_25 = True
			razresh_26 = True
			razresh_27 = True
			razresh_28 = True
			razresh_29 = True
			razresh_30 = True
			razresh_31 = True
			razresh_32 = True
			razresh_33 = True
			razresh_34 = True
			razresh_35 = True
		# конец блока тела4 лестница4
		rasnica = Viigral + Proigral
		print('Разница:', rasnica)
		# начало блока тела5 лестница5
		interval_1 = key01step1(1, dic_ed)
		interval_2 = key01step1(2, dic_ed)
		interval_3 = key01step1(3, dic_ed)
		interval_4 = key01step1(4, dic_ed)
		interval_5 = key01step1(5, dic_ed)
		interval_6 = key01step1(6, dic_ed)
		interval_7 = key01step1(7, dic_ed)
		interval_8 = key01step1(8, dic_ed)
		interval_9 = key01step1(9, dic_ed)
		interval_10 = key01step1(10, dic_ed)
		interval_11 = key01step1(11, dic_ed)
		interval_12 = key01step1(12, dic_ed)
		interval_13 = key01step1(13, dic_ed)
		interval_14 = key01step1(14, dic_ed)
		interval_15 = key01step1(15, dic_ed)
		interval_16 = key01step1(16, dic_ed)
		interval_17 = key01step1(17, dic_ed)
		interval_18 = key01step1(18, dic_ed)
		interval_19 = key01step1(19, dic_ed)
		interval_20 = key01step1(20, dic_ed)
		interval_21 = key01step1(21, dic_ed)
		interval_22 = key01step1(22, dic_ed)
		interval_23 = key01step1(23, dic_ed)
		interval_24 = key01step1(24, dic_ed)
		interval_25 = key01step1(25, dic_ed)
		interval_26 = key01step1(26, dic_ed)
		interval_27 = key01step1(27, dic_ed)
		interval_28 = key01step1(28, dic_ed)
		interval_29 = key01step1(29, dic_ed)
		interval_30 = key01step1(30, dic_ed)
		interval_31 = key01step1(31, dic_ed)
		interval_32 = key01step1(32, dic_ed)
		interval_33 = key01step1(33, dic_ed)
		interval_34 = key01step1(34, dic_ed)
		interval_35 = key01step1(35, dic_ed)
		# конец блока тела5 лестница5
		interval = key01step(key1, dic_ed)  # последний интервал выпавшего числа
		add_step_to_all_1(dic_ed)
		# if rasnica > 80:
		# 	break
		# if rasnica < -4:
		# 	break
	
	# print('количество рзных символов',int_count )
	# print('количество шагов биг',steps_big )
	print('Выиграл:', Viigral)
	print('Проиграл:', Proigral)
	vig = vig + Viigral
	prg = prg + Proigral
	rasnica2 = vig + prg
	if rasnica2> 40:
	    break
	if rasnica2< - 40:
	    break
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

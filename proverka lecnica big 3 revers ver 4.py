import json
import random
import math


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
def postrocno(spisok, name):
	i = 0
	for item in spisok:
		i = i + 1
		print(steps, name, 'стока', i, item)


def stepsbig(interval, porog, steps_big):
	steps_big
	if interval < porog:
		steps_big = steps_big + 1
	return steps_big


def podchet_interv_odd(slovar):
	obshie = 0
	rezult = 0
	for item in slovar:
		if (slovar[item][3] % 2) != 0:
			if (slovar[item][0]) > 180:
				rezult = obshie + slovar[item][0]
	
	return rezult


def podchet_interv_iven(slovar):
	obshie = 0
	rezult = 0
	for item in slovar:
		if (slovar[item][3] % 2) == 0:
			if (slovar[item][0]) > 180:
				rezult = obshie + slovar[item][0]
	return rezult


def podchet_count_odd(slovar):
	obshie = []
	rezult = 0
	for item in slovar:
		if (slovar[item][3] % 2) != 0:
			if (slovar[item][0]) < 10:
				obshie.append(slovar[item][3])
				rezult = len(obshie)
	return rezult


def podchet_count_iven(slovar):
	obshie = []
	rezult = 0
	for item in slovar:
		if (slovar[item][3] % 2) == 0:
			if (slovar[item][0]) < 10:
				obshie.append(slovar[item][3])
				rezult = len(obshie)
	return rezult


def nahogd_big_interv(slovar):
	rezult = 0
	big = 0
	for item in slovar:
		
		if (slovar[item][0]) > big:
			rezult = slovar[item][3]
			slovar[item][0] = big
	return rezult


spisok_minus_balansov = []
rasnica2 = 0
ik = 0
vig = 0
prg = 0
chag = 0
itog = 0
i = 0
for i in range(222, 922):
	# while (ik < 100):
	ik = ik + 1
	# naime_file = '400cikl_ochh.txt'
	# naime_file = 'cikly2/'+str(i) + 'cikl_ochh.txt'
	# file_obj = open(naime_file, 'w')
	# file_obj.close()
	# file_obj = open(naime_file, 'a')
	# for i in range(200):
	#     chislo = random.randint(0, 36)  # генерируем число
	#     file_obj.write(str(chislo) + '\n')
	#
	# file_obj.close()
	
	# naime_file = '148cikl_och.txt'
	# naime_file = 'cikly2/'+str(i) + 'cikl_ochh.txt'
	naime_file = str(i) + 'cikl_och.txt'
	# naime_file = 'cikly2/196cikl_ochh.txt'
	viborka = []
	file_obj = open(naime_file)
	data_list = file_obj.readlines()
	for line in data_list:
		viborka.append(int(line))
	# объявление всех переменных-----------------------------------------------------------------------------------
	dic_ed = {}  # болванка под словарь едениц
	# -----------------------------------------------------------------------------------
	dict_interv_of2 = {}  # болванка под словарь интервалов 2-ек
	dict_interv_of3 = {}  # болванка под словарь интервалов 3-ек
	key = 0
	steps_sesia = 1
	key1 = key
	steps = 0
	steps_big = 0
	key3step = 0
	key2step = 0
	listAll_inter = []  # болванка под список всех интервалов
	log = True
	spisok_vnesh = [0]
	spisok_vnesh2 = [1]
	win = ''
	win1 = True
	win2 = True
	win3 = True
	Viigral = 0
	Proigral = 0
	change = True
	index_predscazan = 0
	good_pred = []
	bad_pred = []
	iven_or_odd = 0
	all_odd = 0
	all_even = 0
	pribyl = 0
	ubyl = 0
	step_of_lecnicu = 0
	my_razmer_stavki = 0.16
	razmer_stavki = 0.20
	promegutocnuy_balans = 0
	balans = 0
	samyy_maly = 0
	samyy_maly_step = 0
	samyy_big_stavka = 0
	samyy_big_stavka_step = 0
	samyy_samyy_big_stavka = 0
	raznica = 0
	pribavka = 0
	step_to_start = 1
	while (steps < len(viborka)):
		key = viborka[steps]
		key1 = key
		steps = steps + 1
		raznica = all_odd - all_even
		if raznica < 0:
			pribavka = math.fabs(raznica)
		# print('raznica',raznica)
		if key == 0:
			# print('pered pribylu - razmer stavki: ',razmer_stavki, 'razmer step_to_start', step_to_start)
			if step_to_start > 1:
				step_to_start = step_to_start - 1
			pribyl = pribyl + my_razmer_stavki * step_to_start
			if step_to_start > 1:
				razmer_stavki = razmer_stavki + 0.20
			step_to_start = step_to_start + 1
			# my_razmer_stavki=my_razmer_stavki+raznica
			# razmer_stavki = razmer_stavki + 1 + pribavka
			step_of_lecnicu = step_of_lecnicu - 1
			# if step_of_lecnicu>80:
			#     razmer_stavki = razmer_stavki * my_razmer_stavki
			all_even = all_even + 1
		elif key == 35:
			# print('pered pribylu - razmer stavki: ',razmer_stavki, 'razmer step_to_start', step_to_start)
			if step_to_start > 1:
				step_to_start = step_to_start - 1
			pribyl = pribyl + my_razmer_stavki * step_to_start
			if step_to_start > 1:
				razmer_stavki = razmer_stavki + 0.20
			step_to_start = step_to_start + 1
			# my_razmer_stavki=my_razmer_stavki+raznica
			# razmer_stavki = razmer_stavki + 1 + pribavka
			step_of_lecnicu = step_of_lecnicu - 1
			# if step_of_lecnicu>80:
			#     razmer_stavki = razmer_stavki * my_razmer_stavki
			all_even = all_even + 1
		# elif key == 1:
		# 	# print('pered pribylu - razmer stavki: ',razmer_stavki, 'razmer step_to_start', step_to_start)
		# 	if step_to_start > 1:
		# 		step_to_start = step_to_start - 1
		# 	pribyl = pribyl + my_razmer_stavki * step_to_start
		# 	if step_to_start > 1:
		# 		razmer_stavki = razmer_stavki + 0.20
		# 	step_to_start = step_to_start + 1
		# 	# my_razmer_stavki=my_razmer_stavki+raznica
		# 	# razmer_stavki = razmer_stavki + 1 + pribavka
		# 	step_of_lecnicu = step_of_lecnicu - 1
		# 	# if step_of_lecnicu>80:
		# 	#     razmer_stavki = razmer_stavki * my_razmer_stavki
		# 	all_even = all_even + 1
		# elif key == 19:
		# 	# print('pered pribylu - razmer stavki: ',razmer_stavki, 'razmer step_to_start', step_to_start)
		# 	if step_to_start > 1:
		# 		step_to_start = step_to_start - 1
		# 	pribyl = pribyl + my_razmer_stavki * step_to_start
		# 	if step_to_start > 1:
		# 		razmer_stavki = razmer_stavki + 0.20
		# 	step_to_start = step_to_start + 1
		# 	# my_razmer_stavki=my_razmer_stavki+raznica
		# 	# razmer_stavki = razmer_stavki + 1 + pribavka
		# 	step_of_lecnicu = step_of_lecnicu - 1
		# 	# if step_of_lecnicu>80:
		# 	#     razmer_stavki = razmer_stavki * my_razmer_stavki
		# 	all_even = all_even + 1
		
		elif  (key == 1) or (key == 3) or (key == 5) or (key == 7) or (key == 9) or (key == 11)or (key == 13)\
				or (key == 15) or (key == 17) or(key == 19) or (key == 21)or (key == 23) or (key == 25)\
				or (key == 27) or (key == 29) or (key == 31)or (key == 33):
			# print('pered ubuly - razmer stavki: ', razmer_stavki, 'razmer step_to_start', step_to_start)
			ubyl = ubyl + razmer_stavki
			razmer_stavki = 0.20
			step_to_start = 1
			# if promegutocnuy_balans< -1:
			#     razmer_stavki =2
			# if promegutocnuy_balans< -2:
			#     razmer_stavki =3
			# if promegutocnuy_balans< -3:
			#     razmer_stavki =4
			# if promegutocnuy_balans< -4:
			#     razmer_stavki =4
			# if promegutocnuy_balans < -5:
			#     razmer_stavki = 6
			# if promegutocnuy_balans < -6:
			#     razmer_stavki = 7
			# if promegutocnuy_balans < -7:
			#     razmer_stavki = 8
			# if promegutocnuy_balans < -8:
			#     razmer_stavki = 9
			# if promegutocnuy_balans< -9:
			#     razmer_stavki =10
			# if promegutocnuy_balans< -10:
			#     razmer_stavki =11
			# if promegutocnuy_balans< -11:
			#     razmer_stavki =12
			# if promegutocnuy_balans< -12:
			#     razmer_stavki =13
			# if promegutocnuy_balans < -13:
			#     razmer_stavki = 14
			# if promegutocnuy_balans < -14:
			#     razmer_stavki = 15
			# if promegutocnuy_balans < -15:
			#     razmer_stavki = 16
			# if promegutocnuy_balans < -16:
			#     razmer_stavki = 17
			# if promegutocnuy_balans < -17:
			#     razmer_stavki = 18
			# if promegutocnuy_balans < -18:
			#     razmer_stavki = 19
			# if promegutocnuy_balans < -19:
			#     razmer_stavki = 20
			# if promegutocnuy_balans < -20:
			#     razmer_stavki = 21
			# if promegutocnuy_balans < -21:
			#     razmer_stavki = 22
			# if promegutocnuy_balans < -22:
			#     razmer_stavki = 23
			# if promegutocnuy_balans < -23:
			#     razmer_stavki = 24
			# if promegutocnuy_balans < -24:
			#     razmer_stavki = 25
			# if promegutocnuy_balans < -25:
			#     razmer_stavki = 26
			# if promegutocnuy_balans < -26:
			#     razmer_stavki = 27
			# if promegutocnuy_balans < -27:
			#     razmer_stavki = 28
			# if promegutocnuy_balans < -28:
			#     razmer_stavki = 29
			# if promegutocnuy_balans < -29:
			#     razmer_stavki = 30
			# if promegutocnuy_balans < -30:
			#     razmer_stavki = 31
			# if promegutocnuy_balans < -31:
			#     razmer_stavki = 32
			# if promegutocnuy_balans < -32:
			#     razmer_stavki = 33
			# if promegutocnuy_balans < -33:
			#     razmer_stavki = 34
			
			# step_to_start = 1
			# my_razmer_stavki = my_razmer_stavki + 1+pribavka
			# step_of_lecnicu = step_of_lecnicu + 1
			all_odd = all_odd + 1
		elif (key % 2 == 0) and (key != 0):
			# print('pered pribylu - razmer stavki: ', razmer_stavki, 'razmer step_to_start', step_to_start)
			if step_to_start > 1:
				step_to_start = step_to_start - 1
			pribyl = pribyl + my_razmer_stavki * step_to_start
			if step_to_start > 1:
				razmer_stavki = razmer_stavki + 0.20
			step_to_start = step_to_start + 1
			# my_razmer_stavki=my_razmer_stavki+raznica
			# razmer_stavki = razmer_stavki + 1 + pribavka
			step_of_lecnicu = step_of_lecnicu - 1
			# if step_of_lecnicu>80:
			#     razmer_stavki = razmer_stavki * my_razmer_stavki
			all_even = all_even + 1
		promegutocnuy_balans = pribyl - ubyl
		# print(steps, ' ubyl:', ubyl)
		print(steps, ' promegutocnuy_balans:', round(promegutocnuy_balans, 2))
		
		if samyy_maly > promegutocnuy_balans:
			samyy_maly = promegutocnuy_balans
			samyy_maly_step = steps
		
		# if promegutocnuy_balans > 2:
		# 	break
		# if promegutocnuy_balans < -5.1:
		# 	break
		# if promegutocnuy_balans > 0:
		#     balans = balans + promegutocnuy_balans
		#     # promegutocnuy_balans = 0
		#     step_of_lecnicu = 0
		#     # razmer_stavki = 1
		#     ubyl = 0
		#     pribyl =0
		# print(steps, ' promegutocnuy_balans:', promegutocnuy_balans)
		if samyy_big_stavka < razmer_stavki:
			samyy_big_stavka = razmer_stavki
			samyy_big_stavka_step = steps
		# print('    razmer stavki:', razmer_stavki)
	print('')
	print('--------------------------------------------------------------------------------------------------------')
	itog_cikla = balans + promegutocnuy_balans
	print('Balans:', balans + promegutocnuy_balans)
	print(' all_odd', all_odd)
	print(' all_even', all_even)
	print(' разница между odd and even', all_odd - all_even)
	print('samyy_maly_step', samyy_maly_step)
	print('samyy_big_stavka_step', samyy_big_stavka_step, 'stavka: ', samyy_big_stavka)
	itog = itog + itog_cikla
	if samyy_samyy_big_stavka < samyy_big_stavka:
		samyy_samyy_big_stavka = samyy_big_stavka
	if promegutocnuy_balans < 0:
		spisok_minus_balansov.append(naime_file)
		spisok_minus_balansov.append(round(promegutocnuy_balans, 2))
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
i = 0
for i in range(len(spisok_minus_balansov)):
	if (i % 2) == 0:
		print(spisok_minus_balansov[i], ': ', spisok_minus_balansov[i + 1])
print('---------------------------------itog', itog, 'samyy big stavka: ', samyy_big_stavka)
# print('общтй итог:',rasnica2)

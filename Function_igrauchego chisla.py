
for i in range(2):
	chis=str(i)
	
	
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
for i in range(2):
	chis=str(i)
	if interval_+'chis' < 120:
		
		if razresh_chis:
			dict_tansf_1 = chislo_chis(razresh_1, key, dict_contr_chis)
			Viigral = Viigral + dict_tansf_chis[0]
			Proigral = Proigral + dict_tansf_chis[1]
			razresh_chis = dict_tansf_chis[2]

def chislo_04(razresh_04, key, dict_contr_04,msg):
	win = 0
	proig = 0
	spisok = [0, 0, True]
	result = []
	if razresh_04:
		if key == 2:
			win = 36 * dict_contr_04["koef"]
			razresh_04 = False
			dict_contr_04["step"] = 0
			dict_contr_04["koef"] = 0.1
			spisok[0] = win
			spisok[2] = razresh_04
		else:
			razresh_04 = True
			dict_contr_04["step"] = dict_contr_04["step"] + 1
			if dict_contr_04["step"] == 36:
				dict_contr_04["koef"] = dict_contr_04["koef"] * 2
			
			if dict_contr_04["step"] == 54:
				dict_contr_04["koef"] = dict_contr_04["koef"] * 2
			if dict_contr_04["step"] == 72:
				dict_contr_04["koef"] = dict_contr_04["koef"] * 2
			if dict_contr_04["step"] == 90:
				dict_contr_04["koef"] = dict_contr_04["koef"] * 2
			if dict_contr_04["step"] == 108:
				razresh_04 = False
			proig = proig - dict_contr_04["koef"]
			spisok[0] = win
			spisok[1] = proig
			spisok[2] = razresh_04
	return spisok

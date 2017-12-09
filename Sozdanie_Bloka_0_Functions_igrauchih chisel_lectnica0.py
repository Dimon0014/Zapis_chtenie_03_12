
for i in range(1,36):
    #chis=str(i)
    
    
    print('def chislo_'+str(i)+'(razresh_'+str(i)+', key, dict_contr_'+str(i)+'):')
    print('    win = 0 ')
    print('    proig = 0 ')
    print('    spisok = [0, 0, True]  ')
    print('    if razresh_'+str(i)+':  ')
    print('       if key == 2:  ')
    print('          win = 36 * dict_contr_'+str(i)+'["koef"]  ')
    print('          razresh_'+str(i)+' = False  ')
    print('          dict_contr_'+str(i)+'["step"] = 0  ')
    print('          dict_contr_'+str(i)+'["koef"] = 0.1  ')
    print('          spisok[0] = win  ')
    print('          spisok[2] = razresh_'+str(i)+'  ')
    print('       else:  ')
    print('          razresh_'+str(i)+' = True  ')
    print('          dict_contr_'+str(i)+'["step"] = dict_contr_'+str(i)+'["step"] + 1  ')
    print('          if dict_contr_'+str(i)+'["step"] == 36:  ')
    print('             dict_contr_'+str(i)+'["koef"] = dict_contr_'+str(i)+'["koef"] * 2  ')
    print('          if dict_contr_'+str(i)+'["step"] == 54:  ')
    print('             dict_contr_'+str(i)+'["koef"] = dict_contr_'+str(i)+'["koef"] * 2  ')
    print('          if dict_contr_'+str(i)+'["step"] == 72:  ')
    print('             dict_contr_'+str(i)+'["koef"] = dict_contr_'+str(i)+'["koef"] * 2  ')
    print('          if dict_contr_'+str(i)+'["step"] == 90:  ')
    print('             dict_contr_'+str(i)+'["koef"] = dict_contr_'+str(i)+'["koef"] * 2  ')
    print('          if dict_contr_'+str(i)+'["step"] == 108:  ')
    print('             razresh_'+str(i)+' = False  ')
    print('          proig = proig - dict_contr_'+str(i)+'["koef"]  ')
    print('          spisok[0] = win  ')
    print('          spisok[1] = proig  ')
    print('          spisok[2] = razresh_'+str(i)+'  ')
    print('    return spisok  ')
# 	def chislo_0(razresh_0, key, dict_contr_0):
# 		win = 0
# 		proig = 0
# 		spisok = [0, 0, True]
# 		result = []
# 		if razresh_0:
# 			if key == 2:
# 				win = 36 * dict_contr_0["koef"]
# 				razresh_0 = False
# 				dict_contr_0["step"] = 0
# 				dict_contr_0["koef"] = 0.1
# 				spisok[0] = win
# 				spisok[2] = razresh_0
# 			else:
# 				razresh_0 = True
# 				dict_contr_0["step"] = dict_contr_0["step"] + 1
# 				if dict_contr_0["step"] == 36:
# 					dict_contr_0["koef"] = dict_contr_0["koef"] * 2
#
# 				if dict_contr_0["step"] == 54:
# 					dict_contr_0["koef"] = dict_contr_0["koef"] * 2
# 				if dict_contr_0["step"] == 72:
# 					dict_contr_0["koef"] = dict_contr_0["koef"] * 2
# 				if dict_contr_0["step"] == 90:
# 					dict_contr_0["koef"] = dict_contr_0["koef"] * 2
# 				if dict_contr_0["step"] == 108:
# 					razresh_0 = False
# 				proig = proig - dict_contr_0["koef"]
# 				spisok[0] = win
# 				spisok[1] = proig
# 				spisok[2] = razresh_0
# 		return spisok
# for i in range(2):
# 	var=str(i)
# 	if interval_0 < 120:
#
# 		if razresh_0:
# 			dict_tansf_1 = chislo_0(razresh_0, key, dict_contr_0)
# 			Viigral = Viigral + dict_tansf_0[0]
# 			Proigral = Proigral + dict_tansf_0[1]
# 			razresh_0 = dict_tansf_0[2]
#
# def chislo_04(razresh_04, key, dict_contr_04,msg):
# 	win = 0
# 	proig = 0
# 	spisok = [0, 0, True]
# 	result = []
# 	if razresh_04:
# 		if key == 2:
# 			win = 36 * dict_contr_04["koef"]
# 			razresh_04 = False
# 			dict_contr_04["step"] = 0
# 			dict_contr_04["koef"] = 0.1
# 			spisok[0] = win
# 			spisok[2] = razresh_04
# 		else:
# 			razresh_04 = True
# 			dict_contr_04["step"] = dict_contr_04["step"] + 1
# 			if dict_contr_04["step"] == 36:
# 				dict_contr_04["koef"] = dict_contr_04["koef"] * 2
#
# 			if dict_contr_04["step"] == 54:
# 				dict_contr_04["koef"] = dict_contr_04["koef"] * 2
# 			if dict_contr_04["step"] == 72:
# 				dict_contr_04["koef"] = dict_contr_04["koef"] * 2
# 			if dict_contr_04["step"] == 90:
# 				dict_contr_04["koef"] = dict_contr_04["koef"] * 2
# 			if dict_contr_04["step"] == 108:
# 				razresh_04 = False
# 			proig = proig - dict_contr_04["koef"]
# 			spisok[0] = win
# 			spisok[1] = proig
# 			spisok[2] = razresh_04
# 	return spisok

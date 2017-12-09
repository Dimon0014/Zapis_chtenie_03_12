def prnt():
	for i in range(2):
		funct="fun"+str(i)
		def prnt_stroka(i):
			print('funct',i)
		#print(prnt_stroka)
		funct=prnt_stroka
		
		#print(funct)
		funct(i)
		
prnt()


#
# def prnt_stroka(i):
# 	print('funct', i)
#
# #print(prnt_stroka)
# funct = prnt_stroka
# i='ghbdtn'
# print(funct)
# funct(i)
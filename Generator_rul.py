import random
file_obj = open('222cikl_och.txt', 'w')
file_obj.close()
file_obj = open('222cikl_och.txt', 'a')
for i in range(400):
 chislo =random.randint(0,36) # генерируем число
 file_obj.write(str(chislo)+'\n')

file_obj.close()
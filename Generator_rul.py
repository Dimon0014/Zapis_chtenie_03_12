import random
file_obj = open('100_xodov.txt', 'w')
file_obj.close()
file_obj = open('100_xodov.txt', 'a')
for i in range(2000):
 chislo =random.randint(0,36) # генерируем число
 file_obj.write(str(chislo)+'\n')

file_obj.close()
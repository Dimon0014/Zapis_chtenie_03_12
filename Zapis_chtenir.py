import random
#запись строки в файл, открытый в режиме 'w'
# file_obj = open('file_to_write_in.txt', 'w')
# string = 'строка для записи в файл\n'
# file_obj.write(string)
# file_obj.close()
#
#
# #запись строки в файл, открытый в режиме 'a'
# file_obj = open('file_to_write_in.txt', 'a')
# second_string = 'третья строка для записи в файл\n'
# file_obj.write(second_string)
# file_obj.close()
#
# #создание списка чисел от 1 до 10
# digits = range(1,11)
#
# #запись в файл списка строк с помощью функции writelines
# file_obj = open('second_file_for_write_in.txt', 'w')
# file_obj.writelines(digit + '\n' for digit in map(str, digits))
# file_obj.close()
#
# #вывод на экран содержимого файла
# with open('second_file_for_write_in.txt', 'r') as file_obj:
#     print (file_obj.read())
lst_of2 = []
lst_of3 = []
lst_of4 = []
lst_of5 = []
lst_of6 = []
lst_of7 = []
file_obj = open('100_xodov.txt', 'w')
file_obj.write('')
file_obj.close()
file_obj = open('100_xodov.txt', 'r')
t=file_obj.read()
file_obj.close()
if not t:  # если t равно False, конструкция not t возращает True( то есть если файл пустой он возращает False,
           # типа прочесть не удалось), а для if  нужно True, поэтому к t добавим not
    print('Пустая строка')
    file_obj2 = open('6_xoda.txt', 'r')
    data_list = list(file_obj2)
    pre_chislo1 = int(data_list[0])
    pre_chislo2 = int(data_list[1])
    pre_chislo3 = int(data_list[2])
    pre_chislo4 = int(data_list[3])
    pre_chislo5 = int(data_list[4])
    pre_chislo6 = int(data_list[5])
    file_obj2.close()
    print('последнее число:', pre_chislo1)
    print('предпоследнее число:',pre_chislo2)
    print('предпоследнее число3:',pre_chislo3)
    print('предпоследнее число4:',pre_chislo4)
    print('предпоследнее число5:', pre_chislo5)
    print('предпоследнее число6:', pre_chislo6)
else:
	pre_chislo1 = 99
	pre_chislo2 = 99
	pre_chislo2 = 99
	pre_chislo3 = 99
	pre_chislo4 = 99
	pre_chislo5 = 99
	pre_chislo6 = 99

file_obj = open('100_xodov.txt', 'a')
for i in range(2000):
 chislo =random.randint(0,36) # генерируем число
 file_obj.write(str(chislo)+'\n')
 # file_obj1 = open('1_xod.txt', 'w')
 # file_obj1.write(str(chislo)+'\n')
 # file_obj2 = open('2_xoda.txt', 'w')
 # file_obj2.write(str(chislo) + '\n'+str(pre_chislo1)+'\n')
 # file_obj3 = open('3_xoda.txt', 'w')
 # file_obj3.write(str(chislo) + '\n' + str(pre_chislo1) + '\n'+ str(pre_chislo2) + '\n')
 vectr2 = (pre_chislo1, chislo)
 vectr3 = (pre_chislo2, pre_chislo1, chislo)
 vectr4 = (pre_chislo3, pre_chislo2, pre_chislo1, chislo)
 vectr5 = (pre_chislo4, pre_chislo3, pre_chislo2, pre_chislo1, chislo)
 vectr6 = (pre_chislo5, pre_chislo4, pre_chislo3, pre_chislo2, pre_chislo1, chislo)
 vectr7 = (pre_chislo6, pre_chislo5, pre_chislo4, pre_chislo3, pre_chislo2, pre_chislo1, chislo)
 lst_of2.append(vectr2)
 lst_of3.append(vectr3)
 lst_of4.append(vectr4)
 lst_of5.append(vectr5)
 lst_of6.append(vectr6)
 lst_of7.append(vectr7)
 file_obj1 = open('1_xoda.txt', 'w')
 file_obj1.write(str(chislo) + '\n')
 file_obj2 = open('2_xoda.txt', 'w')
 file_obj2.write(str(chislo) + '\n' + str(pre_chislo1) + '\n')
 file_obj3 = open('3_xoda.txt', 'w')
 file_obj3.write(str(chislo) + '\n' + str(pre_chislo1) + '\n' + str(pre_chislo2) + '\n')
 file_obj4 = open('4_xoda.txt', 'w')
 file_obj4.write(str(chislo) + '\n' + str(pre_chislo1) + '\n' + str(pre_chislo2) + '\n'+ str(pre_chislo3) + '\n')
 file_obj5 = open('5_xoda.txt', 'w')
 file_obj5.write(str(chislo) + '\n' + str(pre_chislo1) + '\n' + str(pre_chislo2) + '\n' + str(pre_chislo3) + '\n'+ str(pre_chislo4) + '\n')
 file_obj6 = open('6_xoda.txt', 'w')
 file_obj6.write(str(chislo) + '\n' + str(pre_chislo1) + '\n' + str(pre_chislo2) + '\n' + str(pre_chislo3) + '\n'+ str(pre_chislo4) + '\n'+ str(pre_chislo5) + '\n')
 pre_chislo6 = pre_chislo5
 pre_chislo5 = pre_chislo4
 pre_chislo4 = pre_chislo3
 pre_chislo3 = pre_chislo2
 pre_chislo2 = pre_chislo1
 pre_chislo1 = chislo
 #file_obj.write(str(vectr7) + '\n')
 #e=str(vectr7)
 # print('vektor7', e+'\n'+e+'\n')
 # ee=e+e
 # print(ee)

 # data_list = list(ee)
 # print(data_list)
 
 file_obj1.close()
 file_obj2.close()
 file_obj3.close()
 file_obj4.close()
 file_obj5.close()
 file_obj6.close()
 # print(vectr2)
 # print(vectr3)
 # print(vectr4)
 # print(vectr5)
 # print(vectr6)
 # print(vectr7)
file_obj.close()

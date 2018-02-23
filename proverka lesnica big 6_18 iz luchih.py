import json
import random
import math
 #------------- в начале обработка единичных символов

def last_last_seen_steps_of_simv_01(dict,key): # альтернатива  "last_next_seen_all_steps_1"
    result = dict[key][0]

    #print('функия next_seen_steps =',result)
    return result

def dob_next_seen_1(dict,key, steps): # функция добавления/инициализация шагов с последнего появления

  if  (key) in dict: # проверка на наличие значений
      last_seen = last_last_seen_steps_of_simv_01(dict,key)
      #print('steps-last_time seen_in_key =', last_seen)
      #print('печатает dict[key][1][0]', dict[key][1][0])
      dict[key][1].append(last_seen)
      dict[key][2] = len(dict[key][1]) # сколько раз уже выпадала


  else: # инициализация
      dict.update({(key): [0, [steps], 1, key, steps]})  # инициализация
      #print('key in function =', key)

def add_step_to_all_1(dict):
  for item in  dict:
          dict[item][0]=dict[item][0]+1
          dict[item][4] = dict[item][4] + 1

def more_of_1(dict):
    spisok=[]
    a = 0
    s = 0
    spisok2 = []
    for item in dict:
           if dict[item][2]==1:

             if dict[item][4] >100:


                     spisok.append(dict[item])
                     if len(spisok) > 0:
                         a = dict[item][3]
                         s = dict[item][4]

                         #print('spisok', spisok)
                         spisok2.append(a)
                         spisok2.append(s)
                         #print('spisok2', spisok2)
                     break

                 #print("номер", dict[item][3], "выпал", dict[item][2], "раз(а)--шаг", dict[item][4])
    return spisok2
def podchet_simv(s): # подсчет сколько раз встречаются символы в строке(списке)
    d = dict()
    for c in s:
        if c not in d:d[c] = 1
        else:d[c] += 1
    return d

#отсюда функции патернов-------------------------------
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
    #print('из функции достающей интервалы result',result )
    #print('из функции достающей интервалы dictEd[(key)][0]', dictEd[(key)][0])
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
        #  dict2Glob[(key2step,key1step)][3] = steps_sesia # количество шагов в сесии- нужно для предсказанияkey1step # первый символ ключа
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
def postrocno(spisok,name):
    i=0
    for item in spisok:
        i=i+1
        print(steps,name,'стока',i, item)
def stepsbig(interval, porog,steps_big ):
    steps_big
    if interval< porog:
        steps_big=steps_big+1
    return  steps_big
def podchet_interv_odd(slovar):
    obshie=0
    rezult = 0
    for item in slovar:
        if (slovar[item][3]%2)!=0:
          if (slovar[item][0]) > 180:
            rezult =obshie+ slovar[item][0]

    return rezult
def podchet_interv_iven(slovar):
    obshie=0
    rezult =0
    for item in slovar:
        if (slovar[item][3]%2)==0:
           if (slovar[item][0])> 180:
               rezult=obshie+ slovar[item][0]
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
    obshie=[]
    rezult =0
    for item in slovar:
        if (slovar[item][3]%2)==0:
           if (slovar[item][0])< 10:
               obshie.append(slovar[item][3])
               rezult =len(obshie)
    return rezult

def nahogd_big_interv(slovar):
    rezult =0
    big=0
    for item in slovar:

        if (slovar[item][0])>big:
          rezult=slovar[item][3]
          slovar[item][0] = big
    return rezult


# def poslednieChisla(list, key):
#     list[0]=list[1]
#     list[1] = list[2]
#     list[2] = list[3]
#     list[3] = list[4]
#     list[4] = list[5]
#     list[5] = list[6]
#     list[6] = list[7]
#     list[7] = list[8]
#     list[8] = list[9]
#     list[9] = list[10]
#     list[10] = list[11]
#     list[11] = list[12]
#     list[12] = list[13]
#     list[13] = list[14]
#     list[14] = list[15]
#     list[15] = list[16]
#     list[16] = list[17]
#     list[17] = list[18]
#     list[18] = list[19]
#     list[19] = list[20]
#     list[20] = list[21]
#     list[21] = list[22]
#     list[22] = list[23]
#     list[23] = list[24]
#     list[24] = list[25]
#     list[25] = list[26]
#     list[26] = list[27]
#     list[27] = list[28]
#     list[29] = list[30]
#     list[30] = list[31]
#     list[31] = list[32]
#     list[32] = list[33]
#     list[33] = list[34]
#     list[34] = list[35]
#     list[35] = list[36]
#     list[36] = key
#     return list
def dedupe(spisok):
    seen = set()
    i =0
    for i in range(len(spisok)):
        if spisok[i] not in seen:
            yield spisok[i]
            seen.add(spisok[i])
    return seen
def neIgrauchirChisla(spisok):
    spisok.revers  # проверить без реверса

    list2 = spisok[0:18]
    return list2


def igrauchirChisla(list1):

    list2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]

    # for item in set(list2).difference(list)
    # i=0
    # k =0
    # for i in range(len(list2)):
    #     for k in range(len(list)):
    #         if list[k] == list2[i]:
    #               list2.remove(list2[i])
    list3 = list(set(list2)-set(list1))
    return list3
rasnica2 =0
ik = 0
vig = 0
prg = 0
chag = 0
itog =0
i =0
def dedupe(items):
    spisok =[]
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
    # i =0
    # for i in range(len(seen)):
    #   spisok.append(seen[i])
    # return spisok
samyy_samyy_big_stavka = 0
a = [1, 5, 2, 1, 9, 1, 5, 10]
list2 = list(dedupe(a))
print('ЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ')
print('ЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ')
print('ЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕЕ')
print("-----------------------------------------------------------------------------------------ЭТО ЛИСТ",list2)

for i in range(222,825):
# while (ik < 100):
    ik = ik + 1
    # naime_file = 'cikly/400cikl_ochh.txt'
    # naime_file = 'cikly2/'+str(i) + 'cikl_ochh.txt'
    # file_obj = open(naime_file, 'w')
    # file_obj.close()
    # file_obj = open(naime_file, 'a')
    # for i in range(200):
    #     chislo = random.randint(0, 36)  # генерируем число
    #     file_obj.write(str(chislo) + '\n')
    #
    # file_obj.close()

    # naime_file = '700cikl_och.txt'
    # naime_file = 'cikly2/'+str(i) + 'cikl_ochh.txt'
    naime_file = ''+str(i) + 'cikl_och.txt'
    # naime_file = 'cikly2/196cikl_ochh.txt'


    viborka = []
    file_obj = open(naime_file)
    data_list = file_obj.readlines()
    for line in data_list:
        viborka.append(int(line))
    # объявление всех переменных-----------------------------------------------------------------------------------
    dic_ed = {} # болванка под словарь едениц
    #-----------------------------------------------------------------------------------
    dict_interv_of2 = {} # болванка под словарь интервалов 2-ек
    dict_interv_of3 = {} # болванка под словарь интервалов 3-ек
    key=0
    steps_sesia = 1
    key1 = key
    steps = 0
    steps_big =0
    key3step = 0
    key2step = 0
    listAll_inter=[] # болванка под список всех интервалов
    log = True
    spisok_vnesh=[0]
    spisok_vnesh2=[1]
    win =''
    win1=True
    win2 =True
    win3=True
    Viigral =0
    Proigral =0
    change=True
    index_predscazan=0
    good_pred=[]
    bad_pred=[]
    iven_or_odd=0
    all_odd=0
    all_even=0
    pribyl =0
    ubyl= 0
    step_of_lecnicu =0
    # my_razmer_stavki =0.19
    my_razmer_stavki = 0.18
    razmer_stavki = 0.22
    promegutocnuy_balans = 0
    balans =0
    samyy_maly=0
    samyy_maly_step =0
    samyy_big_stavka = 0
    samyy_big_stavka_step = 0

    raznica =0
    pribavka =0
    posledn_chisla =[]
    ne_chisla = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    ig_chisla = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    while (steps <len(viborka)):
        key = viborka[steps]
        key1 = key
        steps = steps + 1


        if steps >24: # чтоб сформировались первые лучшие числа
            raznica = all_odd - all_even
            # if raznica <0:
            #     pribavka = math.fabs(raznica)


            #print('raznica',raznica)
            # print('key1:', key)
            # print('neigrauhie_cisla', ne_chisla)
            # print('igrauchie_cisla00',ig_chisla )


            i = 0
            for i in range(len(ne_chisla)):
                 if key1 == ne_chisla[i]:
                     pribyl = pribyl + razmer_stavki
                     # razmer_stavki = razmer_stavki - 1 + pribavka
                     # razmer_stavki=razmer_stavki+1+pribavka
                     # my_razmer_stavki = my_razmer_stavki + 1
                     # step_of_lecnicu=step_of_lecnicu+1
                     all_even = all_even + 1
                     break
            i = 0
            for i in range(len(ig_chisla)):
                 if key1 ==ig_chisla[i]:


                     ubyl = ubyl + razmer_stavki
                     razmer_stavki = razmer_stavki + 0.19 + (pribavka * my_razmer_stavki)
                     # my_razmer_stavki = my_razmer_stavki + 1+pribavka
                     # step_of_lecnicu = step_of_lecnicu + 1
                     all_odd = all_odd + 1
                     break
            promegutocnuy_balans = pribyl - ubyl
            # print(steps, ' ubyl:', ubyl)
            # print(steps, ' promegutocnuy_balans:', promegutocnuy_balans)

            if samyy_maly>promegutocnuy_balans:
                samyy_maly = promegutocnuy_balans
                samyy_maly_step =steps

            if promegutocnuy_balans< -100:
                break
            if promegutocnuy_balans > 0:
                balans = balans + promegutocnuy_balans
                promegutocnuy_balans = 0
                step_of_lecnicu = 0
                razmer_stavki = 0.22
                ubyl = 0
                pribyl =0
            # print(steps, ' promegutocnuy_balans:', promegutocnuy_balans)
            if samyy_big_stavka<razmer_stavki:
                samyy_big_stavka = razmer_stavki
                samyy_big_stavka_step = steps
            # print('    razmer stavki:', razmer_stavki)
        posledn_chisla.reverse()
        posledn_chisla.append(key)# = poslednieChisla(posledn_chisla, key1)
        # print('ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss poslednie chisla',posledn_chisla)
        if steps> 24:
            #neIgrauchirChisla

            posledn_chisla.reverse()
            # print('ssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssss poslednie chisla', posledn_chisla)
            # list(dedupe(a))
            b = list(dedupe(posledn_chisla))
            ne_chisla = b[0:22]
            #print('wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww ne_chisla: ', ne_chisla)
            ig_chisla =  igrauchirChisla(ne_chisla)

        # print('igrauchie_chisla',ig_chisla )
        # print('key1:', key)
        # print('igrauhie_cisla', igrauhie_cisla[0])
        # print('              ', igrauhie_cisla[1])
        # print('              ', igrauhie_cisla[2])
        # print('              ', igrauhie_cisla[3])
        # print('              ', igrauhie_cisla[4])
        # print('              ', igrauhie_cisla[5])
        # print('              ', igrauhie_cisla[6])
        # print('              ', igrauhie_cisla[7])
        # print('              ', igrauhie_cisla[8])
        # print('              ', igrauhie_cisla[9])
        # print('              ', igrauhie_cisla[10])
        # print('              ', igrauhie_cisla[11])
        # print('              ', igrauhie_cisla[12])
        # print('              ', igrauhie_cisla[13])
        # print('              ', igrauhie_cisla[14])
        # print('              ', igrauhie_cisla[15])
        # print('              ', igrauhie_cisla[16])
        # print('              ', igrauhie_cisla[17])
        # print('              ', igrauhie_cisla[18])
    print('')
    print('--------------------------------------------------------------------------------------------------------')
    itog_cikla=balans+ promegutocnuy_balans
    print('Balans:', balans+ promegutocnuy_balans)
    print(' all_odd', all_odd)
    print(' all_even', all_even)
    print(' разница между odd and even',all_odd - all_even)
    print('samyy_maly_step',samyy_maly_step)
    print('samyy_big_stavka_step',samyy_big_stavka_step,'stavka: ', samyy_big_stavka )
    itog = itog + itog_cikla
    if samyy_samyy_big_stavka < samyy_big_stavka:
       samyy_samyy_big_stavka = samyy_big_stavka
    # if rasnica> 100:
    #     break
    #postrocno(int_count)
    #print('словарь едениц',dic_ed)
    #print('chag', chag)

    # postrocno(bad_pred,'Bad')
    # postrocno(good_pred,'Good')
# print('Выиграл:',vig)
# print('Проиграл:',prg)
rasnica=vig-prg

print('---------------------------------itog', itog, 'samyy samyy big stavka: ', samyy_samyy_big_stavka)
#print('общтй итог:',rasnica2)

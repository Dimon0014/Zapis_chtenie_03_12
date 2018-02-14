import json
import random
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

def upr_stavkami(stavki,schet_shagamm):
        if schet_shagamm > 36 and schet_shagamm < 55:
            stavki = 2
        elif schet_shagamm > 54 and schet_shagamm < 73:
            stavki = 4
        elif schet_shagamm > 72 and schet_shagamm < 91:
            stavki = 8
        elif schet_shagamm > 90 and schet_shagamm < 109:
            stavki = 16
        elif schet_shagamm > 108 and schet_shagamm < 127:
            stavki = 32
        #     #print(steps,' ',key,'------------------------------------------------------------------stavka0.32' )
        elif schet_shagamm > 126 and schet_shagamm < 143:
            stavki = 64
        #     #print(steps,' ',key,'------------------------------------------------------------------stavka0.64' )
        elif schet_shagamm > 142 and schet_shagamm < 161:
            stavki = 128
        # #     #print(steps,' ',key,'-------------------------------------------------------------------stavka0.64' )
        # elif schet_shagamm > 160 and schet_shagamm < 179:
        #     stavki = 256
        #     #print(steps, ' ', key, '-------------------------------------------------------------------stavka1.28')
        # elif schet_shagamm > 178 and schet_shagamm < 197:
        #     stavki = 512
        elif schet_shagamm > 160:
            stavki  = -1
            #print(steps,' ',key,'--------------------------------------------------------------------BANK USHOL' )
        return stavki









rasnica2 =0
ik = 0
vig = 0
prg = 0
chag = 0
itog =0
i=0
vse_minusu=[]
predskaz2 =[0,1,2,3]
for i in range(1,500): #while (ik < 1): # количество файлов

    ik = ik + 1
    naime_file = 'cikly/400cikl_ochh.txt'
    #naime_file = 'cikly/'+str(ik) + 'cikl_ochh.txt'
    file_obj = open(naime_file, 'w')
    file_obj.close()
    file_obj = open(naime_file, 'a')
    for i in range(200):
        chislo = random.randint(0, 36)  # генерируем число
        file_obj.write(str(chislo) + '\n')

    file_obj.close()

    #naime_file = '148cikl_och.txt'
    #naime_file = 'cikly/'+str(i) + 'cikl_ochh.txt'
    naime_file = 'cikly/400cikl_ochh.txt'
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
    razmer_stavki =1
    promegutocnuy_balans = 0
    promegutocnuy_balans2 = 0
    balans =0
    real_balans =0
    raznica =0
    razr =[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    razmer_stavki_all = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    schet_shagam = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    samauy_minus =0
    upravl = 0
    #predskaz = []
    pred = [1, 2, 3, 4, 5, 6,7]
    pred[0] = predskaz2[0]
    pred[1] = predskaz2[1]
    predskaz = viborka[0: 7]
    # print('predskaz', len(predskaz))
    # print('predskaz2', len(predskaz2))
    # print('pred', len(pred))


    i = 0
    k =0
    for i in range(len(razr)):
        for k in range(len(pred)):
            if i == pred[k]:
                razr[i]=0

    print('nachalo fila: ', naime_file, '-----------------------------------------------------------------------------------------------start')

    while (steps <len(viborka)):

        key = viborka[steps]
        key1 = key
        steps = steps + 1

        # if steps == 1:
        #     #pred[2]=k
        #     i =0
        #     for i in range(len(razr)):
        #             if i == key:
        #                 razr[i] = 0
        # if steps == 2:
        #     #pred[3] = k
        #     i = 0
        #     for i in range(len(razr)):
        #         if i == key:
        #             razr[i] = 0
        # if steps == 3:
        #     # pred[3] = k
        #     i = 0
        #     for i in range(len(razr)):
        #         if i == key:
        #             razr[i] = 0
        #
        # if steps == 4:
        #     # pred[3] = k
        #     i = 0
        #     for i in range(len(razr)):
        #         if i == key:
        #             razr[i] = 0




        # if raznica > 30:
        #     if key == 0:
        #         print('                                             vypal 0')
        #         ubyl = ubyl+razmer_stavki
        #         razmer_stavki=razmer_stavki+1
        #         step_of_lecnicu=step_of_lecnicu+1
        #         all_odd=all_odd+1
        #
        #     elif key % 2 != 0:
        #         pribyl = pribyl + razmer_stavki
        #         step_of_lecnicu = step_of_lecnicu - 1
        #
        #         all_even = all_even + 1
        #
        #     elif key % 2 == 0:
        #         ubyl = ubyl + razmer_stavki
        #         razmer_stavki = razmer_stavki + 1
        #         step_of_lecnicu = step_of_lecnicu + 1
        #
        #         all_odd = all_odd + 1
        # else:
        if key == 0 and razr[0] ==1:
            pribyl = pribyl + (35 * razmer_stavki_all[0])
            razr[0] = 0
            razmer_stavki_all[0] = -1
            #print('vupal 0 na shage: ', steps, 'razr[0]: ',razr[0],  'razr[3]: ',razr[3], 'razr[8]: ',razr[8])
        if key != 0 and razr[0] == 1:
            ubyl = ubyl+ razmer_stavki_all[0]
            schet_shagam[0] = schet_shagam[0] +1
            razmer_stavki_all[0] = upr_stavkami(razmer_stavki_all[0], schet_shagam[0])
            if razmer_stavki_all[0]<0:
                razr[0] = 0
            #print('stavka na 0')
        if key == 1 and razr[1] ==1:
            pribyl = pribyl + (35 * razmer_stavki_all[1])
            razr[1] = 0
            razmer_stavki_all[1] = -1
        if key != 1 and razr[1] == 1:
            ubyl = ubyl+ razmer_stavki_all[1]
            schet_shagam[1] = schet_shagam[1] +1
            razmer_stavki_all[1] = upr_stavkami(razmer_stavki_all[1], schet_shagam[1])
            if razmer_stavki_all[1]<0:
                razr[1] = 0
        if key == 2 and razr[2] ==1:
            pribyl = pribyl + (35 * razmer_stavki_all[2])
            razr[2] = 0
            razmer_stavki_all[2] = -1
        if key != 2 and razr[2] == 1:
            ubyl = ubyl+ razmer_stavki_all[2]
            schet_shagam[2] = schet_shagam[2] +1
            razmer_stavki_all[2] = upr_stavkami(razmer_stavki_all[2], schet_shagam[2])
            if razmer_stavki_all[2]<0:
                razr[2] = 0
        if key == 3 and razr[3] ==1:
            pribyl = pribyl + (35 * razmer_stavki_all[3])
            razr[3] = 0
            razmer_stavki_all[3] = -1
           # print('vupal 3 na shage: ', steps, 'razr[3]: ',razr[3],  'razr[0]: ',razr[0],'razr[8]: ',razr[8])
        if key != 3 and razr[3] == 1:
            ubyl = ubyl+ razmer_stavki_all[3]
            schet_shagam[3] = schet_shagam[3] +1
            razmer_stavki_all[3] = upr_stavkami(razmer_stavki_all[3], schet_shagam[3])
            if razmer_stavki_all[3]<0:
                razr[3] = 0
          # print('stavka na 3')
        if key == 4 and razr[4] ==1:
            pribyl = pribyl + (35 * razmer_stavki_all[4])
            razr[4] = 0
            razmer_stavki_all[4] = -1
        if key != 4 and razr[4] == 1:
            ubyl = ubyl+ razmer_stavki_all[4]
            schet_shagam[4] = schet_shagam[4] +1
            razmer_stavki_all[4] = upr_stavkami(razmer_stavki_all[4], schet_shagam[4])
            if razmer_stavki_all[4]<0:
                razr[4] = 0
        if key == 5 and razr[5] ==1:
            pribyl = pribyl + (35 * razmer_stavki_all[5])
            razr[5] = 0
            razmer_stavki_all[5] = -1
        if key != 5 and razr[5] == 1:
            ubyl = ubyl+ razmer_stavki_all[5]
            schet_shagam[5] = schet_shagam[5] +1
            razmer_stavki_all[5] = upr_stavkami(razmer_stavki_all[5], schet_shagam[5])
            if razmer_stavki_all[5]<0:
                razr[5] = 0
        if key == 6 and razr[6] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[6])
            razr[6] = 0
            razmer_stavki_all[6] = -1
        if key != 6 and razr[6] == 1:
            ubyl = ubyl + razmer_stavki_all[6]
            schet_shagam[6] = schet_shagam[6] + 1
            razmer_stavki_all[6] = upr_stavkami(razmer_stavki_all[6], schet_shagam[6])
            if razmer_stavki_all[6]<0:
                razr[6] = 0

        if key == 7 and razr[7] ==1:
            pribyl = pribyl + (35 * razmer_stavki_all[7])
            razr[7] = 0
            razmer_stavki_all[7] = -1
        if key != 7 and razr[7] == 1:
            ubyl = ubyl+ razmer_stavki_all[7]
            schet_shagam[7] = schet_shagam[7] +1
            razmer_stavki_all[7] = upr_stavkami(razmer_stavki_all[7], schet_shagam[7])
            if razmer_stavki_all[7]<0:
                razr[7] = 0


        if key == 8 and razr[8] ==1:
            pribyl = pribyl + (35 * razmer_stavki_all[8])
            razr[8] = 0
           # print('vupal 8 na shage: ', steps, 'razr[8]: ',razr[8], 'razr[0]: ',razr[0], 'razr[3]: ',razr[3],)
            razmer_stavki_all[8] = -1
        if key != 8 and razr[8] == 1:
            #print('stavka na 8')
            ubyl = ubyl+ razmer_stavki_all[8]
            schet_shagam[8] = schet_shagam[8] +1
            razmer_stavki_all[8] = upr_stavkami(razmer_stavki_all[8], schet_shagam[8])
            if razmer_stavki_all[8]<0:
                razr[8] = 0

        if key == 9 and razr[9] ==1:
            pribyl = pribyl + (35 * razmer_stavki_all[9])
            razr[9] = 0
            razmer_stavki_all[9] = -1
        if key != 9 and razr[9] == 1:
            ubyl = ubyl+ razmer_stavki_all[9]
            schet_shagam[9] = schet_shagam[9] +1
            razmer_stavki_all[9] = upr_stavkami(razmer_stavki_all[9], schet_shagam[9])
            if razmer_stavki_all[9]<0:
                razr[9] = 0

        if key == 10 and razr[10] ==1:
            pribyl = pribyl + (35 * razmer_stavki_all[10])
            razr[10] = 0
            razmer_stavki_all[10] = -1
        if key != 10 and razr[10] == 1:
            ubyl = ubyl+ razmer_stavki_all[10]
            schet_shagam[10] = schet_shagam[10] +1
            razmer_stavki_all[10] = upr_stavkami(razmer_stavki_all[10], schet_shagam[10])
            if razmer_stavki_all[10]<0:
                razr[10] = 0
        if key == 11 and razr[11] ==1:
            pribyl = pribyl + (35 * razmer_stavki_all[11])
            razr[11] = 0
            razmer_stavki_all[10] = -1
        if key != 11 and razr[11] == 1:
            ubyl = ubyl+ razmer_stavki_all[11]
            schet_shagam[11] = schet_shagam[11] +1
            razmer_stavki_all[11] = upr_stavkami(razmer_stavki_all[11], schet_shagam[11])
            if razmer_stavki_all[11]<0:
                razr[11] = 0
        if key == 12 and razr[12] ==1:
            pribyl = pribyl + (35 * razmer_stavki_all[12])
            razr[12] = 0
            razmer_stavki_all[12] = -1
        if key != 12 and razr[12] == 1:
            ubyl = ubyl+ razmer_stavki_all[12]
            schet_shagam[12] = schet_shagam[12] +1
            if razmer_stavki_all[12]<0:
                razr[12] = 0
            razmer_stavki_all[12] = upr_stavkami(razmer_stavki_all[12], schet_shagam[12])
            if razmer_stavki_all[12]<0:
                razr[12] = 0

        if key == 13 and razr[13] ==1:
            pribyl = pribyl + (35 * razmer_stavki_all[13])
            razr[13] = 0
            razmer_stavki_all[13] = -1
        if key != 13 and razr[13] == 1:
            ubyl = ubyl+ razmer_stavki_all[13]
            schet_shagam[13] = schet_shagam[13] +1
            razmer_stavki_all[13] = upr_stavkami(razmer_stavki_all[13], schet_shagam[13])
            if razmer_stavki_all[13]<0:
                razr[13] = 0
        if key == 14 and razr[14] ==1:
            pribyl = pribyl + (35 * razmer_stavki_all[14])
            razr[14] = 0
            razmer_stavki_all[14] = -1
        if key != 14 and razr[14] == 1:
            ubyl = ubyl+ razmer_stavki_all[14]
            schet_shagam[14] = schet_shagam[14] +1
            razmer_stavki_all[14] = upr_stavkami(razmer_stavki_all[14], schet_shagam[14])
            if razmer_stavki_all[14]<0:
                razr[14] = 0
        if key == 15 and razr[15] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[15])
            razr[15] = 0
            razmer_stavki_all[15] = -1
        if key != 15 and razr[15] == 1:
            ubyl = ubyl + razmer_stavki_all[15]
            schet_shagam[15] = schet_shagam[15] + 1
            razmer_stavki_all[15] = upr_stavkami(razmer_stavki_all[15], schet_shagam[15])
            if razmer_stavki_all[15]<0:
                razr[15] = 0
        if key == 16 and razr[16] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[16])
            razr[16] = 0
            razmer_stavki_all[16] = -1
        if key != 16 and razr[16] == 1:
            ubyl = ubyl + razmer_stavki_all[16]
            schet_shagam[16] = schet_shagam[16] + 1
            razmer_stavki_all[16] = upr_stavkami(razmer_stavki_all[16], schet_shagam[16])
            if razmer_stavki_all[16]<0:
                razr[16] = 0
        if key == 17 and razr[17] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[17])
            razr[17] = 0
            razmer_stavki_all[17] = -1
        if key != 17 and razr[17] == 1:
            ubyl = ubyl + razmer_stavki_all[17]
            schet_shagam[17] = schet_shagam[17] + 1
            razmer_stavki_all[17] = upr_stavkami(razmer_stavki_all[17], schet_shagam[17])
            if razmer_stavki_all[17]<0:
                razr[17] = 0
        if key == 18 and razr[18] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[18])
            razr[18] = 0
            razmer_stavki_all[18] = -1
        if key != 18 and razr[18] == 1:
            ubyl = ubyl + razmer_stavki_all[18]
            schet_shagam[18] = schet_shagam[18] + 1
            razmer_stavki_all[18] = upr_stavkami(razmer_stavki_all[18], schet_shagam[18])
            if razmer_stavki_all[18]<0:
                razr[18] = 0
        if key == 19 and razr[19] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[19])
            razr[19] = 0
            razmer_stavki_all[19] = -1
        if key != 19 and razr[19] == 1:
            ubyl = ubyl + razmer_stavki_all[19]
            schet_shagam[19] = schet_shagam[19] + 1
            razmer_stavki_all[19] = upr_stavkami(razmer_stavki_all[19], schet_shagam[19])
            if razmer_stavki_all[19]<0:
                razr[19] = 0
        if key == 20 and razr[20] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[20])
            razr[20] = 0
            razmer_stavki_all[20] = -1
        if key != 20 and razr[20] == 1:
            ubyl = ubyl + razmer_stavki_all[20]
            schet_shagam[20] = schet_shagam[20] + 1
            razmer_stavki_all[20] = upr_stavkami(razmer_stavki_all[20], schet_shagam[20])
            if razmer_stavki_all[20]<0:
                razr[20] = 0
        if key == 21 and razr[21] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[21])
            razr[21] = 0
            razmer_stavki_all[21] = -1
        if key != 21 and razr[21] == 1:
            ubyl = ubyl + razmer_stavki_all[21]
            schet_shagam[21] = schet_shagam[21] + 1
            razmer_stavki_all[21] = upr_stavkami(razmer_stavki_all[21], schet_shagam[21])
            if razmer_stavki_all[21]<0:
                razr[21] = 0
        if key == 22 and razr[22] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[22])
            razr[22] = 0
            razmer_stavki_all[22] = -1
        if key != 22 and razr[22] == 1:
            ubyl = ubyl + razmer_stavki_all[22]
            schet_shagam[22] = schet_shagam[22] + 1
            razmer_stavki_all[22] = upr_stavkami(razmer_stavki_all[22], schet_shagam[22])
            if razmer_stavki_all[22]<0:
                razr[22] = 0
        if key == 23 and razr[23] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[23])
            razr[23] = 0
            razmer_stavki_all[23] = -1
        if key != 23 and razr[23] == 1:
            ubyl = ubyl + razmer_stavki_all[23]
            schet_shagam[23] = schet_shagam[23] + 1
            razmer_stavki_all[23] = upr_stavkami(razmer_stavki_all[23], schet_shagam[23])
            if razmer_stavki_all[23]<0:
                razr[23] = 0
        if key == 24 and razr[24] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[24])
            razr[24] = 0
            razmer_stavki_all[24] = -1
        if key != 24 and razr[24] == 1:
            ubyl = ubyl + razmer_stavki_all[24]
            schet_shagam[24] = schet_shagam[24] + 1
            razmer_stavki_all[24] = upr_stavkami(razmer_stavki_all[24], schet_shagam[24])
            if razmer_stavki_all[24]<0:
                razr[24] = 0
        if key == 25 and razr[25] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[25])
            razr[25] = 0
            razmer_stavki_all[25] = -1
        if key != 25 and razr[25] == 1:
            ubyl = ubyl + razmer_stavki_all[25]
            schet_shagam[25] = schet_shagam[25] + 1
            razmer_stavki_all[25] = upr_stavkami(razmer_stavki_all[25], schet_shagam[25])
            if razmer_stavki_all[25]<0:
                razr[25] = 0
        if key == 26 and razr[26] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[26])
            razr[26] = 0
            razmer_stavki_all[26] = -1
        if key != 26 and razr[26] == 1:
            ubyl = ubyl + razmer_stavki_all[26]
            schet_shagam[26] = schet_shagam[26] + 1
            razmer_stavki_all[26] = upr_stavkami(razmer_stavki_all[26], schet_shagam[26])
            if razmer_stavki_all[26]<0:
                razr[26] = 0
        if key == 27 and razr[27] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[27])
            razr[27] = 0
            razmer_stavki_all[27] = -1
        if key != 27 and razr[27] == 1:
            ubyl = ubyl + razmer_stavki_all[27]
            schet_shagam[27] = schet_shagam[27] + 1
            razmer_stavki_all[27] = upr_stavkami(razmer_stavki_all[27], schet_shagam[27])
            if razmer_stavki_all[27]<0:
                razr[27] = 0
        if key == 28 and razr[28] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[28])
            razr[28] = 0
            razmer_stavki_all[28] = -1
        if key != 28 and razr[28] == 1:
            ubyl = ubyl + razmer_stavki_all[28]
            schet_shagam[28] = schet_shagam[28] + 1
            razmer_stavki_all[28] = upr_stavkami(razmer_stavki_all[28], schet_shagam[28])
            if razmer_stavki_all[28]<0:
                razr[28] = 0
        if key == 29 and razr[29] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[29])
            razr[29] = 0
            razmer_stavki_all[29] = -1
        if key != 29 and razr[29] == 1:
            ubyl = ubyl + razmer_stavki_all[29]
            schet_shagam[29] = schet_shagam[29] + 1
            razmer_stavki_all[29] = upr_stavkami(razmer_stavki_all[29], schet_shagam[29])
            if razmer_stavki_all[29]<0:
                razr[29] = 0
        if key == 30 and razr[30] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[30])
            razr[30] = 0
            razmer_stavki_all[30] = -1
        if key != 30 and razr[30] == 1:
            ubyl = ubyl + razmer_stavki_all[30]
            schet_shagam[30] = schet_shagam[30] + 1
            razmer_stavki_all[30] = upr_stavkami(razmer_stavki_all[30], schet_shagam[30])
            if razmer_stavki_all[30]<0:
                razr[30] = 0
        if key == 31 and razr[31] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[31])
            razr[31] = 0
            razmer_stavki_all[31] = -1
        if key != 31 and razr[31] == 1:
            ubyl = ubyl + razmer_stavki_all[31]
            schet_shagam[31] = schet_shagam[31] + 1
            razmer_stavki_all[31] = upr_stavkami(razmer_stavki_all[31], schet_shagam[31])
            if razmer_stavki_all[31]<0:
                razr[31] = 0
        if key == 32 and razr[32] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[32])
            razr[32] = 0
            razmer_stavki_all[32] = -1
        if key != 32 and razr[32] == 1:
            ubyl = ubyl + razmer_stavki_all[32]
            schet_shagam[32] = schet_shagam[32] + 1
            razmer_stavki_all[32] = upr_stavkami(razmer_stavki_all[32], schet_shagam[32])
            if razmer_stavki_all[32]<0:
                razr[32] = 0
        if key == 33 and razr[33] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[33])
            razr[33] = 0
            razmer_stavki_all[33] = -1
        if key != 33 and razr[33] == 1:
            ubyl = ubyl + razmer_stavki_all[33]
            schet_shagam[33] = schet_shagam[33] + 1
            razmer_stavki_all[33] = upr_stavkami(razmer_stavki_all[33], schet_shagam[33])
            if razmer_stavki_all[33]<0:
                razr[33] = 0
        if key == 34 and razr[34] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[34])
            razr[34] = 0
            razmer_stavki_all[34] = -1
        if key != 34 and razr[34] == 1:
            ubyl = ubyl + razmer_stavki_all[34]
            schet_shagam[34] = schet_shagam[34] + 1
            razmer_stavki_all[34] = upr_stavkami(razmer_stavki_all[34], schet_shagam[34])
            if razmer_stavki_all[34]<0:
                razr[34] = 0
        if key == 35 and razr[35] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[35])
            razr[35] = 0
            razmer_stavki_all[35] = -1
        if key != 35 and razr[35] == 1:
            ubyl = ubyl + razmer_stavki_all[35]
            schet_shagam[35] = schet_shagam[35] + 1
            razmer_stavki_all[35] = upr_stavkami(razmer_stavki_all[35], schet_shagam[35])
            if razmer_stavki_all[35]<0:
                razr[35] = 0
        if key == 36 and razr[36] == 1:
            pribyl = pribyl + (35 * razmer_stavki_all[36])
            razr[36] = 0
            razmer_stavki_all[36] = -1
        if key != 36 and razr[36] == 1:
            ubyl = ubyl + razmer_stavki_all[36]
            schet_shagam[36] = schet_shagam[36] + 1
            razmer_stavki_all[36] = upr_stavkami(razmer_stavki_all[36], schet_shagam[36])
            if razmer_stavki_all[36] < 0:
                razr[36] = 0

        # if steps == 29:
        #     i=0
        #     for i in range(len(razr)):
        #         print('nomer: ', i,' ',razr[i])
        #
        # if steps == 29:
        #     i=0
        #     for i in range(len(schet_shagam)):
        #         print('nomer: ', i,' shagi',schet_shagam[i])
        # if steps == 54:
        #     i=0
        #     for i in range(len(razmer_stavki_all)):
        #         print('nomer: ', i,' razmer stavki: ',razmer_stavki_all[i])
        raznica =  pribyl - ubyl

        promegutocnuy_balans = pribyl - ubyl

        # print('     ubyl:', ubyl)
        # print('     pribyl:', pribyl)
        print(steps, ' raznica', raznica)
        #print('     promegutocnuy_balans:', promegutocnuy_balans)
        if samauy_minus > promegutocnuy_balans :
            samauy_minus = promegutocnuy_balans
        if promegutocnuy_balans < -29:
            balans = balans + promegutocnuy_balans
            promegutocnuy_balans = 0
            break
            # i = 0
            # for i in range(len(razmer_stavki_all)):
            #     razmer_stavki_all[i] = 1
            # i = 0
            # for i in range(len(schet_shagam)):
            #     schet_shagam[i] = 1
            # i = 0
            # for i in range(len(razr)):
            #     razr[i] = 1
            # ubyl = 0
            # pribyl = 0
            # i = 0
            # k = 0
            # for i in range(len(razr)):
            #     for k in range(len(pred)):
            #         if i == pred[k]:
            #             razr[i] = 0
            # i = 0
            # for i in range(len(razr)):
            #         if i == key:
            #             razr[i] = 0

        if (promegutocnuy_balans > 0):
            vse_minusu.append(naime_file)
            vse_minusu.append(samauy_minus)
            balans = balans + promegutocnuy_balans
            print('samyi minus v igre: ',samauy_minus)
            print('na shage: ', steps, 'vysel iz igry', 'summ: ', promegutocnuy_balans)
            break
        # if samauy_minus < -400:
        #     print('                  ------------------------------------        ', naime_file, 'shag: ', steps,
        #           'samauy_minus: ', samauy_minus)
        if steps == 195:
            vse_minusu.append(naime_file)
            vse_minusu.append(samauy_minus)
            #print('samyi minus v igre: ', samauy_minus)

        if promegutocnuy_balans > 800:
            print(steps,'shag                                         большой promegutocnuy_balans:', promegutocnuy_balans,'----------------')
            # for i in range(len(razmer_stavki_all)):
            #     print('razmer stavki chisla ',i,':',razmer_stavki_all[i])
        i = 0
        for i in range (len(razr)):
            upravl=upravl+ razr[i]
            # print(
            #     'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU               uprav',
            #     upravl)
        # if upravl< 36:
        #
        #     print('UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU               uprav',upravl )
        # if (razr[0] == 0) and (razr[1] == 0) and (razr[2] == 0)and (razr[3] == 0)\
        #         and (razr[4] == 0)and (razr[5] == 0)and (razr[6] == 0)and (razr[7] == 0):
        if upravl == 0:
            promegutocnuy_balans2 = promegutocnuy_balans2 + promegutocnuy_balans
            promegutocnuy_balans = 0
            print(
                'UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU               uprav',
                upravl)
        upravl=0
        if promegutocnuy_balans >4:

            promegutocnuy_balans = 0
            i=0
            for i in range(len(razmer_stavki_all)):
                razmer_stavki_all[i] = 1
            i=0
            for i in range(len(schet_shagam)):
                schet_shagam[i] =1
            i=0
            for i in range(len(razr)):
                razr[i] = 1
            ubyl = 0
            pribyl =0
            i = 0
            k = 0
            for i in range(len(razr)):
                for k in range(len(pred)):
                    if i == pred[k]:
                        razr[i] = 0

            # print('     promegutocnuy_balans:', promegutocnuy_balans)
            # print('     ubyl:', ubyl)
            # print('     pribyl:', pribyl)
        # print(steps, ' promegutocnuy_balans:', promegutocnuy_balans)

        #     print('-------------------------------------------------------------------------------file ', naime_file)
        # print(steps, '                                            razmer_stavki:', razmer_stavki)
    predskaz2 = predskaz
    print('')
    print('itogovaja chast ---------------------')
    print('file ',naime_file)
    real_balans = real_balans + balans+ promegutocnuy_balans2
    print('REAL BALANS: ',real_balans  )
    if real_balans< 0:
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    #print('Balans:', balans)
    # print(' all_odd', all_odd)
    # print(' all_even', all_even)
    # print(' разница между odd and even',all_odd - all_even)

    itog = itog + real_balans
    #print('                        promejutochyi itog', itog)
    # if rasnica> 100:
    #     break
    #postrocno(int_count)
    #print('словарь едениц',dic_ed)
    #print('chag', chag)
    print('End file ', naime_file, '----------------------------------------------------------------------------------------------------end')
    print('################################################################################################################################')
    print('################################################################################################################################')
    # postrocno(bad_pred,'Bad')
    # postrocno(good_pred,'Good')
# print('Выиграл:',vig)
# print('Проиграл:',prg)
rasnica=vig-prg
print('--------------')
print('itog',itog )
#print('общтй итог:',rasnica2)
i =0
# for i in range(len(vse_minusu)):
#     if i % 2 == 0:
#        print(vse_minusu[i])
#     else:
#         print('               ',vse_minusu[i])
# print('vse minusu: ', vse_minusu)
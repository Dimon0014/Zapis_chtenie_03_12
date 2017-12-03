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
            if (slovar[item][0]) < 110:
                obshie.append(slovar[item][3])
                rezult = len(obshie)
    return rezult

def podchet_count_iven(slovar):
    obshie=[]
    rezult =0
    for item in slovar:
        if (slovar[item][3]%2)==0:
           if (slovar[item][0])< 110:
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

def _podchet_count_12_1(slovar):
    obshie=[]
    rezult =0.1
    for item in slovar:
     if slovar[item][3]  != 0:
        if slovar[item][3]<13:
           if (slovar[item][0])<20:
               obshie.append(slovar[item][3])
               rezult =len(obshie)
    #print('result1', rezult)
    return rezult

def _podchet_count_12_2(slovar):
    obshie=[]
    rezult =0.1
    for item in slovar:
     if slovar[item][3]  != 0:
         if((slovar[item][3]) > 12 and (slovar[item][3]) < 25):
           if (slovar[item][0])<20:
               obshie.append(slovar[item][3])
               rezult =len(obshie)
    #print('result2', rezult)
    return rezult

def _podchet_count_12_3(slovar):
    obshie=[]
    rezult =0.1
    for item in slovar:
     if slovar[item][3]  != 0:
         if slovar[item][3] > 24:
           if (slovar[item][0])< 20:
               obshie.append(slovar[item][3])
               rezult =len(obshie)
    #print('result3',rezult)
    return rezult
def podchet_count_12_1_(slovar):
    obshie=[]
    rezult =0.9
    for item in slovar:
     if slovar[item][3]  != 0:
        if slovar[item][3]<13:
           if (slovar[item][0])> 20:
               obshie.append(slovar[item][3])
               rezult =len(obshie)
    #print('result1', rezult)
    return rezult

def podchet_count_12_2_(slovar):
    obshie=[]
    rezult =0.9
    for item in slovar:
     if slovar[item][3]  != 0:
         if((slovar[item][3]) > 12 and (slovar[item][3]) < 25):
           if (slovar[item][0])> 20:
               obshie.append(slovar[item][3])
               rezult =len(obshie)
    #print('result2', rezult)
    return rezult

def podchet_count_12_3_(slovar):
    obshie=[]
    rezult =0.9
    for item in slovar:
     if slovar[item][3]  != 0:
         if slovar[item][3] > 24:
           if (slovar[item][0])> 20:
               obshie.append(slovar[item][3])
               rezult =len(obshie)
    #print('result3',rezult)
    return rezult

def bolshee_in_12(tw_1,tw_2,tw_3):
    result = 0.9
    if tw_1>tw_2:
        if tw_1 > tw_3:
            result=1
        else:
            result = 3
    else:
        if tw_2 > tw_3:
            result = 2
        else:
            result = 3
    return result
def menshee_in_12(tw_1,tw_2,tw_3):
    result = 0.9
    if tw_1<tw_2:
        if tw_1 < tw_3:
            result=1
        else:
            result = 3
    else:
        if tw_2 < tw_3:
            result = 2
        else:
            result = 3
    return result
def chislo_01(razresh_01, key, dict_01):
     win=0
     proig=0
     spisok=[0,0,True]
     result=[]
     if razresh_01:
         if key ==1:
             win=36*dict_01["koef"]
             razresh_01 =False
             dict_01["step"]=0
             dict_01["koef"]=1
             spisok[0] = win
             spisok[2] = razresh_01
         else:
             razresh_01 = True
             dict_01["step"]=dict_01["step"]+1
             if dict_01["step"]==36:
                 dict_01["koef"]=dict_01["koef"]*2

             if dict_01["step"] ==54:
                 dict_01["koef"] = dict_01["koef"] * 2
             if dict_01["step"] ==72:
                 dict_01["koef"] = dict_01["koef"] * 2
             if dict_01["step"] == 90:
                 razresh_01 = False
             proig=proig-dict_01["koef"]
             spisok[0]=win
             spisok[1]=proig
             spisok[2] = razresh_01
     return spisok


def chislo_02(razresh_02, key, dict_02):
    win = 0
    proig = 0
    spisok = [0, 0, True]
    result = []
    if razresh_02:
        if key == 1:
            win = 36 * dict_02["koef"]
            razresh_02 = False
            dict_02["step"] = 0
            dict_02["koef"] = 1
            spisok[0] = win
            spisok[2] = razresh_02
        else:
            razresh_02 = True
            dict_02["step"] = dict_02["step"] + 1
            if dict_02["step"] == 36:
                dict_02["koef"] = dict_02["koef"] * 2

            if dict_02["step"] == 54:
                dict_02["koef"] = dict_02["koef"] * 2
            if dict_02["step"] == 72:
                dict_02["koef"] = dict_02["koef"] * 2
            if dict_02["step"] == 90:
                razresh_01 = False
            proig = proig - dict_02["koef"]
            spisok[0] = win
            spisok[1] = proig
            spisok[2] = razresh_01
    return spisok


rasnica2 =0
ik = 0
vig = 0
prg = 0
chag = 0
while (ik < 10):
    ik = ik + 1
    file_obj = open('100_xodov.txt', 'w')
    file_obj.close()
    file_obj = open('100_xodov.txt', 'a')
    for i in range(400):
        chislo = random.randint(0, 36)  # генерируем число
        file_obj.write(str(chislo) + '\n')

    file_obj.close()


    viborka = []
    file_obj = open('100_xodov.txt')
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
    proig=0
    change=True
    index_predscazan=0
    good_pred=[]
    bad_pred=[]
    iven_or_odd=0
    all_odd=0
    all_even=0
    tw_1=0
    tw_2 = 0
    tw_3 = 0
    tw_1_ = 0
    tw_2_ = 0
    tw_3_ = 0
    vyig_in_012 =0
    vyig_in_012_pod  =0
    pro_shag=0
    ff=0
    davl=0
    davl2=0
    raznica=0
    while (steps <len(viborka)):
        key = viborka[steps]
        key1 = key
        steps = steps + 1
        # if proig ==1:
        #     proig = 0
        #     pro_shag=pro_shag+1
        #print('davl',davl)
        if (davl > 3) and (rasnica>1):
            if vyig_in_012 ==0:
                Proigral = Proigral + 1

                print('выпал 0')
            else:

                if (key < 13) and (vyig_in_012 ==1):
                    Viigral = Viigral + 2
                    # print('выиграл_tw_1',tw_1)
                    # print('rasnica',rasnica)
                elif ((key > 12) and (key < 25)) and (vyig_in_012 == 2):
                     Viigral = Viigral + 2
                     # print('выиграл_tw_2', tw_2)
                     # print('rasnica', rasnica)
                elif (key > 24) and (vyig_in_012 == 3):
                     Viigral = Viigral + 2
                     #print('выиграл_tw_3', tw_3)
                     #print('rasnica', rasnica)

                else:
                    if (key < 13):
                        Proigral = Proigral + 1
                        if vyig_in_012 == 1:
                           print('проиграл_tw_1', tw_1)
                           print('rasnica', rasnica)
                        if vyig_in_012 == 2:
                           print('проиграл_tw_2', tw_2)
                           print('rasnica', rasnica)
                        if vyig_in_012 == 3:
                           print('проиграл_tw_3', tw_3)
                           print('rasnica', rasnica)
                    elif ((key > 12) and (key < 25)):
                        Proigral = Proigral + 1
                        if vyig_in_012 == 1:
                            print('проиграл_tw_1', tw_1)
                            print('rasnica', rasnica)
                        if vyig_in_012 == 2:
                            print('проиграл_tw_2', tw_2)
                            print('rasnica', rasnica)
                        if vyig_in_012 == 3:
                            print('проиграл_tw_3', tw_3)
                            print('rasnica', rasnica)



                    elif (key > 24):
                        Proigral = Proigral + 1
                        if vyig_in_012 == 1:
                            print('проиграл_tw_1', tw_1)
                            print('rasnica', rasnica)
                        if vyig_in_012 == 2:
                            print('проиграл_tw_2', tw_2)
                            print('rasnica', rasnica)
                        if vyig_in_012 == 3:
                            print('проиграл_tw_3', tw_3)
                            print('rasnica', rasnica)
                        #proig = 1
        #print("выпал", key,"предсказано", bolshee_in_012)
        # if abs(index_predscazan) >0:
        #     if steps < 200:
        #         if key % 2 == 0:
        #             if win1:
        #                 Viigral=Viigral+1
        #                 win2 = True
        #                 steps=steps+0.1
        #                 good_pred.append(index_predscazan)
        #                 good_pred.append(steps)
        #                 steps = int(steps)
        #             else:
        #                 Proigral=Proigral+1
        #                 win2 = False
        #                 steps = steps + 0.1
        #                 bad_pred.append(index_predscazan)
        #                 bad_pred.append(steps)
        #                 steps = int(steps)
        #
        #         if key % 2 != 0:
        #             if win1 == False:
        #                 Viigral = Viigral + 1
        #                 steps = steps + 0.1
        #                 good_pred.append(index_predscazan)
        #                 good_pred.append(steps)
        #                 steps = int(steps)
        #
        #             else:
        #                 Proigral = Proigral + 1
        #                 win2 = False
        #                 steps = steps + 0.1
        #                 bad_pred.append(index_predscazan)
        #                 bad_pred.append(steps)
        #                 steps = int(steps)

        # print('Выпало число:',key)
        rasnica = all_odd - all_even
        # print('Должно было пыпасть если - то чет_+ нечет:', rasnica)
        # if rasnica < 0:
        #      change = not(change)
        # if rasnica > 0:
        #   change = not(change)

        dob_next_seen_1(dic_ed,key, steps) # создание\ обновление словаря едениц
        interval = key01step(key1, dic_ed)  #  последний интервал выпавшего числа
        add_step_to_all_1(dic_ed) # добавление шагов всем еденицам
        # проверочный - dictEd = {(36): [23, [1, 2], 33]}

        chislo1 = random.randint(0, 36)
        all_odd= podchet_count_odd(dic_ed)
            #podchet_interv_odd(dic_ed)
        chislo1 = random.randint(0, 36)
        all_even = podchet_count_iven(dic_ed)
            #podchet_interv_iven(dic_ed)
        index_predscazan = all_odd- all_even
        tw_1 = _podchet_count_12_1(dic_ed)
        tw_2 = _podchet_count_12_2(dic_ed)
        tw_3 = _podchet_count_12_3(dic_ed)
        tw_1_ = podchet_count_12_1_(dic_ed)
        tw_2_ = podchet_count_12_2_(dic_ed)
        tw_3_ = podchet_count_12_3_(dic_ed)
        tw_1 =tw_1/tw_1_
        tw_2 =tw_2/tw_2_
        tw_3 =tw_3/tw_3_
        # print('tw_1',tw_1)
        # print('tw_2', tw_2)
        # print('tw_3', tw_3)
        #if proig != 1:
        vyig_in_012=bolshee_in_12(tw_1,tw_2,tw_3)
        raznica = menshee_in_12(tw_1, tw_2, tw_3)
        if raznica ==3:
            davl2 =tw_3
        if raznica == 2:
            davl2 = tw_2
        if raznica == 1:
            davl2 = tw_1

        if vyig_in_012 ==3:
            davl =tw_3
        if vyig_in_012 == 2:
            davl = tw_2
        if vyig_in_012 == 1:
            davl = tw_1
        raznica = davl-davl2
        if change:
            if all_even != all_odd:
                if all_odd > all_even:
                    win = "выиграет odd"
                    win1 = False
                else:
                    win = "выиграет even"
                    win1 = True
        # else:
        #     if all_even != all_odd:
        #         if all_odd > all_even:
        #             win = "выиграет odd"
        #             win1 = False
        #         else:
        #             win = "выиграет even"
        #             win1 = True
        key1step = interval
       # print('последний интервал выпавшего числа:',interval)  # проверка функции возращающей последний интервал выпавшего числа
        # проверочный -- key3step = 12
        # проверочный -- key2step = 10
        steps_big = stepsbig(interval, 144, steps_big)
        intervals_of_all(key1step, listAll_inter)
        # нужно для инициализации
        # intervals_of_2(key2step, key1step, dict_interv_of2, steps_sesia)
        # print('печатает словар интервалов двоек после создания:', dict_interv_of2)
        #
        # intervals_of_2(key2step, key1step, dict_interv_of2, steps_sesia)
        # print('печатает словар интервалов двоек после обновления:', dict_interv_of2)
        # add_step_to_all_intervals_of_2(dict_interv_of2, key2step, key1step)
        #
        # print('печатает словар интервалов двоек после добавления\обнуления шагов:', dict_interv_of2)
        #
        # intervals_of_3(key3step, key2step, key1step, dict_interv_of3, steps_sesia)
        # print('печатает словар интервалов троек после создания:', dict_interv_of3)

        spisok_vnesh = more_of_1(dic_ed)
        if len(spisok_vnesh)>0:
           spisok_vnesh2= spisok_vnesh

    #print('список интервалов',listAll_inter)
    # print('spisok_vnesh2',spisok_vnesh2)
    with open('intervals_all.txt', 'w') as jsonfile: json.dump(listAll_inter, jsonfile)
    int_count = podchet_simv(listAll_inter)
    int_count = sorted(int_count.items(), key=lambda x: x[1], reverse=True)
    [(4, 74), (2, 47), (3, 32), (0, 17), (1, 12)]
    # print('количество рзных символов',int_count )
    # print('количество шагов биг',steps_big )
    print('Выиграл:',Viigral)
    print('Проиграл:',Proigral)
    vig=vig+Viigral
    prg=prg+Proigral
    rasnica2 = vig - prg
    # if rasnica2> 100:
    #     break
    chag=chag+1
    rasnica=Viigral-Proigral

    print(rasnica)
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
print('---------------------------------')
print('общтй итог:',rasnica2)
# print('chag',ik)
print('pro_shag',pro_shag)
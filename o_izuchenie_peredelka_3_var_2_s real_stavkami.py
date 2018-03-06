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
def podchet_simv(slist): # подсчет сколько раз встречаются символы в строке(списке)
    d = dict()
    for c in slist:
        if c not in d:
              d[c] = 1
        else:
              d[c] += 1
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
          if (slovar[item][0]) < 1000:

            rezult =obshie+ slovar[item][2]

    return rezult
def podchet_interv_iven(slovar):
    obshie=0
    rezult =0
    for item in slovar:
        if (slovar[item][3]%2)==0:
           if (slovar[item][0])< 1000:
               rezult=obshie+ slovar[item][2]
    return rezult
def nahogd_big_interv(slovar):
    rezult =0
    big=0
    for item in slovar:

        if (slovar[item][0])>big:
          rezult=slovar[item][3]
          slovar[item][0] = big
    return rezult

def pre1_predskazatel_1(key,list_of200,steps_of_predscazan ):
    keys=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
    list = list_of200

    for item in keys:
        if item ==key:
            list.append(key)
            if  len(list) > steps_of_predscazan:
                  list.pop(0)
    return list

def pre2_predskazatel_1(list_of200):
       keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,29, 30, 31, 32, 33, 34, 35, 36]
       list = list_of200
       list_par =[]
       for item in  keys:
           list_par.append([item,0])
           for it  in list:
               if it  == item:
                   list_par[item][1]=list_par[item][1]+1
       return list_par
       # for it in keys:
       #     for item in list:
       #         if item not in d:
       #             list_par.append([item])
       #         else:
       #             d[c] += 1

def pre3_predskazatel_1(list_sort):

    list_sort.sort(key = lambda item: item[1])
    list_sort.reverse()
    # nolik = list_sort[0][0]
    # odin = list_sort[1][0]
    # dva = list_sort[2][0]
    # #tri = list_sort[3][0]
    #result =list_sort[0][0] # random.choice([nolik,odin,dva] )
    if list_sort[0][1] >1:
        result =list_sort[0][0] # random.choice([nolik,odin,dva] )
    else:
        result = 99
    return result
def pre3_predskazatel_1_all(list_sort):

    list_sort.sort(key = lambda item: item[1])
    list_sort.reverse()
    # nolik = list_sort[0][0]
    # odin = list_sort[1][0]
    # dva = list_sort[2][0]
    # #tri = list_sort[3][0]
    result =list_sort # random.choice([nolik,odin,dva] )

    return result

def proverka_predskaza_1(key, list_of_win_proverki,winer_1 ):
    if key == list_of_win_proverki[2]:
        list_of_win_proverki[1] = 1 # включение происходит в двух случаях при выигрыше и при превышении количества 54 шагов
        result = list_of_win_proverki  # первое значение - количество шагоd
                # второе значени флаг сброса продолжения проверки
              # третье значение предсказаное число
    else:
        list_of_win_proverki[1] = 0
        list_of_win_proverki[0] = list_of_win_proverki[0] +1 # так как else наступает и в случае (winer_1 == 99) - когда
                                                            #  шагов нет, они прибавляются то ниже при (winer_1 == 99)
                                                            #   эти шаги вычитаются
        result = list_of_win_proverki
    if winer_1 == 99:
        list_of_win_proverki[0] = list_of_win_proverki[0] - 1
        result = list_of_win_proverki
    return result


def pre1_predskazatel_2(key, list_of200, steps_of_predscazan):
    keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
            28, 29, 30, 31, 32, 33, 34, 35, 36]
    list = list_of200

    for item in keys:
        if item == key:
            list.append(key)
            if len(list) > steps_of_predscazan:
                list.pop(0)
    return list

def pre2_predskazatel_2(list_of200):
    keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
            28, 29, 30, 31, 32, 33, 34, 35, 36]
    list = list_of200
    list_par = []
    for item in keys:
        list_par.append([item, 0])
        for it in list:
            if it == item:
                list_par[item][1] = list_par[item][1] + 1
    return list_par
    # for it in keys:
    #     for item in list:
    #         if item not in d:
    #             list_par.append([item])
    #         else:
    #             d[c] += 1

def pre3_predskazatel_2(list_sort):

    list_sort.sort(key=lambda item: item[1])
    list_sort.reverse()
    # nolik = list_sort[0][0]
    # odin = list_sort[1][0]
    # dva = list_sort[2][0]
    # #tri = list_sort[3][0]
    result = list_sort[0][0]  # random.choice([nolik,odin,dva] )

    return result

def proverka_predskaza_2(key, list_of_win_proverki):
    if key == list_of_win_proverki[2]:
        list_of_win_proverki[1] = 1
        result = list_of_win_proverki  # первое значение - количество шагоd
        # второе значени флаг сброса продолжения проверки
        # третье значение предсказаное число

    else:
        list_of_win_proverki[1] = 0
        list_of_win_proverki[0] = list_of_win_proverki[0] +1
        result = list_of_win_proverki
    return result

def podchet_simv(slist): # подсчет сколько раз встречаются символы в строке(списке)
    d = dict()
    for c in slist:
        if c not in d:
              d[c] = 1
        else:
              d[c] += 1
    return d
def podchet_balansa(spisok):
    pribyl = 0
    for item in spisok:
        if (item > 0) and (item < 36):
            pribyl = pribyl + 0.35 - (item*0.01)
        # if (item < 55) and (item >36):
        #    pribyl = pribyl + ((72-36) - (item-36)*2)
        if (item > 35)  and (item < 54):
            pribyl = pribyl + 0.35*2 - (item * 0.01)*2

        if (item  > 53) and (item  < 66):
            pribyl = pribyl + 0.35 * 3 - (item * 0.01) * 3

        if (item > 65) and (item < 75):
            pribyl = pribyl + 0.35 * 4 - (item * 0.01) * 4
        if (item > 74) and (item < 82):
            pribyl = pribyl + 0.35 * 5 - (item * 0.01) * 5

        if (item > 81) and (item < 88):
            pribyl = pribyl + 0.35 * 6 - (item * 0.01) * 6
        if (item > 87) and (item < 93):
            pribyl = pribyl + 0.35 * 7 - (item * 0.01) * 7
        if (item > 92) and (item < 97):
            pribyl = pribyl + 0.35 * 8 - (item * 0.01) * 8
        if (item > 96) and (item < 101):
            pribyl = pribyl + 0.35 * 9 - (item * 0.01) * 9
        if (item > 100) and (item < 105):
            pribyl = pribyl + 0.35 * 10 - (item * 0.01) * 10

        if (item > 104) and (item < 108):
            pribyl = pribyl + 0.35 * 11 - (item * 0.01) * 11
        if (item > 107) and (item < 111):
            pribyl = pribyl + 0.35 * 12 - (item * 0.01) * 12

        if (item > 110) and (item < 114):
            pribyl = pribyl + 0.35 * 13 - (item * 0.01) * 13
        if (item > 113) and (item < 116):
            pribyl = pribyl + 0.35 * 14 - (item * 0.01) * 14
        if (item > 115) and (item < 119):
            pribyl = pribyl + 0.35 * 15 - (item * 0.01) * 15
        if item == 119:
            pribyl = pribyl -5.54
    return pribyl


rasnica2 =0
ik = 0
vig = 0
prg = 0
chag = 0
nol =0
pribyl2 =0
i=0
next_nol = 0
for i in range(1165,1190): #while (ik < 1):
    ik = ik + 1
    # file_obj = open('100_xodov.txt', 'w')
    # file_obj.close()
    # file_obj = open('100_xodov.txt', 'a')
    # for i in range(400):
    #     chislo = random.randint(0, 36)  # генерируем число
    #     file_obj.write(str(chislo) + '\n')
    #
    # file_obj.close()


    naime_file = str(i) + 'cikl_och.txt'
    viborka = []
    file_obj = open(naime_file)
    data_list = file_obj.readlines()
    for line in data_list:
        viborka.append(int(line))
    # объявление всех переменных-----------------------------------------------------------------------------------
    dic_ed = {} # болванка под словарь едениц
    #-----------------------------------------------------------------------------------
    key=0
    steps_sesia = 1
    key1 = key
    steps = 0



   # print("выборка",len(viborka))
    chet=0
    nechet=0
    list_of200_1 = []
    list_par_of200_1 = []
    list_of_win200_1 = []


    winer_1 = 0

    supwiner = 0
    ste_ps_1 = 0

    steps_of_win_1 = 0

   # list_of_win_proverki_1 = [0,0,0]
    list_of_win_proverki_1 = [0, 0, 0, 0, 0, 0, 0, 1]  # первая цифра- подсчет шагов до выигрыша,
    # вторая - активное ли предсказание, третья предсказанное число, четвертое перескок,
    # пятое прибыль, шестое убыль
    # седбмая количество сиклов

    # next_nol = viborka[-1]
    # list_of_win_proverki_1[2] = next_nol
    # if list_of_win_proverki_1[2]<36:
    #  list_of_win_proverki_1[2] = next_nol+1
    # print('nachalo cikla--------------------------------------------------------------------------------')
    # print('viborka[-1]',viborka[-1])
    # print('list_of_win_proverki_1[3]', list_of_win_proverki_1[3])
    steps_to_win_1 = 0

    list_of_steps_toWin_1 = []

    list_of_all_Win_1 = []
    list_of_all_Win_1_and_steps = []
    list_of_win_and_steps =[]
    list_of_winSteps_and_steps = []
    best_chisla =[]
    chislo_stavok =0
    ubyl_v_konce =0
    while (steps < len(viborka)):
        key = viborka[steps]


        key1 = key
        steps = steps + 1
        ############################################################################################
        # БЛОК ЕДЕНИЦЫ
        ############################################################################################
        # print(steps, 'предсказано: ', list_of_win_proverki_1[2], 'выпало:', key1)
        # print('шаги до выигрыша: ', list_of_win_proverki_1[0])
        # print(' ''предсказ-Winner:',winer_1)

        if winer_1 != 99: # если предсказание не на паузе
            list_of_win_proverki_1 = proverka_predskaza_1(key1, list_of_win_proverki_1, winer_1)

            #print('активность предсказа', list_of_win_proverki_1[1])
            if  (list_of_win_proverki_1[1] == 1): # если предсказание активно то
                #print('активность предсказа', list_of_win_proverki_1[1],'        проскочил')
                steps_to_win_1 = list_of_win_proverki_1[0] # забираем в буферную переменную количество шагов до выигрыша
                list_of_win_and_steps.append(list_of_win_proverki_1[2])
                list_of_win_and_steps.append(steps)
                list_of_all_Win_1.append(list_of_win_proverki_1[2])

                #list_of_all_Win_1_and_steps.append(list_of_win_and_steps)
                supwiner = list_of_win_proverki_1[2]
                #if  steps_to_win_1<34:
                list_of_win_proverki_1[2] = winer_1 # назначение нового числа предсказания _ назначение с опаздыванием на один шаг
                list_of_steps_toWin_1.append(steps_to_win_1)
                list_of_winSteps_and_steps.append(steps_to_win_1)
                list_of_winSteps_and_steps.append(steps)
                list_of_win_proverki_1[0]=1 # обнуляем количество шагов до выигрыша
               # print(dic_ed[(key)] )
            if list_of_win_proverki_1[0] > 25:
                list_of_win_proverki_1[0] = 1

            if list_of_win_proverki_1[0] > 118:
                #print('list_of_win_proverki_1[2]',list_of_win_proverki_1[2] )
                list_of_steps_toWin_1.append(119)

                list_of_win_proverki_1[0] = 1
                list_of_win_proverki_1[1] = 0
                winer_1 = 99
                #list_of_win_proverki_1[2] = winer_1
               # list_of_win_proverki_1[2] = winer_1 # назначение нового числа предсказания _ назначение с опаздыванием на один шаг

        list_of200_1 =   pre1_predskazatel_1(key1,list_of200_1,18) # шаг нахождения винера##############################################################
        #if steps > 400:
        list_par_of200_1 = pre2_predskazatel_1(list_of200_1)
        winer_1 =  pre3_predskazatel_1(list_par_of200_1)
        # if winer_1 !=99:
        #     if (list_of_win_proverki_1[0] > 0) and (list_of_win_proverki_1[0] < 37):
        #
        #         if (list_of_win_proverki_1[0] == 36):
        #             chislo_stavok = 0
        #         if (list_of_win_proverki_1[0] == 1):
        #             chislo_stavok = 0
        #         if list_of_win_proverki_1[2] == key1:
        #             chislo_stavok = 0
        #         chislo_stavok = chislo_stavok + 1
        #         print('   ', chislo_stavok, 'stavka na:', list_of_win_proverki_1[2])
        # best_chisla = pre3_predskazatel_1_all(list_par_of200_1)

        #print('winer_1 ',winer_1 )
        # if winer_1 == 99:
        #     list_of200_1 = pre1_predskazatel_1(key1, list_of200_1,12)  # шаг нахождения винера##############################################################
        #     # if steps > 400:
        #     list_par_of200_1 = pre2_predskazatel_1(list_of200_1)
        #     winer_1 = pre3_predskazatel_1(list_par_of200_1)
        #     best_chisla = pre3_predskazatel_1_all(list_par_of200_1)
##################################### --- УЧЕТ ЕДЕНИЦ БЛОК НЕ ТРОГАЕМ --- ######################
################################################################################################
        dob_next_seen_1(dic_ed,key, steps) # создание\ обновление словаря едениц ###############
        interval = key01step(key1, dic_ed)  #  последний интервал выпавшего числа ##############
        add_step_to_all_1(dic_ed) # добавление шагов всем еденицам #############################
################################################################################################
        # проверочный - dictEd = {(36): [23, [1, 2], 33]
       # print('последний интервал выпавшего числа:',interval)  # проверка функции возращающей последний интервал выпавшего числа



    print('111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    keyer = len(list_of200_1)
    print(naime_file)
    print(list_of_all_Win_1, 'list_of_all_Win_1')
    # print(list_of_win_and_steps,'list_of_win_and_steps')
    print(list_of_steps_toWin_1,'list_of_steps_toWin_1')
    # print( list_of_winSteps_and_steps,'list_of_winSteps_and_steps')
    print('последние шаги', list_of_win_proverki_1[0])
    if list_of_win_proverki_1[0]<36:
        ubyl_v_konce = list_of_win_proverki_1[0]*0.01
    if (list_of_win_proverki_1[0] > 35) and (list_of_win_proverki_1[0] < 54):
        ubyl_v_konce = (list_of_win_proverki_1[0] -35) * 0.02+0.35
    if (list_of_win_proverki_1[0] > 53) and (list_of_win_proverki_1[0] < 66):
        ubyl_v_konce = (list_of_win_proverki_1[0] -53) * 0.03 + 0.71
    if (list_of_win_proverki_1[0] > 65) and (list_of_win_proverki_1[0] < 75):
        ubyl_v_konce = (list_of_win_proverki_1[0] -65) * 0.04 + 1.07
    if (list_of_win_proverki_1[0] > 74) and (list_of_win_proverki_1[0] < 82):
        ubyl_v_konce = (list_of_win_proverki_1[0] -74) * 0.05 + 1.43
    if (list_of_win_proverki_1[0] > 81) and (list_of_win_proverki_1[0] < 88):
        ubyl_v_konce = (list_of_win_proverki_1[0] -81) * 0.06 + 1.78
    if (list_of_win_proverki_1[0] > 87) and (list_of_win_proverki_1[0] < 93):
        ubyl_v_konce = (list_of_win_proverki_1[0] -87) * 0.07 + 2.14
    if (list_of_win_proverki_1[0] > 92) and (list_of_win_proverki_1[0] < 97):
        ubyl_v_konce = (list_of_win_proverki_1[0] -92) * 0.08 + 2.48
    if (list_of_win_proverki_1[0] > 96) and (list_of_win_proverki_1[0] < 101):
        ubyl_v_konce = (list_of_win_proverki_1[0] - 96) * 0.09 + 2.81
    if (list_of_win_proverki_1[0] > 100) and (list_of_win_proverki_1[0] < 105):
        ubyl_v_konce = (list_of_win_proverki_1[0] - 100) * 0.10 + 3.17
    if (list_of_win_proverki_1[0] > 104) and (list_of_win_proverki_1[0] < 108):
        ubyl_v_konce = (list_of_win_proverki_1[0] - 104) * 0.11 + 3.57
    if (list_of_win_proverki_1[0] > 107) and (list_of_win_proverki_1[0] < 111):
        ubyl_v_konce = (list_of_win_proverki_1[0] - 107) * 0.12 + 3.9
    if (list_of_win_proverki_1[0] > 110) and (list_of_win_proverki_1[0] < 114):
        ubyl_v_konce = (list_of_win_proverki_1[0] - 110) * 0.13 + 4.26
    if (list_of_win_proverki_1[0] > 113) and (list_of_win_proverki_1[0] < 116):
        ubyl_v_konce = (list_of_win_proverki_1[0] - 113) * 0.14 + 4.65
    if (list_of_win_proverki_1[0] > 115) and (list_of_win_proverki_1[0] < 119):
        ubyl_v_konce = (list_of_win_proverki_1[0] - 115) * 0.15 + 4.93

    if list_of_win_proverki_1[0] > 118:
        ubyl_v_konce = 5.38


    print('ubyl v konce: ',ubyl_v_konce)
    pribyl = podchet_balansa(list_of_steps_toWin_1) - ubyl_v_konce
    print('pribyl: ',podchet_balansa(list_of_steps_toWin_1) - ubyl_v_konce)
    print('best: ',best_chisla )
    pribyl2 = pribyl2+ pribyl
    # print('2222222222222222222222222222222222222222222222222222222222222222222222222222222222')
    # keyer = len(list_of200_2)
    # print(list_par_of200_2[key])
    # print(list_of_all_Win_2)
    # print(list_of_steps_toWin_2)
    # print('pribyl: ',podchet_balansa(list_of_steps_toWin_2))
    #print(dic_ed[(supwiner)])
    # print('chet: ', chet)
    # print('nechet: ',nechet)
    # print('nol:',nol)
    # print('raznica_chet_nechet',chet-nechet)
    # for i in range(37):
    #  print(i,': ',dic_ed[(i)])
    #rasnica=vig-prg
    #print("разница:",rasnica)
print('pribyl2: ', pribyl2)
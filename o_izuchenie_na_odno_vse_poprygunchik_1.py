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
    result = list_of_win_proverki
    if list_of_win_proverki[3]==0: # проверка если до прыжка один подсчет
      if list_of_win_proverki[0]< 37:
        if key == list_of_win_proverki[2]:
            list_of_win_proverki[1] = 1 # если еденица назначить новое число предсказания
            list_of_win_proverki[5] = list_of_win_proverki[5]+35
            result = list_of_win_proverki  # первое значение - количество шагоd
                    # второе значени флаг сброса продолжения проверки
                  # третье значение предсказаное число
        else:
            list_of_win_proverki[1] = 0
            list_of_win_proverki[0] = list_of_win_proverki[0] +1
            list_of_win_proverki[6] = list_of_win_proverki[6] + 1
            result = list_of_win_proverki
        if (list_of_win_proverki[0] > 36) and (list_of_win_proverki[0] < 55):
            if key == list_of_win_proverki[2]:
                list_of_win_proverki[1] = 1  # если еденица назначить новое число предсказания
                list_of_win_proverki[5] = list_of_win_proverki[5] + 70
                result = list_of_win_proverki  # первое значение - количество шагоd
            # второе значени флаг сброса продолжения проверки
            # третье значение предсказаное число
            else:
                list_of_win_proverki[1] = 0
                list_of_win_proverki[0] = list_of_win_proverki[0] + 1
                list_of_win_proverki[6] = list_of_win_proverki[6] + 2
                result = list_of_win_proverki
        if winer_1 == 99: # типа обозначение паузы?
            list_of_win_proverki[0] = list_of_win_proverki[0] - 1
            result = list_of_win_proverki
    if list_of_win_proverki[3] == 1:  # проверка если до прыжка один подсчет
            if list_of_win_proverki[0] < 18:
                if key == list_of_win_proverki[2]:
                    list_of_win_proverki[1] = 1  # если еденица назначить новое число предсказания
                    list_of_win_proverki[5] = list_of_win_proverki[5] + 140
                    result = list_of_win_proverki  # первое значение - количество шагоd
                    # второе значени флаг сброса продолжения проверки
                    # третье значение предсказаное число
                else:
                    list_of_win_proverki[1] = 0
                    list_of_win_proverki[0] = list_of_win_proverki[0] + 1
                    list_of_win_proverki[6] = list_of_win_proverki[6] + 4
                    result = list_of_win_proverki
                if (list_of_win_proverki[0] > 18) and (list_of_win_proverki[0] < 37):
                    if key == list_of_win_proverki[2]:
                        list_of_win_proverki[1] = 1  # если еденица назначить новое число предсказания
                        list_of_win_proverki[5] = list_of_win_proverki[5] + 240
                        result = list_of_win_proverki  # первое значение - количество шагоd
                    # второе значени флаг сброса продолжения проверки
                    # третье значение предсказаное число
                    else:
                        list_of_win_proverki[1] = 0
                        list_of_win_proverki[0] = list_of_win_proverki[0] + 1
                        list_of_win_proverki[6] = list_of_win_proverki[6] + 8
                        result = list_of_win_proverki
                if winer_1 == 99:  # типа обозначение паузы?
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
    pribyl=0
    
    for item in spisok:
        if item <37:
          pribyl = pribyl + 36 - item
        if (item < 55) and (item >36):
           pribyl = pribyl + ((72-36) - (item-36)*2)
        if (item > 54):
            pribyl = pribyl - 72
    return  pribyl


rasnica2 =0
ik = 0
vig = 0
prg = 0
chag = 0
nol =0

i=0
for i in range(138,143): #while (ik < 1):
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
   # print("выборка",len(viborka))
    chet=0
    nechet=0
    list_of200_1 = []
    list_par_of200_1 = []
    list_of_win200_1 = []
    list_of200_2 = []
    list_par_of200_2 = []
    list_of_win200_2 = []

    winer_1 = 0
    winer_2 = 0
    supwiner = 0
    ste_ps_1 = 0
    ste_ps_2 = 0
    steps_of_win_1 = 0
    steps_of_win_2 = 0
    list_of_win_proverki_1 = [0,0,0,0,0,0,0] # первая цифра- подсчет шагов до выигрыша,
    # вторая - активное ли предсказание, третья предсказанное число, четвертое перескок,
    # пятое прибыль, шестое убыль
    list_of_win_proverki_2 = [0,0,0]
    steps_to_win_1 = 0
    steps_to_win_2 = 0
    list_of_steps_toWin_1 = []
    list_of_steps_toWin_2 = []
    list_of_all_Win_1 = []
    list_of_all_Win_2 = []
    best_chisla =[]
    while (steps < len(viborka)):
        key = viborka[steps]
        key1 = key
        steps = steps + 1
        ############################################################################################
        # БЛОК ЕДЕНИЦЫ
        ############################################################################################
        list_of_win_proverki_1 = proverka_predskaza_1(key1, list_of_win_proverki_1, winer_1)

        if winer_1 != 99:
            if  list_of_win_proverki_1[1] == 1:
                if list_of_win_proverki_1[3] ==1:
                    steps_to_win_1 = list_of_win_proverki_1[0]
                    list_of_all_Win_1.append(list_of_win_proverki_1[2])
                    supwiner = list_of_win_proverki_1[2]
                    list_of_win_proverki_1[2] = winer_1 # назначение нового числа предсказания
                    list_of_steps_toWin_1.append(steps_to_win_1)
                    list_of_win_proverki_1[0]=1
                else:
                    steps_to_win_1 = list_of_win_proverki_1[0]
                    list_of_all_Win_1.append(list_of_win_proverki_1[2])
                    supwiner = list_of_win_proverki_1[2]
                    list_of_win_proverki_1[2] = winer_1  # назначение нового числа предсказания
                    list_of_steps_toWin_1.append(steps_to_win_1)
                    list_of_win_proverki_1[0] = 1
               # print(dic_ed[(key)] )
           
            if list_of_win_proverki_1[0] > 54:
                list_of_steps_toWin_1.append(list_of_win_proverki_1[0])
                list_of_win_proverki_1[0] = 1
                list_of_win_proverki_1[1] = 0
                list_of_win_proverki_1[2] = winer_1
                list_of_win_proverki_1[3] = 1
        
        list_of200_1 =   pre1_predskazatel_1(key1,list_of200_1,10) # шаг нахождения винера##############################################################
        #if steps > 400:
        list_par_of200_1 = pre2_predskazatel_1(list_of200_1)
        winer_1 =  pre3_predskazatel_1(list_par_of200_1)
        best_chisla = pre3_predskazatel_1_all(list_par_of200_1)
       

        dob_next_seen_1(dic_ed,key, steps) # создание\ обновление словаря едениц
        interval = key01step(key1, dic_ed)  #  последний интервал выпавшего числа
        add_step_to_all_1(dic_ed) # добавление шагов всем еденицам

        # проверочный - dictEd = {(36): [23, [1, 2], 33]}
       # print('chet: ',chet, ' nechet: ',nechet)
        #print('разница: ', chet - nechet)
        # chislo1 = random.randint(0, 36)
        all_odd= podchet_interv_odd(dic_ed)
        #print('подсчет интервалов нечет: ',all_odd)
            #podchet_interv_odd(dic_ed)
        # chislo1 = random.randint(0, 36)
        all_even = podchet_interv_iven(dic_ed)
        #print('подсчет интервалов чет: ', all_even)
        #podchet_interv_iven(dic_ed)
        index_predscazan = all_odd- all_even
        #print(steps,'raznica_chet_nechet2', chet - nechet-nol)
        #print('разница: ', chet - nechet)
        # if chet != nechet:
        #     if nechet > chet:
        #         win = "выиграет odd"
        #         win1 = False
        #     else:
        #         win = "выиграет even"
        #         win1 = True
        # print( win)
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
        #if key == supwiner:
         # print('winer: ',key, dic_ed[(key)])
    #print('список интервалов',listAll_inter)
    # print('spisok_vnesh2',spisok_vnesh2)
    with open('intervals_all.txt', 'w') as jsonfile: json.dump(listAll_inter, jsonfile)
    int_count = podchet_simv(listAll_inter)
    int_count = sorted(int_count.items(), key=lambda x: x[1], reverse=True)
    [(4, 74), (2, 47), (3, 32), (0, 17), (1, 12)]
    # print('количество рзных символов',int_count )
    # print('количество шагов биг',steps_big )
    #print('Выиграл:',Viigral)
    #print('Проиграл:',Proigral)
    vig=vig+Viigral
    prg=prg+Proigral
    rasnica2 = vig - prg
    # if rasnica2> 100:
    #     break
    chag=chag+1
    rasnica=Viigral-Proigral

    #print(rasnica)
    # if rasnica> 100:
    #     break
    #postrocno(int_count)
    #print('словарь едениц',dic_ed)
    #print('chag', chag)

# postrocno(bad_pred,'Bad')
# postrocno(good_pred,'Good')
# print('Выиграл:',vig)
# print('Проиграл:',prg)
#print(key)
    print('111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    keyer = len(list_of200_1)
    priboy = 0
    uboy = 0
    # for item in range(len(list_of_win_proverki_1)):
    #     priboy = priboy+list_of_win_proverki_1[5]
    #     uboy = uboy + list_of_win_proverki_1[6]
    print('suroy result:', priboy - uboy)
    print(naime_file)
    print(list_of_all_Win_1) # список выигрышных чисел
    print(list_of_steps_toWin_1) # список интервалов до выигрыша
    print('pribyl: ',podchet_balansa(list_of_steps_toWin_1))
    print('best: ',best_chisla )
   
import json
import random
from time import clock
 #------------- в начале обработка единичных символов
# функция по ключу возращает когда последний раз выпадало число
def last_last_seen_steps_of_simv_01(dict,key): # альтернатива  "last_next_seen_all_steps_1"
    result = dict[key][0]

    #print('функия next_seen_steps =',result)
    return result
# функция  обновляет словарь цифр новыми данными, если числа нет в словаре она его туда вносит
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
# функция печатает список ?
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
# функция вычисляет когда последний раз выпадал номер
def key01step(key, dictEd):
    result = dictEd[(key)][0]
    dictEd[key][0] = 0  # после того как достанет обнуляет
    #print('из функции достающей интервалы result',result )
    #print('из функции достающей интервалы dictEd[(key)][0]', dictEd[(key)][0])
    return result


# key01step = key01step(key,dictEd) # вычисляем когда последний раз был виден выпавший номер



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
        print(name,'стока',i, item)


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
        list_of_win_proverki[1] = 1
        result = list_of_win_proverki  # первое значение - количество шагоd
                # второе значени флаг сброса продолжения проверки
              # третье значение предсказаное число
    else:
        list_of_win_proverki[1] = 0
        list_of_win_proverki[0] = list_of_win_proverki[0] +1
        result = list_of_win_proverki
    if winer_1 == 99:
        list_of_win_proverki[0] = list_of_win_proverki[0] - 1
        result = list_of_win_proverki
    return result
def pre3_predskazatel_couple(list_sort):
    quantity = [0.0]
    list_sort.sort(key = lambda item: item[1])
    list_sort.reverse()
    # nolik = list_sort[0][0]
    # odin = list_sort[1][0]
    # dva = list_sort[2][0]
    # #tri = list_sort[3][0]
    #quantity[0] = list_sort[ind][0]
    #quantity[1] = list_sort[ind][1]
    #result =list_sort[ind][0] # random.choice([nolik,odin,dva] )
    if list_sort[0][1] > 1:
        result = list_sort[0][0]  # random.choice([nolik,odin,dva] )
    else:
        result = 99
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
def sozdan_conteynerov_v_spiske(spisok_conteynerov, steps, winner, spisok_podch_ciklov, dict_ed): # функция добавления/инициализация шагов с последнего появления
    spisok =[0,0,0,0,0,0,0,0,0,0,0,0]
                       # 0 - число
                       # 1 - шаг начала предсказания,
                       # 2 - шаг когда предсказание сбылось
                       # 3 - количество шагов потребовашихся чтоб сбылось предсказание
                       # 4 - баланс предсказания
                       # 5 - хороше или плохое предсказание
                       # 6 - показатель среднего за прошлую игру
                       # 7 - показатель среднего за эту игру
                       # 8 - значение винера, 2- 3- 4 числа попали
                       # 9 - количество промежутков между двумя  числами винер
                       # 10 - количество шаго которое число висело как виннер, перед назначением

                       # 11 - логическая переменная отыграл -0, в игре -1
    spisok[0] = winner
    spisok[1] = steps
    spisok[6] = 10 #spisok_sredn_za_proshl_igru[число][значение среднего за прошлую игру]
    spisok[7] = round((steps / (dict_ed[(spisok[0])][2] + 1)), 1)
    spisok[8] = 2 # из переменной подсчета
    spisok[9] = dict_ed[(key)][0]  # опять таки через словарь цифр, просто значение словаря [-1] если до обработки словаря или [1][-2] после обработки словаря
    if winner == spisok_podch_ciklov[0]:
        spisok[10] = spisok_podch_ciklov[1]
    spisok[11] = 1 # запускаем в игру
    spisok_conteynerov.append(spisok)  # инициализация
    return    spisok_conteynerov                                   #print('key in function =', key)

def proverka_conteynerov_na_pedskazanie(spisok_conteynerov,key, steps,dict_ed):
    for item in   spisok_conteynerov:
       if item[11] ==1:
         if item[0] == key:
            item[2] = steps
            item[3] = steps - item[1]
            item[11] = 0
            #item[7] = round((steps / (dict_ed[(item[0])][2] + 1)), 1)
            if item[3]> 54:
               item[4] = -72
               item[5] = 0
               item[11] = 0
            else:
               if (item[3]< 37):
                   item[4] = 36-item[3]
               item[11] = 0
               if (item[3]> 36)  and (item[3] < 55):
                   item[4] = ((72 - 36) - (item[3] - 36) * 2)


               item[5] = 1
               item[11] = 0
            if item[7] > 18:
                 item[4]=0
             # подсчет среднего за эту игру (если добавлять до прибавления шагов еденице добавить +1 делителю)
           # item[8] = dict_ed # как то подсчитать через словарь цифр и значения первого шага когда назначено лучшим числом
           #  if steps  < 10:
           #       item[4] = 0
        #else:
    return   spisok_conteynerov
# подсчет винера должен стоять ранше инициализации и добавления в список винера
def  spisok_podcheta_serii_winnera(winer_1,spisok_podch_ciklov):  #spisok_podch_ciklov[proshliy winer, kolichestvo ciklov]
          if winer_1 == spisok_podch_ciklov[0]:
              spisok_podch_ciklov[1]=spisok_podch_ciklov[1]+1
              spisok_podch_ciklov[0] = winer_1
          else:
              spisok_podch_ciklov[1] =1
              spisok_podch_ciklov[0] = winer_1
          return spisok_podch_ciklov


rasnica2 =0
ik = 0
vig = 0
prg = 0
chag = 0
nol =0
pribyl =0
ind =0
pribyl_glob = 0

start1 = clock()
k =7
pribyl = 0
spisok_podch_ciklov =[0,0]
spisok_conteynerov=[]
for i in range(1,29):#while (ik < 1):
    ik = ik + 1


    naime_file = str(i)+'cikl_och.txt'
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

    listAll_inter=[] # болванка под список всех интервалов
    log = True

    good_pred=[]
    bad_pred=[]

    #print("выборка",len(viborka))

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
    list_of_win_proverki_1 = [0,0,0]
    list_of_win_proverki_2 = [0,0,0]
    steps_to_win_1 = 0
    steps_to_win_2 = 0
    list_of_steps_toWin_1 = []
    list_of_steps_toWin_2 = []
    list_of_all_Win_1 = []
    list_of_all_Win_2 = []
    best_chisla =[]
    best_chisla_couple = []
    winner_bufer=[]
    spisok_podch_ciklov=[0,0]
    while (steps < len(viborka)):
        key = viborka[steps]
        key1 = key
        steps = steps + 1
        ############################################################################################
        # БЛОК ЕДЕНИЦЫ
        ############################################################################################
        list_of_win_proverki_1 = proverka_predskaza_1(key1, list_of_win_proverki_1,winer_1)
        proverka_conteynerov_na_pedskazanie(spisok_conteynerov, key, steps, dic_ed)

        if  list_of_win_proverki_1[1] == 1:
            steps_to_win_1 = list_of_win_proverki_1[0]
            list_of_all_Win_1.append(list_of_win_proverki_1[2])
            supwiner = list_of_win_proverki_1[2]
            list_of_win_proverki_1[2] = winer_1 # назначение нового числа предсказания
            list_of_steps_toWin_1.append(steps_to_win_1)
            list_of_win_proverki_1[0]=1
           # print(dic_ed[(key)] )
        if list_of_win_proverki_1[0] > 54:
            list_of_steps_toWin_1.append(60)
            list_of_win_proverki_1[0] = 1
            list_of_win_proverki_1[1] = 0
            list_of_win_proverki_1[2] = winer_1

        list_of200_1 =   pre1_predskazatel_1(key1,list_of200_1,k) # шаг нахождения винера##############################################################
        #if steps > 400:
        list_par_of200_1 = pre2_predskazatel_1(list_of200_1)
        winer_1 =  pre3_predskazatel_1(list_par_of200_1)

        best_chisla_couple.append(pre3_predskazatel_couple(list_par_of200_1))
        best_chisla = pre3_predskazatel_1_all(list_par_of200_1)

        dob_next_seen_1(dic_ed,key, steps) # создание\ обновление словаря едениц
        # до добавление еденицы шагам
        if winer_1 != 99:
            spisok_podch_ciklov = spisok_podcheta_serii_winnera(winer_1, spisok_podch_ciklov)
            spisok_conteynerov = sozdan_conteynerov_v_spiske(spisok_conteynerov, steps, winer_1, spisok_podch_ciklov, dic_ed)

        interval = key01step(key1, dic_ed)  #  последний интервал выпавшего числа
        add_step_to_all_1(dic_ed) # добавление шагов всем еденицам
        #if winer_1 != 99:
        #print(steps,'winer', winer_1, key)
        key1step = interval
        #if key == supwiner:
         # print('winer: ',key, dic_ed[(key)])

        #print(steps,'winer',spisok_conteynerov)
    pribyl =podchet_balansa(list_of_steps_toWin_1)
    print(k,'obch_pribyl: ', pribyl)

pribyl_glob = pribyl_glob+pribyl
summa=0
for item in spisok_conteynerov:
    print(item)
    summa= summa+item[4]

print('summa', summa)
# end1 = clock()
# print(ind, 'glob_pribyl: ', pribyl_glob, 'Время:', (end1 - start1)/60)
#print('2222222222222222222222222222222222222222222222222222222222222222222222222222222222')
# print(list_of_all_Win_2)
# print(list_of_steps_toWin_2)
# print('pribyl: ',podchet_balansa(list_of_steps_toWin_2))
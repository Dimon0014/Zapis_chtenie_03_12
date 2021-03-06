import json
import random
from datetime import datetime, timedelta
from time import clock
# ------------- в начале обработка единичных символов
import math


def last_last_seen_steps_of_simv_01(dict, key):  # альтернатива  "last_next_seen_all_steps_1"
    result = dict[key][0]

    # print('функия next_seen_steps =',result)
    return result


def dob_next_seen_1(dict, key, steps):  # функция добавления/инициализация шагов с последнего появления

    if (key) in dict:  # проверка на наличие значений
        last_seen = last_last_seen_steps_of_simv_01(dict, key)
        # print('steps-last_time seen_in_key =', last_seen)
        # print('печатает dict[key][1][0]', dict[key][1][0])
        dict[key][1].append(last_seen)
        dict[key][2] = len(dict[key][1])  # сколько раз уже выпадала


    else:  # инициализация
        dict.update({(key): [0, [steps], 1, key, steps]})  # инициализация
        # print('key in function =', key)


def add_step_to_all_1(dict):
    for item in dict:
        dict[item][0] = dict[item][0] + 1
        dict[item][4] = dict[item][4] + 1


def more_of_1(dict):
    spisok = []
    a = 0
    s = 0
    spisok2 = []
    for item in dict:
        if dict[item][2] == 1:

            if dict[item][4] > 100:

                spisok.append(dict[item])
                if len(spisok) > 0:
                    a = dict[item][3]
                    s = dict[item][4]

                    # print('spisok', spisok)
                    spisok2.append(a)
                    spisok2.append(s)
                    # print('spisok2', spisok2)
                break

                # print("номер", dict[item][3], "выпал", dict[item][2], "раз(а)--шаг", dict[item][4])
    return spisok2


def podchet_simv(slist):  # подсчет сколько раз встречаются символы в строке(списке)
    d = dict()
    for c in slist:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d


# отсюда функции патернов-------------------------------
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
    # print('из функции достающей интервалы result',result )
    # print('из функции достающей интервалы dictEd[(key)][0]', dictEd[(key)][0])
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
def postrocno(spisok, name):
    i = 0
    for item in spisok:
        i = i + 1
        print(steps, name, 'стока', i, item)


def stepsbig(interval, porog, steps_big):
    steps_big
    if interval < porog:
        steps_big = steps_big + 1
    return steps_big


def podchet_interv_odd(slovar):
    obshie = 0
    rezult = 0
    for item in slovar:
        if (slovar[item][3] % 2) != 0:
            if (slovar[item][0]) < 1000:
                rezult = obshie + slovar[item][2]

    return rezult


def podchet_interv_iven(slovar):
    obshie = 0
    rezult = 0
    for item in slovar:
        if (slovar[item][3] % 2) == 0:
            if (slovar[item][0]) < 1000:
                rezult = obshie + slovar[item][2]
    return rezult


def nahogd_big_interv(slovar):
    rezult = 0
    big = 0
    for item in slovar:

        if (slovar[item][0]) > big:
            rezult = slovar[item][3]
            slovar[item][0] = big
    return rezult


def pre1_predskazatel_1(key, list_of200, steps_of_predscazan):
    keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
            29, 30, 31, 32, 33, 34, 35, 36]
    list = list_of200

    for item in keys:
        if item == key:
            list.append(key)
            if len(list) > steps_of_predscazan:
                list.pop(0)
    return list


def pre2_predskazatel_1(list_of200):
    keys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
            29, 30, 31, 32, 33, 34, 35, 36]
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


def pre3_predskazatel_1(list_sort):
    list_sort.sort(key=lambda item: item[1])
    list_sort.reverse()
    # nolik = list_sort[0][0]
    # odin = list_sort[1][0]
    # dva = list_sort[2][0]
    # #tri = list_sort[3][0]
    # result =list_sort[0][0] # random.choice([nolik,odin,dva] )
    if list_sort[0][1] > 1:
        result = list_sort[0][0]  # random.choice([nolik,odin,dva] )
    else:
        result = 99
    return result


def pre3_predskazatel_1_all(list_sort):
    list_sort.sort(key=lambda item: item[1])
    list_sort.reverse()
    # nolik = list_sort[0][0]
    # odin = list_sort[1][0]
    # dva = list_sort[2][0]
    # #tri = list_sort[3][0]
    result = list_sort  # random.choice([nolik,odin,dva] )

    return result


def proverka_predskaza_1(key, list_of_win_proverki, winer_1):
    if key == list_of_win_proverki[2]:
        list_of_win_proverki[
            1] = 1  # включение происходит в двух случаях при выигрыше и при превышении количества 54 шагов
        result = list_of_win_proverki  # первое значение - количество шагоd
        # второе значени флаг сброса продолжения проверки
        # третье значение предсказаное число
    else:
        list_of_win_proverki[1] = 0
        list_of_win_proverki[0] = list_of_win_proverki[
                                      0] + 1  # так как else наступает и в случае (winer_1 == 99) - когда
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
        list_of_win_proverki[0] = list_of_win_proverki[0] + 1
        result = list_of_win_proverki
    return result


def podchet_simv(slist):  # подсчет сколько раз встречаются символы в строке(списке)
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
        if item == 1 :
            pribyl = pribyl + 0.35  # - (item*0.01)
        if item == 2 :
            pribyl = pribyl + 0.34  # - (item*0.01)
        if item == 3 :
            pribyl = pribyl + 0.33  # - (item*0.01)

        if item == 4:
            pribyl = pribyl + 0.32  # - (item*0.01)

        if item == 5:
            pribyl = pribyl + 0.31  # - (item*0.01)

        if item == 6:
            pribyl = pribyl + 0.30  # - (item*0.01)
        ########################################################## +0.06
        if item == 7:
            pribyl = pribyl + 0.64  # - (item*0.01)

        if item == 8:
            pribyl = pribyl + 0.62  # - (item*0.01)
        if item == 9:
            pribyl = pribyl + 0.60  # - (item*0.01)
        if item == 10:
            pribyl = pribyl + 0.58  # - (item*0.01)
        if item == 11:
            pribyl = pribyl + 0.56  # - (item*0.01)
        if item == 11:
            pribyl = pribyl + 0.54  # - (item*0.01)
        if item == 12:
            pribyl = pribyl + 0.52  # - (item*0.01)
        if item == 13:
            pribyl = pribyl + 0.50  # - (item*0.01)
        if item == 14:
            pribyl = pribyl + 0.48  # - (item*0.01)
        if item == 15:
            pribyl = pribyl + 0.46  # - (item*0.01)
        if item == 16:
            pribyl = pribyl + 0.44  # - (item*0.01)
        if item == 17:
            pribyl = pribyl + 0.42  # - (item*0.01)
        if item == 18:
            pribyl = pribyl + 0.40  # - (item*0.01)
        if item == 19:
            pribyl = pribyl + 0.38  # - (item*0.01)
        if item == 20:
            pribyl = pribyl + 0.36  # - (item*0.01)
        if item == 21:
            pribyl = pribyl + 0.34  # - (item*0.01)
        if item == 22:
            pribyl = pribyl + 0.32  # - (item*0.01)
        if item == 23:
            pribyl = pribyl + 0.30  # - (item*0.01)
        ###########################################################      +0.36 =0.42
        if item == 24:
            pribyl = pribyl + 0.66  # - (item*0.01)

        if item == 25:
            pribyl = pribyl + 0.63  # - (item*0.01)
        if item == 26:
            pribyl = pribyl + 0.60  # - (item*0.01)
        if item == 27:
            pribyl = pribyl + 0.57  # - (item*0.01)
        if item == 28:
            pribyl = pribyl + 0.54  # - (item*0.01)
        if item == 29:
            pribyl = pribyl + 0.51  # - (item*0.01)
        if item == 30:
            pribyl = pribyl + 0.48  # - (item*0.01)
        if item == 31:
            pribyl = pribyl + 0.45  # - (item*0.01)
        if item == 32:
            pribyl = pribyl + 0.42  # - (item*0.01)
        if item == 33:
            pribyl = pribyl + 0.39  # - (item*0.01)
        if item == 34:
            pribyl = pribyl + 0.36  # - (item*0.01)
        if item == 35:
            pribyl = pribyl + 0.33  # - (item*0.01)
        if item == 36:
            pribyl = pribyl + 0.30  # - (item*0.01)
        # if (item > 0) and (item < 37):
        #     pribyl = pribyl + 0.35 #- (item*0.01)





        # if (item < 55) and (item >36):
        #    pribyl = pribyl + ((72-36) - (item-36)*2)
        # if (item > 35)  and (item < 54):
        #     pribyl = pribyl + 0.35*2 - (item * 0.01)*2
        #
        # if (item  > 53) and (item  < 66):
        #     pribyl = pribyl + 0.35 * 3 - (item * 0.01) * 3
        #
        # if (item > 65) and (item < 75):
        #     pribyl = pribyl + 0.35 * 4 - (item * 0.01) * 4
        # if (item > 74) and (item < 82):
        #     pribyl = pribyl + 0.35 * 5 - (item * 0.01) * 5
        #
        # if (item > 81) and (item < 88):
        #     pribyl = pribyl + 0.35 * 6 - (item * 0.01) * 6
        # if (item > 87) and (item < 93):
        #     pribyl = pribyl + 0.35 * 7 - (item * 0.01) * 7
        # if (item > 92) and (item < 97):
        #     pribyl = pribyl + 0.35 * 8 - (item * 0.01) * 8
        # if (item > 96) and (item < 101):
        #     pribyl = pribyl + 0.35 * 9 - (item * 0.01) * 9
        # if (item > 100) and (item < 105):
        #     pribyl = pribyl + 0.35 * 10 - (item * 0.01) * 10
        #
        # if (item > 104) and (item < 108):
        #     pribyl = pribyl + 0.35 * 11 - (item * 0.01) * 11
        # if (item > 107) and (item < 111):
        #     pribyl = pribyl + 0.35 * 12 - (item * 0.01) * 12
        #
        # if (item > 110) and (item < 114):
        #     pribyl = pribyl + 0.35 * 13 - (item * 0.01) * 13
        # if (item > 113) and (item < 116):
        #     pribyl = pribyl + 0.35 * 14 - (item * 0.01) * 14
        # if (item > 115) and (item < 119):
        #     pribyl = pribyl + 0.35 * 15 - (item * 0.01) * 15
        if item == 37:
            pribyl = pribyl -0.81
    return pribyl


rasnica2 = 0
ik = 0
vig = 0
prg = 0
chag = 0
nol = 0
real_pribyl = 0
pribyl2 = 0
neuch = ''
neuch2 = 0
i = 0
next_nol = 0
uchet_intervala = 0
for i in range(1200, 1286):  # while (ik < 1): # количество файлов
    # ik = ik + 1
    # file_obj = open('200cikl_ochh.txt', 'w')
    # file_obj.close()
    # file_obj = open('200cikl_ochh.txt', 'a')
    # for i in range(200+1):               # количество ходов в файле
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
    dic_ed = {}  # болванка под словарь едениц
    # -----------------------------------------------------------------------------------
    key = 0
    steps_sesia = 1
    key1 = key
    steps = 0

    # print("выборка",len(viborka))
    chet = 0
    nechet = 0
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
    # пятое прибыль, шестое убыль,
    # седьмое номер игрового цикла.

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
    list_of_win_and_steps = []
    list_of_winSteps_and_steps = []
    urezanuy_spisok = []
    best_chisla = []
    chislo_stavok = 0

    chislo_levyh_stavok = 0
    razreshenie_na_stavku = False
    sum_of_stavok = 0
    sum_of_win = 0
    now_name = datetime.now()
    tme_name = now_name.strftime("%d,%m,%y %H.%M.%S")
    name_of_log_stavok = 'stavki_' + '_data ' + tme_name + '.txt'
    file_obj_log = open(name_of_log_stavok, 'a')
    buffer_shagov = 0
    otdel_podchet_stavok = 0
    tecuchajaStavka = 99
    kolichestvoVyigrashey = 0
    razreshenie_na_stavku_2 = True
    razmer_stavki = 0.01
    stavka = 99
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
        # print(steps,'list_of_win_proverki_1[0]', list_of_win_proverki_1[0])
        # if list_of_win_proverki_1[0] > buffer_shagov:
        #     otdel_podchet_stavok = otdel_podchet_stavok+1
        #     #print('list_of_win_proverki_1[0]',list_of_win_proverki_1[0])
        #     buffer_shagov = list_of_win_proverki_1[0]
        # if (key1 == tecuchajaStavka) and list_of_win_proverki_1[7] == 1:
        #     list_of_win_proverki_1[7] = list_of_win_proverki_1[7] + 1
        #     razreshenie_na_stavku = False
        # if (key1 == tecuchajaStavka) and razreshenie_na_stavku:
        #     kolichestvoVyigrashey = kolichestvoVyigrashey + 1
        #     print(steps, '      vyigrysh n:', kolichestvoVyigrashey, '#', 'vyigrysh vypal na: ', key1,
        #           '#  shag stavok:', list_of_win_proverki_1[0])
        #     if razmer_stavki == 0.01:
        #         sum_of_win = sum_of_win + 0.35
        #         list_of_win_proverki_1[7] = list_of_win_proverki_1[7] + 1
        #         razreshenie_na_stavku = False
        #     if razmer_stavki == 0.02:
        #         print(' AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAprib: 70, na shage: ', steps)
        #         sum_of_win = sum_of_win + 0.70
        #         list_of_win_proverki_1[7] = list_of_win_proverki_1[7] + 1
        #         razreshenie_na_stavku = False
        #         razmer_stavki = 0.01
                      ##############################################################################################3
                #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
                # if (item > 0) and (item < 36):
                #     pribyl = pribyl + 0.35 - (item * 0.01)
                # # if (item < 55) and (item >36):
                # #    pribyl = pribyl + ((72-36) - (item-36)*2)
                # if (item > 35) and (item < 54):
                #     pribyl = pribyl + 0.35 * 2 - (item * 0.01) * 2
                #
                # if (item > 53) and (item < 66):
                #     pribyl = pribyl + 0.35 * 3 - (item * 0.01) * 3
                #
                # if (item > 65) and (item < 75):
                #     pribyl = pribyl + 0.35 * 4 - (item * 0.01) * 4
                # if (item > 74) and (item < 82):
                #     pribyl = pribyl + 0.35 * 5 - (item * 0.01) * 5
                #
                # if (item > 81) and (item < 88):
                #     pribyl = pribyl + 0.35 * 6 - (item * 0.01) * 6
                # if (item > 87) and (item < 93):
                #     pribyl = pribyl + 0.35 * 7 - (item * 0.01) * 7
                # if (item > 92) and (item < 97):
                #     pribyl = pribyl + 0.35 * 8 - (item * 0.01) * 8
                # if (item > 96) and (item < 101):
                #     pribyl = pribyl + 0.35 * 9 - (item * 0.01) * 9
                # if (item > 100) and (item < 105):
                #     pribyl = pribyl + 0.35 * 10 - (item * 0.01) * 10
                #
                # if (item > 104) and (item < 108):
                #     pribyl = pribyl + 0.35 * 11 - (item * 0.01) * 11
                # if (item > 107) and (item < 111):
                #     pribyl = pribyl + 0.35 * 12 - (item * 0.01) * 12
                #
                # if (item > 110) and (item < 114):
                #     pribyl = pribyl + 0.35 * 13 - (item * 0.01) * 13
                # if (item > 113) and (item < 116):
                #     pribyl = pribyl + 0.35 * 14 - (item * 0.01) * 14
                # if (item > 115) and (item < 119):
                #     pribyl = pribyl + 0.35 * 15 - (item * 0.01) * 15
                # if item == 119:
                #     pribyl = pribyl - 5.54
                #AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA

        if winer_1 != 99:  # если предсказание не на паузе

            # if steps ==137:
            #     print('key1 ', key1, 'list_of_win_proverki_1[2] ', list_of_win_proverki_1[2])
            # if steps == 155:
            #         print('key1 ', key1, 'list_of_win_proverki_1[2] ', list_of_win_proverki_1[2])
            if list_of_win_proverki_1[2] == key1:
                # if list_of_win_proverki_1[0]>0 and list_of_win_proverki_1[0]< 37:
                ######        #sum_of_win = sum_of_win + 35
                file_obj_log.write('      step: ' + str(steps) + ' vyigrush na: ' + str(
                    list_of_win_proverki_1[2]) + ' na shage: ' + str(list_of_win_proverki_1[0]) + '\n')
                buffer_shagov = 0
            list_of_win_proverki_1 = proverka_predskaza_1(key1, list_of_win_proverki_1, winer_1)

            # print('активность предсказа', list_of_win_proverki_1[1])
            if list_of_win_proverki_1[1] == 1:  # если предсказание активно то
                # print('активность предсказа', list_of_win_proverki_1[1],'        проскочил')
                steps_to_win_1 = list_of_win_proverki_1[
                    0]  # забираем в буферную переменную количество шагов до выигрыша
                list_of_win_and_steps.append(list_of_win_proverki_1[2])
                list_of_win_and_steps.append(steps)
                list_of_all_Win_1.append(list_of_win_proverki_1[2])

                # list_of_all_Win_1_and_steps.append(list_of_win_and_steps)
                supwiner = list_of_win_proverki_1[2]
                # if  steps_to_win_1<34:
                list_of_win_proverki_1[
                    2] = winer_1  # назначение нового числа предсказания _ назначение с опаздыванием на один шаг
                # if steps_to_win_1 == 19:
                #     print('19-ka na shage: ', steps)
                list_of_steps_toWin_1.append(steps_to_win_1)
                list_of_winSteps_and_steps.append(steps_to_win_1)
                list_of_winSteps_and_steps.append(steps)
                list_of_win_proverki_1[0] = 1  # обнуляем количество шагов до выигрыша
                if list_of_win_proverki_1[0] == 1:
                    buffer_shagov = 0
                    # if (steps > 150)and (list_of_win_proverki_1[0] == 1): #################################### если начинается новый цикл
                    #     print('-------------------------------------------------------------------------------выходим из программы на шаге: ', steps, 'neuch',list_of_win_proverki_1[0])
                    #     break
                    # print(dic_ed[(key)] )
            if list_of_win_proverki_1[0] > 36:
                # print('list_of_win_proverki_1[2]',list_of_win_proverki_1[2] )
                list_of_steps_toWin_1.append(37)
                stavka = 0.01
                list_of_win_proverki_1[0] = 1
                list_of_win_proverki_1[1] = 0
                winer_1 = 99
                # list_of_win_proverki_1[2] = winer_1
                # list_of_win_proverki_1[2] = winer_1 # назначение нового числа предсказания _ назначение с опаздыванием на один шаг

        list_of200_1 = pre1_predskazatel_1(key1, list_of200_1,
                                           6)  # шаг нахождения винера##############################################################№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№№
        # if steps > 400:
        list_par_of200_1 = pre2_predskazatel_1(list_of200_1)

        # print('urezanuy_spisok',urezanuy_spisok)

        winer_1 = pre3_predskazatel_1(list_par_of200_1)
        ######################### start BLOK Stavki
        # print('list_of_win_proverki_1[0]',list_of_win_proverki_1[0],'buffer_shagov',buffer_shagov)
        razreshenie_na_stavku = False
        # if ((list_of_win_proverki_1[0]) == 1) and (steps>90):
        #     break
        # if (list_of_win_proverki_1[0] > buffer_shagov) and (list_of_win_proverki_1[0] < 37) and (stavka != 2):
        #     # otdel_podchet_stavok = otdel_podchet_stavok + 1
        #     # if list_of_win_proverki_1[0] == 0:
        #     #     stavka = 32
        #     # elif list_of_win_proverki_1[0] == 1:
        #     #     stavka = 20
        #     # elif list_of_win_proverki_1[0] == 2:
        #     #     stavka = 25
        #     # elif list_of_win_proverki_1[0] == 3:
        #     #     stavka = 26
        #     # elif list_of_win_proverki_1[0] == 4:
        #     #     stavka = 21
        #     # elif list_of_win_proverki_1[0] == 5:
        #     #     stavka = 24
        #     # elif list_of_win_proverki_1[0] == 6:
        #     #     stavka = 27
        #     # elif list_of_win_proverki_1[0] == 7:
        #     #     stavka = 28
        #     # elif list_of_win_proverki_1[0] == 8:
        #     #     stavka = 23
        #     # elif list_of_win_proverki_1[0] == 9:
        #     #     stavka = 22
        #     # elif list_of_win_proverki_1[0] == 10:
        #     #     stavka = 5
        #     # elif list_of_win_proverki_1[0] == 11:
        #     #     stavka = 30
        #     # elif list_of_win_proverki_1[0] == 12:
        #     #     stavka = 35
        #     # elif list_of_win_proverki_1[0] == 13:
        #     #     stavka = 36
        #     # elif list_of_win_proverki_1[0] == 14:
        #     #     stavka = 31
        #     # elif list_of_win_proverki_1[0] == 15:
        #     #     stavka = 19
        #     # elif list_of_win_proverki_1[0] == 16:
        #     #     stavka = 33
        #     # elif list_of_win_proverki_1[0] == 17:
        #     #     stavka = 34
        #     # elif list_of_win_proverki_1[0] == 18:
        #     #     stavka = 29
        #     # elif list_of_win_proverki_1[0] == 19:
        #     #     stavka = 4
        #     # elif list_of_win_proverki_1[0] == 20:
        #     #     stavka = 14
        #     # elif list_of_win_proverki_1[0] == 21:
        #     #     stavka = 2
        #     # elif list_of_win_proverki_1[0] == 22:
        #     #     stavka = 18
        #     # elif list_of_win_proverki_1[0] == 23:
        #     #     stavka = 10
        #     # elif list_of_win_proverki_1[0] == 24:
        #     #     stavka = 16
        #     # elif list_of_win_proverki_1[0] == 25:
        #     #     stavka = 17
        #     # elif list_of_win_proverki_1[0] == 26:
        #     #     stavka = 0
        #     # elif list_of_win_proverki_1[0] == 27:
        #     #     stavka = 13
        #     # elif list_of_win_proverki_1[0] == 28:
        #     #     stavka = 12
        #     # elif list_of_win_proverki_1[0] == 29:
        #     #     stavka = 7
        #     # elif list_of_win_proverki_1[0] == 30:
        #     #     stavka = 8
        #     # elif list_of_win_proverki_1[0] == 31:
        #     #     stavka = 9
        #     # elif list_of_win_proverki_1[0] == 32:
        #     #     stavka = 15
        #     # elif list_of_win_proverki_1[0] == 33:
        #     #     stavka = 1
        #     # elif list_of_win_proverki_1[0] == 34:
        #     #     stavka = 6
        #     # elif list_of_win_proverki_1[0] == 35:
        #     #     stavka = 3
        #     # elif list_of_win_proverki_1[0] == 36:
        #     #     stavka = 11
        #
        #     # print('   ',list_of_win_proverki_1[0],'predskazanie STAVKA na shag: ',steps+1,'vypadet n: ',list_of_win_proverki_1[2])
        #     buffer_shagov = list_of_win_proverki_1[0]
        #
        #     razreshenie_na_stavku = True
        #     if razreshenie_na_stavku:
        #
        #         # tecuchajaStavka = stavka
        #         tecuchajaStavka = list_of_win_proverki_1[2]
        #         if list_of_win_proverki_1[7] != 1:
        #             chislo_stavok = chislo_stavok + 1
        #             sum_of_stavok = sum_of_stavok + 1
        #             razmer_stavki = 0.01
        #         else:
        #             razreshenie_na_stavku = False
        # else:
        #     chislo_levyh_stavok = chislo_levyh_stavok + 1
        #     tecuchajaStavka = tecuchajaStavka
        #     razreshenie_na_stavku = False
        # if (list_of_win_proverki_1[0] > buffer_shagov) and (list_of_win_proverki_1[0] < 37) and (stavka == 2):
        #     # otdel_podchet_stavok = otdel_podchet_stavok + 1
        #     # if list_of_win_proverki_1[0] == 0:
        #     #     stavka = 32
        #     # elif list_of_win_proverki_1[0] == 1:
        #     #     stavka = 20
        #     # elif list_of_win_proverki_1[0] == 2:
        #     #     stavka = 25
        #     # elif list_of_win_proverki_1[0] == 3:
        #     #     stavka = 26
        #     # elif list_of_win_proverki_1[0] == 4:
        #     #     stavka = 21
        #     # elif list_of_win_proverki_1[0] == 5:
        #     #     stavka = 24
        #     # elif list_of_win_proverki_1[0] == 6:
        #     #     stavka = 27
        #     # elif list_of_win_proverki_1[0] == 7:
        #     #     stavka = 28
        #     # elif list_of_win_proverki_1[0] == 8:
        #     #     stavka = 23
        #     # elif list_of_win_proverki_1[0] == 9:
        #     #     stavka = 22
        #     # elif list_of_win_proverki_1[0] == 10:
        #     #     stavka = 5
        #     # elif list_of_win_proverki_1[0] == 11:
        #     #     stavka = 30
        #     # elif list_of_win_proverki_1[0] == 12:
        #     #     stavka = 35
        #     # elif list_of_win_proverki_1[0] == 13:
        #     #     stavka = 36
        #     # elif list_of_win_proverki_1[0] == 14:
        #     #     stavka = 31
        #     # elif list_of_win_proverki_1[0] == 15:
        #     #     stavka = 19
        #     # elif list_of_win_proverki_1[0] == 16:
        #     #     stavka = 33
        #     # elif list_of_win_proverki_1[0] == 17:
        #     #     stavka = 34
        #     # elif list_of_win_proverki_1[0] == 18:
        #     #     stavka = 29
        #     # elif list_of_win_proverki_1[0] == 19:
        #     #     stavka = 4
        #     # elif list_of_win_proverki_1[0] == 20:
        #     #     stavka = 14
        #     # elif list_of_win_proverki_1[0] == 21:
        #     #     stavka = 2
        #     # elif list_of_win_proverki_1[0] == 22:
        #     #     stavka = 18
        #     # elif list_of_win_proverki_1[0] == 23:
        #     #     stavka = 10
        #     # elif list_of_win_proverki_1[0] == 24:
        #     #     stavka = 16
        #     # elif list_of_win_proverki_1[0] == 25:
        #     #     stavka = 17
        #     # elif list_of_win_proverki_1[0] == 26:
        #     #     stavka = 0
        #     # elif list_of_win_proverki_1[0] == 27:
        #     #     stavka = 13
        #     # elif list_of_win_proverki_1[0] == 28:
        #     #     stavka = 12
        #     # elif list_of_win_proverki_1[0] == 29:
        #     #     stavka = 7
        #     # elif list_of_win_proverki_1[0] == 30:
        #     #     stavka = 8
        #     # elif list_of_win_proverki_1[0] == 31:
        #     #     stavka = 9
        #     # elif list_of_win_proverki_1[0] == 32:
        #     #     stavka = 15
        #     # elif list_of_win_proverki_1[0] == 33:
        #     #     stavka = 1
        #     # elif list_of_win_proverki_1[0] == 34:
        #     #     stavka = 6
        #     # elif list_of_win_proverki_1[0] == 35:
        #     #     stavka = 3
        #     # elif list_of_win_proverki_1[0] == 36:
        #     #     stavka = 11
        #
        #     # print('   ',list_of_win_proverki_1[0],'predskazanie STAVKA na shag: ',steps+1,'vypadet n: ',list_of_win_proverki_1[2])
        #     buffer_shagov = list_of_win_proverki_1[0]
        #
        #     razreshenie_na_stavku = True
        #     if razreshenie_na_stavku:
        #
        #         # tecuchajaStavka = stavka
        #         tecuchajaStavka = list_of_win_proverki_1[2]
        #         if list_of_win_proverki_1[7] != 1:
        #             chislo_stavok = chislo_stavok + 2
        #             sum_of_stavok = sum_of_stavok + 2
        #             razmer_stavki = 0.02
        #         else:
        #             razreshenie_na_stavku = False
        # else:
        #     chislo_levyh_stavok = chislo_levyh_stavok + 1
        #     tecuchajaStavka = tecuchajaStavka
        #     razreshenie_na_stavku = False
        #
        # if list_of_win_proverki_1[0] == 54:
        #     buffer_shagov = 0
        #     # razreshenie_na_stavku_2 =False глобальная не используется сейчас
        #     if steps > 750:
        #         break
        #         # list_of_win_proverki_1[2] =winer_1
        #         ######################### end BLOK Stavki
        #         # if winer_1 !=99:
        #         #     # if list_of_win_proverki_1[0] > buffer_shagov:
        #         #     #     otdel_podchet_stavok = otdel_podchet_stavok + 1
        #         #     #     # print('list_of_win_proverki_1[0]',list_of_win_proverki_1[0])
        #         #     #     buffer_shagov = list_of_win_proverki_1[0]
        #         #         if (list_of_win_proverki_1[0] > 0) and (list_of_win_proverki_1[0] < 55): # ошибка повторы тоже считаются
        #         #         # if (list_of_win_proverki_1[0] > 0) and (list_of_win_proverki_1[0] < 37):
        #         #             if (list_of_win_proverki_1[0] == 54):
        #         #                 chislo_stavok = 0
        #         #             if (list_of_win_proverki_1[0] == 1):
        #         #                 chislo_stavok = 0
        #         #             if list_of_win_proverki_1[2] == key1:
        #         #                 #sum_of_win = sum_of_win+35
        #         #                 chislo_stavok = 0
        #         #
        #         #             #chislo_stavok = chislo_stavok + 1
        #         #             #print('   ', chislo_stavok, 'stavka na:', list_of_win_proverki_1[2])
        #         #             sum_of_stavok = sum_of_stavok+1
        #         #             file_obj_log.write(
        #         #                 'chislo stavok ' + str(sum_of_stavok) + '\n' + 'step: ' + str(steps) + ' stavka na: ' + str(
        #         #                     list_of_win_proverki_1[2])+ '\n')
        #         # else:
        #         #      file_obj_log.write('     propusk iz za prevyshenie porog 54'+ '\n')
        #         # else:
        #         #     print('')
        #         # print('   ', chislo_stavok, 'net stavka na:', list_of_win_proverki_1[2])
        # else:
        #     file_obj_log.write('       propusk iz za winer_1 !=99' + '\n')

        best_chisla = pre3_predskazatel_1_all(list_par_of200_1)
        # if steps == 136:
        #     print('предсказание на 137:','list_of_win_proverki_1[2] :',list_of_win_proverki_1[2] ,'winer_1:', winer_1)
        #     print('количество шагов до выигрыша',list_of_win_proverki_1[0])
        # print('winer_1 ',winer_1 )
        # if winer_1 == 99:
        #     list_of200_1 = pre1_predskazatel_1(key1, list_of200_1,12)  # шаг нахождения винера#####
        #     # if steps > 400:
        #     list_par_of200_1 = pre2_predskazatel_1(list_of200_1)
        #     winer_1 = pre3_predskazatel_1(list_par_of200_1)
        #     best_chisla = pre3_predskazatel_1_all(list_par_of200_1)
        ##################################### --- УЧЕТ ЕДЕНИЦ БЛОК НЕ ТРОГАЕМ --- ######################
        ################################################################################################
        dob_next_seen_1(dic_ed, key, steps)  # создание\ обновление словаря едениц ###############
        interval = key01step(key1, dic_ed)  # последний интервал выпавшего числа ##############
        add_step_to_all_1(dic_ed)  # добавление шагов всем еденицам #############################
        if (steps>140) and (list_of_win_proverki_1[0] == 1):
            break
        if list_of_steps_toWin_1:
          if list_of_steps_toWin_1[0]==37:
            break
    ################################################################################################
    # проверочный - dictEd = {(36): [23, [1, 2], 33]
    # print('последний интервал выпавшего числа:',interval)  # проверка функции возращающей последний интервал выпавшего числа



    print('111111111111111111111111111111111111111111111111111111111111111111111111111111111')
    keyer = len(list_of200_1)
    print(naime_file)
    print(list_of_all_Win_1, 'list_of_all_Win_1')
    print(list_of_win_and_steps, 'list_of_win_and_steps')
    print(list_of_steps_toWin_1, 'list_of_steps_toWin_1')
    print(list_of_winSteps_and_steps, 'list_of_winSteps_and_steps')
    print('summa stavok', sum_of_stavok)
    print('chislo_levyh_stavok', chislo_levyh_stavok)
    # print('otdel_podchet_stavok', otdel_podchet_stavok)
    bonus = sum_of_stavok - otdel_podchet_stavok  ####???
    # print('summa pribuli', sum_of_win)
    print('kollichestvo vyigrushey', sum_of_win / 35)
    # print('real pribul', sum_of_win - (sum_of_stavok))
    # prybyl_rel = sum_of_win - (sum_of_stavok)
    print('list_of_win_proverki_1[0]: ', list_of_win_proverki_1[0])

 #    if list_of_win_proverki_1[0] == 1:
 #        uchet_intervala = 0.01
 #    elif list_of_win_proverki_1[0] == 2:
 #        uchet_intervala = 0.02
 #    elif list_of_win_proverki_1[0] == 3:
 #        uchet_intervala = 0.03
 #    elif list_of_win_proverki_1[0] == 4:
 #        uchet_intervala = 0.04
 #    elif list_of_win_proverki_1[0] == 5:
 #        uchet_intervala = 0.05
 #    elif list_of_win_proverki_1[0] == 6:
 #        uchet_intervala = 0.06
 # ###################################################
 #    elif list_of_win_proverki_1[0] == 7:
 #        uchet_intervala = 0.08
 #    elif list_of_win_proverki_1[0] == 8:
 #        uchet_intervala = 0.10
 #    elif list_of_win_proverki_1[0] == 9:
 #        uchet_intervala = 0.12
 #    elif list_of_win_proverki_1[0] == 10:
 #        uchet_intervala = 0.14
 #    elif list_of_win_proverki_1[0] == 11:
 #        uchet_intervala = 0.16
 #    elif list_of_win_proverki_1[0] == 12:
 #        uchet_intervala = 0.18
 #    elif list_of_win_proverki_1[0] == 13:
 #        uchet_intervala = 0.20
 #    elif list_of_win_proverki_1[0] == 14:
 #        uchet_intervala = 0.22
 #    elif list_of_win_proverki_1[0] == 15:
 #        uchet_intervala = 0.24
 #    elif list_of_win_proverki_1[0] == 16:
 #        uchet_intervala = 0.26
 #    elif list_of_win_proverki_1[0] == 17:
 #        uchet_intervala = 0.28
 #    elif list_of_win_proverki_1[0] == 18:
 #        uchet_intervala = 0.30
 #    elif list_of_win_proverki_1[0] == 19:
 #        uchet_intervala = 0.32
 #    elif list_of_win_proverki_1[0] == 20:
 #        uchet_intervala = 0.34
 #    elif list_of_win_proverki_1[0] == 21:
 #        uchet_intervala = 0.36
 #    elif list_of_win_proverki_1[0] == 22:
 #        uchet_intervala = 0.38
 #    elif list_of_win_proverki_1[0] == 23:
 #        uchet_intervala = 0.40
 #
 #    elif list_of_win_proverki_1[0] == 24:
 #        uchet_intervala = 0.43
 #    elif list_of_win_proverki_1[0] == 25:
 #        uchet_intervala = 0.46
 #    elif list_of_win_proverki_1[0] == 26:
 #        uchet_intervala = 0.49
 #    elif list_of_win_proverki_1[0] == 27:
 #        uchet_intervala = 0.52
 #    elif list_of_win_proverki_1[0] == 28:
 #        uchet_intervala = 0.55
 #    elif list_of_win_proverki_1[0] == 29:
 #        uchet_intervala = 0.58
 #    elif list_of_win_proverki_1[0] == 30:
 #        uchet_intervala = 0.61
 #    elif list_of_win_proverki_1[0] == 31:
 #        uchet_intervala = 0.64
 #    elif list_of_win_proverki_1[0] == 32:
 #        uchet_intervala = 0.67
 #    elif list_of_win_proverki_1[0] == 33:
 #        uchet_intervala = 0.70
 #    elif list_of_win_proverki_1[0] == 34:
 #        uchet_intervala = 0.73
 #    elif list_of_win_proverki_1[0] == 35:
 #        uchet_intervala = 0.77
 #    elif list_of_win_proverki_1[0] == 36:
 #        uchet_intervala = 0.80

    # if list_of_win_proverki_1[0] > 118:
    #     uchet_intervala = 5.39
    # else:
    #     uchet_intervala = list_of_win_proverki_1[0]*0.01
    print('posledniy interval iz shagov', uchet_intervala)
    pribyl = podchet_balansa(list_of_steps_toWin_1) - uchet_intervala
    pribyl_0 = podchet_balansa(list_of_steps_toWin_1)
    print('pribyl: ', pribyl)
    # print('pribyl_0: ', pribyl_0)
    # # print('best: ',best_chisla )
    # if (prybyl_rel < 0) and (pribyl < 0):
    #     print('raznica mejdu real_prib i prib', math.fabs(prybyl_rel) - math.fabs(pribyl))
    # if (prybyl_rel > 0) and (pribyl > 0):
    #     print('raznica mejdu real_prib i prib', prybyl_rel - pribyl)
    # if (prybyl_rel > 0) and (pribyl < 0):
    #     print('raznica mejdu real_prib i prib -', prybyl_rel - pribyl)
    # if (prybyl_rel < 0) and (pribyl > 0):
    #     print('raznica mejdu real_prib i prib -', pribyl - prybyl_rel)
    print('kolichestvoVyigrashey: ', kolichestvoVyigrashey)
    bu = uchet_intervala
    # neuch = str(bu)
    neuch2 = neuch2 + bu
    print('neuchtenka: ', bu)
    print('---------------------------------------------------------------end', naime_file)
    print('steps: ', steps)
    print('-------------nachalo-nachlo-------------------------------------------------start next of', naime_file)
    pribyl2 = pribyl2 + pribyl
    # real_pribyl = real_pribyl + prybyl_rel
    file_obj_log.close()
    # print('2222222222222222222222222222222222222222222222222222222222222222222222222222222222')
    # keyer = len(list_of200_2)
    # print(list_par_of200_2[key])
    # print(list_of_all_Win_2)
    # print(list_of_steps_toWin_2)
    # print('pribyl: ',podchet_balansa(list_of_steps_toWin_2))
    # print(dic_ed[(supwiner)])
    # print('chet: ', chet)
    # print('nechet: ',nechet)
    # print('nol:',nol)
    # print('raznica_chet_nechet',chet-nechet)
    # for i in range(37):
    #  print(i,': ',dic_ed[(i)])
    # rasnica=vig-prg
    # print("разница:",rasnica)
print('---------------------------------------')
print('pribyl2: ', pribyl2)
# print('real_pribyl_all: ', real_pribyl)

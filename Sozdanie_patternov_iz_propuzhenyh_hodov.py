
   # отсюда функции патернов
   # сначала из двух цифр
key3_step=23
key2_step=34
key1 = 36
#listIntervStps_all[]
#dictIntervStps_2{}
#dict_ed[(key)][0] # доступ к словарю выпавшей цифры и ее количеству шагов последний раз когда выпадала
dictEd = {(36):[ 23,[1, 2], 33]}

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
def key01step(key,dictEd):
    result = dictEd[(key)][0]
    return result
# key01step = key01step(key,dictEd) # вычисляем когда последний раз был виден выпавший номер
def intervals_of_2(key2step,key1step,dict2Glob,steps_sesia): # функция добавления интервалов как для глобал так и для локал
        if (key2step,key1step) in dict2Glob: # проверка dict2Glob на наличие ключа, если нет то инициализация

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


def intervals_of_3(key3step, key2step,key1step , dict3Glob,steps_sesia):  # функция добавления интервалов как для глобал так и для локал
    if (key3step, key2step,key1step) in dict3Glob:  # проверка dict2Glob на пустоту, если пусто то инициализация
        last_seen = dict3Glob[(key3step, key2step, key1step)][0]  # переменную последний раз видели загоняем в буфер
        dict3Glob[(key3step, key2step, key1step)][0] = 0  # переменную последний раз видели обнуляем
        dict3Glob[(key3step, key2step, key1step)][1].append(
            last_seen)  # добавляем значение к списку последний раз видели
        count = len(dict3Glob[(key3step, key2step, key1step)][1])  # переменную переменную раз видели загоняем в буфер
        dict3Glob[(key3step, key2step, key1step)][2] = count
        # dict3Glob[(key3step, key2step,key1step)][3] = steps_sesia   #количество шагов в сесии- нужно для предсказания
        #  dict3Glob[(key3step, key2step,key1step)][4] = key3step  # первый символ ключа
        #  dict3Glob[(key3step, key2step,key1step)][5] = key2step   # второй символ ключа
        #  dict3Glob[(key3step, key2step,key1step)][6] = key1step # третий символ ключа
        print(' обновление словаря')
    else:
        dict3Glob.update({(key3step, key2step, key1step): [0, [1], 1, key3step, key2step, key1step, steps_sesia]})  # инициализация
        print(' создание словаря')
def intervals_of_all(key1step,listAll_inter): # список всех подряд интервалов
        listAll_inter.append(key1step)
# функция добавляющая шаги к словарям
def add_step_to_all_intervals_of_2(dict_interv2,key2step, key1step):  # а вот функция которая добовляет всем шаги
     #key=(key2step, key1step)
     for item in dict_interv2:
         # if item != key:

            dict_interv2[item][0] = dict_interv2[item][0] + 1
            dict_interv2[item][3] = dict_interv2[item][3] + 1
            print('dict_interv2[item][0]', dict_interv2[item][0])
            print('dict_interv2[item][3]',dict_interv2[item][3])
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
dict_interv_of2={}
dict_interv_of3={}
interval = key01step(key1,dictEd)
print('печатает последний интервал выпавшего числа:', interval) # проверка функции возращающей последний интервал выпавшего числа
key3step =12
key2step =10
key1step = interval

steps_sesia =34 # нужно для инициализации
intervals_of_2(key2step,key1step,dict_interv_of2,steps_sesia)
print('печатает словар интервалов двоек после создания:', dict_interv_of2)

intervals_of_2(key2step,key1step,dict_interv_of2,steps_sesia)
print('печатает словар интервалов двоек после обновления:', dict_interv_of2)
add_step_to_all_intervals_of_2(dict_interv_of2,key2step, key1step)

print('печатает словар интервалов двоек после добавления\обнуления шагов:', dict_interv_of2)

intervals_of_3(key3step, key2step,key1step , dict_interv_of3,steps_sesia)
print('печатает словар интервалов троек после создания:', dict_interv_of3)
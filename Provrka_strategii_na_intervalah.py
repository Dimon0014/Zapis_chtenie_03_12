import json

with open('intervals_all.txt', 'r') as f:  # извлекаем  из файла
    intervals_All = json.load(f)
# for item in intervals_All:
#     print(item)

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

def key01step(key, dictEd):
    result = dictEd[(key)][0]
    dictEd[key][0] = 0  # после того как достанет обнуляет
    #print('из функции достающей интервалы result',result )
    #print('из функции достающей интервалы dictEd[(key)][0]', dictEd[(key)][0])
    return result

def intervals_of_all(key1step, listAll_inter):  # список всех подряд интервалов
    listAll_inter.append(key1step)
def intervals_test(key_of_interval,spisok_intervalov,shagi_mej_interv):
    inter_in = shagi_mej_interv
    for item in spisok_intervalov:
        if item == key_of_interval:
            print("совпало на шаге:",inter_in)
            return 0
        else:
            return inter_in
def intervals_test_big(key_of_interval,spisok_intervalov,shagi_mej_interv):
    inter_in =
    for item in spisok_intervalov:
        if item == key_of_interval:
viborka = intervals_All
# объявление всех переменных-----------------------------------------------------------------------------------
dic_ed = {} # болванка под словарь интервалов
#-----------------------------------------------------------------------------------
key=0
steps_sesia = 1
key1 = key
steps = 0
key3step = 0
key2step = 0
listAll_inter=[] # болванка под список всех интервалов
log = True
spisok_vnesh=[0]
spisok_vnesh2=[1]
spisok_intervalov=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]
shagi_mej_interv=0
while (steps <len(viborka)):
    key = viborka[steps]
    key1 = key
    #print('Выпало число:',key)
    steps=steps+1
    shagi_mej_interv =shagi_mej_interv+1
    dob_next_seen_1(dic_ed,key, steps) # создание\ обновление словаря едениц
    interval = key01step(key1, dic_ed)  #  последний интервал выпавшего числа
    add_step_to_all_1(dic_ed) # добавление шагов всем еденицам
    # проверочный - dictEd = {(36): [23, [1, 2], 33]}


    key1step = interval
   # print('последний интервал выпавшего числа:',interval)  # проверка функции возращающей последний интервал выпавшего числа
    # проверочный -- key3step = 12
    # проверочный -- key2step = 10
    shagi_mej_interv = intervals_test(key1step, spisok_intervalov, shagi_mej_interv)

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

# for i in range(len(dic_ed)):
#     print("интервал",dic_ed[i][3])
#     print("интервалы", dic_ed[i][1])
print('количество шагов',steps )
print('список интервалов',listAll_inter)
#print('spisok_vnesh2',spisok_vnesh2)
#with open('intervals_all.txt', 'w') as jsonfile: json.dump(listAll_inter, jsonfile)
# int_count = podchet_simv(listAll_inter)
# int_count = sorted(int_count.items(), key=lambda x: x[1], reverse=True)
# [(4, 74), (2, 47), (3, 32), (0, 17), (1, 12)]

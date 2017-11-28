def last_next_seen_all_steps_1(dict,key):
    all=0
    for seen_step in dict[key][1]:
        all = all+seen_step
    print('функия all =',all)
    return all
def dob_next_seen_1(dict,key,steps): # функция добавления шагов с последнего появления
  if  len(dict[(key)][1]) != 0: # проверка на наличие значений
      #times_seen = len(dict[key][1])
      all_stps_in_key = last_next_seen_all_steps_1(dict, key)
      lst_tim_sen = steps - all_stps_in_key
      print('steps-all_stps_in_key =',lst_tim_sen)
      print('вычисл. добавление к уже существующим данным- разница между последни видимым',lst_tim_sen )
      dict[key][1].append(lst_tim_sen)
      dict[key][2] = len(dict[key][1])
      dict[key][0]=0
      print('key in function =', key)
  else:
    print('печатает dict[key][1][0]',dict[key][1][0])
    dict[key][1].append(steps)
    dict[key][2] = len(dict[key][1])
    dict[key][0] = 0
def add_step_to_all_1(dict, key):
  for item in  dict:
      if item != key:
          dict[item][0]=dict[item][0]+1


# собственно тело программы начинается здесь
steps = 225 # типа имитатор счетчика ходов
# значение словаря еденичных символо на текущий момент
d = {(36):[ 1,[1, 2], 33],(35):[ 11,[101, 102], 31],(34):[ 13,[103, 106], 71]}
# типа число полученное от распознователя символов
key = (35)
# print('печатает dict[37,35][0]',d[(37,35)][0])
# print('печатает dict[37,34][0]',d[(37,34)][0])
# print('печатает dict[37,36][0]',d[(37,36)][0])
add_step_to_all_1(d, key)
# print('печатает d[37,35][0] после функции',d[(37,35)][0])
# print('печатает d[37,34][0] после функции',d[(37,34)][0])
# print('печатает d[37,36][0] после функции',d[(37,36)][0])
# print(d)
# Проверить, есть ли такое имя в словаре и вывести результат
if key in d:
 print(str(d[key]) + ' is the value of ' + str(key))
 dob_next_seen_1(d,key,steps)
 print('if key in d')
# Если имени нет…
else:
# Вывести на экран

 d.update({key: [ 13,[], 30]})# непонятная конструкция?
 print('I don\'t have ' + str(key) + '\'s value, what is it?')
 dob_next_seen_1(d,key,steps)
 print("Обновленный словарь",d)
 print('else of if key in d')
#print(d[(37,36)][1][0])# ура, есть доступ к значениям промежутков между появлениями,
# надо по умолчанию чтоб значение было 99
#vct=5

if len(d[key][1]) != 0: # проверка на наличие значений
    print(d[key][1]) # печатаем список
   # ---------------------------------------------------------------------------------------------
   # отсюда функции патернов
   # сначала из двух цифр
key3_step=23
key2_step=34
key1 = 36
listIntervStps_all[]
dictIntervStps_2{}
dict[key][0] # доступ к словарю выпавшей цифры и ее количеству шагов последний раз когда выпадала
d = {(36):[ 0,[1, 2], 33]}
#key1, key2_step -- паттерн который нужно сравнить \\ dict -- словарь одиночек, откуда нужно
# взять значение step(dict[key][0])\\ dict2 -- словарь интервалов двоек глобал
# \\dict2lok -- словарь интервалов двоек локал\\ listAll_inter -- список всех интервалов друг за другом -- сплошняком
def intervals_of_2(key1,key2_step, dict, dict2,listAll_inter):
    #  перебор всех значений словаря по ключу
    if len(dict2[(key)][0]) != 0:  # проверка на наличие значений, проверяется длинна словаря- умно
        # times_seen = len(dict[key][1])
        listAll_inter.append(0) # в принципе интервал равный нулю может быть только в начале, как и интервал [1,0], [2,1] в
                           # общем первые значения интервалов в мусор
        listAll_inter.append(dict[key1][0])
        key2_step=key1
        print('первая запись в списке интервалов', key1)
    else:
        listAll_inter.append(dict[key1][0])
        dict[(key)][0]
        for item in dict:
            if item == key1:
                dict2[item][0] = dict[item][0] + 1

        print('печатает dict[key][1][0]', dict[key][1][0])


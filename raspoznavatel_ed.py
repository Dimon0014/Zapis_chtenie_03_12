# главная функция - распознователь еденичных символов - заполнение словаря статистик
def last_next_seen_all_steps_1(dict,key):
    all=0
    for seen_step in dict[key][1]:
        all = all+seen_step
    print('функия all =',all)
    return all
def last_last_seen_steps_of_simv_01(dict,key): # альтернатива  "last_next_seen_all_steps_1"
    result = dict[key][0]

    print('функия next_seen_steps =',result)
    return result

def dob_next_seen_1(dict,key, steps): # функция добавления шагов с последнего появления

  if  (key) in dict: # проверка на наличие значений
      last_seen = last_last_seen_steps_of_simv_01(dict,key)
      print('steps-last_time seen_in_key =', last_seen)
      print('печатает dict[key][1][0]', dict[key][1][0])
      dict[key][1].append(last_seen)
      dict[key][2] = len(dict[key][1]) # сколько раз уже выпадала
      dict[key][0] = 0

  else: # инициализация
      dict.update({(key): [0, [steps], 1, key, steps]})  # инициализация
      print('key in function =', key)

def add_step_to_all_1(dict):
  for item in  dict:
          dict[item][0]=dict[item][0]+1
          dict[item][4] = dict[item][4] + 1
# собственно тело программы начинается здесь
steps = 225 # типа имитатор счетчика ходов
# значение словаря еденичных символо на текущий момент
d = {(36):[ 1,[1, 2], 33, 22,2],(35):[ 11,[101, 102], 31, 22,2],(34):[ 13,[103, 106], 71, 22,2]}
# типа число полученное от распознователя символов
key = (35)
# print('печатает dict[37,35][0]',d[(37,35)][0])
# print('печатает dict[37,34][0]',d[(37,34)][0])
# print('печатает dict[37,36][0]',d[(37,36)][0])
add_step_to_all_1(d)
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

 d.update({key: [ 13,[], 30]})
 print('I don\'t have ' + str(key) + '\'s value, what is it?')
 dob_next_seen_1(d,key,steps)
 print("Обновленный словарь",d)
 print('else of if key in d')
#print(d[(37,36)][1][0])# ура, есть доступ к значениям промежутков между появлениями,
# надо по умолчанию чтоб значение было 99
#vct=5

if len(d[key][1]) != 0: # проверка на наличие значений
    print(d[key][1]) # печатаем список


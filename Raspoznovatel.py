def last_next_seen_all_steps(dict,key):
    all=0
    for seen_step in dict[key][1]:
        all = all+seen_step
    print('функия all =',all)
    return all
def dob_next_seen(dict,key,steps): # функция добавления шагов с последнего появления
  if  len(dict[(key)][1]) != 0: # проверка на наличие значений
      #times_seen = len(dict[key][1])
      all_stps_in_key = last_next_seen_all_steps(dict, key)
      lst_tim_sen = steps - all_stps_in_key
      print('steps-all_stps_in_key =',lst_tim_sen)
      print('вычисл. добавление к уже существующим данным- разница между последни видимым',lst_tim_sen )
      dict[key][1].append(lst_tim_sen)
      print('key in function =', key)
  else:
    print(dict[(37, 35)][1][0])
    dict[key][1].append(steps)
steps = 207
d = {(37,36):[ 1,[1, 2], 33],(37,35):[ 11,[101, 102], 31]}
key = (37,35)
# Проверить, есть ли такое имя в словаре и вывести результат
if key in d:
 print(str(d[key]) + ' is the value of ' + str(key))
 dob_next_seen(d,key,steps)
 print('if key in d')
# Если имени нет…
else:
# Вывести на экран

 d.update({key: [ 13,[], 30]})
 print('I don\'t have ' + str(key) + '\'s value, what is it?')
 dob_next_seen(d,key,steps)
 print("Обновленный словарь",d)
 print('else of if key in d')
#print(d[(37,36)][1][0])# ура, есть доступ к значениям промежутков между появлениями,
# надо по умолчанию чтоб значение было 99
#vct=5

if len(d[key][1]) != 0: # проверка на наличие значений
    print(d[key][1]) # печатаем список


import json
data = [(1,2),(3,4),(5,7)] # начальная переменная
with open('no.txt', 'w') as jsonfile: json.dump(data, jsonfile) # сохраняем в файл

with open('no.txt', 'r') as f: # извлекаем  из файла
    data2 = json.load(f)

#print(data2)
data_fin=[]
i=0
for item in data2:              # приводим к типу Python
	data_fin.append(tuple(item))

print(data_fin) # проверка готового результата

fr=hash(data[0])
fr2=hash(data_fin[2])
if fr == fr2:
	print('Они равны')
else:
	print('Не равны')